FROM praekeltfoundation/django-bootstrap
RUN ./manage.py collectstatic --noinput
CMD ["mama_ng_contentstore.wsgi:application"]
