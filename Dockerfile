FROM ubuntu
RUN apt-get update && \
    apt-get -y install python-pip && \
    apt-get -y install supervisor && \
    pip install google-cloud-speech
ADD etc /etc
ADD .token /.token
ADD scripts /var/scripts
ADD app /app
ADD resources /resources
RUN chmod 755 /var/scripts/*.sh
EXPOSE 80
CMD ["/var/scripts/entrypoint.sh"]
