# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "demoutrei's guidebooks"
copyright = '2026, demoutrei'
author = 'demoutrei'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
  "shibuya",
  "sphinx_contributors",
  "sphinx_design",
  "sphinx_docsearch",
  "sphinx_tabs.tabs"
]

docsearch_app_id = "7SK6I97BWU"
docsearch_api_key = "1a20bb0af63a8bd4ac12fea09b41ed0c"
docsearch_index_name = "guidebooks_crawler_pages"

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_context = {
  "source_type": "github",
  "source_user": "demoutrei",
  "source_repo": "guides",
  "source_version": "main",
  "source_docs_path": "/",
  "source_edit_template": "https://github.com/demoutrei/guides/blob/main/{0}"
}
html_favicon = "_static/demoutrei.png"
html_theme = 'shibuya'
html_theme_options = {
  "accent_color": "demoutrei",
  "dark_code": True,
  "globaltoc_expand_depth": 1,
  "toctree_maxdepth": 1,
  "show_ai_links": False
}
html_static_path = ['_static']
html_css_files = [ "custom.css" ]