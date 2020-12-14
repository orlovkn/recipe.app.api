### commands

start tests
```buildoutcfg
docker-compose run app sh -c "python manage.py test"
```

create an app
```buildoutcfg
docker-compose run app sh -c "python manage.py startapp core"
```

make migrations
```
docker-compose run app sh -c "python manage.py makemigrations core"
```