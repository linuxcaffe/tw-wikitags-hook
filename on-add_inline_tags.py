#!/usr/bin/env python
#
# PoC for "inline tags", as described in TW-1357
# https://bug.tasktools.org/browse/TW-1357
#
# Turns
#    $ task add I saw @bob in the @garden
# Into the equivalent of
#    $ task add I saw bob in the garden +bob +garden

import json
import re
import sys

t = json.loads(sys.stdin.readline())

inline_tags = re.findall(r"(?:\A| )@([^ ]+)", t['description'])
for newtag in inline_tags:
 if 'tags' not in t:
  t['tags'] = [newtag]
 elif newtag not in t['tags']:
  t['tags'].append(newtag)
t['description'] = re.sub(r"(\A| )@([^ ]+)", r"\1\2", t['description'])

print(json.dumps(t))