import falcon
import config
import json
import logging


class UserAccessResource(object):
    def on_get(self, req, resp, user_token):
        if user_token not in config.ACCESS_MOCK_DB:
            logging.error(f"{user_token} not found")
            # Raise error
            raise falcon.HTTPNotFound(description=f"Token: \"{user_token}\" not found")

        # Set the body of the response to the access of the token
        resp.body = json.dumps({"access": config.ACCESS_MOCK_DB[user_token]})