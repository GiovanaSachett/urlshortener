import random
import string
from .models import URL, MAX_URL_SIZE, HASH_SIZE
from .exceptions import *
from django.db.utils import IntegrityError
from django.db import transaction

MAX_RETRY_SAFETY = 10

def _validate_url(url_string):
    if len(url_string) > MAX_URL_SIZE:
        raise UrlDestinationTooLongException


def shorten_url(url):
    _validate_url(url)

    retry = 0
    while retry < MAX_RETRY_SAFETY:
        url_hash = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(HASH_SIZE))
        try:
            with transaction.atomic():
                URL.objects.create(
                    original_url=url,
                    hash=url_hash,
                    enabled=True
                )
                return url_hash
        except IntegrityError:
            retry += 1

    raise UrlHashCollisionException



def get_original_url(url_hash):
    try:
        url = URL.objects.get(hash=url_hash)
    except URL.DoesNotExist:
        raise UrlNotFoundException

    if url.enabled:
        return url.original_url
    raise UrlDisabledException


def update_url(url_hash, field, new_info):
    try:
        url = URL.objects.get(hash=url_hash)
    except URL.DoesNotExist:
        raise UrlNotFoundException

    if field == 'enabled':
        url.enabled = new_info
    elif field == 'destination':
        _validate_url(new_info)
        url.original_url = new_info
    else:
        raise UrlUpdateException

    url.save()
    return
