from bs4 import BeautifulSoup
import requests
import time
import os
def find_jobs():
    page = 0
    while page != 50:
        html_text = requests.get(f'https://jobbsafari.se/lediga-jobb?q=python&page={page}').text.encode('utf8').decode('ascii', 'ignore')
        page = page + 1
        soup = BeautifulSoup(html_text, 'lxml')
        jobs = soup.find_all('a', class_='Link__StyledLink-r4qx99-0 gklRDo JobCard__JobLink-sc-13r9v14-0 cgCLde')
        lacking_skillset_and_experience = ["Linux", "Java", "Senior"]
        l = lacking_skillset_and_experience
        for index, job in enumerate(jobs):
            Job_title = job.get('aria-label')
            link = "jobbsafari.se"+job.get('href')
            if l[0] not in Job_title and l[1] not in Job_title and l[2] not in Job_title:
                Company_place = job.find('p', class_='Bold-l7d4pe-0 Default__EmployerAndRegion-sc-1r9u2f-2 dHQklC hTUlBE') or job.find('p', class_='Bold-l7d4pe-0 Volume__EmployerRegion-novs97-4 dHQklC kmSPrK')
                Employment_type = job.find('span', class_ ='Default__WorkingHours-sc-1r9u2f-3 LzxXB') or job.find('span', class_='Volume__WorkingHours-novs97-5 FNHVA') or job.find('span', class_='Default__EmploymentType-sc-1r9u2f-4 kgKEQ')
                with open(f'jobscrape/{page }{index}.txt', 'w') as f:
                        f.write(f"Job title: {Job_title} \n")
                        f.write(f"Company and place: {Company_place.text} \n")
                        f.write(f"Employment type: {Employment_type.text} \n")
                        f.write(f"Link to job ad: {link} \n")
                        f.write("\n")
                        print(f'File saved:{page } {index}')
                        list_ = []
                        for file in os.listdir("jobscrape"):
                            if file.endswith(".txt"):
                                list_.append(os.path.join("jobscrape",file))
                with open (f'jobscrape/merged_job_ads.text', 'w') as outfile:
                    for fname in list_:
                        with open(fname,encoding="utf-8", errors='ignore') as infile:
                            outfile.write(infile.read())
if __name__== '__main__':
        while True:
            find_jobs()
            time_wait = 10
            print(f'waiting{time_wait} seconds...')
            time.sleep(time_wait * 10)