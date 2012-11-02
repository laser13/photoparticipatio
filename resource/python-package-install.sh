#!/bin/bash
# Установка django с пакетами

#Python-Dev
sudo apt-get install python-dev

#Python-MySQL
sudo apt-get install python-mysqldb

#Python-Yaml
sudo apt-get install python-yaml

git clone https://github.com/django/django.git
cd django
sudo python setup.py install
cd ..

#Необходимые пакеты

#easy_install http://pypi.python.org/pypi/setuptools
wget http://pypi.python.org/packages/source/s/setuptools/setuptools-0.6c11.tar.gz
tar xzvf setuptools-0.6c11.tar.gz
cd setuptools-0.6c11
sudo python setup.py install
cd ..

#pip
sudo easy_install pip

#Python Imaging Library (PIL) http://www.pythonware.com/products/pil/
wget http://effbot.org/downloads/Imaging-1.1.7.tar.gz
tar xzvf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
sudo python setup.py install
cd ..

#Сборка пользовательской структуры
sudo pip install django_structurer