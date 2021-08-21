"""
Custom Storages
----------------

Custom Storages for AWS.
"""

from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """Sets location for Static Storage."""
    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """Sets location for Media Storage."""
    location = settings.MEDIAFILES_LOCATION
