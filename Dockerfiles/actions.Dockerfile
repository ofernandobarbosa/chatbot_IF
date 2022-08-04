FROM rasa/rasa-sdk:latest
WORKDIR /app
USER root
COPY ../bot/actions /app/actions
RUN python -m pip install requests
# RUN ["chmod", "+x","./entrypoint.sh"]
# ENTRYPOINT ["./entrypoint.sh"]
