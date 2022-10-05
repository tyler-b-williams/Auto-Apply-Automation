# !install selenium!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import getpass
import time
import re

# variable initialization
chromeDriverPath = 'Auto-Apply-Automation/chromedriver_win32/chromedriver.exe'
email = 'tylerbrentwilliams@gmail.com'
job_queries_dic = {'easy apply entry full time associate data analyst remote': 'https://www.linkedin.com/jobs/search/?currentJobId=3183780921&distance=25&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=2&geoId=103644278&keywords=associate%20data%20analyst&sortBy=R',
                   'easy apply entry full time associate data analyst hybrid/onsite': 'https://www.linkedin.com/jobs/search/?currentJobId=3112257270&distance=25&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=1%2C3&geoId=100249151&keywords=associate%20data%20analyst&location=Rockville%2C%20Maryland%2C%20United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time junior data analyst remote': 'https://www.linkedin.com/jobs/search/?currentJobId=3254138415&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=2&geoId=103644278&keywords=junior%20data%20analyst&location=United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time junior data analyst hybrid/onsite': 'https://www.linkedin.com/jobs/search/?currentJobId=3161099022&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=1%2C3&geoId=100249151&keywords=junior%20data%20analyst&location=Rockville%2C%20Maryland%2C%20United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time intern data analyst remote': 'https://www.linkedin.com/jobs/search/?currentJobId=3254138415&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=2&geoId=103644278&keywords=junior%20data%20analyst&location=United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time intern data analyst hybrid/onsite': 'https://www.linkedin.com/jobs/search/?currentJobId=3245367348&distance=25&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=1%2C3&geoId=100249151&keywords=intern%20data%20analyst&location=Rockville%2C%20Maryland%2C%20United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time business analyst remote': 'https://www.linkedin.com/jobs/search/?currentJobId=3051705411&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=2&geoId=103644278&keywords=business%20analyst&location=United%20States&refresh=true&sortBy=R',
                   'easy apply entry full time business analyst hybrid/onsite': 'https://www.linkedin.com/jobs/search/?currentJobId=3128671693&f_AL=true&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=1%2C3&geoId=100249151&keywords=business%20analyst&location=Rockville%2C%20Maryland%2C%20United%20States&refresh=true&sortBy=R'}
# statistic variables
numPostingsViewed = 0
numEasyAppliedCompleted = 0
numComplexPostings = 0
# get password while hiding characters
password = getpass.getpass(prompt='Enter account password: ', stream=None)
# open driver and navigate to website
driver = webdriver.Chrome(executable_path=chromeDriverPath)
# open linkedin
driver.get('https://www.linkedin.com')

# sign into account
driver.find_element(By.CLASS_NAME, 'input__input').send_keys(email)
driver.find_element(By.ID, 'session_password').send_keys(password, Keys.ENTER)
# wait some time to not get flagged
time.sleep(1)
# iterate through job criteria urls in queries
for posting_url in list(job_queries_dic.values())[2:3]:
    # for posting_url in job_queries_dic.values():
    # go to post
    driver.get(posting_url)
    # current_page = driver.current_url
    # print(f"current job criteria url: {posting_url}")

    total_results = driver.find_element(
        By.CLASS_NAME, "display-flex.t-12.t-black--light.t-normal")
    total_results_int = int(
        total_results.text.split(' ', 1)[0].replace(",", ""))
    # print('total results for this url: {total_results_int}')

    # get number of pages to scroll through individual query
    find_pages = driver.find_elements(
        By.CLASS_NAME, "artdeco-pagination__indicator.artdeco-pagination__indicator--number")
    total_pages = find_pages[len(find_pages)-1].text
    total_pages_int = int(re.sub(r"[^\d.]", "", total_pages))

    # print(f'total_pages: {total_pages_int}')
    # scrolls through all available pages
    for pagenum in range(0, total_pages_int):
        print(f'page: {pagenum}')
        # loop this for every page
        # see each page's job postings
        jobs_block = driver.find_element(
            By.CLASS_NAME, 'jobs-search-results-list')
        jobs_list = jobs_block.find_elements(
            By.CSS_SELECTOR, '.jobs-search-results__list-item')
        # go through each job listing
        for job_listing in jobs_list:
            # print(f'current job_listing: {job_listing}')
            hover = ActionChains(driver).move_to_element(job_listing)
            hover.perform()
            job_listing.click()
            # wait some time to not get flagged
            time.sleep(.35)
        # once done looping, go to next page via url magic
        # every "page" is just another 25 items shown via query and moving start position
        addstring = '&start='+str(25*(pagenum))
        # move onto next page
        driver.get(posting_url + addstring)
        # wait some time to not get flagged
        time.sleep(1)
# driver.close() # !run when done

# [try catch statements]
# 3 cases: easy application, already applied, too complex
# for the easy easy apply postings, fill out automatically
# for the more complex easy apply postings, save for filling out later
# (perhaps save as dictionary with post url,along with information to store and fill out later)
# have complex postings saved to file and opened with part 2 program

# keep track of statistics (# applications filled out, # complex postings saved for later, etc.)

# later down line, add possible cover letter fill in blanks, extending previous cover letter generator app functionality

# log
