FROM praekeltfoundation/django-bootstrap
ENV DJANGO_SETTINGS_MODULE "mama_ng_contentstore.settings"
RUN django-admin collectstatic --noinput
CMD ["mama_ng_contentstore.wsgi:application"]
