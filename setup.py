#!/usr/bin/env python

from distutils.core import setup

setup(name='i3ipc',
    version='0.1',
    description='i3 IPC communication library.',
    author='Nathan Middleton',
    author_email='nathan.middleton@gmail.com',
    url='https://github.com/thepub/i3ipc',
    py_modules=['i3ipc',],
    scripts=['i3ipc','i3wsbar',],
    )
