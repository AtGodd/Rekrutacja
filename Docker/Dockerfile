FROM ubuntu:latest
LABEL "Author"="JW"
LABEL "Project"="nano"
RUN apt update && apt install apache2 git -y
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]
EXPOSE 80
WORKDIR /var/www/html
VOLUME /var/log/apache2
ADD nano.tar.gz /var/www/html
