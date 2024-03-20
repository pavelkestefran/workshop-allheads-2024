# Secret Management with Hashicorp Vault

 Workshop at Allheads IT Bratislava 2024, FEI STU, 20th March 2024

 ----

Everybody has many secrets… EVERYWHERE. In any organization, sensitive secrets are scattered in various form across many locations in their infrastructure. May be stored in k8s, CICD servers or Terraform variables, including all other places they are essential to keep things running. This imposes a security risk. That’s where HashiCorp Vault comes in. Secret consolidation is its key use case and often a first step. But there’s much, much more.

----

## Quick Start

If you feel like it, you may start developing and playing around with attached python app right away and read more later or as the app starts...

```bash
cp .env.default .env && make && make develop
```

----

### Disclaimer

Please always keep in mind, that this is an example application that will enable us to get to know the Vault CLI and usage of Vault HVAC Python API. It is not production ready, and therefore also shouldn't be used in production. You can apply the concepts tho, and maybe even reuse some code if you ever try to implement Vault into your real-world application.

### Overview

Vault is an open-source secret management tool, encryption as a service and privileged access management tool.

This workshop will discuss a brief introduction to Vault.

I've already included some technologies, libraries and frameworks in this repository. For more details on each see a list below, including a link to corresponding documentation and resources.

* [Vault HTTP API](https://developer.hashicorp.com/vault/api-docs)
* [Vault CLI](https://developer.hashicorp.com/vault/docs/commands)
* [Getting Started with Vault Secrets Engines](https://developer.hashicorp.com/vault/tutorials/getting-started/getting-started-secrets-engines)
* [How (and Why) to Use AppRole Correctly in HashiCorp Vault](https://www.hashicorp.com/blog/how-and-why-to-use-approle-correctly-in-hashicorp-vault)
* [Python 3.11](https://docs.python.org/3/)
* [HashiCorp Vault API client for Python (hvac)](https://hvac.readthedocs.io/en/stable/overview.html)
* [Flask](https://flask.palletsprojects.com/en/2.3.x/)

### Requirements

You will need to install the following things locally, to run our prepared sample application:

* docker
* docker-compose
* make
* jq

Please configure Docker accordingly:

* minimum 2 CPU, 2 GB of RAM
* enabled file sharing with docker

### Usage

We've prepared a `Makefile` that helps you get things up and running.

To use the default environment configuration:

```bash
cp .env.default .env
```

#### Vault

To start Vault locally simply run:

```bash
make 
```

To stop and clean up everything run:

```bash
make clean
```

##### Vault UI

To check Vault UI browse to <http://localhost:8200> and user <root_token> to log in.

##### Vault CLI

To use Vault CLI as root, export its address and log in:

```bash
export VAULT_ADDR=http://localhost:8200
vault login <root_token>
```

To look around in Vault CLI run:

```bash
# Returns vault status
vault status

# List existing secret engines
vault secrets list

# Returns all entries in a secret engine
vault kv get secret/allheads/kv/general

# Returns value of specific field
vault kv get -field=event secret/allheads/kv/general

# Adds new entry to specific endpoint
vault kv patch secret/allheads/kv/general target=hello

# Replaces all entries at specific endpoint
vault kv put secret/allheads/kv/general target=hello

# List all auth methods
vault auth list

# Prints out specifc approle configuration
vault read auth/approle/role/allheads

# Lists vault policies
vault policy list

# Prints out specific vault policy
vault policy read allheads-policy
```

##### Vault variables

Ansible included in this workshop should do it for you in `.env` file, yet if you need to run something from `examples` folder you need to register both the `VAULT_ADDR` and `VAULT_TOKEN` in your environment:

```bash
export VAULT_ADDR=http://localhost:8200
export VAULT_TOKEN=<approle_client_token>
```

#### Examples

To run anything from `examples` folder make sure you have working python installed including all requirements.

```bash
pip install -r examples/requirements.txt

python examples/auth.py

python examples/read.py
```

#### Backend

To start the Flask backend via Docker locally on <http://localhost:5001> (this will also use the `.env` file mentioned above for configuration):

```bash
make backend-start
```

To stop the Flask backend container:

```bash
make backend-stop
```

If you aim for a more immediate developer experience, working on the backend, you can just set up a virtual environment and install the requirements. You can use a local `.env` file in the backend folder, in order to easily feed the application with your environment variables for configuration purposes. The backend uses `python-dotenv` to load the environment variables. See the script below to start your backend locally, without Docker. This of course requires a Python installation on your machine (we recommend Python 3.11).

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 -m flask run --port 5001
```

#### Cleanup

To stop and clean up everything run:

```bash
make clean
```
