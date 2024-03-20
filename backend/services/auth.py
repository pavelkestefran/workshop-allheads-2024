import hvac
import os


def is_authenticated() -> bool:
    VAULT_ADDR = os.getenv('VAULT_ADDR', "http://localhost:8200")
    client = hvac.Client(url=VAULT_ADDR)
    return client.is_authenticated()
