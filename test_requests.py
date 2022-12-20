import re
from datetime import datetime
import time
from dateutil import parser
import requests
import json



# r = requests.post('http://127.0.0.1:8000/api/apex/filenames/', data=payload)
# print(r.content)

# r = requests.get('http://127.0.0.1:8000/api/apex/deployments')
# print(json.loads(r.content))


data = [{'gps_hhmmss': 100726.47, 'latitude': 23.6419361, 'longitude': 63.363935, 'apex': 'APEX 12', 'deployment_site': 'BELLOWS'}, {'gps_hhmmss': 100746.17, 'latitude': 23.6419914, 'longitude': 63.364437, 'apex': 'APEX 11', 'deployment_site': 'BELLOWS'}, {'gps_hhmmss': 100804.67, 'latitude': 23.6420456, 'longitude': 63.364962, 'apex': 'APEX 12', 'deployment_site': 'BELLOWS'}, {'gps_hhmmss': 100821.37, 'latitude': 23.6420912, 'longitude': 63.365407, 'apex': 'APEX 11', 'deployment_site': 'BELLOWS'}]

data = [{'gps_hhmmss': 100726.47, 'latitude': 23.6419361, 'longitude': 63.363935, 'apex': 'APEX 12', 'deployment_site': 'BELLOWS'}]

data = [{"gps_hhmmss": 100726.47, "latitude": 23.6419361, "longitude": 63.363935, "apex": "APEX 11", "deployment_site": "BELLOWS", "filename": "APEX11-20220512-BAF_IVS1_DQC_000002_2022132_001.dat"}, {"gps_hhmmss": 100746.17, "latitude": 23.6419914, "longitude": 63.364437, "apex": "APEX 11", "deployment_site": "BELLOWS", "filename": "APEX11-20220512-BAF_IVS1_DQC_000002_2022132_001.dat"}, {"gps_hhmmss": 100804.67, "latitude": 23.6420456, "longitude": 63.364962, "apex": "APEX 11", "deployment_site": "BELLOWS", "filename": "APEX11-20220512-BAF_IVS1_DQC_000002_2022132_001.dat"}, {"gps_hhmmss": 100821.37, "latitude": 23.6420912, "longitude": 63.365407, "apex": "APEX 11", "deployment_site": "BELLOWS", "filename": "APEX11-20220512-BAF_IVS1_DQC_000002_2022132_001.dat"}]

data = [{'gps_hhmmss': 30646.29, 'latitude': 38.6018722, 'longitude': 42.123559, 'apex': 'APEX 4', 'deployment_site': 'CROFT', 'filename': 'Apex4_cc__pmqc_DQC_000001_2022132_003.dat', 'uniqueID': '3064600APEX4CROFT', 'deployment': 2}]

print(data)
print(json.dumps(data))
r = requests.post('http://127.0.0.1:8000/api/apex/crud/', json=data)
print(r.content)