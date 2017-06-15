FROM ubuntu
RUN apt-get update && \
    apt-get -y install python-pip && \
    apt-get -y install supervisor
ADD app /app
RUN pip install -r /app/requirements.txt
ADD etc /etc
ADD scripts /var/scripts
ADD resources /resources
RUN chmod 755 /var/scripts/*.sh
EXPOSE 80
CMD ["/var/scripts/entrypoint.sh"]
