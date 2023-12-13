import requests
from django.utils import timezone

from v1.API_CONFIG import API_KEY, API_KHADAMATI_LINK, PATTERN_BODY_ID
from v1.models import Number, Colab


send_by_pattern_link = API_KHADAMATI_LINK
api_auth_link = API_KEY


api_link = send_by_pattern_link+api_auth_link

# thi function checks if the given number is new for data base or no
def number_is_new(phonenumber):
    if Number.objects.filter(number=phonenumber).exists():
        return False
    
    return True

# For New users (after inserting into database)
# entry number should start with 0 and be string !!!!
def send_sms_new_user(number):
    data = {'bodyId': PATTERN_BODY_ID, 'to': number, 'args': [number]}
    response = requests.post(api_link, json=data)
    print(response.json())


# For repeated requests for sign up 
def send_sms_duplicate_number(number):
    pass
    # This function is disabled for commercial issues


# Validate data from colab form
def validate_phonenumber(number):
    if number.isnumeric() and len(number) == 11:
        if number.startswith('0'):
            return True
        
    return False


def validate_code_melli(code):
    if code.isnumeric() and len(code) == 10:
        return True
    
    return False
    


def new_number_row(number):
    new_row = Number(number = str(number),
                        pub_date = timezone.now())
    
    new_row.save() 

def new_colab_row(fullname, number, code_melli):
    new_row = Colab(fullname = fullname,
                    number = number,
                    code_melli = code_melli,
                    pub_date = timezone.now())

    new_row.save()



def colab_number_is_new(phonenumber):
    if Colab.objects.filter(number=phonenumber).exists():
        return False
    
    return True