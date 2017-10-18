# -*- coding: utf-8 -*-
__author__ = "Roman Chernikov, Konstantin Klementiev"
__date__ = "18 Oct 2017"

import re

#  Spyderlib modules can reside in either Spyder or Spyderlib, so we check both
#  It's definitely not the optimal solution, but it works.
try:
    from spyderlib.widgets.sourcecode import codeeditor
    isSpyderlib = True
except ImportError:
    try:
        from spyder.widgets.sourcecode import codeeditor
        isSpyderlib = True
    except ImportError:
        isSpyderlib = False

try:
    from spyderlib.widgets.externalshell import pythonshell
    isSpyderConsole = True
except ImportError:
    try:
        from spyder.widgets.externalshell import pythonshell
        isSpyderConsole = True
    except ImportError:
        isSpyderConsole = False

try:
    from spyderlib.utils.inspector.sphinxify import (CSS_PATH, sphinxify,
                                                     generate_context)
    isSphinx = True
except (ImportError, TypeError):
    try:
        from spyder.utils.inspector.sphinxify import (CSS_PATH, sphinxify,
                                                      generate_context)
        isSphinx = True
    except ImportError:
        CSS_PATH = None
        sphinxify = None
        isSphinx = False

if not isSphinx:
    try:
        from spyderlib.utils.help.sphinxify import (CSS_PATH, sphinxify,  # analysis:ignore
                                                    generate_context)  # analysis:ignore
        isSphinx = True
    except (ImportError, TypeError):
        try:
            from spyder.utils.help.sphinxify import (CSS_PATH, sphinxify,  # analysis:ignore
                                                        generate_context)  # analysis:ignore
            isSphinx = True
        except ImportError:
            pass

if isSphinx:
    if CSS_PATH is not None:
        CSS_PATH = re.sub('\\\\', '/', CSS_PATH)
