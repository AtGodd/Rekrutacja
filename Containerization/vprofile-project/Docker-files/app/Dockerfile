FROM maven:3.9.9-eclipse-temurin-21 AS build_image
RUN git clone https://github.com/hkhcoder/vprofile-project.git
RUN cd vprofile-project && git checkout containers && mvn install

FROM tomcat:10-jdk21
LABEL "Project"="goddb"
LABEL "Author"="JW"
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=build_image vprofile-project/targe/vprofile-v2.war /usr/local/tomcat/webapps/ROOT*

EXPOSE 8080
CMD {"catalina.sh", "run"}