try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='buffalo',
      version='1.0',
      py_modules=['pygame'],      
      )
