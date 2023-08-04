#!/usr/bin/env python
"""
sentry-redis-nodestore
==============
An extension for Sentry which implements an Redis NodeStorage backend
"""
from setuptools import setup

install_requires = [
    'sentry>=23.7.1',
]


setup(
    name='sentry-redis-nodestore',
    version='1.0.0',
    author='Negashev Alexandr',
    author_email='i@negash.ru',
    url='http://github.com/negashev/sentry-redis-nodestore',
    description='A Sentry extension to add Redis as a NodeStore backend.',
    long_description=__doc__,
    packages=['sentry_redis_nodestore'],
    license='BSD',
    zip_safe=False,
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
