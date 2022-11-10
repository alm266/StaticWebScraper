import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    URL = "https://realpython.github.io/fake-jobs/"
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='ResultsContainer')

    job_elements = results.find_all('div', class_='card-content')

    job_objects = []
    for job_element in job_elements:
        title_element = job_element.find('h2', class_='title')
        company_element = job_element.find('h3', class_='company')
        location_element = job_element.find('p', class_='location')

        link_url = job_element.find_all('a')[1]['href']

        job_objects.append({
            'title': title_element.text.strip(),
            'company': company_element.text.strip(),
            'location': location_element.text.strip(),
            'url': link_url
        })

    print(str(job_objects))
    python_jobs = results.find_all(
        'h2', string=lambda text: 'python' in text.lower()
    )

    python_job_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    print(python_jobs[0].text)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
