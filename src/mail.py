import smtplib
# import requests

from config import rules

from email.mime.text import MIMEText

#
# def send_api_email(subject, body):
#     return requests.post(
#         "https://api.mailgun.net/v3/inprobes/messages",
#         auth=("api", paswd),
#         data={
#             "from": "Hosein finance@inprobes.com",
#             "to": ["hs.ramezanpoor@gmail.com", "hosein@inprobes.com"],
#             "subject": subject,
#             "text": body
#         }
#     )
#

def send_smtp_email(subject, body):
    """
    Inside our email file with a message from the fixer site
    We received it and sent it to an email simulator that we used from the mailtrap site
    :param subject:
    :param body:
    :return:
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = rules['email']['sender']
    msg['To'] = rules['email']['RECEIVER']

    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as mail_server:
        mail_server.login(rules['email']['user'], rules['email']['paswd'])
        mail_server.sendmail(msg['From'], msg['To'], msg.as_string())
        # mail_server.quit()





