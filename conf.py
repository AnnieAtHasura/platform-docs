#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Hasura Platform documentation build configuration file, created by
# sphinx-quickstart on Thu Jun 30 19:38:30 2016.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from os.path import abspath, dirname, join
sys.setrecursionlimit(2000)

# Monkey patching StandaloneHTMLBuilder to not include unnecessary scripts

from sphinx.builders.html import StandaloneHTMLBuilder
# from sphinx.util.osutil import relative_uri
StandaloneHTMLBuilder.script_files = ["_static/vendor.js"]
# StandaloneHTMLBuilder.imgpath = relative_uri("v0.13", '_images')

# Defaults to development
CURRENT_ENV = os.getenv("ENV") if os.getenv("ENV") else "development"
BASE_DOMAIN = os.getenv("BASE_DOMAIN", "development")

# Algolia variables
ALGOLIA_SECRETS = {
    "development": {
        "APPLICATION_ID": "WCBB1VVLRC",
        "APPLICATION_SEARCH_KEY": "19a7f1bbd9ca23d0b8ae2b5e655ebeb9",
        "ALGOLIA_INDEX_NAME": "stg_docs_search",
    },
    "production": {
        "APPLICATION_ID": "WCBB1VVLRC",
        "APPLICATION_SEARCH_KEY": "0ca574a476e8fe0db465410151288730",
        "ALGOLIA_INDEX_NAME": "docs_search",
    }
}

ALGOLIA_APPLICATION_ID = ALGOLIA_SECRETS[CURRENT_ENV]["APPLICATION_ID"]
ALGOLIA_SEARCH_KEY = ALGOLIA_SECRETS[CURRENT_ENV]["APPLICATION_SEARCH_KEY"]
# Get from env if set
if os.getenv("ALGOLIA_APPLICATION_ID") and os.getenv("ALGOLIA_SEARCH_KEY"):
    ALGOLIA_APPLICATION_ID = os.getenv("ALGOLIA_APPLICATION_ID")
    ALGOLIA_SEARCH_KEY = os.getenv("ALGOLIA_SEARCH_KEY")

ALGOLIA_INDEX_NAME = ALGOLIA_SECRETS[CURRENT_ENV]["ALGOLIA_INDEX_NAME"]
# Get from env if set
if os.getenv("ALGOLIA_INDEX_NAME"):
    ALGOLIA_INDEX_NAME = os.getenv("ALGOLIA_INDEX_NAME")

# set context
html_context = {
    "SITEMAP_DOMAIN": "https://docs.hasura.io/",
    "BASE_DOMAIN": "hasura.io" if BASE_DOMAIN == "production" else "hasura-stg.hasura-app.io",
    "ALGOLIA_APPLICATION_ID": ALGOLIA_APPLICATION_ID,
    "ALGOLIA_SEARCH_KEY": ALGOLIA_SEARCH_KEY,
    "ALGOLIA_INDEX_NAME": ALGOLIA_INDEX_NAME
}

# End of it

# sys.path.insert(0, os.path.abspath('.'))

sys.path.append(abspath(join(dirname(__file__), "_ext")))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

# "sphinxcontrib.fulltoc",
extensions = [
    "djangodocs",
    "fulltoc",
    "generate_index",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinxcontrib.swaggerdoc",
    "sphinxcontrib.httpdomain",
    "sphinx.ext.todo",
    "fullpage_tabs",
    "sphinx_tabs.tabs",
    "graphiql",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The encoding of source files.
#
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Hasura'
copyright = '2016, Hasura'
author = 'Hasura Developers'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = 'x.y'
# The full version, including alpha/beta/rc tags.
release = 'x.y'

#epilog rst lines for frequently reference links in docs
rst_epilog = """
"""

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#
# today = ''
#
# Else, today_fmt is used as the format for a strftime call.
#
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'venv', 'Thumbs.db', '.DS_Store']

# The reST default role (used for this markup: `text`) to use for all
# documents.
#
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------
# import sphinx_rtd_theme
# html_theme = "sphinx_rtd_theme"
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_theme = "djangodocs"

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ["_theme"]
# html_title = '| Hasura ' + version + ' documentation'

# The name for this set of Sphinx documents.
# "<project> v<release> documentation" by default.
#
# html_title = 'Hasura Platform valpha'

# A shorter title for the navigation bar.  Default is the same as html_title.
#
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#
# html_logo = None

# The name of an image file (relative to this directory) to use as a favicon of
# the docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#
html_favicon = "img/layout/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
#
# html_extra_path = []

# If not None, a 'Last updated on:' timestamp is inserted at every page
# bottom, using the given strftime format.
# The empty string is equivalent to '%b %d, %Y'.
#
# html_last_updated_fmt = ''

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#
# html_additional_pages = {}

# If false, no module index is generated.
#
# html_domain_indices = True

# If false, no index is generated.
#
# html_use_index = True

# If true, the index is split into individual pages for each letter.
#
# html_split_index = False

# If true, links to the reST sources are added to the pages.
#
html_show_sourcelink = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Language to be used for generating the HTML full-text search index.
# Sphinx supports the following languages:
#   'da', 'de', 'en', 'es', 'fi', 'fr', 'h', 'it', 'ja'
#   'nl', 'no', 'pt', 'ro', 'r', 'sv', 'tr', 'zh'
#
# html_search_language = 'en'

# A dictionary with options for the search language support, empty by default.
# 'ja' uses this config value.
# 'zh' user can custom change `jieba` dictionary path.
#
# html_search_options = {'type': 'default'}

# The name of a javascript file (relative to the configuration directory) that
# implements a search results scorer. If empty, the default will be used.
#
# html_search_scorer = 'scorer.js'

# Output file base name for HTML help builder.
htmlhelp_basename = 'Hasuradoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
     # The paper size ('letterpaper' or 'a4paper').
     #
     # 'papersize': 'letterpaper',

     # The font size ('10pt', '11pt' or '12pt').
     #
     # 'pointsize': '10pt',

     # Additional stuff for the LaTeX preamble.
     #
     # 'preamble': '',

     # Latex figure (float) alignment
     #
     # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Hasura.tex', 'Hasura Documentation',
     author, 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#
# latex_use_parts = False

# If true, show page references after internal links.
#
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
#
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
#
# latex_appendices = []

# If false, no module index is generated.
#
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'hasura', 'Hasura Documentation',
     [author], 1)
]

# If true, show URL addresses after external links.
#
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'Hasura', 'Hasura Documentation',
     author, 'Hasura', 'Hasura documentation',
     'Docs'),
]

# Documents to append as an appendix to all manuals.
#
# texinfo_appendices = []

# If false, no module index is generated.
#
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
#
# texinfo_no_detailmenu = False
