
from requests import get
from bs4 import BeautifulStoneSoup
# open(file,encoding='UTF-8')

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_item = "python"

response = get(f"{base_url}{search_item}")
if response.status_code != 200:
    print("Can't request website")
else:
    results = []
    soup = BeautifulStoneSoup(response.text, 'html.parser')
    # print(soup.find_all('title'))
    jobs = soup.find_all('section', class_="jobs")
    # print(len(jobs))
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            company, kind, region = anchor.find_all('span', class_="company")
            title = region.string, title.string
            job_data = {
                'company' : company.string,
                'region' : region.string,
                'position' : title.string
            }
            results.append(job_data)
    for result in results:
        print(result)
        print("///////////")
    