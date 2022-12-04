[![Python microservice test with Github Actions](https://github.com/Banhawy/python-aws-microservice/actions/workflows/devops.yml/badge.svg)](https://github.com/Banhawy/python-aws-microservice/actions/workflows/devops.yml)

# Python Microservice

This is a sample python microservice project using GitHub Actions to be deployed in a containerized environment.

## Local Development

To start a local server run the following command:

```bash
uvicorn main:app --reload
```

## Container Development

To run the app inside a Docker container, first build the Docker image with the following command:

```bash
make build
```

Then run the Docker container with the following command:

```bash
make run
```

You could then access your application at the following url: `http://127.0.0.1:8080/`

## Testing

Unit tests are included in the `test_logic.py` file

To run tests run the following command:

```bash
make test
```
