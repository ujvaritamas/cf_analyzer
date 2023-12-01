import logging

def configure_logging_basic():
    logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(name)s  %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

    # set up logging to file

    logging.info('Logger configured')




