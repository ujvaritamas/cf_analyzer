import logging

import log_handler
import scrap_data


url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"

def main():
    log_handler.configure_logging_basic()
    logger = logging.getLogger(__name__)

    scrap_data.save_html_to_file(url, 'test.html')


if __name__ == "__main__":
    main()