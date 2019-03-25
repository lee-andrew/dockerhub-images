FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install ffmpeg
RUN apt-get -y install language-pack-en-base
RUN apt-get -y install cifs-utils
RUN apt-get -y install wget

ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en

RUN pip3 install psycopg2
RUN pip3 install pathlib
RUN pip3 install BeautifulSoup4
RUN pip3 install youtube_dl
RUN pip3 install pafy
RUN pip3 install spotipy
RUN pip3 install mutagen
RUN pip3 install unicode-slugify
RUN pip3 install titlecase
RUN pip3 install plexapi
RUN pip3 install xmltodict

RUN wget https://github.com/ritiek/spotify-downloader/archive/v1.2.0.tar.gz
RUN tar -zxvf v1.2.0.tar.gz
RUN cd spotify-downloader-* && pip3 install .
