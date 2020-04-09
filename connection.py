import requests
import json
from api import authentication

class Connection(object):
    """
    Creates a connection object which is used in subsequent requests and manages the user's connection
    with the True Grist REST API.
    # import
    from tgrio import connection
    # connect to the environment and chosen project
    conn = connection.Connection(   username="username",
                                    password="password",
                                    )
    conn.connect()
    Attributes:
        username: Username.
        password: Password.
    """

    auth_token = None
    base_url = 'https://truegrist.ca/wp-json'

    def __init__(self, username, password):
        """
        Establishes a connection with True Grist REST API
        Args:
            username (str): Username
            password (str): Password
        """

        self._username = username
        self._password = password


    def connect(self):
        """Creates a connection
            Authenticate a user and create an HTTP session.
            This request returns an authorization token (JSON web token) which will be submitted with subsequent requests.
            The body of the request contains the information needed to create the session.
        """
        r = authentication.token(connection=self)


        self.auth_token = r.json().get('token')

    @property
    def username(self):
        return self._username

    @property
    def password(self):
        return self._password
