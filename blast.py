import os
import sys
import smtplib
from getpass import getpass
import json
from argparse import ArgumentParser
from mail import create_email
from template import get_fields

def build_parser():
    parser = ArgumentParser(description="Mail-blast application")

    parser.add_argument('-f','-from', 
            dest='from_address', help='sender email',
            metavar='FROM', required=True)

    parser.add_argument('-t', '-email',
            dest='email_id', help='email subject',
            metavar="EMAIL", required=True)

    return parser


def main():
    parser = build_parser()
    options = parser.parse_args()

    from_address = options.from_address
    email_file = options.email_id+ ".json"

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    gmail = raw_input("G-Mail Address: ")
    password = getpass(prompt="Password: ")

    try:
        server.login(gmail, password)
    except SMTPAuthenticationError, e:
        print "Wrong combination of email and password. Try again."
        sys.exit(1)

    with open(email_file) as json_data:
	    data = json.load(json_data, strict=False)
	    json_data.close()

    sending_emails = True

    while sending_emails:
    
        to_address = raw_input("To: ")
        while not to_address:
            to_address = raw_input("To: ")

        message = data["message"].encode('ascii', 'ignore')

        print "\nTime to fill out the fields in the email: "
        fields = get_fields(message)
        for field in fields:
            inp = raw_input(field[1:-1] + ": ")
            message = message.replace(field, inp)

        email_content = {}
        email_content['subject'] = data['subject']
        email_content['from_address'] = from_address
        email_content['to_address'] = to_address
        email_content['message'] = message

        if data['cc'] != "None":
            email_content['cc'] = data['cc']

        if data['image'] != "None":
            email_content['image'] = data['image']

        if data['pdf'] != "None":
            email_content['pdf'] = data['pdf']

        email = create_email(**email_content)

        server.sendmail(from_address, to_address, email)
        print "Email sent..."

        more = raw_input("\nMore? (Y/N): ")
        if more.lower() != "y":
            sending_emails = False

if __name__ == '__main__':
    main()