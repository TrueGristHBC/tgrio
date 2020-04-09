import requests
import json
import connection

from api import user

class User:
    """Populate user information from True Grist REST API
    Attributes:
        connection (Connection): Connection to api.
        username (str): Username.
    """
    def __init__(self, connection, username):
        self._username = username
        self._user_id = None
        self._email = None
        self._registered = None
        self._groups = []
        self._experience = None
        self._website = None
        self._description = None
        self._city = None
        self._bjcp = None
        self._system_fuel = None
        self._author_biography = None

        response = user.user_info_from_username(connection, username)

        self.__populate_user(response)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def __populate_user(self,response):
        j = response.json()[0]
        self._user_id = j.get('id')
        self._email = j.get('email')
        self._registered = j.get('registered')
        self._groups = j.get('groups')
        self._experience = j.get('experience')
        self._website = j.get('website')
        self._description = j.get('description')
        self._city = j.get('city')
        self._bjcp = j.get('bjcp')
        self._system_fuel = j.get('system_fuel')
        self._author_biography = j.get('author_biography')

    @property
    def username(self):
        return self._username

    @property
    def user_id(self):
        return self._user_id

    @property
    def email(self):
        return self._email

    @property
    def registered(self):
        return self._registered

    @property
    def groups(self):
        return self._groups

    @property
    def experience(self):
        return self._experience

    @property
    def website(self):
        return self._website

    @property
    def description(self):
        return self._description

    @property
    def city(self):
        return self._city

    @property
    def bjcp(self):
        return self._bjcp

    @property
    def system_fuel(self):
        return self._system_fuel

    @property
    def author_biography(self):
        return self._author_biography

