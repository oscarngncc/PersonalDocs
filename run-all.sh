#!/bin/bash
set -e

cp -r ../Obsidiandocs/* docs/

python3 ./gen_index_md.py
python3 ./gen_graph.py
python3 -m mkdocs build --no-directory-urls
python3 ./inject_security_headers.py

wslview site/index.html

