# -*- coding: utf-8 -*-

import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('.'))

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'pyexample'
copyright = u'2015, rtfd'
author = u'rtfd'
version = '0.1'
release = '0.1'
language = None
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'pyexampledoc'



extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'docfx_yaml.extension']

napoleon_use_admonition_for_examples = True 

exclude_patterns = [
  '_build',
  '*.tests.rst',
  'ref/azure.batch*.rst',
  'ref/azure.graphrbac*.rst',
  'ref/azure.keyvault*.rst',
  'ref/azure.monitor*.rst',
  'ref/azure.servicebus*.rst',
  'ref/azure.servicefabric*.rst',
  'ref/azure.servicemanagement*.rst'
]
