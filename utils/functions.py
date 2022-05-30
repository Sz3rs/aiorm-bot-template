from os import getenv


def list_admins():
    data = getenv('admins', '')
    return data.split(',')
