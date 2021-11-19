# Configuration file for the Sphinx documentation builder.

import os
import sys
import sphinx_rtd_theme
from os import environ

sys.path.insert(0, os.path.abspath('.'))

rtd_tag = 'latest'
if environ.get('READTHEDOCS_VERSION') is not None:
    rtd_tag = os.environ['READTHEDOCS_VERSION']

placeholder_replacements = {
    "{BRANCH}" : "main",
    "{BRANCH_DOC}" : "latest", # Used to target the correct ReadTheDocs distribution version
    "{RTD_TAG}": rtd_tag
}
# -- Project information

project = 'VIN Developer Guide'
copyright = '2021, Virgil Systems'
author = 'Dion Hicks'

release = '0.1'
version = '0.1.0'
    
# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'

# -- Options for EPUB output
epub_show_urls = 'footnote'

html_static_path = ['_static']

#html_style = 'css/custom.css'

def setup(app):
    app.add_css_file('custom.css', 200)
#html_css_files = [
#    'css/custom.css',
#]


