# Configuration file for the Sphinx documentation builder.
import os
import sys
sys.path.append(os.path.abspath('../..'))
sys.path.append(os.path.abspath('..'))
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

# These folders are copied to the documentation's HTML output
html_static_path = ['_static']

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)
html_css_files = [
    'css/custom.css',
]

# A workaround for the responsive tables always having annoying scrollbars.
#def setup(app):
#    app.add_css_file("no_scrollbars.css")
    #app.add_stylesheet("no_scrollbars.css")
