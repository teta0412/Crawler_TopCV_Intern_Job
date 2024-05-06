## TopCV Job Scraper

This Python script scrapes job listings from the TopCV website, focusing on IT positions. It extracts details like job title, company, salary, location, and deadline, and saves them to a CSV file named "crawl_intern_job.csv".

### Dependencies

The script relies on the following external libraries:

* `requests`: Handles making HTTP requests to websites. [requests library](https://requests.readthedocs.io/)
* `BeautifulSoup`: Parses HTML content retrieved from websites. [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#)
* `csv`: Used for working with CSV files. Part of the Python standard library.

### Functionality

1. **Web Scraping (`web_scrap` function):**
   - Takes a job listing URL as input.
   - Fetches the webpage content using `requests.get`.
   - Parses the HTML content with `BeautifulSoup`.
   - Extracts job details from the listings section and recursively calls itself for nested job URLs (starting with "[https://www.topcv.vn/viec-lam/](https://www.topcv.vn/viec-lam/)").
   - Implements a 10-second delay between requests to avoid overwhelming the server.
   - Returns a list of dictionaries containing scraped job data.

2. **Job Detail Extraction (`job_scrap` function):**
   - Takes a specific job detail URL as input.
   - Fetches the webpage content using `requests.get`.
   - Parses the HTML content with `BeautifulSoup`.
   - Extracts job title, company name, address, salary, deadline, and job URL.
   - Returns a dictionary containing the extracted job information.

3. **Writing to CSV (`write_to_csv` function):**
   - Takes a list of dictionaries containing job data as input.
   - Creates a new CSV file named "crawl_intern_job.csv".
   - Writes the header row with field names ("Job Title", "Salary", "Company", "Location", "Due Date", "Job Link").
   - Writes each job dictionary as a separate row in the CSV file.

4. **Appending to CSV (`append_to_csv` function):**
   - Takes a list of dictionaries containing job data as input.
   - Opens the existing "crawl_intern_job.csv" file in append mode.
   - Writes the header row only if the file is empty.
   - Appends each job dictionary as a new row to the CSV file.

5. **Main Function (`main`):**
   - Iterates through a loop for a specified number of pages (default: 2).
   - Constructs the URL for each page of IT job listings on TopCV.
   - Calls the `web_scrap` function to scrape job listings from that page.
   - Writes the scraped data from the first page to a new CSV file using `write_to_csv`.
   - Appends scraped data from subsequent pages to the existing CSV file using `append_to_csv`.

### Running the Script

1. Ensure you have Python 3 and the required libraries (`requests`, `BeautifulSoup`) installed. You can install them using `pip install requests beautifulsoup4`.
2. Save the script as a Python file (e.g., `topcv_job_scraper.py`).
3. Execute the script from your terminal using `python topcv_job_scraper.py`.

This will scrape job listings from the first two pages (or a different number of pages if you modify the loop in the `main` function) of IT positions on TopCV and save the extracted data to "crawl_intern_job.csv".

### Notes

* The script includes a 10-second delay between requests to avoid overloading the TopCV website. Adjust this delay if necessary, but be mindful of website scraping etiquette.
* The script currently targets IT positions on TopCV. You can modify the URL construction in the `main` function to scrape jobs from other categories.
* Error handling is included for potential issues like invalid URLs or website errors.
