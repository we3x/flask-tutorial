#!/bin/bash

cp /vagrant/jessie-backports.list /etc/apt/sources.list.d
apt-get update
apt-get upgrade -y
apt-get install -y docker.io
apt-get clean -y
docker pull python:2-onbuild
