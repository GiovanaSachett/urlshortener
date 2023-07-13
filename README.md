# URL Shortener
Application to shorten urls.

## Description

This is a [django](https://www.djangoproject.com/) project. The main architecture is structured in a urlshotener app, which has the project settings and a urlmanager app that does the main operations for URLs, create, retrieve and update.

![Captura de tela de 2023-07-12 09-35-46](https://github.com/GiovanaSachett/urlshortener/assets/23011531/394c2bf2-cd1d-4f9a-8879-3fc330dba02a)

### Stress test
The tool for stress test used was [siege](https://github.com/JoeDog/siege).

![Captura de tela de 2023-07-13 18-32-02](https://github.com/GiovanaSachett/urlshortener/assets/23011531/a0ace65d-40db-4a31-8cdb-21fe920717f2)

### Prometheus and Grafana

For monitoring there is the [prometheus](https://prometheus.io/) and [grafana](https://grafana.com/) tools 
The bellow graph is the responses for the requisitions using the siege test. The data source used by grafana is in the url `http://prometheus:9090`. 

![Captura de tela de 2023-07-13 17-32-50](https://github.com/GiovanaSachett/urlshortener/assets/23011531/83c3a1ae-3d87-42d5-8f28-ed7ce42b9338)


## Running

- `make run` to run your server

- `make test` to run the unit tests

- `make stress-test` to run the siege stress test (for this you need to have the application running)

- `make stop` to stop the containers

- `make clean` to remove the containers

## Requesting
### shortening a url

```
curl  -w '\n' --location --request POST 'http://0.0.0.0:8000/u/' \
--header 'Content-Type: application/json' \
--data-raw '<url to be shortened>'
```

### updating a url
The put request updates the url given a url hash. There are two properties accepted, `destination` or `enabled`.

Update url:
```
curl -w '\n' --location --request PUT 'http://0.0.0.0:8000/u/<url hash>' \
--header 'Content-Type: application/json' \
--data-raw '{"destination": "<new url>"}'
```

Enable or disable url:
```
curl -w '\n' --location --request PUT 'http://0.0.0.0:8000/u/<url hash>' \
--header 'Content-Type: application/json' \
--data-raw '{"enabled": true}'
```
