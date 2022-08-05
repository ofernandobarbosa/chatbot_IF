FROM python:3.8.13


USER root
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
	postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /sci
COPY ./sistema-de-controle-de-informacoes-ifrs/requirements.txt /sci
RUN pip install -r ./requirements.txt
# RUN pip install sdv
COPY ./sistema-de-controle-de-informacoes-ifrs /sci
COPY ./sistema-de-controle-de-informacoes-ifrs/entrypoint.sh /sci
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "./entrypoint.sh" ]

EXPOSE 8000
