# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = 'WHOTS-16'
copyright = f'{datetime.now().year}, Fernando Carvalho Pacheco'
author = 'Fernando Carvalho Pacheco'

# The full version, including alpha/beta/rc tags
release = '0.0.1'
version = '1.0'

# -- General configuration ---------------------------------------------------
extensions = [
    "myst_parser",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "nbsphinx",
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
]

intersphinx_mapping = {
    "cchdo-website": ("https://exchange-format.readthedocs.io/en/latest/", None),
}

myst_url_schemes = ["http", "https", ]

# Added cross reference for headings
myst_heading_anchors = 3

# Add numbered roles
numfig = True

# Enable some MyST extensions.
myst_enable_extensions = [
    "colon_fence",
]

# Make sure the explicity target is unique
autosectionlabel_prefix_document = True
autosectionlabel_maxdepth = 3

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
source_suffix = '.md'
# master_doc = 'index'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'build', 'Thumbs.db', '.DS_Store', '.env']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_book_theme"
html_logo = "_static/_images/logo_HOT.png"
html_title = "WHOTS-16"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_theme_options = {
    "repository_url": "https://github.com/hot-dogs/whots16-data-report",
    "use_repository_button": True,
    "use_issues_button": True,
    "home_page_in_toc": False,
}

# -- Options for LaTeX output ---------------------------------------------
latex_engine = 'pdflatex'

