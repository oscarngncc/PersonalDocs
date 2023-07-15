#!/usr/bin/env python

"""
Generates a graph of the Obsidian vault.
Code modified based on: https://github.com/ObsidianPublisher/sync_template/blob/5577a88f28cadb1811423afc3782ebbc898f8b16/overrides/hooks/on_env.py#L13-L36
For more context, see: https://obsidian-publisher.netlify.app/advanced/customization/#graph-view

Prerequisite: must run script within PersonalDocs directory, where the script is located
Warning: lib folder will be completely removed. Beaware if there's an actual lib library for other purposes
Usage: gen_graph.py
"""

import shutil
from pathlib import Path
import obsidiantools.api as otools
from pyvis.network import Network

def obsidian_graph():
    vault_path = Path(Path.cwd(), "docs")
    vault = otools.Vault(vault_path).connect().gather()
    graph = vault.graph
    net = Network(
        height="750px", 
        width="100%", 
        bgcolor="pink", 
        font_color="black",
    )
    net.from_nx(graph)
    
    html_graph_path = str(Path.cwd() / "docs" / "obsidian_graph.html")
    try:
        net.save_graph(html_graph_path)
    except OSError:
        print("OS error! Maybe missing file in " + html_graph_path + "?")
        pass
    shutil.rmtree(Path.cwd() / "lib")


obsidian_graph()