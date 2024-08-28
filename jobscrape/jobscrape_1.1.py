from bs4 import BeautifulSoup
import requests


def jobstreet_scrape(*keywords, filter=None):
    JOBSTREET = 'https://www.jobstreet.com.ph'
    search = '/' + '-'.join(list(keywords)) + '-jobs'
    html_text = requests.get(JOBSTREET+search).text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('article', class_='_1decxdv0 _1decxdv1 _110qf3s7i _110qf3s6e _110qf3s9q _110qf3s8m _110qf3sh _110qf3s66 _110qf3s5e pj3kj2b pj3kj29 pj3kj2a _1vcc81d18 _1vcc81d1b _110qf3s32 _110qf3s35')

    listed_jobs = []
    for job in jobs:
        position = job['aria-label']
        company = job.find('span', class_='_1decxdv0 _110qf3s4y _1vcc81d0 _1vcc81d1 _1vcc81d21 _1708b944 _1vcc81da').text.split('at')[1].strip()
        listed_time = job.find('div', class_='_1decxdv0 _110qf3s5i _110qf3s0 ggz3ey0').text
        link = job.find('div', class_='_1decxdv0 _110qf3s5g _110qf3s52')

        job_details = {
            'Position': position,
            'Company': company,
            'Listed Time': listed_time,
            'Link': JOBSTREET + link.a['href'],
        }

        if filter and filter not in job_details['Position'] or 'days' in job_details['Listed Time']:
            continue
        else:
            listed_jobs.append(job_details)

    def display():
        print(f"Found {len(listed_jobs)} jobs!")
        print('')
        for job in listed_jobs:
            print(job['Position'])
            print(job['Company'])
            print(job['Listed Time'])
            print(job['Link'])
            print('')

    display()




if __name__ == "__main__":
    jobstreet_scrape('junior', 'python', 'developer', filter='Python')