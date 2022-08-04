FROM python:3.8.13

USER root
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /sci
COPY ./sistema-de-controle-de-informacoes-ifrs/requirements.txt /sci
RUN pip install -r ./requirements.txt
EXPOSE 8000
ENTRYPOINT [ "python3" ]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]


USER 1001
