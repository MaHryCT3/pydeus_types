from .abc import ABCModelJsonGetter
from urllib.parse import urljoin

from httpx import AsyncClient
from script.models_api_links.abc import ABCModelURL


class ModelJsonGetter(ABCModelJsonGetter):

    def __init__(self,  token: str) -> None:
        """
        Получение JSON с помощью запроса в MODEUS API для дальнейшей генерации схемы, а затем моделек
        :param token: Bearer Token Для авторизации в модеус
        """
        self._client = AsyncClient(timeout=10*60)
        self._client.headers['Content-Type'] = 'application/json'
        self.authorize(token)

    async def get_json(self, model_url: type[ABCModelURL]) -> dict:
        response = await self._client.request(
            method=model_url.HTTP_METHOD,
            url=urljoin(model_url.API_BASE_URL, model_url.REQUEST_URL_ENDPOINT),
            json=model_url.build_request_dict(),
        )
        response.raise_for_status()
        return response.json()

    def authorize(self, token: str):
        self._client.headers.update(
            {'Authorization': f'Bearer {token}'}
        )
