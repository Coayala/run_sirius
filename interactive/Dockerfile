FROM cyversevice/jupyterlab-scipy:latest

# Install zip

RUN sudo apt-get install -y zip
RUN sudo apt install -y default-jre

# Install Python libraries required

RUN pip3 install natsort

# Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

# Create working directory

USER jovyan

WORKDIR /home/jovyan/work/

# Add scripts for running SIRIUS

ADD --chown=jovyan https://raw.githubusercontent.com/Coayala/run_sirius/main/scripts/1_automate_sirius.py /home/jovyan/work/1_automate_sirius.py
ADD --chown=jovyan https://raw.githubusercontent.com/Coayala/run_sirius/main/scripts/1_sirius_cli_run.sh /home/jovyan/work/1_sirius_cli_run.sh
ADD --chown=jovyan https://raw.githubusercontent.com/Coayala/run_sirius/main/scripts/0_ms2_into_groups.py /home/jovyan/work/0_ms2_into_groups.py
ADD --chown=jovyan https://raw.githubusercontent.com/Coayala/run_sirius/main/scripts/2_fix_sirius_output.py /home/jovyan/work/2_fix_sirius_output.py
ADD --chown=jovyan https://raw.githubusercontent.com/Coayala/run_sirius/main/scripts/entry.sh /home/jovyan/work/entry.sh

# Make executables

RUN chmod +x /home/jovyan/work/*
