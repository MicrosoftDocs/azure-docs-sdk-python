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
  'azure.servicemanagement*.rst'
]


namespace_package_dict = {
  'azure_batch-([A-Za-z0-9\-\.]*).egg': 'azure-batch',
  'azure_common-([A-Za-z0-9\-\.]*).egg': 'azure-common',
  'azure_graphrbac-([A-Za-z0-9\-\.]*).egg': 'azure-graphrbac',
  'azure_keyvault-([A-Za-z0-9\-\.]*).egg': 'azure-keyvault',
  'azure_mgmt_authorization-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-authorization',
  'azure_mgmt_batch-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-batch',
  'azure_mgmt_billing-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-billing',
  'azure_mgmt_cdn-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-cdn',
  'azure_mgmt_cognitiveservices-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-cognitiveservices',
  'azure_mgmt_commerce-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-commerce',
  'azure_mgmt_compute-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-compute',
  'azure_mgmt_consumption-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-consumption',
  'azure_mgmt_containerregistry-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-containerregistry',
  'azure_mgmt_datalake_analytics-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-datalake_analytics',
  'azure_mgmt_datalake_store-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-datalake-store',
  'azure_mgmt_devtestlabs-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-devtestlabs',
  'azure_mgmt_dns-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-dns',
  'azure_mgmt_documentdb-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-documentdb',
  'azure_mgmt_eventhub-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-eventhub',
  'azure_mgmt_iothub-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-iothub',
  'azure_mgmt_keyvault-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-keyvault',
  'azure_mgmt_logic-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-logic',
  'azure_mgmt_media-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-media',
  'azure_mgmt_monitor-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-monitor',
  'azure_mgmt_network-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-network',
  'azure_mgmt_notificationhubs-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-notificationhubs',
  'azure_mgmt_powerbiembedded-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-powerbiembedded',
  'azure_mgmt_rdbms-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-rdbms',
  'azure_mgmt_recoveryservicesbackup-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-recoveryservicesbackup',
  'azure_mgmt_redis-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-redis',
  'azure_mgmt_resource-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-resource',
  'azure_mgmt_scheduler-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-scheduler',
  'azure_mgmt_search-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-search',
  'azure_mgmt_servermanager-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-servermanager',
  'azure_mgmt_servicebus-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-servicebus',
  'azure_mgmt_sql-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-sql',
  'azure_mgmt_storage-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-storage',
  'azure_mgmt_trafficmanager-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-trafficmanager',
  'azure_mgmt_web-([A-Za-z0-9\-\.]*).egg': 'azure-mgmt-web',
  'azure_monitor-([A-Za-z0-9\-\.]*).egg': 'azure-monitor',
  'azure_servicebus-([A-Za-z0-9\-\.]*).egg': 'azure-servicebus',
  'azure_servicefabric-([A-Za-z0-9\-\.]*).egg': 'azure-servicefabric',
  'azure_servicemanagement_legacy-([A-Za-z0-9\-\.]*).egg': 'azure-servicemanagement-legacy',
}
