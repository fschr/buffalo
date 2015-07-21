try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='buffalo',
      author='Thomas D. Fischer',
      version='1.0.2',
      py_modules=['buffalo', 'buffalo.examples'],
      )
