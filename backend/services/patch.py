import hvac
import json


def patch_secret():
    client = hvac.Client(url="http://localhost:8200")
    patch_response = client.secrets.kv.v2.patch(
        mount_point="secret/allheads/kv",
        path="general",
        secret=dict(password="aSecretString123")
    )

    print(json.dumps(patch_response, indent=4, sort_keys=True))
