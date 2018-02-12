# -*- coding: utf-8 -*-
DESCRIPTION = (
    'Install pyecharts extensions into jupyter' +
    ''
)
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

project = u'pyecharts-jupyter-installer'
copyright = u'2018 pyecharts dev team'
version = '0.0.2'
release = '0.0.2'
exclude_patterns = []
pygments_style = 'sphinx'
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pyecharts-jupyter-installerdoc'
latex_elements = {}
latex_documents = [
    ('index', 'pyecharts-jupyter-installer.tex',
     'pyecharts-jupyter-installer Documentation',
     'pyecharts dev team', 'manual'),
]
man_pages = [
    ('index', 'pyecharts-jupyter-installer',
     'pyecharts-jupyter-installer Documentation',
     [u'pyecharts dev team'], 1)
]
texinfo_documents = [
    ('index', 'pyecharts-jupyter-installer',
     'pyecharts-jupyter-installer Documentation',
     'pyecharts dev team', 'pyecharts-jupyter-installer',
     DESCRIPTION,
     'Miscellaneous'),
]
