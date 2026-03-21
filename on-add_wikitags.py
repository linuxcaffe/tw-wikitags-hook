#!/usr/bin/env python3
import os as _os_timing, time as _time_module
if _os_timing.environ.get('TW_TIMING'):
    import atexit as _atexit
    _t0 = _time_module.perf_counter()

    def _report_timing(_f=__file__):
        elapsed = (_time_module.perf_counter() - _t0) * 1000
        import os.path as _osp
        print(f"[timing] {_osp.basename(_f)}: {elapsed:.1f}ms", file=__import__('sys').stderr)

    _atexit.register(_report_timing)

## version 0.2.0
import json
import re
import sys

# licenced under the M.I.T. licence (do what you will, don't blame me)
# Adds the ability to create inline tags from description text 

# inspired by https://gist.github.com/wbsch/164757889ba4554df359
# idea and whining by djp
# working code by bqf

# Turns
#    $ task add I saw :bob: in the :tool:shed:
# Into the equivalent of
#    $ task add I saw :bob: in the :tool:shed: +bob +tool +shed
# This :tag:format: is used by vimwiki (taskwiki), orgmode and  *ledger

### SETUP
# Save (or symlink) this file as
#   ~/.task/hooks/on-add_wikitags.py
# change to that directory:
#   $ cd ~/.task/hooks
# make the script executable:
#   $ chmod +x on-add_wikitags.py
# then create a symlink to that file, to make it an on-modify hook as well:
#   $ ln -s on-add_wikitags.py on-modify_wikitags.py
# so that tags are created whether you are adding OR modifying a task

def add_inline_tags(task):
    inline_tags = re.findall(r"(?:\A| ):([^ ]+):", task['description'])
    for tags in inline_tags:
       for tag in tags.split(":"):
           if 'tags' not in task:
              task['tags'] = [tag]
           elif tag not in task['tags']:
              task['tags'].append(tag)

    print(json.dumps(task))


old = sys.stdin.readline()
new = sys.stdin.readline()

if not new:
    add_inline_tags(json.loads(old))
else:
    add_inline_tags(json.loads(new))
