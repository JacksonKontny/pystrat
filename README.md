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
`Makefile`.

### Getting Started

#### Running the app locally using docker

1. Set SECRET_KEY and [GOOGLE_APPLICATION_CREDENTIALS](https://googleapis.dev/python/google-api-core/latest/auth.html)
   in
   the `OVERRIDE` section of the `.env` file. Account credentials will need ability to upload files to Google Cloud
   Storage. Credentials file should be downloaded and stored in `/creds/google-account-creds.json`.
2. Start the server in docker (preferred): `make run-docker`
3. Backup service is located at `localhost:5000/backup`

#### Testing

1. Setup python virtual environment: `make setup-python`
2. Run tests: `make test`

#### Running app on host machine

To start the server locally (use at your own risk): `make run-local`

After starting the server, the UI can be accessed at `http://127.0.0.1:5000/`.