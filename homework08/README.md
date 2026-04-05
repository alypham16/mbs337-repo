# Homework 08

This directory is for homework 8 of MBS 337, Research Computing in Biology.

## Setup

The tools for this homework involve setting up a Dash dashboard and Docker to containerize the app and dependencies. Docker compose and a Makefile were also created to automate workflows.

Use the following to clone the repository:
``` bash
git clone https://github.com/alypham16/mbs337-repo/
cd homework08
```
To start the dashboard production:

```bash
make compose-up
docker ps
```
The dashboard should be available via browser showing "Hello, Dash!" :
http://localhost:8050

To run staging deployment:
```bash
make compose-up-staging
```

The staging dashboard should run on:

http://localhost:8051

Staging maps host port 8051 to container 8050.

To stop running the containers, use either of the following:
```bash
make compose-down
docker compose down
```

## Exercise Descriptions 

This homework is composed of 2 parts (https://mbs-337-sp26.readthedocs.io/en/latest/homework/homework08.html).

1. Creating the Demo dashboard. This container may be defined using:

- Dockerfile - Builds the Python environment and installs requirements
- requirements.txt - Python packages required for the Dash app
- docker-compose.yml - Production container configuration
- docker-compose-staging.yml - Staging deployment configuration
- Makefile - simplifies container management

2. Creating two GitHub Actions workflows for (1) running the integration test for every repository push and (2) automatically building and pushing a container image to the GitHub Container Registry with every tag added.

- integration-test.yml - Runs integration tests using pytest when code is pushed to the repository.
- push-to-registry.yml - Automatically builds and pushes a container image to GitHub Container Registry when a new version tag is added to the repository.

## Miscellaneous
The following non-exercise files are also in the Git directory
- README.md: This file, which contains an overview of the homework08 directory.
- test/test_app.py - integration test checking if the Dash app responds with http 200.

The following non-exercise files are in the repository and utilized:
- .github/workflows/ - contains GitHub Actions workflows used for automated testing and container publishing

## AI Usage

No AI was used for this assignment.