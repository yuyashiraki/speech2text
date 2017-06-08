FROM ubuntu
RUN apt-get update && \
    apt-get -y install python-pip &&\
    apt-get -y install supervisor
EXPOSE 80
ADD entrypoint.sh /
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
RUN chmod 755 /entrypoint.sh
CMD ["/entrypoint.sh"]
