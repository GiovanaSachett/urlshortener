run:
	docker build -t urlshortener . && docker run -p 8000:8000 -t urlshortener

test:
	docker build -t urlshortener . && docker run urlshortener sh -c "python manage.py test"

stress-test:
	docker build -t urlshortener . && docker run urlshortener sh -c "siege -t60S -f test-urls.txt"

stop:
    docker stop urlshortener

clean:
    docker rm urlshortener && docker rmi urlshortener