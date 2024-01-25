import csv
import logging
import json
import Athlete

import database_handling.database_handler as db_handler

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
            writer.writerow(Athlete.Athlete.get_header())
            for athlete in self.athletes:
                writer.writerow(athlete.list_csv())

    def write_to_json(self, file_path):
        json_string = json.dumps([vars(athlete) for athlete in self.athletes])
        with open(file_path, 'w') as file:
            file.write(json_string)

    def log_athletes(self):
        logger = logging.getLogger(__name__)
        for athlete in self.athletes:
            logger.info(athlete)

    def concat_athletes(self, athletes_obj):
        self.athletes = self.athletes + athletes_obj.athletes

    def save_to_db(self):
        db_h = db_handler.DataBaseHandler()
        for athlete in self.athletes:
            db_h.insert_athlete(athlete)
