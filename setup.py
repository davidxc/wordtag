"""

Setup script for the Word Tag program.
Note on dependencies: Word Tag has dependencies on NLTK >= 2.0, 
wxPython >= 2.8,and NumPy > 1.6. NumPy needs a C compiler to install its
extensions, but it's often easier to install NumPy from a binary package.
wxPython cannot currently be installed from PyPi, it must be installed manually from
the wxPython website.

"""


from setuptools import setup, find_packages

setup(
      name = "WordTag",
      version = "1.0",
      packages = find_packages(),
      
      install_requires = ['nltk >= 2.0', 'wxPython >= 2.8', 'numpy >= 1.6'],
      
      include_package_data = True,
       
      author = "David Wong",
      author_email = "davidwong.xc@gmail.com",
      description = "GUI part of speech tagger that uses the NLTK library.",
      license = "BSD",
      keywords = "natural language, grammar",
      url = "https://github.com/david92",
)
      

