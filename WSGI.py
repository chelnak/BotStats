#!venv/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/botstats/")

from app import app as application

if __name__ == "__main__":
    application.run()
