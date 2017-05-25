# -*- coding: utf-8 -*-

import io
import shutil
import yaml

# Write YAML file
    #shutil.move('.\\_build\\docfx_yaml\\toc.yml', '.\\_build\\docfx_yaml\\toc.yml.back')
def rewrite_yml(data):
    with io.open('.\\_build\\docfx_yaml\\toc.yml', 'w', encoding='utf8') as outfile:
        yaml.dump(data, outfile, default_flow_style=False, allow_unicode=True)

        
with open(".\\_build\\docfx_yaml\\toc.yml", 'r') as stream:
    try:
        data_loaded = yaml.load(stream)

        # should only have one root node: cntk
        if len(data_loaded) == 1:
            cntk_node = data_loaded[0]
            if 'name' in cntk_node:
                print(cntk_node['name'])
                cntk_node['name'] = 'Reference'

            # change leave 2 node's name: remove 'cntk' prefix
            if 'items' in cntk_node:
                for item in cntk_node['items']:
                    if 'name' in item:
                        if item['name'].startswith('cntk.'):
                            item['name'] = item['name'][5:]
                            print('update old name to %s' % item['name'])

        rewrite_yml(data_loaded)
    except yaml.YAMLError as exc:
        print(exc)

