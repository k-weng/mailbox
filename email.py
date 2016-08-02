from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def create_email(from_addr, to_addr, subj, body, cc=None):

    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subj

    if cc:
        msg['Cc'] = cc

    msg.attach(MIMEText(body, 'plain'))    

    return msg.as_string