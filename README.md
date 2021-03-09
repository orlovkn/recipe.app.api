### commands

```buildoutcfg
docker-compose build
```

run the server
```buildoutcfg
docker-compose up
```

start tests
```buildoutcfg
docker-compose run app sh -c "python manage.py test"
docker-compose run app sh -c "python manage.py test && flake8"
```

create an app
```buildoutcfg
docker-compose run app sh -c "python manage.py startapp core"
docker-compose run --rm app sh -c "python manage.py startapp user"
```

make migrations
```buildoutcfg
docker-compose run app sh -c "python manage.py makemigrations core"
```

address
```buildoutcfg
http://127.0.0.1:8000/
```

create a superuser
```buildoutcfg
docker-compose run app sh -c "python manage.py createsuperuser"
```