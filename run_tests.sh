#!/usr/bin/bash

# Run unit tests
mkdir -p test-reports
py.test --ignore=venv --junitxml=test-reports/test-hello.xml --cov-report term-missing --cov-report=html --cov . tests
