FROM rasa/rasa-sdk:latest
WORKDIR /actions
USER root
COPY ./actions /actions