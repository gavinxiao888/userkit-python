from requestor import Requestor
from users import UserManager
from invites import InviteManager
from session import Session


class UserKit(object):
    api_version = 1.0
    api_base_url = None
    api_key = None
    _NQ = None
    users = None
    invites = None

    def __init__(self, api_key, api_base_url=None, _requestor=None):
        if api_key is None:
            raise TypeError('api_key cannot be blank.')

        if api_base_url is None:
            api_base_url = 'https://api.userkit.io/v1'
        else:
            api_base_url += '/v1'

        self.api_key = api_key
        self.api_base_url = api_base_url

        # make the encapsulated objects
        self._NQ = _requestor or Requestor(self.api_key, self.api_base_url)
        self.users = UserManager(self._NQ)
        self.invites = InviteManager(self._NQ)

    @classmethod
    def version(cls):
        return cls.api_version
