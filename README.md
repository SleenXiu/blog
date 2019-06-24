# blog

a little blog based on Flask


~~development: [opehshift](http://blog-blog-xiu.a3c1.starter-us-west-1.openshiftapps.com/)~~


references
> Flask Web Development: Developing Web Applications with Python


```
export MAIL_PASSWORD='...'
```

```
python manage.py shell

> from app import db
> db.create_all()
> from app.models import Role
> Role.insert_roles()

```
