from abc import ABC


class ABCModelURL(ABC):
    API_BASE_URL: str

    HTTP_METHOD: str
    REQUEST_URL_ENDPOINT: str

    REQUEST_JSON_TO_GET_RESPONSE: dict | None = None
    FULL_REQUEST_JSON_PARAMETERS: dict | None = None

    @classmethod
    @property
    def model_name(cls) -> str:
        return cls.__name__
