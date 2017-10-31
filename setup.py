import os
import re

from setuptools import setup, find_packages

requires = [
    'boto3>=1.4.7',
    'requests>=2.18.4',
    'google-cloud-bigquery>=0.27.0',
]

ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


def get_version():
    init = open(os.path.join(os.path.join(ROOT, 'blueforge'), '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='blueforge',
    version=get_version(),
    description='The Blueforge for Python',
    long_description=open('README.rst').read(),
    author='Bluehack',
    author_email='jh.lim@bluehack.net',
    url='https://github.com/BlueHack-Core/blueforge',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={
        'blueforge': [
            'data/*/*/*.json',
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 1 - Planning',
    ],
)
