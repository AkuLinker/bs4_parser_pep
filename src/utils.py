import logging

from requests import RequestException

from exceptions import ParserFindTagException


def get_response(session, url):
    """
    Функция для получения http ответа по url.
    Если ответ не получен, сообщает об ошибке.
    """
    try:
        response = session.get(url) 
        response.encoding = 'utf-8'
        return response
    except RequestException:
        logging.exception(
            f'Возникла ошибка при загрузке страницы {url}',
            stack_info=True
        )

def find_tag(soup, tag, attrs=None, string=None):
    """
    Функция для поиска тега в html странице.
    Если тег не найден, сообщает об этом.
    """
    searched_tag = soup.find(tag, attrs=(attrs or {}), string=(string or None))
    if searched_tag is None:
        error_msg = f'Не найден тег {tag} {attrs} {string}'
        logging.error(error_msg, stack_info=True)
        raise ParserFindTagException(error_msg)
    return searched_tag
