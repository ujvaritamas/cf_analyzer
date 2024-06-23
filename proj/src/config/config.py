class BasicConfig:
    BASE_URL_FEMALE = "https://games.crossfit.com/leaderboard/open/{year}?division=2&region=0&sort=0"
    BASE_URL_MALE = "https://games.crossfit.com/leaderboard/open/{year}?division=1&region=0&sort=0"

    YEARS = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
    PAGES_PER_YEAR = 8  # Assuming there are 8 pages for each year


    def generateUrls(base_url, years, pages_per_year)-> list:
        # Loop through each year and construct the URLs for each page
        urls = []
        for year in years:
            year_urls = [base_url.format(year=year)]
            for page in range(2, pages_per_year + 1):
                year_urls.append(f"{base_url.format(year=year)}&page={page}")
            urls += year_urls
        return urls

    TESTURLS = ["https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=2",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=3",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=4",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=5",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=6",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=7",
            "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0&page=8",
            ]