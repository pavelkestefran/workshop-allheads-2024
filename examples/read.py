import hvac
import json


def read_secret():
    client = hvac.Client(url='http://localhost:8200')
    read_response = client.secrets.kv.v2.read_secret_version(
        mount_point='secret/allheads/kv',
        path='general',)

    print(json.dumps(read_response, indent=4, sort_keys=True))


read_secret()
