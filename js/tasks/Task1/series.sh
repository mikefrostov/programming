#!/bin/bash

set -e

docker pull nginx:latest

docker images -q nginx:latest

docker run -p 8888:80 nginx


