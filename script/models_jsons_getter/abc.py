from abc import ABC, abstractmethod

from script.models_api_links.abc import ABCModelURL


class ABCModelJsonGetter(ABC):

    @abstractmethod
    async def get_json(self, model_url: type[ABCModelURL]) -> dict:
        ...
