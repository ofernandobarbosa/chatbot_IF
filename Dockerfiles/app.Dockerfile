FROM python:3.8.13
USER root

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV LANG pt_BR.UTF-8
ENV DJANGO_SETTINGS_MODULE sdv.settings.qa
ENV DEBUG False

RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY ../sistema-de-controle-de-informacoes-ifrs /app
RUN pip install -r requirements.txt
RUN sudo apt install python3-psycopg2
EXPOSE 8000

RUN ["chmod", "+x","docker-entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


USER 1001
