import argparse
import os
import json
import fnmatch
import re
import yaml
import glob
from distutils.dir_util import copy_tree


LEGACY_SOURCE_FOLDER = "workaround"

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))

if __name__ == "__main__":
  # parse packages.json
  with open(os.path.join(root_dir, "workaround", 'targets.json'), 'r') as f:
    text = f.read().rstrip("\n")
    json = json.loads(text)
    migrating_namespaces = json["migrating_namespaces"]

  for config_item in migrating_namespaces:
    target_folder = os.path.join(root_dir, list(config_item.keys())[0])
    target_toc_loc = os.path.join(target_folder, "toc.yml")
    source_toc_loc = os.path.join(root_dir, LEGACY_SOURCE_FOLDER, "docs-ref-autogen", "toc.yml")
    selected_targets = config_item[list(config_item.keys())[0]]

    print("target folder {} has selected_targets {}".format(target_folder, selected_targets))

    # get the source yaml
    with open(source_toc_loc, "r", encoding="utf-8") as source_yml:
      source_yml = yaml.safe_load(source_yml)

    if not selected_targets:
      continue

    toc_items = []
    folders_for_move = []

    # filter that toc
    for index, top_level_toc_item in enumerate(source_yml):
      if top_level_toc_item["name"] in selected_targets:
        toc_items.append(top_level_toc_item)
        folders_for_move.append(os.path.join(root_dir, LEGACY_SOURCE_FOLDER, "docs-ref-autogen", top_level_toc_item["name"]))

    appended_content = yaml.dump(toc_items, default_flow_style=False)

    # write the toc
    with open(target_toc_loc, "a", encoding="utf-8") as stable_toc:
      stable_toc.write(appended_content)

    for folder in folders_for_move:
      target = os.path.join(target_folder, os.path.basename(folder))
      print("copying {} to {}".format(folder, target))
      copy_tree(folder, target)
