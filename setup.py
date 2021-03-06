#!/usr/bin/env python

from distutils.core import setup

setup(name='django-mathfilters',
      version='0.2.1',
      description='A set of simple math filters for Django',
      long_description=open('README.rst').read(),
      author='Danilo Bargen',
      author_email='gezuru@gmail.com',
      url='https://github.com/dbrgn/django-mathfilters',
      license='MIT',
      keywords='django template filters math',
      packages=['mathfilters', 'mathfilters.templatetags'],
      package_dir={'mathfilters': 'mathfilters'},
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )
