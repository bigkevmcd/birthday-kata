import os
from datetime import date
from unittest import TestCase

try:
   from unittest import mock
except ImportError:
    import mock

from birthday.service import BirthdayService, Employee, Greeting


def get_filepath(filename):
    dirname = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(dirname, filename)


class EmployeeTest(TestCase):

    def test_is_birthday(self):
        """
        """
        employee = Employee(
            "Smith", "John", "1979/01/02", "testing@example.com")
        self.assertTrue(
            employee.is_birthday(date(2013, 1, 2)), "Failed to match dates")


def GreetingTest(TestCase):

    def test_instantiation(self):
        """
        We can instantiate Greetings.
        """
        employee = Employee(
            "Smith", "John", "1979/01/02", "testing@example.com")
        greeting = Greeting(employee, "subject", "body")


class BirthdayServiceTest(TestCase):

    def test_instantiation(self):
        """
        We can create BirthdayServices.
        """
        smtp_mock = mock.MagicMock()
        with mock.patch("smtplib.SMTP", smtp_mock):
            service = BirthdayService()
            service.send_greetings(
                get_filepath("employee_data.txt"),
                date(2008, 10, 8), "localhost", 25)

            # TODO: Convert this to a Message.to_string()
            smtp_mock.assert_has_calls(
                [mock.call("localhost", 25),
                 mock.call().sendmail("sender@example.com", ["testing1@example.com"], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: Happy Birthday!\nFrom: sender@example.com\nTo: testing1@example.com\n\nHappy Birthday, dear John'),
                 mock.call().quit()])

    def test_send_message(self):
        """
        BirthdayService.send_message should send the email through the specified
        SMTP server.
        """
        smtp_mock = mock.MagicMock()
        with mock.patch("smtplib.SMTP", smtp_mock):
            service = BirthdayService()
            employee = Employee(
                "Smith", "James", "1979/1/2", "testing@example.com")
            greeting = Greeting(employee, "subject", "body")
            service.send_message("localhost", 25, "sender@example.com", greeting)
            # TODO: Convert this to a Message.to_string()
            smtp_mock.assert_has_calls(
                [mock.call("localhost", 25),
                 mock.call().sendmail("sender@example.com",
                   ["testing@example.com"], 'Content-Type: text/plain; charset="us-ascii"\nMIME-Version: 1.0\nContent-Transfer-Encoding: 7bit\nSubject: subject\nFrom: sender@example.com\nTo: testing@example.com\n\nbody'),
                 mock.call().quit()])
