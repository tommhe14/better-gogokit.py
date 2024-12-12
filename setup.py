import os, sys
from setuptools import setup, find_packages

package_dir = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(package_dir, 'gogokit'))

from config import __version__, __pypi_packagename__

with open(os.path.join(package_dir, 'LICENSE.txt')) as license_file:
    license_text = license_file.read()

with open(os.path.join(package_dir, 'README.md')) as readme_file:
    long_description = readme_file.read()

setup(
    name=__pypi_packagename__,
    version=__version__,
    author='Mane',
    author_email='theckley@yahoo.co.yk',
    packages=find_packages(include=['gogokit', 'gogokit.*']),
    url='https://github.com/tommhe14/better-gogokit.py',
    license=license_text,
    description='A lightweight, viagogo API client library for Python.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=[
        'requests>=2.7.0',
        'uritemplate>=0.6',
        'iso8601>=0.1.10',
        'six>=1.9.0',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['viagogo', 'rest', 'sdk', 'api'],
    python_requires='>=3.7',
)
