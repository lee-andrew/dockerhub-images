#!/bin/bash
set -e

apt-get install wget
wget https://github.com/concourse/concourse/releases/download/v3.8.0/fly_linux_amd64
chmod +x fly*

cp fly_linux_amd64 fly

./fly -t ci login -c "http://$concourse_host:8080" --username=$concourse_username --password=$concourse_password

pushd git_docker_image
	../fly -t ci set-pipeline -n -p docker-image -c <(python pipeline.py) -l <(echo $creds)
popd
