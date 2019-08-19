#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wang Tao'
SITENAME = 'Zodiac Wang'
#SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh'

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
SOCIAL = (('github', 'https://github.com/zodiac911'))
          

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#=======================================================================================
LOAD_CONTENT_CACHE = False
SITESUBTITLE = 'A Fantastic Learner'

THEME = "themes/elegant"
MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['pelican-ipynb.markup', 'tipue_search', 'extract_toc', 'neighbors', 'sitemap']
MARKDOWN = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc']
DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', '404'))
STATIC_PATHS = ['theme/images', 'images']
USE_SHORTCUT_ICONS = True
IGNORE_FILES = [".ipynb_checkpoints"]


MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' :{'permalink' : 'true'},

    },
    'output_format': 'html5',
}

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


RECENT_ARTICLES_COUNT = 15
SITE_DESCRIPTION = "WangTao's Magic Box"

# Landing Page
            
LANDING_PAGE_ABOUT = {
    'title': 'A Walker in the Desert of Knowledge',
    'details': """<div itemscope itemtype="http://schema.org/Person">
        <p><b>掌握过去是探索未来的第一步！</b></p>
        
        <p>Hello, 我是王涛(Zodiac Wang), 可以在<a href="https://github.com/zodiac911/" title="Github" itemprop="url"><span>Github</span></a>找到我，或者<a href="mailto:wangtao_skyedge@outlook.com">邮件</a>联系，欢迎交流。</p>

       <div align="center">  <img src="http://image-bed-zodiac.oss-cn-qingdao.aliyuncs.com/landscapephotographer201911.jpg" width="800"/></div>
       </div>
       """}