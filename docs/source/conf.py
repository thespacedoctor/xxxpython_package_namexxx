# -*- coding: utf-8 -*-

from builtins import str
import sys
import os
from xxxpython_package_namexxx import cl_utils
from datetime import datetime, date, time
# -- Allow Markdown -----------------------------------------------------
# source_suffix = ['.rst', '.md']

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
# sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------
# Fake modules requring C-Libraries
from mock import Mock as MagicMock


class Mock(MagicMock):

    @classmethod
    def __getattr__(cls, name):
        return Mock()

MOCK_MODULES = ['numpy', 'scipy', 'matplotlib', 'matplotlib.colors',
                'matplotlib.pyplot', 'matplotlib.cm', 'matplotlib.path', 'matplotlib.patches', 'matplotlib.projections', 'matplotlib.projections.geo', 'healpy', 'astropy', 'astropy.io', 'pylibmc', 'HMpTy', 'HMpTy.mysql', 'ligo', 'ligo.gracedb', 'ligo.gracedb.rest']
sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)


moduleDirectory = os.path.dirname(os.path.realpath(__file__))
exec(open(moduleDirectory + "/../../xxxpython_package_namexxx/__version__.py").read())

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.todo',
              'sphinx.ext.mathjax', 'sphinx.ext.viewcode', 'sphinx.ext.autosummary', 'sphinx.ext.graphviz', 'recommonmark', 'sphinx_search.extension']

# Generate Summaries
autosummary_generate = True

# Show Todos
todo_include_todos = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
# source_parsers = {
#     '.md': 'recommonmark.parser.CommonMarkParser'
# }

master_doc = 'index'

# General information about the project.

now = datetime.now()
now = now.strftime("%Y")
project = u'xxxpython_package_namexxx'
copyright = u'%(now)s, Dave Young' % locals()


version = "v" + str(__version__)
release = version
today_fmt = '%Y'

pygments_style = 'monokai'
# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build', '_templates',
                    '**__version__.py', '**setup.py', 'api/xxxpython_package_namexxx.rst']
# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ["xxxpython_package_namexxx."]


# -- Options for HTML output ---------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_images/thespacedoctor_icon_white_circle.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_images/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'


# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
# html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

html_add_permalinks = u"  ∞"

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
html_help_basename = 'xxxpython_package_namexxxdoc'


