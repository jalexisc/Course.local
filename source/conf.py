# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
import datetime
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'Higgs'
author = 'Jose Alexis Correa Valencia'
year_now = datetime.date.today().year
copyright = '2012-' + str(year_now) + ' Jose Alexis Correa Valencia'
language = 'es'
version = 'Curso de PHP8.4 By @jalexiscv'
release = '7.0.2'

# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinxcontrib.phpdomain',
	'sphinx_rtd_theme',
	'sphinx_sitemap',
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects htmlstatic_path and html_extra_path.
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'trac'

# The default language to highlight source code in.
highlight_language = 'html+php'

# A dictionary of options that modify how the lexer specified by
# highlight_language generates highlighted source code.
highlight_options = {'startinline': True}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['static']

# Specify the directory where static files should be copied to and how they should be referenced
html_static_path_suffix = ''
html_use_static_prefix = False
html_context = {
    'css_files': [
        'static/pygments.css',
        'static/css/theme.css',
        'static/css/citheme.css',
    ],
}

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
	'collapse_navigation': False,
	'sticky_navigation': False,
	'navigation_depth': 1,
	'includehidden': False,
	'logo_only': True,
	'display_version': True,
}

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
html_last_updated_fmt = '%b %d, %Y'

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'static/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs. This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'static/favicon.ico'

# The name of an style sheet to use for HTML pages.
# html_style = 'css/citheme.css' # Deprecated, using html_css_files instead

# Output file base name for HTML help builder.
htmlhelp_basename = 'Higgsdoc'

# If true, the reST sources are included in the HTML build as _sources/name.
html_copy_source = False

# A list of CSS files.
html_css_files = [
    'css/citheme.css',
    # 'css/citheme_dark.css', # Uncomment to enable dark theme
]

# A list of JS files.
html_js_files = [
	'js/citheme.js',
	'js/carbon.js'
]

# -- Options for LaTeX output --------------------------------------------------

# This value determines how to group the document tree into LaTeX source files.
# It must be a list of tuples (startdocname, targetname, title, author, theme,
# toctree_only)
latex_documents = [
	('index', 'Higgs.tex', 'Higgs(AI) Documentation',
	'Higgs(AI)', 'manual'),
]

# -- Options for manual page output --------------------------------------------

# This value determines how to group the document tree into manual pages. It
# must be a list of tuples (startdocname, name, description, authors, section)
man_pages = [
	('index', 'Higgs', 'Higgs(AI) Documentation',
	['Higgs(AI)'], 1)
]

# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core metadata.
epub_title = 'Higgs(AI)'
epub_author = 'Higgs(AI)'
epub_publisher = 'Higgs(AI)'
epub_copyright = copyright


html_baseurl = 'https://higgs.com.co/'


