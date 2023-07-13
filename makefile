run:
	docker compose up -d

test:
	docker build -t urlshortener . && docker run urlshortener sh -c "python manage.py test"

stress-test:
	docker build -t urlshortener . && docker run urlshortener sh -c "apt update -y && apt install siege -y && siege -t60S -f test-urls.txt"

stop:
	docker stop urlshortener && docker stop prometheus && docker stop grafana

clean:
	docker rm urlshortener && docker rm prometheus && docker rm grafana