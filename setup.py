#!/usr/bin/env python2
#Copyright (C) 2014, Cameron Brandon White
# -*- coding: utf-8 -*-

import setuptools

if __name__ == "__main__":
    setuptools.setup(
        name="Flask-CAS",
        version="0.1.0",
        description="Flask extension for CAS",
        author="Cameron Brandon White",
        author_email="cameronbwhite90@gmail.com",
        packages=[
            "flask_cas",
        ],
        install_requires = [
            "Flask",
            "Nose",
        ],
        include_package_data=True,
        classifiers=[
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
    )
