# selenium for web driving
import selenium
from selenium import webdriver

# time for pausing between navigation
import time

# Datetime for recording time of submission
import datetime

# os for file management
import os


def post_nairaland(new_post):
	# Using Chrome to access web
	driver = webdriver.Chrome()
    #driver = webdriver.Chrome(executable_path='C:\Users\Administrator\Downloads\chromedriver_win32\chromedriver.exe')

	time.sleep(5)

	# Open the website
	driver.get('https://www.nairaland.com/login')

	# Locate id and password
	id_box = driver.find_element_by_name('name')
	pass_box = driver.find_element_by_name('password')

	# Send login information
	# id_box.send_keys('adivaB')
	# pass_box.send_keys('sampleNaira')

	id_box.send_keys(new_post["name"])
	pass_box.send_keys(new_post["password"])

	# Click login
	pass_box.submit()
	time.sleep(5)
	forum = driver.find_elements_by_xpath("/html/body/div/table[2]/tbody/tr[2]/td/a[1]/b")
	for i in forum:
		i.click()
		time.sleep(5)
		topic_button = driver.find_element_by_link_text('Create New Topic')
		topic_button.click()
		time.sleep(2)

		#Locate create new topic fields
		subject = driver.find_element_by_name('title')
		message = driver.find_element_by_name('body')

		#Send Subject and Message details
		# subject.send_keys('Python Programming')
		# message.send_keys('Step 1: Research the topic\n Step 2: Phone a friend')
		subject.send_keys(new_post["subject"])
		message.send_keys(new_post["body"])
		
		# Click Submit
		message.submit()
		time.sleep(2)

		print('{} New topic for nairaland {} successfully created at {}.'.format(subject, message, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

		return("post created succesfully")
# if __name__ == "__main__":
# 	post_nairaland()

    






