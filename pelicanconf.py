import sys
from urllib.parse import quote_plus as _quote_plus

AUTHOR = 'Chris Richards'
SITENAME = 'Noodlecentric'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'output'
IGNORE_FILES = ['.#*', '.DS_Store']
TIMEZONE = 'America/New_York'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'reviews'

THEME = 'theme'

ARTICLE_URL = '{slug}/'
ARTICLE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DIRECT_TEMPLATES = ['index']
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
CATEGORY_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
TAG_SAVE_AS = ''
TAGS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''


def _date_fmt(value, fmt='long'):
    if not hasattr(value, 'strftime'):
        return str(value) if value else ''
    if fmt == 'short':
        return value.strftime('%b %Y')
    if sys.platform == 'win32':
        return value.strftime('%B %d, %Y').replace(' 0', ' ')
    return value.strftime('%B %-d, %Y')


def _maps_url(location):
    return f'https://www.google.com/maps/search/?api=1&query={_quote_plus(str(location))}'


JINJA_FILTERS = {'date_fmt': _date_fmt, 'maps_url': _maps_url}
