#!/usr/bin/env python
import os
import sys

import dotenv

if __name__ == "__main__":
    dotenv.load()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cse_slack_bot.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
