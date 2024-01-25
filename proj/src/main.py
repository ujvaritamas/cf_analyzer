import logging
import os

import log_handler
import scrap_data
import parse_data
import AthleteContainer

import database_handling.database_handler as db_handler


URLS = ["https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=2",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=3",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=4",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=5",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=6",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=7",
        "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=8",
        ]


def main():
    log_handler.configure_logging_basic()
    logger = logging.getLogger(__name__)
    filename = 'test.html'

    athletes = AthleteContainer.AthleteContainer()
    db_h = db_handler.DataBaseHandler()
    db_h.create_athlete_table()

    for url in URLS:
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