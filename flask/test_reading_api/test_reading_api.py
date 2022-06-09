import requests

url="http://127.0.0.1:105/reading"
thejson={"id": "362", "readings": [{"timestamp": "2021-09-29T16:08:15+01:00", "count": 2},
                                   {"timestamp": "2021-10-29T16:08:15+01:00", "count": 12},
                                   {"timestamp": "2021-09-29T16:09:15+01:00", "count": 15},
                                   {"timestamp": "2021-09-29T16:09:15+01:00", "count": "15"},
                                   {"timestamp": "2021-09-29T16:09:15+01:00", "count": "3"}]}
tst=requests.post(url, json=thejson)
print(tst.text)