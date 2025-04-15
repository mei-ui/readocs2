project = 'InfoScan'
copyright = '2021, Zilch'
author = 'Zilch'
release = '0.1'

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx_copybutton',
    'sphinx.ext.viewcode'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_js_files = ['js/baidutongji.js']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'myst',
    '.txt': 'myst'
}

autodoc_mock_imports = ['myst_parser']
needs_sphinx = '4.0'
nitpicky = True
nitpick_ignore = [('py:class', 'myst_parser.main.MdParserConfig')]

def setup(app):
    app.add_css_file('css/custom-style.css')
