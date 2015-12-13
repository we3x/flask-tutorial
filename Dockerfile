FROM python:2-onbuild
MAINTAINER Goran Mekić <meka@tilda.center>

CMD [ "/usr/src/app/manage.py" ]
EXPOSE 5000