latex_elements = {
    'papersize': 'a4paper',
    # Sonny, Lenny, Glenn, Conny, Rejne, Bjarne and Bjornstrup # 'fncychap': '\\usepackage[Lenny]{fncychap}',
    'fncychap': '\\usepackage[Bjornstrup]{fncychap}',
    'fontpkg': '\\usepackage{amsmath,amsfonts,amssymb,amsthm}',
    'figure_align': 'htbp',
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    'preamble': r'''
        %%%%%%%%%%%%%%%%%%%% Meher %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%% add number to subsubsection 2=subsection, 3=subsubsection
        %%% below subsubsection is not good idea.
        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
        \setcounter{secnumdepth}{3}
        %
        %%%% Table of content upto 2=subsection, 3=subsubsection
        \setcounter{tocdepth}{3}

        \usepackage{amsmath,amsfonts,amssymb,amsthm}
        
        % Include Imagesi
        \usepackage{graphicx}

%       %%% Reduce spaces for Table of contents, figures and tables
%       %%% It is used "\addtocontents{toc}{\vskip -1.2cm}" etc. in the document
%       \usepackage[notlot,nottoc,notlof]{}

%       \usepackage{color}
%       \usepackage{transparent}
%       \usepackage{eso-pic}
%       \usepackage{lipsum}

%       \usepackage{footnotebackref} %%link at the footnote to go to the place of footnote in the text

%       %% spacing between line
%       \usepackage{setspace}
%       %%%%\onehalfspacing
%       %%%%\doublespacing
%       \singlespacing


%       %%%%%%%%%%% datetime
%       \usepackage{datetime}

%       \newdateformat{MonthYearFormat}{%
%           \monthname[\THEMONTH], \THEYEAR}


%       %% RO, LE will not work for 'oneside' layout.
%       %% Change oneside to twoside in document class
%       \usepackage{fancyhdr}
%       \pagestyle{fancy}
%       \fancyhf{}

%       %%% Alternating Header for oneside
%       \fancyhead[L]{\ifthenelse{\isodd{\value{page}}}{ \small \nouppercase{\leftmark} }{}}
%       \fancyhead[R]{\ifthenelse{\isodd{\value{page}}}{}{ \small \nouppercase{\rightmark} }}

%       %%% Alternating Header for two side
%       %\fancyhead[RO]{\small \nouppercase{\rightmark}}
%       %\fancyhead[LE]{\small \nouppercase{\leftmark}}

%       %% for oneside: change footer at right side. If you want to use Left and right then use same as header defined above.
%       \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{{\tiny Meher Krishna Patel} }{\href{http://pythondsp.readthedocs.io/en/latest/pythondsp/toc.html}{\tiny PythonDSP}}}

%       %%% Alternating Footer for two side
%       %\fancyfoot[RO, RE]{\scriptsize Meher Krishna Patel (mekrip@gmail.com)}

%       %%% page number
%       \fancyfoot[CO, CE]{\thepage}

%       \renewcommand{\headrulewidth}{0.5pt}
%       \renewcommand{\footrulewidth}{0.5pt}

%       \RequirePackage{tocbibind} %%% comment this to remove page number for following
%       \addto\captionsenglish{\renewcommand{\contentsname}{Table of contents}}
%       \addto\captionsenglish{\renewcommand{\listfigurename}{List of figures}}
%       \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}}
%       \addto\captionsenglish{\renewcommand{\listtablename}{List of tables}} %%% Heading for TOC


%       %%reduce spacing for itemize
%       \usepackage{enumitem}
%       \setlist{nosep}

%       %%%%%%%%%%% Quote Styles at the top of chapter
%       \usepackage{epigraph}
%       \setlength{\epigraphwidth}{0.8\columnwidth}
%       \newcommand{\chapterquote}[2]{\epigraphhead[60]{\epigraph{\textit{#1}}{\textbf {\textit{--#2}}}}}
%       %%%%%%%%%%% Quote for all places except Chapter
%       \newcommand{\sectionquote}[2]{{\quote{\textit{``#1''}}{\textbf {\textit{--#2}}}}}
    ''',

    'maketitle': r'''
        \pagenumbering{Roman} %%% to avoid page 1 conflict with actual page 1

        \begin{titlepage}
            \centering

            \vspace*{40mm} %%% * is used to give space from top
            {\scshape\Large {University of Hawaii at Manoa} \par}
            \rule{\textwidth}{0.4pt}\vspace*{-\baselineskip}\vspace{3.2pt} 
            \rule{\textwidth}{1.6pt}
            
            \vspace{1mm}
            
            \hbox{\hspace{0em}\includegraphics[width=16cm]{all_whot_report.png}}
            \rule{\textwidth}{1.6pt}\vspace*{-\baselineskip}\vspace*{2pt} % Thick 
            \rule{\textwidth}{0.4pt} % Thin horizontal rule
            
            {\Large \textbf{Hydrographic Observations At the Woods Hole Oceanographic 
            Institution Hawaii Ocean Time-series Site: 2019 - 2020} \par}
            
            by\par

            \vspace{0mm}
            
            {\normalsize \ 
            Fernando Carvalho Pacheco\footnote{The University of Hawaii at Manoa}, 
            Fernando Santiago-Mandujano\footnotemark[\value{footnote}], 
            Albert Plueddemann\footnote{Woods Hole Oceanographic Institution},
            Robert Weller\footnotemark[\value{footnote}],
            James Potemra\footnotemark[1],
            Daniel Fitzgerald\footnotemark[1] 
            and Nan Galbraith\footnotemark[2] \par}
            
            \vspace{0.25cm}
            {\normalsize \today\par} 
            {\Large\bfseries Data Report - 16 \par}
            \vspace{1cm}
            
            {\normalsize \ Approved for public release; distribution unlimited. \par}
            
            % Bottom of the page
            \vspace{1.5cm} 

            {\normalsize \ The University of Hawaii at Manoa \\
            School of Ocean and Earth Science and Technology \\
            1000 Pope Road, Honolulu, Hawaii 96822\par}
            \vspace{1cm}
            
            {\large\ SOEST Publication no. xXxXxXxXxXxXxX \par} 
            
            \vspace{0.25cm}

        \end{titlepage}

        \clearpage
        \pagenumbering{roman}
        \tableofcontents
        % \listoffigures
        % \listoftables
        \clearpage
        \pagenumbering{arabic}

        ''',
    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
    'sphinxsetup': \
        'hmargin={0.7in,0.7in}, vmargin={1in,1in}, \
        verbatimwithframe=true, \
        TitleColor={rgb}{0,0,0}',

    'tableofcontents': ' ',

}

latex_additional_files = ['figures/*']

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = "_static/_images/all_whots_report.png"

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
    ('index', 'whots16-data-report.tex',
     u'WHOTS-16: Data Report',
     u'Fernando Carvalho Pacheco', 'report'),
]


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
latex_domain_indices = True

# -- Options for manual page output ---------------------------------------


# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
# man_pages = [
#     ('index', 'whots-manual-page-test', u'whots-manual-page-test',
#      [u'Fernando Carvalho Pacheco'], 1)
# ]
#
# latex_logo = "../source/_static/_images/logo_HOT.jpg"

# -- Options for Epub output ----------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'whots-epub-test'
epub_author = u'Fernando Carvalho Pacheco'
epub_publisher = u'Fernando Carvalho Pacheco'
epub_copyright = f'2022-04-02-{datetime.now().year}, Fernando Carvalho Pacheco'
