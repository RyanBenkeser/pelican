#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Ryan Benkeser'
SITENAME = 'Data Deductions'
SITETITLE = 'Data Deductions'
SITESUBTITLE = 'By Ryan Benkeser, Rising Data Scientist'
SITEDESCRIPTION = 'Making deductions from data'

PATH = 'content'
STATIC_PATHS = ['images']
SITELOGO = 'images/data_deductions.png'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Me', 'http://datadeductions.com/data-deductions.html#data-deductions'),
         ('Posts', 'http://datadeductions.com/'))

# Social widget
SOCIAL = (('linkedin','http://linkedin.com/in/ryanbenkeser/'),
          ('github', 'http://github.com/ryanbenkeser/'),)

DEFAULT_PAGINATION = 5

# THEME = "/Users/rbenkeser/opt/anaconda3/lib/python3.7/site-packages/pelican/themes/Flex"
THEME = "/Users/rbenkeser/Data_Deductions_Blog/pelican-themes/Flex"

DISQUS_SITENAME = "datadeductions-com"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True