# -- Options for LaTeX output --------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'xxxpython_package_namexxx.tex', u'xxxpython_package_namexxx Documentation',
     u'Dave Young', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_images/thespacedoctor_icon_dark.png"

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output --------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'xxxpython_package_namexxx', u'xxxpython_package_namexxx Documentation',
     [u'Dave Young'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output ------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'xxxpython_package_namexxx', u'xxxpython_package_namexxx Documentation',
     u'Dave Young', 'xxxpython_package_namexxx', 'xxxpackage_descriptionxxx',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'


trim_footnote_reference_space = True


def updateUsageRST():

    from xxxpython_package_namexxx import cl_utils
    usage = cl_utils.__doc__

    if not "Usage:" in usage or "todo:" in usage:
        return None
    usageString = ""
    for l in usage.split("\n"):
        usageString += "    " + l + "\n"

    usage = """Command-Line Usage
==================

.. code-block:: bash 
   
%(usageString)s""" % locals()

    moduleDirectory = os.path.dirname(__file__)
    uFile = moduleDirectory + "/_includes/usage.rst"
    exists = os.path.exists(uFile)
    if exists:
        import codecs
        writeFile = codecs.open(uFile, encoding='utf-8', mode='w')
        writeFile.write(usage)
        writeFile.close()

    return None


updateUsageRST()


def generateAutosummaryIndex():

    import xxxpython_package_namexxx
    import inspect
    import os.path
    import time

    # CHECK FOR LAST MODIFIED TIME - DON'T UPDATE IF < 5 SEC
    # autobuild GOES INTO INFINITE LOOP OTHERWISE
    moduleDirectory = os.path.dirname(__file__)
    file = moduleDirectory + "/autosummary.rst"
    pathToWriteFile = file
    exists = os.path.exists(file)
    if not exists:
        pathToWriteFile = file
        try:
            writeFile = open(pathToWriteFile, 'w')
            writeFile.write("")
            writeFile.close()
        except IOError as e:
            message = 'could not open the file %s' % (pathToWriteFile,)
            raise IOError(message)

    now = time.time()
    delta = now - os.path.getmtime(file)
    if delta < 5:
        return None

    # GET ALL SUBPACKAGES
    allSubpackages = ["xxxpython_package_namexxx"]
    allSubpackages += findAllSubpackges(
        pathToPackage="xxxpython_package_namexxx"
    )

    # INSPECT TO FIND ALL MODULES, CLASSES AND FUNCTIONS
    allModules = []
    allClasses = []
    allFunctions = []
    for sp in allSubpackages:
        for name, obj in inspect.getmembers(__import__(sp, fromlist=[''])):
            if inspect.ismodule(obj):
                if name in ["numpy"]:
                    continue
                thisMod = sp + "." + name
                if thisMod not in allSubpackages and len(name) and name[0:2] != "__" and name[-5:] != "tests" and name != "cl_utils" and name != "utKit":
                    allModules.append(sp + "." + name)

    for spm in allSubpackages + allModules:
        for name, obj in inspect.getmembers(__import__(spm, fromlist=[''])):
            if inspect.isclass(obj):
                thisClass = spm + "." + name
                if (thisClass == obj.__module__ or spm == obj.__module__) and len(name) and name[0:2] != "__":
                    allClasses.append(thisClass)
            if inspect.isfunction(obj):
                thisFunction = spm + "." + name
                if (spm == obj.__module__ or obj.__module__ == thisFunction) and len(name) and name != "main" and name[0:2] != "__":
                    allFunctions.append(thisFunction)

    allSubpackages = allSubpackages[1:]
    allSubpackages.sort(reverse=False)
    allModules.sort()
    allClasses.sort()
    allFunctions.sort()
    allSubpackages = ("\n   ").join(allSubpackages)
    allModules = ("\n   ").join(allModules)
    allClasses = ("\n   ").join(allClasses)
    allFunctions = ("\n   ").join(allFunctions)

    # FOR SUBPACKAGES USE THE SUBPACKAGE TEMPLATE INSTEAD OF DEFAULT MODULE
    # TEMPLATE
    thisText = u""
    if len(allSubpackages):
        thisText += """
Subpackages
-----------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:
   :template: autosummary/subpackage.rst

   %(allSubpackages)s 

""" % locals()

    if len(allModules):
        thisText += """
Modules
-------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allModules)s 

""" % locals()

    if len(allClasses):
        thisText += """
Classes
-------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allClasses)s 

""" % locals()

    if len(allFunctions):
        thisText += """
Functions
---------

.. autosummary::
   :toctree: _autosummary
   :nosignatures:

   %(allFunctions)s 

""" % locals()

    import codecs
    moduleDirectory = os.path.dirname(__file__)
    writeFile = codecs.open(
        moduleDirectory + "/autosummary.rst", encoding='utf-8', mode='w')
    writeFile.write(thisText)
    writeFile.close()

    import re
    regex = re.compile(r'\n\s*.*?utKit\.utKit(\n|$)', re.I)
    allClasses = regex.sub("\n", allClasses)

    classAndFunctions = u"""
**Classes**

.. autosummary::
   :nosignatures:

   %(allClasses)s 

**Functions**

.. autosummary::
   :nosignatures:

   %(allFunctions)s 
""" % locals()

    moduleDirectory = os.path.dirname(__file__)
    writeFile = codecs.open(
        moduleDirectory + "/classes_and_functions.rst", encoding='utf-8', mode='w')
    writeFile.write(classAndFunctions)
    writeFile.close()

    return thisText


def findAllSubpackges(
    pathToPackage
):
    import pkgutil
    importedPackage = __import__(
        pathToPackage, fromlist=[''])
    subPackages = []

    for importer, modname, ispkg in pkgutil.walk_packages(importedPackage.__path__, prefix=importedPackage.__name__ + '.',
                                                          onerror=lambda x: None):
        if ispkg and "tests" != modname[-5:] and "._" not in modname and ".tests." not in modname:
            subPackages.append(modname)

    return subPackages


autosummaryText = generateAutosummaryIndex()

# Add substitutions here
rst_epilog = u"""
.. |tsd| replace:: thespacedoctor
""" % locals()
