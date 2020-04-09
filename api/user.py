import requests
import json

def user_info_from_username(connection, username):
    response = requests.get(url=connection.base_url + '/jwt-auth/v1/user/?slug=' + username,
                            headers={'Authorization': 'Bearer ' + connection.auth_token,
                                     'Content-type': 'application/json'},)

    if not response.ok:
        response.raise_for_status()

    return response


