run:
	docker build -t urlshortener . && docker run -p 8000:8000 -t urlshortener

test:
	docker build -t urlshortener . && docker run urlshortener sh -c "python manage.py test"

stress-test:
	siege -t60S -f test-urls.txt