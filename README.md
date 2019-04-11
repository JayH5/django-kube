# django-kube
🐴 📦 Docker images for running vanilla Django on Kubernetes with best practices

## django-bootstrap
The work here is based on [`django-bootstrap`](https://github.com/praekeltfoundation/docker-django-bootstrap)
but is specialised for use on Kubernetes and also removes a lot of legacy stuff.
Unlike `django-bootstrap` this image...
* Supports only Python 3 and Django 2
* Uses [WhiteNoise](http://whitenoise.evans.io/en/stable/django.html) for static
  file handling rather than Nginx config.
* Does not support running Gunicorn and Celery in a single container.
* Does not perform startup tasks like database migrations. There are other
  abstractions in Kubernetes for this such as init containers or batch jobs.
* Removes a number of custom configuration options.
* Runs Nginx in a separate container to Gunicorn.
* Is not based on the `praekeltfoundation` images.
