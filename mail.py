from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEImage import MIMEImage
from email.mime.application import MIMEApplication

def create_email(from_address, to_address, subject, message, cc=None, image=None, pdf=None):
    msg = MIMEMultipart('alternative')

    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject

    if cc:
        msg['Cc'] = cc

    if image:
        msg_img = MIMEImage(open(image, 'rb').read())
        msg_img.add_header('Content-ID', '<image>')
        msg_img.add_header('Content-Disposition', 'inline', filename=image)

    if pdf:
        msg_pdf = MIMEApplication(open(pdf, 'rb').read(), 'pdf')
        msg_pdf.add_header('Content-ID', '<pdf>')
        msg_pdf.add_header('Content-Disposition', 'attachment', filename=pdf)
        msg_pdf.add_header('Content-Disposition', 'inline', filename=pdf)

    msg.attach(MIMEText(message, 'html'))
    msg.attach(msg_img)
    msg.attach(msg_pdf)

    return msg.as_string()