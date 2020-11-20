# TuLangRaPho
Official website of TuLangRaPho page

### Installation Guide

### Clone from Git
* `git clone git@github.com:phamngocthinh/TuLangRaPho.git`

### Make virtual environment
* virtualenv -p /usr/bin/python3 .venv

### Setup
* Create env setting file: `cp .env.sample .env`
* Install require packages: `.venv/bin/pip install -r requirements.txt`
* Run migrate: `.venv/bin/python manage.py migrate`
* Publish assets: `.venv/bin/python manage.py collectstatic`
* Create superuser `.venv/bin/python manage.py createsuperuser --email admin@mail.vn --username admin`.
* Using `admin123` as password.

### Startup
* Run project on port **8080** : `.venv/bin/python manage.py runserver 0.0.0.0:8080`
* Access `http://localhost:8080` for testing.

### Module api structure
```
.
├── home  
│   ├── admin           # Admin models  
│   ├── migrations      # Migrations  
│   ├── models          # Define models  
│   ├── tests           # Testing directory  
│   └── views           # Controllers  
├── static              # Static files  
│   └── images          # Images  
├── templates           # Contain html templates  
└── tlrp                # Contain settings, wsgi, urls files
```

### 📙 Libraries
- Django https://www.djangoproject.com/ 

### Contributing
If you want to contribute to this boilerplate, clone the repository and just start making pull requests.
