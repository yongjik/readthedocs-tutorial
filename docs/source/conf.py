# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Lumache'
copyright = '2021, Graziella'
author = 'Graziella'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',

    # YONGJIK
    # Copied from https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html
    'sphinx.ext.extlinks',
]

extlinks = {
    'githublink': (
        'https://github.com/yongjik/readthedocs-tutorial/blob/main/%s',
        'file %s',
    ),
}

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

# YONGJIK: Install Playwright.
import subprocess
subprocess.check_call('playwright install firefox'.split())
