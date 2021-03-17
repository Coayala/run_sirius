FROM cyversevice/jupyterlab-scipy:latest

# Install zip

RUN sudo apt-get install -y zip

# Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

# Download scripts for running SIRIUS

RUN git clone https://github.com/Coayala/run_sirius.git

WORKDIR 'run_sirius'
RUN chmod +x 1_automate_sirius.py
RUN chmod +x 1_sirius_cli_run.sh

