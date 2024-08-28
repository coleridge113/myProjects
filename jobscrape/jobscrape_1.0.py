from bs4 import BeautifulSoup
import requests


def jobstreet_scrape(*keywords):
    JOBSTREET = 'https://www.jobstreet.com.ph'
    search = '/' + '-'.join(list(keywords)) + '-jobs'
    html_text = requests.get(JOBSTREET+search).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('div', class_='_1decxdv0 _6e905u0 _6e905u5')

    list_jobs = []
    for job in jobs:
        position = job.find('div', class_='_1decxdv0 _110qf3s5g _110qf3s52')
        company = job.find('span', class_='_1decxdv0 _110qf3s4y _1vcc81d0 _1vcc81d1 _1vcc81d21 _1708b944 _1vcc81da')
        link = job.find('div', class_='_1decxdv0 _110qf3s5g _110qf3s52')

        if position is not None and 'Python' in position.text:
            details = [position.text, company.text.split('at')[1].strip(),JOBSTREET + link.a['href']]
            if details not in list_jobs:
                list_jobs.append(details)

    def display_jobs():
        print('')
        print(f"Found {len(list_jobs)} positions\n")
        for job in list_jobs:
            print(f"Position: {job[0]}")
            print(f"Company: {job[1]}")
            print(f"Link: {job[2]}")
            print('')

    display_jobs()


if __name__ == "__main__":
    jobstreet_scrape('junior','python','developer')
