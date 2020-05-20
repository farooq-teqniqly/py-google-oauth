from flask_dance.consumer import oauth_authorized, oauth_error
from flask_dance.contrib.google import make_google_blueprint

from flaskgoogleoauth.oauthconfig import OAuthConfig
from .errors import OAuthError


class GoogleOAuthProvider:
    def __init__(self, flask_app, config: OAuthConfig):
        self.google_blueprint = make_google_blueprint(
            client_id=config.client_id,
            client_secret=config.client_secret,
            scope=config.scope,
        )

        flask_app.register_blueprint(self.google_blueprint, url_prefix="/login")

    @oauth_authorized.connect
    def logged_in(self, blueprint, token):
        if not token:
            raise OAuthError(f"Failed to login with {blueprint.name}.")

        response = blueprint.session.get("/oauth/v1/userinfo")

        if not response.ok:
            raise OAuthError(f"Failed to fetch user info from {blueprint.name}.")

        response_json = response.json()
        pass

    @oauth_error.connect
    def google_error(self, blueprint, error, error_description=None, error_uri=None):
        raise OAuthError(
            f"OAuth error from {blueprint.name}; error={error}; "
            f"description={error_description}; uri={error_uri}"
        )
