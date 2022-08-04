FROM rasa/rasa-sdk:latest
WORKDIR /app

COPY ./bot/actions /app/actions
RUN python -m pip install requests

