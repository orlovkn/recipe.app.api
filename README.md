### commands

```buildoutcfg
docker-compose build
```

start tests
```buildoutcfg
docker-compose run app sh -c "python manage.py test"
```

create an app
```buildoutcfg
docker-compose run app sh -c "python manage.py startapp core"
```

make migrations
```buildoutcfg
docker-compose run app sh -c "python manage.py makemigrations core"
```