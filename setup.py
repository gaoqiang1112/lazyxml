#!/usr/bin/env python
# -*- coding: utf-8 -*-


from __future__ import with_statement

import sys
if sys.version_info < (2, 5):
    sys.exit('Python 2.5 or greater is required.')

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import lazyxml


with open('README.rst') as fp:
    readme = fp.read()

with open('LICENSE') as fp:
    license = fp.read()

setup(name='lazyxml',
      version=lazyxml.__version__,
      description='Simple xml parse and build lib.',
      long_description=readme,
      author='Zonglong Fan',
      author_email='lazyboy.fan@gmail.com',
      maintainer='Zonglong Fan',
      maintainer_email='lazyboy.fan@gmail.com',
      url='https://github.com/heronotears/lazyxml',
      packages=['lazyxml'],
      license=license,
      platforms=['any'],
      classifiers=[]
      )
