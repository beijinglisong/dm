FROM docker.dever.cc/dev/python:latest

MAINTAINER Rabin "https://github.com/shemic"

ENV DEMETER_HOME=/usr/local/demeter
ENV DEMETER_LIB=/usr/lib/python2.7/site-packages/demeter
ENV DEMETER_CONF=env
ENV PATH=$PATH:$DEMETER_HOME

RUN apk add --no-cache --update py-gevent py-psycopg2 git && \
	pip install tornado && \
	pip install pytest-runner && \
	pip install paho-mqtt && \
	pip install influxdb && \
	pip install short_url && \
	pip install oss2 --upgrade && \
	#pip install qrcode && \
	git clone http://git.dever.cc:3000/python/demeter.git $DEMETER_LIB && \
	git clone http://git.dever.cc:3000/python/xinnongbaohe.git $DEMETER_HOME && \
	#mkdir -p /etc/supervisor/conf.d/ && \
	rm -R $DEMETER_HOME/runtime/postgresql/device_* $DEMETER_HOME/runtime/postgresql/hardware $DEMETER_HOME/runtime/postgresql/farm_* $DEMETER_HOME/runtime/postgresql/msg $DEMETER_HOME/runtime/postgresql/origin_*  $DEMETER_HOME/runtime/postgresql/log $DEMETER_HOME/runtime/postgresql/manage_log && \
	chmod -R +x $DEMETER_HOME/*.py

EXPOSE 8087 8088

COPY demeter.sh /entrypoint/demeter.sh
#COPY supervisor/ /etc/supervisor/