FROM ubuntu

RUN apt-get -y update
RUN apt-get install -y wget
RUN apt-get install -y python
RUN apt-get install -y wget
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install spotipy
RUN wget https://github.com/concourse/concourse/releases/download/v3.8.0/fly_linux_amd64 && chmod +x fly* && cp fly* /usr/local/bin/fly

