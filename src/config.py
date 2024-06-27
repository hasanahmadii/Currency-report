
# Inside this file, we put the settings related to the files that are used in the whole program
url = "http://data.fixer.io/api/latest?access_key="
API_KEY = "0f6010c46178e4bfa274231ccfed2243"

KEY = url+API_KEY


#
# rules = {
#
#     'send_mail': True,
#
#
# }
rules = {
    'archive': True,
    'email': {
        'RECEIVER': 'hasanahmadi781377@gmail.com',
        'paswd': '43d8367dd6349d',
        'user': 'f5064d243c26b8',
        'sender': 'ha3an19978@gmail.com',
        'enable': True,
        'is_valid': ["ETB", 'IQD', 'IRR', 'MXN', 'ZMK'],
    },
    'notification': {
        'enable': True,
        'RECEIVER': '09938557295',
        'sender': '09219319545',
        'is_valid': {
            'BTC': {'min': 3.70012, 'max': 0.000110},
            'IRR': {'min': 45000, 'max': 50000}
        },
    }
}