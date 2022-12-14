#!/usr/bin/env python


from page_loader import download
from page_loader.cli import parse
import logging
import sys


def main():

    logging.basicConfig()
    logger = logging.getLogger()

    try:
        args = parse()
        print(download(args.url, path=args.output))
        sys.exit(0)
    except Exception as ex:
        logger.error(ex)
        sys.exit(1)


if __name__ == '__main__':
    main()
