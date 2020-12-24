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
```

make migrations
```buildoutcfg
docker-compose run app sh -c "python manage.py makemigrations core"
```