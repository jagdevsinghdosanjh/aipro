import os

def control_device(user):
    if user == 'recognized_user':
        os.system('echo "Turning on the light"')
        # Code to turn on the light
    else:
        os.system('echo "User not recognized"')
