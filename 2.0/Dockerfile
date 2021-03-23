## Base image

FROM ubuntu:rolling

## Install CyVerse VICE Depends (from https://github.com/rbartelme/phenophasebbn/blob/main/rstudio-bayes-cpu/Dockerfile)
## lsb is deprecated
RUN apt-get update && apt-get install -y lsb-base lsb-release wget \
  apt-transport-https python2.7 python-requests curl supervisor nginx gnupg2 \
  clang libfuse2

RUN curl "http://ftp.se.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u8_amd64.deb" -O && \
    dpkg -i libssl1.0.0_1.0.1t-1+deb8u8_amd64.deb && \
    rm libssl1.0.0_1.0.1t-1+deb8u8_amd64.deb

## Install iCommands
RUN wget https://files.renci.org/pub/irods/releases/4.1.10/ubuntu14/irods-icommands-4.1.10-ubuntu14-x86_64.deb && dpkg -i irods-icommands-4.1.10-ubuntu14-x86_64.deb

ADD https://github.com/hairyhenderson/gomplate/releases/download/v2.5.0/gomplate_linux-amd64 /usr/bin/gomplate
RUN chmod a+x /usr/bin/gomplate

## Install zip and java

RUN sudo apt-get install -y zip
RUN sudo apt install default-jre

## Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

## Create working directory

WORKDIR /home/jovyan/work/

## Add scripts for running SIRIUS

ADD https://github.com/Coayala/run_sirius/blob/main/1_automate_sirius.py /home/jovyan/work/1_automate_sirius.py
ADD https://github.com/Coayala/run_sirius/blob/main/1_sirius_cli_run.sh /home/jovyan/work/1_sirius_cli_run.sh
ADD https://github.com/Coayala/run_sirius/blob/main/0_ms2_into_groups.ipynb /home/jovyan/work/0_ms2_into_groups.ipynb

RUN sudo chmod +x /home/jovyan/work/1_automate_sirius.py
RUN sudo chmod +x /home/jovyan/work/1_sirius_cli_run.sh
