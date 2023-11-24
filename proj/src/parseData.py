from bs4 import BeautifulSoup

with open('file.txt', 'r') as file:
    data = file.read().replace('\n', '')



def parse_data(page_content):
    soup = BeautifulSoup(page_content, "html.parser")

    athlete_table = soup.find_all("table", {"class": "desktop athletes"})
    import pdb; pdb.set_trace()

    t_body = athlete_table[0].find_all('tbody')[0]

    for athlete_top in t_body.find_all('tr'):
        name = athlete_top.find_all("div", {"class": "full-name"})[0].text
        info_ul_list = athlete_top.find_all("ul", {"class": "info"})[0].find_all("li")
        country = info_ul_list[0].text
        region = info_ul_list[1].text
        affiliate = info_ul_list[2].text
        age = info_ul_list[3].text
        size = info_ul_list[4].text
        print(name, country, region, affiliate, age, size)

parse_data(data)

