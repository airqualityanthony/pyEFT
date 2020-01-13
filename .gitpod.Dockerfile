FROM gitpod/workspace-full-vnc
                    
USER root

# Install custom tools, runtime, etc. using apt-get
# For example, the command below would install "bastet" - a command line tetris clone:
#
# RUN sudo apt-get -q update && #     sudo apt-get install -yq bastet && #     sudo rm -rf /var/lib/apt/lists/*
#
# More information: https://www.gitpod.io/docs/42_config_docker/
RUN sudo apt-get -q update && sudo apt-get install python3-pyqt5 && sudo apt-get install python3-pandas

USER root
