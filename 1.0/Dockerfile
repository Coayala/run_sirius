FROM cyversevice/jupyterlab-scipy:latest

# Install zip

RUN sudo apt-get install -y zip

# Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

# Create working directory

WORKDIR /home/jovyan/work/

# Add scripts for running SIRIUS

ADD https://github.com/Coayala/run_sirius/blob/main/1_automate_sirius.py /home/jovyan/work/
ADD https://github.com/Coayala/run_sirius/blob/main/1_sirius_cli_run.sh /home/jovyan/work/
ADD https://github.com/Coayala/run_sirius/blob/main/0_ms2_into_groups.ipynb /home/jovyan/work/

RUN sudo chmod +x 1_automate_sirius.py
RUN sudo chmod +x 1_sirius_cli_run.sh
