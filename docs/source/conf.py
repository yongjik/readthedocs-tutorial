# Configuration file for the Sphinx documentation builder.

import os, re, subprocess

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

# Horrible hack: Inside readthedocs, we want to know which branch we're
# generating the documents for.  Readthedocs appends its own configuration
# *after* the contents of this file, so we read our own script to find it out.
def _get_current_branch():
    if PROJECT_VERSION in os.environ:
        print(f'PROJECT_VERSION is set to {PROJECT_VERSION}.')
        return f'v{PROJECT_VERSION}'

    with open(__file__, 'rt') as f:
        for line in f:
            m = re.search(r"'github_version': *'(.*)'", line)
            if m: return m.group(1)

    return 'main'
_my_current_branch = _get_current_branch()

extlinks = {
    'githublink': (
        f'https://github.com/yongjik/readthedocs-tutorial/blob/{_my_current_branch}/%s',
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
subprocess.check_call('playwright install firefox'.split())
