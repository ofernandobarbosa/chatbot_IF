FROM python:3.8.13

ENV PYTHONUNBUFFERED 1
ENV PYTHONIOENCODING UTF-8
ENV LANG pt_BR.UTF-8
ENV DEBUG False

USER root
RUN apt-get update \
	&& apt-get install -y --no-install-recommends \
		postgresql-client \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8000

RUN ["chmod", "+x","docker-entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


USER 1001
