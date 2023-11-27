import csv
import logging
import json

class AthleteContainer(object):
    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):
        self.athletes.append(athlete)

    def __str__(self):
        return f"{self.athletes}"

    def write_to_file(self, file_path):
        with open(file_path, 'w') as file:
            for athlete in self.athletes:
                file.write(f"{athlete}\n")

    def write_to_csv(self, file_path):
        with open(file_path, 'w') as file:
            writer = csv.writer(file)
            for athlete in self.athletes:
                writer.writerow([athlete.name, athlete.country, athlete.region, athlete.affiliate, athlete.age, athlete.size])

    def write_to_json(self, file_path):
        json_string = json.dumps([vars(athlete) for athlete in self.athletes])
        with open(file_path, 'w') as file:
            file.write(json_string)

    def log_athletes(self):
        logger = logging.getLogger(__name__)
        for athlete in self.athletes:
            logger.debug(athlete)