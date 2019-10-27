FROM tdevco/otr-service:base

ENV PYTHONUNBUFFERED 1

RUN export DEBIAN_FRONTEND=noninteractive

RUN mkdir -p /src

WORKDIR /src

ADD . /src/

# Install Run Apt
RUN apt-get -y update
RUN apt-get -y install gettext
RUN apt-get -y install binutils libproj-dev gdal-bin python3-gdal
RUN apt-get -y install postgis

# Install any needed packages specified in requirements.txt
RUN pypy3 -m pip install -r requirements.txt

