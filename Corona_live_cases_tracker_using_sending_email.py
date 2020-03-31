# install requests
# install beautifulsoul
# install lxml 

import requests
import bs4
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# country_name = input('Enter Country Name : ')

def Covid19_data(country):
    res = requests.get('https://www.worldometers.info/coronavirus/#countries')
    soup = bs4.BeautifulSoup(res.text , 'lxml')
    index = -1 
    data = soup.select('tr td')

    for i in range(len(data)):
        if data[i].text == country :
            index = i 
            break 
    current_data = str()
    for i in range(6):
        if i == 0 :
            current_data = current_data + "Country Name : "+str(data[i+index].text) + "\n"
        elif i == 1 :
            current_data = current_data + "Total Cases : "+str(data[i+index].text)+ "\n"
        elif i == 2 :
            current_data = current_data + "New Cases : "+str(data[i+index].text)+ "\n"
        elif i == 3 :
            current_data = current_data + "Total Deaths : "+str(data[i+index].text)+ "\n"
        elif i == 4 :
            current_data = current_data + "New Deaths : "+str(data[i+index].text)+ "\n"
        elif i == 5 :
            current_data = current_data + "Total Recovered : "+str(data[i+index].text)+ "\n"
    return current_data

sender_email = 'sender email id'
reciever_email = 'reciever email id '
password = 'sender email id password'
subject = 'Covid-19 Latest Report'
message = str(Covid19_data('Italy'))

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = reciever_email
msg['Subject'] = subject
msg.attach(MIMEText(message , 'plain'))

server = smtplib.SMTP('smtp.gmail.com' , 587)
server.starttls()
server.login(sender_email , password)
text = str(msg)
server.sendmail(sender_email , reciever_email , text)
print("Mail Sent!")