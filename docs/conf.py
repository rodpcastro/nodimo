# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

sys.path.insert(0, os.path.abspath('../nodimo'))

# from inspect import getsourcefile
# # Get path to directory containing this file, conf.py.
# DOCS_DIRECTORY = os.path.dirname(os.path.abspath(getsourcefile(lambda: 0)))
# def ensure_pandoc_installed(_):
#     import pypandoc
#     # Download pandoc if necessary. If pandoc is already installed and on
#     # the PATH, the installed version will be used. Otherwise, we will
#     # download a copy of pandoc into docs/bin/ and add that to our PATH.
#     pandoc_dir = os.path.join(DOCS_DIRECTORY, "bin")
#     # Add dir containing pandoc binary to the PATH environment variable
#     if pandoc_dir not in os.environ["PATH"].split(os.pathsep):
#         os.environ["PATH"] += os.pathsep + pandoc_dir
#     pypandoc.ensure_pandoc_installed(
#         targetfolder=pandoc_dir,
#         delete_installer=True,
#     )
# def setup(app):
#     app.connect("builder-inited", ensure_pandoc_installed)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Nodimo'
copyright = '2024, Rodrigo Castro'
author = 'Rodrigo Castro'
release = '1.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'nbsphinx',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# autodoc
autodoc_inherit_docstrings = False
autosummary_generate = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
