# coding=utf-8
from __future__ import unicode_literals, absolute_import

__version__ = "0.1.0"
__author__ = "webee.yw"
__license__ = "MIT"
__description__ = "extras commands to Flask-Script."
__uri__ = "https://github.com/webee/flask-script-extras"
__email__ = "webee.yw@gmail.com"

from flask.ext.script import Command

__all__ = ["Celery"]


class Celery(Command):
    """execute celery"""

    def __init__(self, celery_app):
        self.celery_app = celery_app
        self.capture_all_args = True

    def run(self, *args, **kwargs):
        self.celery_app.start(argv=['celery'] + args[0])
