# -*- coding: utf-8 -*-
#
import sys
import os

# -- General configuration ------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
# This doesn't work on ReadTheDocs
## also add these in a requirements.txt file in the configuration build directory.
extensions = ['sphinxcontrib.phpdomain']

# Default domain
primary_domain = 'php'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'