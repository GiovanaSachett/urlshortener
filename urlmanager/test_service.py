import pytest
from django.test import TestCase
from .service import *
from .exceptions import *
from .models import *

import random


class UrlServiceShortenTestCase(TestCase):

    def test_shorten_url_success(self):
        response = shorten_url("abc.com")
        self.assertEqual(len(response), HASH_SIZE)

    def test_shorten_url_too_long(self):
        with pytest.raises(UrlDestinationTooLongException):
            shorten_url("a"*(MAX_URL_SIZE+1))

    def test_shorten_url_hash_collision_retry(self):
        random.seed(2)
        shorten_url("abc.com")
        random.seed(2)
        shorten_url("cde.com")



class UrlServiceGetOriginalTestCase(TestCase):

    def test_get_original_url_not_found(self):
        with pytest.raises(UrlNotFoundException):
            get_original_url("a")

    def test_get_original_url_enabled(self):
        URL.objects.create(
            original_url="abc.com",
            enabled=True,
            hash="a"
        )
        response = get_original_url("a")
        self.assertEqual(response,"abc.com")


    def test_get_original_url_disabled(self):
        URL.objects.create(
            original_url="abc.com",
            enabled=False,
            hash="b"
        )
        with pytest.raises(UrlDisabledException):
            get_original_url("b")



class UrlServiceUpdateTestCase(TestCase):

    def test_update_url_not_found(self):
        with pytest.raises(UrlNotFoundException):
            update_url("a", "field", "new_info")

    def test_update_url_enabled_field(self):
        url = URL.objects.create(
            original_url="abc.com",
            enabled=True,
            hash="a"
        )
        update_url("a", 'enabled', False)
        url.refresh_from_db()
        self.assertFalse(url.enabled)

    def test_update_url_destination_field(self):
        url = URL.objects.create(
            original_url="abc.com",
            enabled=True,
            hash="a"
        )
        update_url("a", 'destination', 'cde.com')
        url.refresh_from_db()
        self.assertEqual(url.original_url, 'cde.com')

    def test_update_url_destination_field_too_long(self):
        URL.objects.create(
            original_url="abc.com",
            enabled=True,
            hash="a"
        )
        with pytest.raises(UrlDestinationTooLongException):
            update_url("a", 'destination', 'm'*(MAX_URL_SIZE+1))

    def test_update_url_invalid_field(self):
        URL.objects.create(
            original_url="abc.com",
            enabled=True,
            hash="a"
        )
        with pytest.raises(UrlUpdateException):
            update_url("a", "field", False)

