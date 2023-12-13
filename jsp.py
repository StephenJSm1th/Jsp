#Jackery solar panel price checker
import requests
from bs4 import BeautifulSoup as bs
import smtplib
from email.message import EmailMessage
import os

# Put your email address and password into environment variables.
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')

#The page to scrape.
url = 'https://uk.jackery.com/products/solarsaga-100w-solar-panel'
response = requests.get(url)

page = response.text

soup = bs(page, features='lxml')

#Get the text you want
price = soup.find_all(class_="price text-xl barnd-color main-producr__price")

#Put the bs4.element.ResultSet into a list
a_list =[]
for i in price:
    a_list.append(i.text)

#Remove newline chars
b_list = [item.replace('\n', "") for item in a_list]

#Remove blank spaces
c_list = [item.strip() for item in b_list]

#Email yourself the results.
msg = EmailMessage()
msg['Subject'] = 'Solar Panel Alert'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'PLACE RECIPIENT EMAIL ADDRESS HERE'
msg.set_content(f"The price is {c_list}\n{url}")

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    smtp.send_message(msg)
