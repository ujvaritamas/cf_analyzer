import pytest
import os
import shutil
from bs4 import BeautifulSoup

import proj.src.parse_data as parser

class TestIntegration():
    TEST_PAGE_CONTENT_PATH = 'tests/test_file.txt'
    @pytest.fixture(scope='module')
    def project_file(self, tmpdir_factory):
        my_tmpdir = tmpdir_factory.mktemp("data")
        yield my_tmpdir
        shutil.rmtree(str(my_tmpdir))

    def test_parse_data__create_csv(self, project_file):

        test_file = os.path.join(project_file, "test.csv")

        parser.parse_data(TestIntegration.TEST_PAGE_CONTENT_PATH, result_path_csv= test_file)

        assert os.path.exists(test_file)

    def test_parse_data__create_json(self, project_file):

        test_file = os.path.join(project_file, "test.json")

        parser.parse_data(TestIntegration.TEST_PAGE_CONTENT_PATH, result_path_json= test_file)

        assert os.path.exists(test_file)

    def test_parse_data__create_json_and_scv(self, project_file):

        test_file_csv = os.path.join(project_file, "test.csv")
        test_file_json = os.path.join(project_file, "test.json")

        
        parser.parse_data(TestIntegration.TEST_PAGE_CONTENT_PATH, result_path_csv = test_file_csv, result_path_json= test_file_json)

        assert os.path.exists(test_file_csv)
        assert os.path.exists(test_file_json)

    def test_parse_info__custom_data_US(self):
        test_content ='''<div class="full-name"><div class="full-name">Mallory O'Brien</div>
        </div><div class="country-flag"><img src="https://assets.crossfit.com/build/img/sites/games/country-flags/us.svg" title="United States" alt="United States"></div></div><div class="bottom collapsed-hide">

        <ul class="info">
        <li>United States</li>
        <li>North America</li>
        <li>802 CrossFit</li>
        <li>Age 18</li>
        <li>63 in | 135 lb</li>

        <a href="/athlete/1239980" class="profile-link">View Profile</a></ul></div></div></td><td class="total-points"><div class="cell-inner">4</div></td><td data-workout="1" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">1st</span><span class="result"> (392 reps)</span></span></div><div class="details collapsed-hide"><div class="breakdown">13 rounds +<br>2 wall walks<br></div><div class="judge"><div>R. Judge: Mathew Fraser</div></div></div></div></td><td data-workout="2" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">2nd</span><span class="result"> (7:09)</span></span></div><div class="details collapsed-hide"><div class="breakdown">200 reps</div><div class="judge"><div>At: 802 CrossFit</div><div>R. Judge: Sara Franco</div></div></div></div></td><td data-workout="3" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">1st</span><span class="result"> (4:11)</span></span></div><div class="details collapsed-hide"><div class="breakdown">216 reps</div><div class="judge"><div>At: 802 CrossFit</div><div>R. Judge: Mathew Fraser</div></div></div></div></td></tr><tr class="collapsed"><td class="pos active-sort"><div class="cell-inner">2</div></td><td class="name"><div class="cell-inner"><div class="top"><div class="expand"></div>'''

        test_soup_obj = BeautifulSoup(test_content, "html.parser")

        test_result = parser.parse_info('test_name', test_soup_obj)

        assert test_result.name == 'test_name'
        assert test_result.age == 18
        assert test_result.weight == pytest.approx(61.235, rel = 1e-3)          #135lbs = 61.235kg
        assert test_result.height == pytest.approx(160.02, rel= 1e-3)           #63IN = 160.02cm

    def test_parse_info__custom_data_EU(self):
        test_content ='''<div class="full-name"><div class="full-name">Mallory O'Brien</div>
        </div><div class="country-flag"><img src="https://assets.crossfit.com/build/img/sites/games/country-flags/us.svg" title="United States" alt="United States"></div></div><div class="bottom collapsed-hide">

        <ul class="info">
        <li>United States</li>
        <li>North America</li>
        <li>802 CrossFit</li>
        <li>Age 18</li>
        <li>165 cm | 60 kg</li>

        <a href="/athlete/1239980" class="profile-link">View Profile</a></ul></div></div></td><td class="total-points"><div class="cell-inner">4</div></td><td data-workout="1" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">1st</span><span class="result"> (392 reps)</span></span></div><div class="details collapsed-hide"><div class="breakdown">13 rounds +<br>2 wall walks<br></div><div class="judge"><div>R. Judge: Mathew Fraser</div></div></div></div></td><td data-workout="2" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">2nd</span><span class="result"> (7:09)</span></span></div><div class="details collapsed-hide"><div class="breakdown">200 reps</div><div class="judge"><div>At: 802 CrossFit</div><div>R. Judge: Sara Franco</div></div></div></div></td><td data-workout="3" class="score"><div class="cell-inner"><div class="rank-result"><span><span class="rank">1st</span><span class="result"> (4:11)</span></span></div><div class="details collapsed-hide"><div class="breakdown">216 reps</div><div class="judge"><div>At: 802 CrossFit</div><div>R. Judge: Mathew Fraser</div></div></div></div></td></tr><tr class="collapsed"><td class="pos active-sort"><div class="cell-inner">2</div></td><td class="name"><div class="cell-inner"><div class="top"><div class="expand"></div>'''

        test_soup_obj = BeautifulSoup(test_content, "html.parser")

        import pdb; pdb.set_trace()
        test_result = parser.parse_info('test_name', test_soup_obj)

        assert test_result.name == 'test_name'
        assert test_result.age == 18
        assert test_result.weight == pytest.approx(60, rel = 1e-3)          #135lbs = 61.235kg
        assert test_result.height == pytest.approx(165, rel= 1e-3)           #63IN = 160.02cm