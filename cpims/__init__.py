from .celery import app as celery_app

__version__ = '2.0.3'
VERSION = __version__

# Celery
__all__ = ("celery_app",)
