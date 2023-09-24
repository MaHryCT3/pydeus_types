
from typing import TypeAlias

from genson import SchemaStrategy
from genson.schema.strategies.object import Object


LinkDict: TypeAlias = dict[str, dict[str, str]]


class LinkInValuesStrategy(Object):
    @classmethod
    def match_object(cls, obj):
        """
        Проверяет есть ли в значениях объекта ссылки (links)
        """
        if not isinstance(obj, dict):
            return False

        for key, value in obj.items():
            if isinstance(value, list):
                for val in value:
                    if isinstance(val, dict) and '_links' in val.keys():
                        return True
            elif isinstance(value, dict) and '_links' in value.keys():
                return True
        return False

    def add_object(self, obj: dict):
        self._rename_links(obj)
        super().add_object(obj)

    def _rename_links(self, obj: dict):
        """
        Меняет все значения _links на <key>_links,
        т.к _links используется почти везде и начинаются конфликты с именами моделей
        """
        for key, value in obj.items():
            if isinstance(value, list):
                for val in value:
                    if isinstance(val, dict) and '_links' in val.keys():
                        val[f'{key}_links'] = val.pop('_links')
            elif isinstance(value, dict) and '_links' in value.keys():
                value[f'{key}_links'] = value.pop('_links')


class LinksStrategy(SchemaStrategy):
    """
    Изменяет форматирование линков в схеме
    по дефолту они выглядят так:
    {'lesson-realization': {'href': '/api/lesson-realizations/1'}}
    а мы делаем так
    {'lesson-realization': '/api/lesson-realizations/1'}
    """

    @classmethod
    def match_object(cls, obj):
        # Если это объект links, то он всегда содержит ссылку на самого себя по ней и находим
        return isinstance(obj, dict) and 'self' in obj.keys()
    
    def add_object(self, obj: LinkDict):
        self._extra_keywords['type'] = 'object'
        properties = {}
        for link_name, href_dictionary in obj.items():
            if link_name == 'self':
                continue
            properties.update(
                {link_name: {'type': 'string'}}
            )

        self._extra_keywords['properties'] = properties