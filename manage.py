#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

# test git push
# cambio en llave y git.config
# cambio en user.name
# correccion de user.email
# Prueba cambio de user.name


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practica.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
