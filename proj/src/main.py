import logging
import os

import log_handler
import scrap_data
import parse_data
import AthleteContainer

import database_handling.database_handler as db_handler
from config.config import BasicConfig





def main():
    log_handler.configure_logging_basic()
    logger = logging.getLogger(__name__)
    filename = 'test.html'

    athletes = AthleteContainer.AthleteContainer()
    db_h = db_handler.DataBaseHandler()
    db_h.create_athlete_table()

    urls = BasicConfig.generateUrls(BasicConfig.BASE_URL_FEMALE, BasicConfig.YEARS, 3)


    for url in urls:
        logger.info("Saving html ({0}) to file {1}".format(url, filename))
        scrap_data.save_html_to_file(url, filename)

        logger.info("Parsing html the file {}".format(filename))
        parsed_athletes = parse_data.parse_data(filename)
        athletes.concat_athletes(parsed_athletes)

        logger.info("Remove file: {}".format(filename))
        os.remove(filename)


    athletes.write_to_csv("parsedAthletes.csv")
    athletes.save_to_db()





if __name__ == "__main__":
    main()