import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import csv
import time


driver = webdriver.Firefox()
c = csv.writer(open('result.csv','wb'))
# first_row = "Full_name,Fmaily_name,Given_name,Gender,city,state,country,continent,normalized_location,general_location,angellist_username,angellist_url,facebook_username,facebook_url,foursquare_username,foursquare_url,klout_username,klout_url,linkedin_username,linkedin_url,twitter_username,twitter_url"
c.writerow(["Full_name","Fmaily_name","Given_name","Gender","city","state","country","continent","normalized_location","general_location","angellist_username","angellist_url","facebook_username","facebook_url","foursquare_username","foursquare_url","klout_username","klout_url","linkedin_username","linkedin_url","twitter_username","twitter_url"])
for i in csv.reader(open('input.csv','rb')):
	print i[0]
	url = "https://api.fullcontact.com/v2/person.json?email="+str(i[0])+"&style=dictionary&apiKey=891f653fab77f251"

	
	p = driver.get(url)
	time.sleep(2)
	# html_source = driver.page_source
	soup = BeautifulSoup(driver.page_source)
	# print html_source
	# print soup
	data = json.loads(soup.find("body").text)
	# print data
	try:
		Full_name = data['contactInfo']['fullName']
		# print "First Name:",Full_name
	except Exception,e:
		Full_name = "#N/A"
	try:	
		Fmaily_name = data['contactInfo']['familyName']
		# print "Family Name:", Fmaily_name
	except Exception,e:
		Fmaily_name = "#N/A"
	try:
		Given_name = data['contactInfo']['givenName']
		# print "Given Name:",Given_name
	except Exception,e:
		Given_name = "#N/A"
	try:
		Gender = data['demographics']['gender']
	except Exception,e:
		Gender = "#N/A"
	try:
		city = data['demographics']['locationDeduced']['city']['name']
	except Exception,e:
		city = "#N/A"
	# print "City:",city

	try:
		state = data['demographics']['locationDeduced']['state']['name']
	except Exception,e:
		state = "#N/A"
	# print "state:",state

	try:
		country = data['demographics']['locationDeduced']['country']['name']
	except Exception,e:
		country = "#N/A"
	# print "Country:",country

	try:
		continent = data['demographics']['locationDeduced']['continent']['name']
	except Exception,e:
		continent = "#N/A"
	# print "continent:",continent

	try:
		normalized_location = data['demographics']['locationDeduced']['normalizedLocation']
	except Exception,e:
		normalized_location = "#N/A"
	# print "Normalized_location: ",normalized_location

	try:
		general_location = data['demographics']['locationGeneral']
	except Exception,e:
		general_location = "#N/A"
	# print "gender_location:",general_location
	# print city
	try:
		angellist_username = data['socialProfiles']['angellist'][0]['username']
	except Exception,e:
		angellist_username = "#N/A"
	# print "angellist_username:",angellist_username

	try:
		angellist_url = data['socialProfiles']['angellist'][0]['url']
	except Exception,e:
		angellist_url = "#N/A"
	# print "angellist_url:",angellist_url

	try:
		facebook_username = data['socialProfiles']['facebook'][0]['username']
	except Exception,e:
		facebook_username = "#N/A"
	# print "facebook_username:",facebook_username

	try:
		facebook_url = data['socialProfiles']['facebook'][0]['url']
	except Exception,e:
		facebook_url = "#N/A"
	# print "facebook_url:",facebook_url

	try:
		foursquare_username = data['socialProfiles']['foursquare'][0]['username']
	except Exception,e:
		foursquare_username = "#N/A"
	# print "foursquare_username:",foursquare_username

	try:
		foursquare_url = data['socialProfiles']['foursquare'][0]['url']
	except Exception,e:
		foursquare_url = "#N/A"
	# print "foursquare_url:",foursquare_url

	try:
		klout_username = data['socialProfiles']['klout'][0]['username']
	except Exception,e:
		klout_username = "#N/A"
	# print "klout_username:",klout_username

	try:
		klout_url = data['socialProfiles']['klout'][0]['url']
	except Exception,e:
		klout_url = "#N/A"
	# print "klout_url:",klout_url

	try:
		linkedin_username = data['socialProfiles']['linkedin'][0]['username']
	except Exception,e:
		linkedin_username = "#N/A"
	# print "linkedin_username:",linkedin_username

	try:
		linkedin_url = data['socialProfiles']['linkedin'][0]['url']
	except Exception,e:
		linkedin_url = "#N/A"
	# print "linkedin_url:",linkedin_url

	try:
		twitter_username = data['socialProfiles']['twitter'][0]['username']
	except Exception,e:
		twitter_username = "#N/A"
	# print "twitter_username:",twitter_username

	try:
		twitter_url = data['socialProfiles']['twitter'][0]['url']
	except Exception,e:
		twitter_url = "#N/A"
	# print "twitter_url",twitter_url


	c.writerow([Full_name,Fmaily_name,Given_name,Gender,city,state,country,continent,normalized_location,general_location,angellist_username,angellist_url,facebook_username,facebook_url,foursquare_username,foursquare_url,klout_username,klout_url,linkedin_username,linkedin_url,twitter_username,twitter_url])


