import logging

import log_handler

logger = logging.getLogger(__name__)

def main():
    log_handler.configure_logging_basic()


if __name__ == "__main__":
    main()