#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kaustuv Deolal'
SITENAME = u'Rock and Code'
SITEURL = ''
PATH = 'content'
THEME='alchemy'
TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

from datetime import datetime
CURRENT_YEAR = datetime.now().year

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PAGES_ON_MENU = True
PROFILE_IMAGE = 'http://rs97.pbsrc.com/albums/l224/hometownclassic/Bioworld/Pink%20Floyd/Bioworld002.jpg~c200'
SHOW_ARTICLE_AUTHOR = True

EXTRA_FAVICON = True

# LICENSE_URL = ''
# LICENSE_NAME = ''
DELETE_OUTPUT_DIRECTORY = False

STATIC_PATHS = ['images']

MARKUP=('.md')


GITHUB_ADDRESS = 'https://github.com/Vutsuak16'


