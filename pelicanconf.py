#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Geoffrey Valdes'
SITENAME = u'toronjil morado'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['pelican_javascript', 'i18n_subsites']

RELATIVE_URLS = True  # overwritten to false in publishconf
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'es': {
        'SITENAME': u'toronjil morado',
        'THEME': 'theme',
        'SITEURL': '/es'
        }
    }

languages_lookup = {
             'en': 'English',
             'es': 'Español',
             }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]


def my_ordered_items(ordered_dict):
    items = list(ordered_dict.items())
    # swap first and last using tuple unpacking
    items[0], items[-1] = items[-1], items[0]
    return items

JINJA_FILTERS = {
             'lookup_lang_name': lookup_lang_name,
             'my_ordered_items': my_ordered_items,
             } 

JINJA_EXTENSIONS = ['jinja2.ext.i18n']   

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'theme'
