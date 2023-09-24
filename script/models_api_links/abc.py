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

    @classmethod
    def build_request_dict(cls) -> dict:
        return cls.REQUEST_JSON_TO_GET_RESPONSE
