import smtplib
import requests
import datetime
import os
# ------------------------- Getting Sheet information ----------------------- #

url = os.environ.get("URL")
response = requests.get(url)

data = response.json()
sheet_info = data["sheet1"]

class_info = {}

assignments_list = []

for item in sheet_info:
    assignment_dict = {
        'dueDate': item.get('dueDate', 'N/A'),
        'class_name': item.get('class', 'N/A'),
        'assignment_name': item.get('assignment', 'N/A'),
        'time': item.get('time', 'N/A')
    }
    assignments_list.append(assignment_dict)


# ------------------------- Getting Today's date ----------------------- #

day = datetime.datetime.now().strftime("%d")
month = datetime.datetime.now().strftime("%m")

todays_date = f"{month}-{day}"

# ------------------------- Sending email notification ----------------------- #

smtp_port = 587
my_email = os.environ.get("EMAIL")
my_password = os.environ.get("PASSWORD")

for assignment in assignments_list:
    if todays_date == assignment['dueDate']:
        with smtplib.SMTP("smtp.office365.com", smtp_port) as connection:
            connection.starttls()  # Secure the connection
            connection.login(user=my_email, password=my_password)
            message = (f"Subject: Learning Reminder {todays_date}\n\n"
                       f"This is a reminder that the deadline for '{assignment['assignment_name']}' "
                       f"for the course '{assignment['class_name']}' is coming up.\n\n"
                       f"Due date : {assignment['dueDate']} at {assignment['time']}")
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=message
            )
        print(f'Email sent for assignment due on: {todays_date}')
