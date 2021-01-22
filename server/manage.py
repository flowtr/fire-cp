#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from server.config import config
from django.core.management.commands.runserver import Command as runserver
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
django.setup()


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
    host = config.get().host
    port = config.get().port

    runserver.default_port = port
    runserver.default_addr = host

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
