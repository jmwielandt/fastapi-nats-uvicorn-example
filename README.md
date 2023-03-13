# Template for NATS+FastAPI app

Python 3.10

Poetry

FastAPI + Uvicorn + NATS-py

## Set up

Create a file ".env" in "conf/". Set:

```env
NATS_SERVER = (str)  # nats server uri
NATS_TOPIC = (str)   # nats topic to subscribe
HOST = (str)         # webserver host
PORT = (int)         # webserver port
```

## Run?

- `poetry run py tp2`
- `poetry run py -m uvicorn --factory tp2:main`
  (this method won't use the .env host and port)

Create a venv:
```bash
virtualenv venv
poetry export -r requirements.txt > requirements.txt

# unix:
venv/bin/pip install -r requirements.txt
venv/bin/python -m tp2


# windows:
venv/scripts/pip.exe install -r requirements.txt
venv/scripts/python.exe -m tp2
```
