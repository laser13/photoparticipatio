#!/bin/bash
# Установка django с пакетами

#Debug toolbar
git clone https://github.com/django-debug-toolbar/django-debug-toolbar.git
cd django-debug-toolbar
sudo python setup.py install
cd ..

#Миграции http://south.readthedocs.org/en/latest/installation.html
sudo easy_install South
sudo easy_install -U South

#Миниатюры и редактирование картинок http://sorl-thumbnail.readthedocs.org/en/latest/
sudo pip install sorl-thumbnail

#Простая регистрация пользователей
sudo pip install django-registration

#Собственно теги
sudo pip install django-tagging

#Pytils это инструменты для работы с русскими строками (транслитерация, числительные слоами, русские даты и т.д.)
#https://github.com/j2a/pytils
git clone https://github.com/j2a/pytils.git
cd pytils
sudo python setup.py install
cd ..