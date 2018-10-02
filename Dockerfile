FROM python:3.6

EXPOSE 8000
COPY requirements.txt manage.py ./
RUN pip install -r requirements.txt

COPY . ./


#CMD ["echo ${DJANGO_DEBUG}"]
CMD ["gunicorn", "blog_example.wsgi", "-b 0.0.0.0:8000"]