# Github Repository Explorer

A fullstack, microservice, web application for exploring github repositories of organizations, bookmark and take notes about them.

Note: This was tested on a Linux based system (Arch Linux):

```shell
❯ docker --version
Docker version 19.03.13-ce, build 4484c46d9d
❯ python --version
Python 3.8.5
❯ vue --version  
@vue/cli 4.5.6
```

## Usage

`make dev` will spin the repository service (AKA: 'the backend') and the frontend repository
Frontend accessible via localhost:8080
Backend accessible via localhost:5000

## Test

run `make test` to spin the containers and run the tests.
