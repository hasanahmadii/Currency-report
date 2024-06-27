from kavenegar import *
# from config import rules
def send_sms(text):
    """
    The task is to come and send the received message to the desired user
    :param text:
    :return:
    """
    try:
        api = KavenegarAPI('4F7378636E67746B3732527368526466665A59746F684E436B4865657978487036687A30547A54753455553D')
        params = {
            'sender': '1000689696',
            'receptor': '09219319545',
            'message': text
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
