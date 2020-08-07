import argparse
import os
import json
import fnmatch
import re
import yaml
import glob
import shutil


LEGACY_SOURCE_FOLDER = "workaround"

root_dir = os.path.abspath(os.path.join(os.path.abspath(__file__), ".."))

if __name__ == "__main__":
  # parse packages.json
  with open(os.path.join(root_dir, "workaround", 'targets.json'), 'r') as f:
    text = f.read().rstrip("\n")
    json = json.loads(text)
    migrating_namespaces = json["migrating_namespaces"]

  for config_item in migrating_namespaces:
    target_toc_loc = os.path.join(root_dir, list(config_item.keys())[0],"toc.yml")
    source_toc_loc = os.path.join(root_dir, LEGACY_SOURCE_FOLDER, "docs-ref-autogen", "toc.yml")
    selected_targets = config_item[list(config_item.keys())[0]]

    # get the source yaml
    with open(source_toc_loc, "r", encoding="utf-8") as source_yml:
      source_yml = yaml.safe_load(source_yml)

    # with open(target_toc_loc, "r", encoding="utf-8") as target_yml:
    #   target_yml = yaml.safe_load(target_yml)

    if not selected_targets:
      continue

    # import pdb
    # pdb.set_trace()

    toc_items = []
    files_for_move = []

    # filter that toc
    for index, top_level_toc_item in enumerate(source_yml):
      if top_level_toc_item["name"] in selected_targets:
        toc_items.append(top_level_toc_item)

    appended_content = yaml.dump(toc_items, default_flow_style=False)

    # write the toc
    with open(target_toc_loc, "a", encoding="utf-8") as stable_toc:
      stable_toc.write(appended_content)

  # for file_name in files_for_move:
  #   shutil.copy(file_name, os.path.join(root_dir, TARGET_SOURCE_FOLDER))
