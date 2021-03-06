#!/usr/bin/env python

from distutils.core import setup

setup(name='i3ipc',
    version='0.1',
    description='i3 IPC communication library.',
    author='Nathan Middleton',
    author_email='nathan.middleton@gmail.com',
    url='https://github.com/thepub/i3ipc',
    packages=['i3ipc', 'i3ipc.I3Bar', 'i3ipc.I3Bar.modules'],
    scripts=['bin/i3ipc','bin/i3wsbar',],
    )
