# URL Shortener
A 

## Description
The project has one main app that is the urlshotener, it has the main configurations of the project. Also, there is the urlmanager app that is responsible for the url operations. In this app we have two main files:
- `views.py`: creates the views, i.e., our endpoints, makes the calls to the service;
- `service.py`: responsible to make the operations with the database.

![image](https://github.com/GiovanaSachett/urlshortener/assets/23011531/b91f3b66-68a1-4925-97a1-98ad261416e1)


## Running

- `make run` to run your server

- `make test` to run the unit tests

- `make stress-test` to run the siege stress test (for this you need to have the application running)

## Requesting
### shortening a url

```
curl  -w '\n' --location --request POST 'http://0.0.0.0:8000/' \
--header 'Content-Type: application/json' \
--data-raw '<url to be shortened>'
```

### updating a url
The put request updates the url given a url hash. There are two properties accepted, `description` and `enabled`

```
curl -w '\n' --location --request PUT 'http://0.0.0.0:8000/<url hash>' \
--header 'Content-Type: application/json' \
--data-raw '{"destination": "<new url>"}'
```
