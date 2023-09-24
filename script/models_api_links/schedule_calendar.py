from typing import Final, Any
from abc import ABC
from uuid import UUID
from datetime import datetime, timedelta

from .abc import ABCModelURL


class BaseScheduleCalendar(ABCModelURL, ABC):
    API_BASE_URL: Final[str] = 'https://utmn.modeus.org/schedule-calendar-v2/api/'


class StudyTeam(BaseScheduleCalendar):
    """Фильтр учебная команда"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'courses/cycle-realizations/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'fulltext': str,
        'page': int,
        'size': int,
        'sort': str
    }


class StudyDirection(BaseScheduleCalendar):
    """Фильтр направление подготовки"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'curriculum/specialties/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'fulltext': str,
        'sort': str,
        'size': int,
        'page': int
    }


class StudyProfile(BaseScheduleCalendar):
    """Фильтр профиль подготовки"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'curriculum/profiles/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'name': [
            str,
        ],
        'sort': str,
        'size': int,
        'page': int,
        'specialityId': str,
    }


class StudyEvents(BaseScheduleCalendar):
    """Расписание"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'calendar/events/search'

    REQUEST_JSON_TO_GET_RESPONSE = {'size': 500}
    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'size': int,
        'timeMin': str,
        'timeMax': str,
        'roomId': [
            UUID,
        ],
        'attendeePersonId': [
            UUID,
        ],
        'courseUnitRealizationId': [
            UUID,
        ],
        'cycleRealizationId': [
            UUID,
        ],
        'specialtyCode': [
            str,
        ],
        'learningStartYear': [
            int,
        ],
        'profileName': [
            str,
        ],
        'typeId': [
            str,
        ],
    }

    @classmethod
    def build_request_dict(cls) -> dict:
        # Берем просто месяц у нас эневией сайз стоит
        start = datetime.now()
        end = start + timedelta(days=30)
        return cls.REQUEST_JSON_TO_GET_RESPONSE | {
            'timeMin': start.isoformat() + 'Z',
            'timeMax': end.isoformat() + 'Z',
        }


class StudyModule(BaseScheduleCalendar):
    """Фильтр модуль"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'courses/course-unit-realizations/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'name': str,
        'page': int,
        'size': int,
        'sort': str,
    }


class CalendarPerson(BaseScheduleCalendar):
    """Фильтр участник"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'people/persons/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'id': [
            UUID,
        ],
        'fullName': str,
        'sort': str,
        'page': int,
        'size': int,
    }


class StudyEventType(BaseScheduleCalendar):
    """Фильтр тип занятия"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'calendar/event-types'


class BuildingRoom(BaseScheduleCalendar):
    """Фильтр аудитория"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'campus/rooms/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'name': str,
        'sort': str,
        'size': int,
        'page': int,
    }


class StudyFlow(BaseScheduleCalendar):
    """Фильтр поток"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'catalog/academic-period-realizations/start-years'
