FROM rasa/rasa-sdk:latest
WORKDIR /app
USER root
RUN pip3 install 
COPY ./actions /app/actions