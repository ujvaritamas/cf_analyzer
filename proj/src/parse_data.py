from bs4 import BeautifulSoup
import os
import re
import logging

import Athlete
import AthleteContainer

class WeightHeightConverter():
    INCH_TO_CM_CONVERSION_VALUE = 2.54
    LBS_TO_KG_CONVERSION_VALUE = 0.45359237

    @staticmethod
    def convert_inch_to_cm(height_in_inch):
        return float(height_in_inch) * WeightHeightConverter.INCH_TO_CM_CONVERSION_VALUE

    @staticmethod
    def convert_lbs_to_kg(weight_in_lbs):
        return float(weight_in_lbs) * WeightHeightConverter.LBS_TO_KG_CONVERSION_VALUE

def read_data_from_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read().replace('\n', '')
    return data

def parse_info(atlete_name:str, page_content) -> Athlete.Athlete:
    info_list = page_content.find_all("ul", {"class": "info"})[0].find_all("li")
    age_pattern = re.compile(r'Age (\d+)')
    weight_lbs_pattern = re.compile(r'(\d+) lb')
    weight_kg_pattern = re.compile(r'(\d+) kg')
    height_in_pattern = re.compile(r'(\d+) in')
    height_cm_pattern= re.compile(r'(\d+) cm')
    age = None
    weight = None
    height = None
    for info in info_list:

        # Finding the match
        age_match = age_pattern.search(info.text)

        # Extracting the age value
        if age_match:
            age = int(age_match.group(1))

        weight_lbs_match = weight_lbs_pattern.search(info.text)
        weight_kg_match = weight_kg_pattern.search(info.text)
        height_in_match = height_in_pattern.search(info.text)
        height_cm_match = height_cm_pattern.search(info.text)

        if weight_lbs_match:
            weight = WeightHeightConverter.convert_lbs_to_kg(weight_lbs_match.group(1))
        if weight_kg_match:
            weight = float(weight_kg_match.group(1))
        if height_in_match:
            height = height_in_match.group(1)
            height = WeightHeightConverter.convert_inch_to_cm(height_in_match.group(1))
        if height_cm_match:
            height = float(height_cm_match.group(1))

    return Athlete.Athlete(atlete_name, age, height, weight)

def parse_data(page_content_path, result_path_csv = None, result_path_json = None):

    logger = logging.getLogger(__name__)

    athletes = AthleteContainer.AthleteContainer()

    page_content = read_data_from_file(page_content_path)
    logger.info("Read page content from file finished.")

    soup = BeautifulSoup(page_content, "html.parser")
    athlete_table = soup.find_all("table", {"class": "desktop athletes"})
    t_body = athlete_table[0].find_all('tbody')[0]

    logger.info("Parsing athletes")
    for athlete_top in t_body.find_all('tr'):
        name = athlete_top.find_all("div", {"class": "full-name"})[0].text

        athletes.add_athlete(parse_info(name, athlete_top))

    athletes.log_athletes()
    if result_path_csv:
        athletes.write_to_file(result_path_csv)
    if result_path_json:
        athletes.write_to_json(result_path_json)

#parse_data(data)

