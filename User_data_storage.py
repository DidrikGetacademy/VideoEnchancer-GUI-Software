_user_data = {}

def set_user_data(data):
    global _user_data
    _user_data = data


def get_user_data():
    return _user_data