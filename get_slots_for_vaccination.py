import requests
import smtplib
import datetime
import schedule
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#configs
min_age_limit = 45
pincode = "413312"
email = "your email"
password = "your pass"

def get_current_date():
    date = datetime.datetime.now()
    date = strftime("%d-%m-%Y")
    return date

def get_api_response():
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin"
    date = get_current_date()
    params = {"pincode": pincode, "date": date}
    headers = {"accept": "application/json", "Accept-Language": "hi_IN"}
    response = requests.get(url=url, headers=headers, params=params)
    res = response.json()
    contents = "Available slots::\n"
    for session in res['sessions']:
        if session["min_age_limit"] == min_age_limit and session["slots"] != []:
            contents = contents + "Date::" + " " + str(session['date']) + "\n"
            contents = contents + "Slots::" + " " + str(session['slots']) + "\n"
            contents = contents + "Center_id::" + " " + str(session['center_id']) + "\n"
            contents = contents + "Name::" + " " + str(session['name']) + "\n"
            contents = contents + "\n\n"

    return contents

def get_current_date():
    date = datetime.datetime.now()
    date = date.strftime("%d-%m-%Y")
    return date

def send_email(contents):
    mail_content = contents
    sender_address = email
    sender_pass = password
    receiver_address = email
    message = MIMEMultipart()
    message['From'] = sender_address
    message['To'] = receiver_address
    message['Subject'] = 'Vaccination alert: Slots are available for booking!'   #The subject line
    message.attach(MIMEText(mail_content, 'plain'))
    session = smtplib.SMTP('smtp.gmail.com', 587)
    session.starttls()
    session.login(sender_address, sender_pass)
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')

def run_core_functionality(time):
    print("Running the job at: "+(time))
    contents = get_api_response()
    if "Center_id" in contents:
        send_email(contents)

schedule.every().day.at("12:00").do(run_core_functionality,'12:00')
