FROM rasa/rasa:latest-full

USER root

RUN python3 -m spacy download pt_core_news_lg

USER 1001