import os
import re

from setuptools import setup

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')

requires = []


def get_version():
    init = open(os.path.join(ROOT, 'python_package_template', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='python-package-template',
    version=get_version(),
    description='Python package template',
    long_description=open('README.rst').read(),
    author='phesSofthouse',
    author_email='philip.esmailzade@softhouse.se',
    url='https://github.com/phesSofthouse/python-package-template',
    scripts=[],
    packages=['python_package_template'],
    install_requires=requires,
    license='MIT License',
    python_requires='>= 3.7',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)
