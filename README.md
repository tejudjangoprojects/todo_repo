# todo_repo
# todo_repo
Project Title:To-DO List App
Project Description:This application will give support for TODO List of Tasks on what time and date&time we should do the task.
Prerequisites:- we should install these requirements compulsory in our system to execute the project in our system
altgraph==0.16.1
argon2-cffi==18.3.0
asn1crypto==0.24.0
atomicwrites==1.3.0
attrs==18.2.0
bcrypt==3.1.4
certifi==2018.11.29
cffi==1.11.5
chardet==3.0.4
Click==7.0
colorama==0.4.1
coreapi==2.3.3
coreschema==0.0.4
cryptography==2.2.2
cx-Oracle==6.4
cycler==0.10.0
dash==0.39.0
dash-core-components==0.44.0
dash-daq==0.1.0
dash-html-components==0.14.0
dash-renderer==0.20.0
dash-table==3.6.0
decorator==4.4.0
Django==1.11.9
django-filter==2.0.0
django-rest-swagger==2.2.0
django-taggit==0.23.0
djangorestframework==3.9.0
djangorestframework-jwt==1.11.0
Faker==0.9.0
Flask==1.0.2
Flask-Compress==1.4.0
future==0.16.0
httpie==1.0.2
idna==2.7
ipython-genutils==0.2.0
itsdangerous==0.24
itypes==1.1.0
Jinja2==2.10
jsonschema==3.0.1
jupyter-core==4.4.0
kiwisolver==1.0.1
macholib==1.11
Markdown==3.0.1
MarkupSafe==1.0
matplotlib==2.2.3
more-itertools==6.0.0
mysqlclient==1.3.14
nbformat==4.4.0
numpy==1.15.0
openapi-codec==1.3.2
pefile==2018.8.8
pitest==0.1
plotly==3.7.1
pluggy==0.9.0
py==1.8.0
pycparser==2.18
Pygments==2.3.1
PyInstaller==3.3.1
PyJWT==1.7.1
pymongo==3.8.0
pymssql==2.1.4
PyMySQL==0.9.1
pyparsing==2.2.0
pypiwin32==223
pyrsistent==0.14.11
pytest==4.3.0
pytest-html==1.20.0
pytest-metadata==1.8.0
pytest-ordering==0.6
python-dateutil==2.7.3
pytube==9.2.2
pytz==2018.5
pywin32==223
requests==2.21.0
retrying==1.3.3
selenium==3.141.0
simplejson==3.16.0
six==1.11.0
SQLAlchemy==1.2.18
text-unidecode==1.2
traitlets==4.3.2
uritemplate==3.0.0
urllib3==1.24.1
Werkzeug==0.14.1
Installing:-
django-admin startproject projectname
py manage.py startapp appname
add app in settings.py in installedapps 
create model in models.py file
register the model in the admin.py file if we want to display the data to the admin interface
py manage.py makemigrations:to generate sql code
py manage.py migrate:to execute the generated sql code from this table will be created in the database
create views for list of tasks and delete tasks and update tasks and create a new resource
write urlpattern for each view and link urlpatterns with the views
provide path for static and template files in settings.py so that django can aware about the location.
and start the development server with command:py manage.py runserver
and send the request with the url pattern and the corresponding view will be identified and and functionality will be displayed to the templatefile
create super user with the command:py manage.py createsuperuser and login to django-admin interface
Deployment to pythoanywhere.com:
make virtualenv with required installations and run the project in live bash console,add staticfiles and sourcecodepath and virtualenv path in the webapp.
and run the project and send the request 
