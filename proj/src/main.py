import logging
import os
import pandas as pd

import log_handler
import scrap_data
import parse_data
import AthleteContainer


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

    for url in URLS:
        scrap_data.save_html_to_file(url, 'test.html')
        parsed_athletes = parse_data.parse_data(filename)
        athletes.concat_athletes(parsed_athletes)
        os.remove(filename)


    athletes.write_to_csv("parsedAthletes.csv")





if __name__ == "__main__":
    main()