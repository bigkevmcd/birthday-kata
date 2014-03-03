import smtplib
from datetime import datetime
from email.mime.text import MIMEText


class Employee:
    def __init__(self, last_name, first_name, birth_date, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.birth_date = datetime.strptime(birth_date, "%Y/%m/%d").date()

    def is_birthday(self, today):
        return self.birth_date.replace(year=today.year) == today


class Greeting:
    def __init__(self, employee, subject, body):
        self.employee = employee
        self.subject = subject
        self.body = body


class BirthdayService:
    """
    Python implementation of the Birthday Kata problem.
    """
    def send_greetings(self, filename, our_date, smtp_host, smtp_port):
        """
        1. Read employee records from a file
        2. Filter employees whose birthday is today
        3. Send a personalized greetings message by email
        """
        with open(filename) as f:
            for line in f.readlines():
                employee_data = line.strip().split(", ")
                employee = Employee(*employee_data)
                if employee.is_birthday(our_date):
                    body = "Happy Birthday, dear {name}".format(
                        name=employee.first_name)
                    subject = "Happy Birthday!"
                    greeting = Greeting(employee, subject, body)
                    self.send_message(
                        smtp_host, smtp_port, "sender@example.com", greeting)

    def send_message(self, smtp_host, smtp_port, sender, greeting):
        """
        """
        msg = MIMEText(greeting.body)
        msg["Subject"] = greeting.subject
        msg["From"] = sender
        msg["To"] = greeting.employee.email

        s = smtplib.SMTP(smtp_host, smtp_port)
        s.sendmail(sender, [greeting.employee.email], msg.as_string())
        s.quit()
