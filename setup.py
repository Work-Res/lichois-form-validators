# -*- coding: utf-8 -*-
import os

from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='lichois-form-validators',
    version='0.1.0',
    author=u'Coulson Kgathi',
    author_email='ckgathi@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/Work-Res/lichois-form-validators',
    license='GPL license, see LICENSE',
    description='Form validator classes for django ModelForms',
    long_description=README,
    zip_safe=False,
    keywords='django modelform form validation lichois',
    #  install_requires=['pandas'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
