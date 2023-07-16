# Personal Docs

![Site-Deploy](https://github.com/oscarngncc/PersonalDocs/actions/workflows/ci.yml/badge.svg)

## Run Locally

1. Install python and pip

2. run `pip install -r requirements.txt`

3. Run `python ./gen_index_md.py` to generate index.md for vault

4. Run `python ./gen_graph.py` to generate content for obsidian_graph.html

5. Run `python -m mkdocs build --no-directory-urls`. Remove `python -m` if not in Windows

6. Run `start "site\index.html"` (or `wslview site/index.html` and any linux equivalent of opening static html)

## Configuring the website

### Arranging GitHub Nav and Site

Navigation is done through `nav` option in the `mkdocs.yml`, similar to the setup for [the Blue Book](https://lyz-code.github.io/blue-book/) at [github](https://github.com/lyz-code/blue-book/blob/master/mkdocs.yml).

However, in addition to mkdocs's default yml setting, two additional mkdocs plugins are used to streamline the process:

- literate-nav: introduce wildcard option for files to be included, and possibility of SUMMARY.md as nav
- section-index: use `index.md` within section if it's available in the folder

## Alternatives for Obsidian Docs Public Hosting

- [kmaasrud/oboe](https://github.com/kmaasrud/oboe): tool to convert an Obsidian vault into a static directory of HTML files.
- [Jackiexiao/foam-mkdocs-template](https://github.com/Jackiexiao/foam-mkdocs-template): template for Obsidian/Foam using mkdocs/mkdocs-material/mkdocs-roamlinks-plugin
- [foambubble/foam-template](https://github.com/foambubble/foam-template): Foam workpace template
- [mathieudutour/gatsby-digital-garden: digital garden with Gatsby](https://github.com/mathieudutour/gatsby-digital-garden)
- [TuanManhCao/digital-garden: Free Obisidian Publish alternative](https://github.com/TuanManhCao/digital-garden)

