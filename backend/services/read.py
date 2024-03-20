import hvac
import os


def read_secret():
    VAULT_ADDR = os.getenv('VAULT_ADDR', "http://localhost:8200")
    client = hvac.Client(url=VAULT_ADDR)
    read_response = client.secrets.kv.v2.read_secret_version(
        mount_point="secret/allheads/kv",
        path="general",)

    return read_response
