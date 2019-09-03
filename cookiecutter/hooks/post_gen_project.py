#!/usr/bin/env python3

import os
import shutil


def test_empty(path):
    try:
        with open(path, 'rb') as f:
            content = f.read().strip()
            if len(content) == 0:
                return True
    except Exception:
        pass
    return False


paths_to_delete = []
for path in [os.path.join(x[0], y) for x in os.walk('.') for y in x[2]]:
    if path.endswith('.rename'):
        continue
    if test_empty(path):
        paths_to_delete.append(path)
    if path.endswith('.delete'):
        if not test_empty(path):
            paths_to_delete.append(path.replace('.delete', ''))
            paths_to_delete.append(path)

for path in paths_to_delete:
    if os.path.basename(path) in ['__init__.py']:
        continue
    try:
        print("remove %s" % path)
        os.unlink(path)
    except Exception:
        pass


paths_to_rename = []
paths_to_delete = []
for path in [os.path.join(x[0], y) for x in os.walk('.') for y in x[2]]:
    if path.endswith('.rename'):
        if test_empty(path):
            paths_to_delete.append(path)
            paths_to_delete.append(path.replace('.rename', ''))
            continue
        with open(path, 'rb') as f:
            content = f.read().strip().decode("utf8")
            if len(content.encode('utf8').split(b"\n")) != 1:
                raise Exception("bad content: [%s] for path=%s" %
                                (content, path))
            newpath = os.path.join(os.path.dirname(path), content)
            paths_to_rename.append((path.replace('.rename', ''), newpath))
            paths_to_delete.append(path)

for source, target in paths_to_rename:
    print("move %s => %s" % (source, target))
    shutil.move(source, target)

for path in paths_to_delete:
    print("remove %s" % path)
    os.unlink(path)

if os.path.exists("README.md.improve") and os.path.exists("README.md"):
    print("improving README.md...")
    os.system("improve_readme.sh ./README.md")
    os.unlink("README.md.improve")
