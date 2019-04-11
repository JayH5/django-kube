FROM jamiehewland/django-kube

COPY requirements/prod.txt requirements.txt
RUN pip install --no-cache -r requirements.txt

COPY . .
RUN pip install --no-cache -e .

ENV DJANGO_SETTINGS_MODULE mysite.settings
RUN django-admin collectstatic
