# -*- coding: utf-8 -*-

import io
import yaml


def rewrite_yml(data):
    with io.open('.\\_build\\docfx_yaml\\toc.yml', 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

with open(".\\_build\\docfx_yaml\\toc.yml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)
        for node in data_loaded:
            if 'name' in node:
                if node['name'].startswith('azure.'):
                    node['name'] = node['name'].replace('.', '-')
                    print('update old name to %s' % node['name'])

        rewrite_yml(data_loaded)
    except yaml.YAMLError as exc:
        print(exc)

