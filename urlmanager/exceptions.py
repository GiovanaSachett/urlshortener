class UrlNotFoundException(Exception):
    """
    Exception thrown when the url was not found
    """


class UrlUpdateException(Exception):
    """
    Exception thrown when the update was not successful
    """


class UrlDestinationTooLongException(Exception):
    """
    Exception thrown when the url to be shortened is too long
    """


class UrlDisabledException(Exception):
    """
    Exception thrown when the url is disabled
    """


class UrlHashCollisionException(Exception):
    """
    Exception thrown when there is a hash collision
    """
