"""This module generates xrefmap from external links."""
import os
import urllib.request
import yaml

from sphinx.ext.intersphinx import read_inventory

EXTERNAL_LINKS = ['https://docs.python.org/3.5/',
                  'http://msrestazure.readthedocs.io/en/latest/',
                  'http://msrest.readthedocs.io/en/latest/']
xref_map = []

for external_Link in EXTERNAL_LINKS:
    obj_link = os.path.join(external_Link, 'objects.inv')
    stream = urllib.request.urlopen(obj_link)
    inventory = read_inventory(stream, external_Link, os.path.join)
    for role_key, role_value in inventory.items():
        if role_key.startswith('py:'):
            for ref_name, ref_value in role_value.items():
                # Only use last element in ref_name
                title_name = ref_name.split('.')[-1]
                xref_map.append({'uid': ref_name,
                                 'name': title_name,
                                 'href': ref_value[2],
                                 'fullName': ref_name})

with open('xrefmap.yml', 'w', encoding='utf8') as out_file:
    yaml.dump({'references': xref_map}, out_file, default_flow_style=False, allow_unicode=True)
