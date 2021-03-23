FROM cyversevice/jupyterlab-scipy:latest

# Install zip

RUN sudo apt-get install -y zip
RUN sudo apt install default-jre

# Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

# Create working directory

WORKDIR /home/jovyan/work/

# Add scripts for running SIRIUS

ADD https://github.com/Coayala/run_sirius/blob/main/1_automate_sirius.py /home/jovyan/work/1_automate_sirius.py
ADD https://github.com/Coayala/run_sirius/blob/main/1_sirius_cli_run.sh /home/jovyan/work/1_sirius_cli_run.sh
ADD https://github.com/Coayala/run_sirius/blob/main/0_ms2_into_groups.ipynb /home/jovyan/work/0_ms2_into_groups.ipynb

RUN sudo chmod +x /home/jovyan/work/1_automate_sirius.py
RUN sudo chmod +x /home/jovyan/work/1_sirius_cli_run.sh
