FROM rasa/rasa:latest-full

USER root

RUN pip3 install -U spacy 
RUN python3 -m spacy download pt_core_news_lg
RUN ["chmod", "+x","entrypoint.sh"]
ENTRYPOINT ["./entrypoint.sh"]
CMD [ "run","-m","/bot/models" "--enable-api","--cors", "*"]


USER 1001