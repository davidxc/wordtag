"""
This is the initialization file that makes Python treat the 
root directory for the text-tagger files as containing modules.

The text-tagger program can be run from the main.py file.

The main.py file contains the code for creating the GUI and binding events. 
It imports the application logic from logic.py, which contains the code for application events.

Author: David Wong <davidwong.xc@gmail.com>
License: 3 clause BSD license
"""

from word_tag.main import startapp
