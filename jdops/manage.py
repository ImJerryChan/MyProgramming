#!/usr/bin/env python
import os
import sys


def main():
    profile = os.environ.setdefault('AUTOOPS_PROFILE', 'develop')
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jdops.settings.%s" % profile)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
