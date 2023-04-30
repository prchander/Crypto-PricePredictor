#!/bin/bash

# Update apt-get
sudo apt-get update

# Install pip3
sudo apt-get install python3-pip -y

# Install pandas
pip3 install pandas==2.0.1

# Install matplotlib
pip3 install matplotlib==3.4.2

# Install scikit-learn
pip3 install scikit-learn==0.24.2

# Install requests
pip3 install requests==2.25.1

# Install lxml
sudo apt-get install python3-lxml -y

# Install html5lib
pip3 install html5lib==1.1

#install bs4
pip3 install bs4