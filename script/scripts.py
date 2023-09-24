from os import getenv
from json import dump

from script.models_api_links.abc import ABCModelURL
from script.models_jsons_getter.getter import ModelJsonGetter


# TODO: Добавить параметры, чтобы указывать какую часть апи генерить
async def generate_request_modeus_json(models_urls: list[type[ABCModelURL]]):
    token = get_authorization_token()
    model_json_getter = ModelJsonGetter(token)

    # Сначала мы записываем все словарь, только потом будет создавать, чтобы при
    # возникновение ошибки у геттера ничего не создалось
    generated_json: dict[type[ABCModelURL], dict] = []
    for model_url in models_urls:
        json = await model_json_getter.get_json(model_url)
        generated_json[model_url] = json

    for model_url, json in generated_json.items():
        _add_request_json(model_url, json)


def _add_request_json(model_url: type[ABCModelURL], json: dict):
    with open(f'modeus_jsons/responses/{model_url.model_name}.json') as f:
        dump(json, f)



def get_authorization_token() -> str:
    bearer_token = getenv('MODEUS_TOKEN')
    assert bearer_token, 'Для генерации JSON необходимо указать переменную окружения `MODEUS_TOKEN`'
    return bearer_token