# Captain Console

## Environmental Variables
Eftirfarandi env breytur þurfa að vera rétt stilltar til að ná gagnagrunnstengingu.
- DB_NAME: captain_console
- DB_USER: postgres
- DB_PASSWORD: AnnaðVerklegaNámskeiðið
- DB_HOST: captainconsole47.ddns.net
- DB_PORT: 5432
- DB_ENGINE: django.db.backends.postgresql
- DATABASE_URL: postgres://postgres:p4ssw0rd@captainconsole47.ddns.net/captain_console
- ENV: development

- PORT=8000 # Svo heroku local sé á réttu porti.

## Installing
virtualenv venv
. venv/bin/activate
pip install -r requirements.txt

## Gulp Skipanir
gulp scss

gulp watch

## Local Deployment
heroku local 

eða 

python3 manage.py runserver

## Remote Deployment
git push heroku master

## Testing
### Frontend testing
npm run test-rest


### Run pytest stuff
python3 -m pytest tests

### Run django tests
python3 manage.py test



## Links
### SASS/SCSS
- https://sass-lang.com/guide
- https://www.w3schools.com/sass/

### Chai.js
- https://buddy.works/guides/how-automate-nodejs-unit-tests-with-mocha-chai
- https://www.chaijs.com

### pytest
- https://docs.pytest.org/en/latest/

### Django REST Framework
- https://www.django-rest-framework.org

### PostgreSQL
https://www.postgresql.org


### JSONAPI
https://jsonapi.org
