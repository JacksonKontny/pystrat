### Requirements

- Python (3.11)
- [pip](https://pypi.org/project/pip/)
- [Docker](https://www.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

### Project Structure

The `data` directory contains example dicom files for uploading to flask for testing

The env file `.env` contains custom environmental values like what port to run the webserver on.

The `creds` file contains the credentials for google cloud storage. This is not included in the repo for security
reasons.

Outside of updating the `creds` and `.env` file, everything can be setup and run through make commands defined in the
Makefile.

### Getting Started

1. Start a virtual environment with `python -m venv .venv`
2. Activate the environment with `source .venv/bin/activate`
3. Install dependencies with `pip install -r requirements.txt`
4. Set SECRET_KEY and [GOOGLE_APPLICATION_CREDENTIALS](https://googleapis.dev/python/google-api-core/latest/auth.html)
   in
   the `OVERRIDE` section of the `.env` file. Account credentials will need ability to upload files to Google Cloud
   Storage. Credentials file should be downloaded and stored in `/creds/google-account-creds.json`.

To start the server in docker (preferred): `make run-docker`
To start the server locally (use at your own risk): `make run-local`
To run tests: `make test`

After starting the server, the UI can be accessed at `http://127.0.0.1:5000/`.