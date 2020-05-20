from typing import List


class OAuthConfig:
    def __init__(self, client_id: str, client_secret: str, scope: List[str]):
        self._client_id = client_id
        self._client_secret = client_secret
        self._scope = scope

    @property
    def client_id(self) -> str:
        return self._client_id

    @property
    def client_secret(self) -> str:
        return self._client_secret

    @property
    def scope(self) -> List[str]:
        return list(self._scope)
