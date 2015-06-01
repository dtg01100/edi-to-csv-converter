from distutils.core import setup
import py2exe

setup(windows=["converter_ui.py"])
data_files = ['logo.jpg']
options = {'py2exe': {
"optimize": 2,
"bundle_files": 2, # This tells py2exe to bundle everything
  }},