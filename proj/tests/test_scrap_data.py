import pytest
import shutil
import os

import proj.src.scrap_data as scrapper

class TestIntegrationScrap():

    TEST_PAGE_CONTENT_PATH = 'tests/test_file.txt'
    @pytest.fixture(scope='module')
    def create_test_dir(self, tmpdir_factory):
        my_tmpdir = tmpdir_factory.mktemp("data")
        yield my_tmpdir
        shutil.rmtree(str(my_tmpdir))

    @pytest.mark.skip(reason="This is for debugging selenium")
    def test_save_html_to_file(self, create_test_dir):
        test_url = "https://games.crossfit.com/leaderboard/open/2022?view=0&division=2&region=0&scaled=0&sort=0"
        test_file = os.path.join(create_test_dir, "test.html")

        scrapper.save_html_to_file(test_url, test_file)

        assert os.path.exists(test_file)


