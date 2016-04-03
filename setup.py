#!/usr/bin/python

import os
import sys
from setuptools import setup
from setuptools.command.test import test as TestCommand


def read(fname):
    """read file from same path as setup.py"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


class Tox(TestCommand):
    """proxy class that enables tox to be run with setup.py test"""
    user_options = [('tox-args=', 'a', "Arguments to pass to tox")]

    def initialize_options(self):
        """initialize the user-options"""
        TestCommand.initialize_options(self)
        self.tox_args = None

    def finalize_options(self):
        """finalize user-options"""
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        """run tox and pass on user-options"""
        # import here, cause outside the eggs aren't loaded
        import tox
        import shlex
        args = self.tox_args
        if args:
            args = shlex.split(self.tox_args)
        errno = tox.cmdline(args=args)
        sys.exit(errno)

setup(
    name='python-escpos',
    use_scm_version=True,
    url='https://github.com/python-escpos/python-escpos',
    download_url='https://github.com/python-escpos/python-escpos/archive/master.zip',
    description='Python library to manipulate ESC/POS Printers',
    bugtrack_url='https://github.com/python-escpos/python-escpos/issues',
    license='GNU GPL v3',
    long_description=read('README.rst'),
    author='Manuel F Martinez',
    author_email='manpaz@bashlinux.com',
    platforms=['linux'],
    packages=[
        'escpos',
    ],
    package_data={'': ['COPYING']},
    classifiers=[
        'Development Status :: 1 - Alpha',
        'License :: OSI Approved :: GNU GPL v3',
        'Operating System :: GNU/Linux',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: System :: Peripherals',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'pyusb',
        'Pillow>=2.0',
        'qrcode>=4.0',
        'pyserial',
        'six',
        'appdirs',
        'pyyaml',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    tests_require=['tox', 'nose', 'scripttest'],
    cmdclass={'test': Tox},
)
