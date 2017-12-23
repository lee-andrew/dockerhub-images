#!/bin/bash
set -e

fly -t ci login -c "http://$concourse_host:8080" --username=$concourse_username --password=$concourse_password

pushd git_docker_image
  fly -t ci set-pipeline -n -p docker-image -c <(python pipeline.py) -l <(echo $creds)
popd
