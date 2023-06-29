


# conn.request("POST", "/post",body=body)

# resp = conn.getresponse()

# print(resp.status, resp.reason, resp.version)

import requests
import json
from requests.packages import urllib3

urllib3.disable_warnings()


url = "https://172.24.12.75/base/login"
locationUrl = "https://172.24.12.75/base/location/table"

headers = {"Ssep_token":"ZXlKaGJHY2lPaUpCUlZNaUxDSjBlWEFpT2lKS1YxUWlmUT09LmV5SmxlSEFpT2lJeE5qZzNPRGswTmpZM016UTFJaXdpWlhod1JHRjBZU0k2ZXlKM1pXSnphWFJsU1dRaU9pSm1ZbVkzTkdWa00yRXdNV0kwTkdRMVlUWTVPREEwT0RKbE1qazBaREZqWkNJc0luVnpaWEpKWkNJNkltSmpZMlk0WkRNeU9URXhORFF4WVdNNE9UbGhPV1E1TVRJME9UYzBNbUkzSWl3aWFYTlhaV0p6YVhSbFFXUnRhVzRpT2lJeEluMHNJbWxoZENJNklqRTJPRGM0TmpVNE5qY3pORFVpTENKcGMzTWlPaUpUYVdWdFpXNXpJRkJ2ZDJWeUlFRjFkRzl0WVhScGIyNGdUSFJrTGlKOS5GNEp4UUlzWS9sSmdHMDU4c3JnSzFKQTJ5TTF0RUJPTkp0dktPMTZubVgvTjk4TzErRit4ZlhiYWdkMkdURUsxQTVub3ExSkFYUVBaUzN3aG10bE96QT09"}
# conn = http.client.HTTPSConnection("172.24.12.75/base/login",context=ssl._create_unverified_context())
# dict_opu = dict(sape=223,jack="980",zyz=908)

payload = {
    "pageSize": 15,
    "pageNo": 1
}
str = json.dumps(payload)

res = requests.post(locationUrl,json=payload,headers=headers,verify=False)

print(res.status_code)
print(res.text)
print(res.headers)

