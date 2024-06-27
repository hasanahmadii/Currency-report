import requests
import config
import json
import mail
from notification import send_sms
import khayyam
from datetime import datetime


def get_requests():
    """
    In this part, we receive a request from the site and check it to see if it is correct or not
    Then we return it in the form of a dictionary
    :return:
    """
    respon = requests.get(config.KEY)
    if respon.status_code == 200:
        return json.loads(respon.text)
    return None


def get_archive(file_name, rates):
    """
    In this function, we have the file in question, that is, the same file that we received from the site
    We save a file
    :param file_name:
    :param rates:
    :return:
    """
    with open(f"archive/{file_name}.json", "w") as f:
        f.write(json.dumps(rates))
def send_mail(sub, rats):
    """
    In this case, we use it to send messages, but first we have to
    Let's check which currency we want in the config file
    :param sub:
    :param rats:
    :return:
    """
    now = khayyam.JalaliDatetime(datetime.now())
    subject = f"{sub} rates"
    if config.rules['email']['is_valid'] is not None:
        temp=dict()
        for index in config.rules['email']['is_valid']:
                temp[index] = rats[index]
        rats = temp

    text = json.dumps(rats) + "\nthis is for the hasna ahmadi\n"+f"{now.strftime('%Y-%B-%d   %A  %H:%M')}"
    mail.send_smtp_email(subject, text)

def check_notif(rates):
    """
    In this method, we will first check whether something has changed or not
    If it has changed, text me
    :param rates:
    :return:
    """
    now = khayyam.JalaliDatetime(datetime.now())
    msg = ''
    res = config.rules['notification']['is_valid']
    for ext in res:
        if rates[ext] <= res[ext]['min']:
            msg += f'{ext} get racher min :{rates[ext]}\n{now.strftime("%Y-%B-%d  %A %H:%M")}'
        if rates[ext] >= res[ext]['max']:
            msg += f'{ext} get racher max :{rates[ext]}\n{now.strftime("%Y-%B-%d  %A %H:%M")}'
    print(msg)
    return msg
def notification(sms):
    """
Well, in this method we will also send SMS
    :param sms:
    :return:
    """
    send_sms(sms)



if __name__ == "__main__":
    """
    Here we check if what is set to be sent so that we only send the same information
    """
    result = get_requests()
    if config.rules['archive']:
        get_archive(result['timestamp'], result['rates'])
    if config.rules['email']['enable']:
        send_mail(result['timestamp'], result['rates'])
    if config.rules['notification']['enable']:
        notif_msg = check_notif(result['rates'])
        if notif_msg:
            notification(notif_msg)