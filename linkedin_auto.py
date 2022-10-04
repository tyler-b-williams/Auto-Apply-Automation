# !install selenium!
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass
# variable initialization
chromeDriverPath = 'Auto-Apply-Automation/chromedriver_win32/chromedriver.exe'
email = 'tylerbrentwilliams@gmail.com'

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
# seems they changed how find element is handled, will tackle tomorrow
sign_in_button = driver.find_element_by_link_text("Sign in")
sign_in_button.click()
email_field = driver.find_element_by_id("username")
email_field.send_keys(email)
password_field = driver.find_element_by_id("password")
password_field.send_keys(password)
password_field.send_keys(Keys.ENTER)
# logged in

# driver.get('https://www.linkedin.com')

# now cycle through job listings
# all_listings = driver.find_elements_by_css_selector(
#     "job-card-container--clickable")
# for listing in all_listings:
#     print("called")
#     listing.click()


# driver.close() # !run when done
# log into linkedin with information
# cycle through easy applies possible
# search queries that can be set via variable
# (data analytics remote, data analytics, D.C, data science intern, etc.)


# tonight: install selenium, have bot log into linkedin, and save specific queries to
# likely use dictionary for search queries {search term:url}


# cycle through specific jobpostings
# [try catch statements]

# for the easy easy apply postings, fill out automatically
# for the more complex easy apply postings, save for filling out later
# (perhaps save as dictionary with post url,along with information to store and fill out later)
# have complex postings saved to file and opened with part 2 program

# keep track of statistics (# applications filled out, # complex postings saved for later, etc.)

# later down line, add possible cover letter fill in blanks, extending previous cover letter generator app functionality

# log
