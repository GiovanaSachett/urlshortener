from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import viewsets

from .exceptions import *
from .service import *


class URLView(viewsets.ViewSet):
    def create(self, request):
        try:
            shortened_url = shorten_url(request.body.decode('utf-8'))
        except UrlDestinationTooLongException:
            return HttpResponse("url too long", status=400)
        except UrlHashCollisionException:
            return HttpResponse("hash collision", status=500)

        return HttpResponse("http://0.0.0.0:8000/" + shortened_url)

    def retrieve(self, request, pk):
        try:
            original_url = get_original_url(pk)
        except UrlNotFoundException:
            return HttpResponse(status=404)
        except UrlDisabledException:
            return HttpResponse("url disabled", status=204)

        return HttpResponseRedirect("http://" + original_url)

    def update(self, request, pk):
        body = request.data
        if len(body) == 1:
            try:
                update_url(pk, list(body.keys())[0], list(body.values())[0])
            except UrlNotFoundException:
                return HttpResponse(status=404)
            except UrlUpdateException:
                return HttpResponse(status=400)
            return HttpResponse(status=200)
        return HttpResponse(status=400)
