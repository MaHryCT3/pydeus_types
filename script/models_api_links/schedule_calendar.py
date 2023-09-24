from typing import Final, Any

from .abc import ABCModelURL
from .types import integer, string, UUID


class BaseScheduleCalendar(ABCModelURL):
    API_BASE_URL: Final[str] = 'https://utmn.modeus.org/schedule-calendar-v2/api/'


class StudyTeam(BaseScheduleCalendar):
    """Фильтр учебная команда"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'courses/cycle-realizations/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'fulltext': string,
        'page': integer,
        'size': integer,
        'sort': string
    }


class StudyDirection(BaseScheduleCalendar):
    """Фильтр направление подготовки"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'curriculum/specialties/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'fulltext': string,
        'sort': string,
        'size': integer,
        'page': integer
    }


class StudyProfile(BaseScheduleCalendar):
    """Фильтр профиль подготовки"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'curriculum/profiles/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'name': [
            string,
        ],
        'sort': string,
        'size': integer,
        'page': integer,
        'specialityId': string,
    }


class StudyEvents(BaseScheduleCalendar):
    """Расписание"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'calendar/events/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'size': integer,
        'timeMin': string,
        'timeMax': string,
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
            string,
        ],
        'learningStartYear': [
            integer,
        ],
        'profileName': [
            string,
        ],
        'typeId': [
            string,
        ],
    }


class StudyModule(BaseScheduleCalendar):
    """Фильтр модуль"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'courses/course-unit-realizations/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'name': string,
        'page': integer,
        'size': integer,
        'sort': string,
    }


class CalendarPerson(BaseScheduleCalendar):
    """Фильтр участник"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'people/persons/search'

    FULL_REQUEST_JSON_PARAMETERS: Final[dict[str, Any]] = {
        'id': [
            UUID,
        ],
        'fullName': string,
        'sort': string,
        'page': integer,
        'size': integer,
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
        'name': string,
        'sort': string,
        'size': integer,
        'page': integer,
    }


class StudyFlow(BaseScheduleCalendar):
    """Фильтр поток"""

    HTTP_METHOD: Final[str] = 'POST'
    REQUEST_URL_ENDPOINT: Final[str] = 'catalog/academic-period-realizations/start-years'
