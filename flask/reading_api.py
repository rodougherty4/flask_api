from flask import Flask, request
import pandas as pd
from cerberus import Validator
import datetime
from datetime import datetime as dt
from dateutil import parser

app = Flask(__name__)

tpath = '/tmp/'

request_schema = {'id': {'type': 'string', 'required': True},
                  'readings': {'type': 'list', 'required': True}
                  }
reading_schema = {'timestamp': {'type': 'string', 'required': True},
                  'count': {'type': 'integer', 'required': True}
                  }


@app.route('/reading', methods=['POST'])
def process_reading():
    # set current time as UTC
    timestamp_str = dt.strftime(dt.now(datetime.timezone.utc), "%Y-%m-%d %H:%M:%S")

    try:
        request_data = request.get_json()
    except:
        return "malformed json"

    v = Validator(request_schema)
    if not v.validate(request_data):
        return "malformed json"

    id = request_data['id']
    output_file = f"{tpath}{id}.csv"

    # loop through readings to log posts
    for reading in request_data['readings']:
        # if reading dictionary is malformed, move on to next reading
        v = Validator(reading_schema)
        if v.validate(reading):
            # parse ISO 8601 and set UTC string
            reading_timestamp = parser.parse(reading["timestamp"])
            reading_timestamp_str = dt.strftime(reading_timestamp, "%Y-%m-%d %H:%M:%S")

            # save current time, posted reading time, reading count, and device id
            output_string = f"{timestamp_str}|{reading_timestamp_str}|{reading['count']}|{id}"
            with open(output_file, "a") as id_file:
                id_file.write(output_string + "\n")

    # read device data to aggregate
    id_df = pd.read_csv(output_file, sep="|", header=None,
                        names=["api_post_time", "reading_time", "reading_count", "device_id"])

    # remove duplicate readings and sort by reading timestamp descending
    id_df = id_df[["reading_time","reading_count","device_id"]].drop_duplicates().sort_values("reading_time",ascending=False)

    last_reading = id_df["reading_count"].iat[0]
    cummulative_readings = id_df.reading_count.sum()

    id_df["last_reading"] = last_reading
    id_df["cummulative_readings"] = cummulative_readings

    response_payload = {"last_reading" : str(last_reading),
                        "cummulative_readings" : str(cummulative_readings)}

    return response_payload


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234, debug=True)
