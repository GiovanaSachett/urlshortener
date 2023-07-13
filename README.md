# URL Shortener
Technical chalange

## Description

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