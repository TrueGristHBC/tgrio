import requests

def token(connection):
    response = requests.post(url=connection.base_url + '/jwt-auth/v1/token',
                                     data={'username': connection.username,
                                           'password': connection.password,
                                           },)
    if not response.ok:
        response.raise_for_status()

    return response