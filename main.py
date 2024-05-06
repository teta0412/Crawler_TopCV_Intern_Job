import time
import csv
import requests
from bs4 import BeautifulSoup


def web_scrap(url):
    job_lists = []
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        html_lists = soup.find('div', class_='job-list-2')
        jobs = html_lists.find_all('div', class_='job-item-2')
        for j in jobs:
            job_url = j.find('h3', class_='title').find('a').get('href')
            if job_url.startswith("https://www.topcv.vn/viec-lam/"):
                time.sleep(10)
                job_detail = job_scrap(job_url)
                if job_detail is not None:
                    job_lists.append(job_detail)
            else:
                print("Error link : " + job_url)
                time.sleep(10)
    else:
        print(str(response.status_code) + " web error")
    return job_lists


def job_scrap(job_url):
    response = requests.get(job_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        html_list = soup.find('div', class_="job-detail")
        job_data = html_list.find_all('div', class_="job-detail__body")
        for j in job_data:
            job_title = j.find('h1', class_="job-detail__info--title").get_text().strip()
            job_company = j.find('h2', class_="company-name-label").find('a').get_text().strip()
            # job_company_link = j.find('div', class_="job-detail__company--link").find('a').get('href')
            job_address = j.find('div', class_="job-detail__company--information-item company-address").find('div',
                                                                                                             class_="company-value").get_text().strip()
            job_salary = j.find('div', class_="job-detail__info--section-content-value").get_text().strip()
            job_deadline = j.find('div', class_="job-detail__info--deadline").get_text().strip()
            tmp = {
                'Job Title': job_title,
                'Salary': job_salary,
                'Company': job_company,
                'Location': job_address,
                'Due Date': job_deadline,
                'Job Link': job_url
            }
            return tmp
    else:
        print(str(response.status_code) + " job error")
    time.sleep(10)  # Must have


def write_to_csv(mydict):
    fields = ['Job Title', 'Salary', 'Company', 'Location', 'Due Date', 'Job Link']
    file_name = 'crawl_intern_job.csv'
    with open(file_name, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers (field names)
        writer.writeheader()

        # writing data rows
        writer.writerows(mydict)


def append_to_csv(mydict):
    # Path to the existing CSV file
    csv_file_path = 'crawl_intern_job.csv'

    # Append data to the CSV file
    with open(csv_file_path, 'a', newline='') as csvfile:
        # Define the writer object with delimiter and quoting options
        writer = csv.DictWriter(csvfile, fieldnames=mydict[0].keys())

        # Write header only if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write data from the list of dictionaries
        for row in mydict:
            writer.writerow(row)

    print("Data appended to CSV file successfully.")


def main():
    for pageNum in range(1, 3):
        url = 'https://www.topcv.vn/viec-lam-it?sort=&skill_id=&skill_id_other=&keyword=&company_field=&position=50&salary=&page='+str(pageNum)
        print(url)
        data = web_scrap(url)
        time.sleep(10)
        if pageNum == 1:
            write_to_csv(data)
        else:
            append_to_csv(data)


main()
