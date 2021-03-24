FROM cyversevice/jupyterlab-scipy:latest

# Install zip

RUN sudo apt-get install -y zip
RUN sudo apt install -y default-jre

# Download SIRIUS

RUN wget https://bio.informatik.uni-jena.de/repository/dist-release-local/de/unijena/bioinf/ms/sirius/4.6.1/sirius-4.6.1-linux64-headless.zip
RUN unzip sirius-4.6.1-linux64-headless.zip
RUN echo "export SIRIUS=/home/jovyan/sirius/bin/sirius" >> /home/jovyan/.bashrc

# Create working directory

WORKDIR /home/jovyan/work/

# Add scripts for running SIRIUS

ADD https://github.com/Coayala/run_sirius/blob/main/executable/automate_sirius.py /home/jovyan/work/automate_sirius.py
ADD https://github.com/Coayala/run_sirius/blob/main/executable/1_sirius_cli_run.sh /home/jovyan/work/1_sirius_cli_run.sh
ADD https://github.com/Coayala/run_sirius/blob/main/executable/0_ms2_into_groups.py /home/jovyan/work/0_ms2_into_groups.ipynb
ADD https://github.com/Coayala/run_sirius/blob/main/executable/2_fix_sirius_output.py /home/jovyan/work/2_fix_sirius_output.py

RUN sudo chmod +x /home/jovyan/work/*

ENTRYPOINT ["/home/jovyan/work/automate_sirius.py", "-i ms2spectra_consensus.mgf"]
