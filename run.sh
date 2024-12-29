#!/bin/bash

appname=searchdisplay
source ~/.${appname}.env.sh
if [ "$ENV" == "test" ]
then
    DJANGO_SETTINGS_MODULE=${appname}.settings.test
else
    DJANGO_SETTINGS_MODULE=${appname}.settings.production
fi
export DJANGO_SETTINGS_MODULE
echo "Running environment: [$ENV] [$DJANGO_SETTINGS_MODULE]"

PATH=$PATH:$PWD/venv/bin
source venv/bin/activate
cd ${appname}/
./manage.py migrate
./manage.py runserver 0.0.0.0:7900
#gunicorn --workers 2 --timeout 60 --bind :7900 \
#    ${appname}.wsgi:application
cd -
