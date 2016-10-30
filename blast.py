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
            dest='from_addr', help='sender email',
            metavar='FROM', required=True)

    parser.add_argument('-t', '-email',
            dest='email_id', help='email subject',
            metavar="EMAIL", required=True)

    return parser


def main():

    parser = build_parser()
    options = parser.parse_args()

    from_addr = options.from_addr
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
        to_addr = raw_input("To: ")
        while not to_addr:
            to_addr = raw_input("To: ")
        name = raw_input("Name of Recipient: ")

        cc = data["cc"]
        subj = data["subject"]
        body = data["message"].encode('ascii', 'ignore')

        fields = get_fields(body)
        for field in fields:
            inp = raw_input(field[1:-1] + ": ")
            body = body.replace(field, inp)

        email = create_email(from_addr, to_addr, subj, body, cc)

        server.sendmail(from_addr, to_addr, email)
        print "Email sent..."

        more = raw_input("More? (y/n): ")
        if more.lower() != "y":
            sending_emails = False

if __name__ == '__main__':
    main()