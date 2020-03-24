import os
import sys

from setuptools import find_packages, setup

version = '0.9.3'

setup(
    name='pyeverywhere',
    version=version,
    description='Build and deploy cross-platform desktop and mobile apps using Python.',
    author='Kevin Ollivier',
    author_email='kevin@kosoftworks.com',
    license='APL',
    package_dir={'': 'src'},
    package_data={'': ['controllers/files/*']},
    packages=find_packages('src'),
    install_requires=['requests', 'six', 'virtualenv-api', 'pbxproj', 'pyinstaller'],
    extras_require={
        ':sys_platform=="darwin"': ['dmgbuild'],
        ':sys_platform=="darwin" and platform_machine=="x86_64"': ['wxPython'],
        ':sys_platform=="linux"': ['pygobject'],
    },
    # test_suite = 'your.module.tests',
    entry_points={
        'console_scripts': [
            'pew = pew.cli.tool:main'
        ]
    }
)
