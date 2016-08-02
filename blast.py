"""
To Dos
    Different from email option
    Access and edit google sheet
    Parser for arguments
    Actual mail blast
    JSON templates

"""

import os
import sys
import smtplib
from email import create_email
from getpass import getpass
import json
from argpaser import ArgumentParser

def build_parser():
    parser = ArgumentParser(description="Mail-blast application")

    parser.add_argument('-f','-from', 
            dest='from_addr', help='sender email',
            metavar='FROM', required=True)

    return parser

def load_json():


def main():

	parser = build_parser()
	options = parser.parse_args()

	from_addr = options.from_addr

	to_addr = "wengk97@gmail.com"
	subj = "HI"
	msg = "df"

	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()

	password = getpass(prompt="Email Password: ")

	try:
		server.login(from_addr, password)
	except SMTPAuthenticationError:
		print "Wrong combination of email and password. Try again."
		sys.exit(1)

	email = create_email(from_addr, to_addr, subj, body, )

if __name__ == '__main__':
    main()