from unittest import TestCase

from flaskgoogleoauth.googleoauthprovider import GoogleOAuthProvider
from flaskgoogleoauth.oauthconfig import OAuthConfig


class MockFlaskApp:
    def register_blueprint(self, **args):
        pass


google_client_id = (
    "669264709149-45m95k80c0j5irnde9hhmgom4bct0tbi.apps.googleusercontent.com"
)
google_client_secret = "X9ye4YQoO8epHCTYj4nSiQeJ"
google_scope = ["profile", "email"]


class GoogleOAuthProviderTests(TestCase):
    def test_login(self):
        mock_flask_app = MockFlaskApp()
        config = OAuthConfig(google_client_id, google_client_secret, google_scope)
        provider = GoogleOAuthProvider(mock_flask_app, config)
        provider.login()
