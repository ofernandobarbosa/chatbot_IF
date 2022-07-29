FROM rasa/rasa-sdk:latest
WORKDIR /app
USER root
COPY ./actions /app/actions
COPY calendarios.json /app/