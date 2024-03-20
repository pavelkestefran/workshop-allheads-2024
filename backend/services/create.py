import hvac
import json


def create_secret():
    client = hvac.Client(url="http://allheads-vault:8200")
    create_response = client.secrets.kv.v2.create_or_update_secret(
        mount_point="secret/allheads/kv",
        path="general",
        secret=dict(username="Pavel")
    )

    print(json.dumps(create_response, indent=4, sort_keys=True))
