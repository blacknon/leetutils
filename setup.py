#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =======================================================


import os
import platform

import setuptools
import sphinx.ext.apidoc
from sphinx.setup_command import BuildDoc


class BuildDocApiDoc(BuildDoc, object):
    # inherit from object to enable 'super'
    user_options = []
    description = 'sphinx'

    def run(self):
        # metadata contains information supplied in setup()
        metadata = self.distribution.metadata

        # package_dir may be None, in that case use the current directory.
        src_dir = (self.distribution.package_dir or {'': ''})['']
        src_dir = os.path.join(os.getcwd(), src_dir, 'docs')
        print(src_dir)

        # Run sphinx by calling the main method, '--full' also adds a conf.py
        cmd_line = ['-f', '-H', metadata.name, '-A', metadata.author,
                    '-V', metadata.version, '-R', metadata.version, '-T',
                    '-o', os.path.join('docs', '_build'), src_dir]

        print(cmd_line)
        sphinx.ext.apidoc.main(cmd_line)

        super(BuildDocApiDoc, self).run()


try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''


name = 'leetutils'
version = '1.0.0'
release = '1.0.0'

if __name__ == "__main__":
    setuptools.setup(
        name=name,
        version=version,
        author='blacknon',
        author_email='blacknon@orebibou.com',
        maintainer='blacknon',
        maintainer_email='blacknon@orebibou.com',
        description='Return as leet convert string.',
        long_description=readme,
        license="MIT",
        install_requires=[
            'sphinx',
        ],
        url='https://github.com/blacknon/leetutils',
        packages=setuptools.find_packages(),
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'License :: OSI Approved :: MIT License',
        ],
        cmdclass={'build_sphinx': BuildDocApiDoc},
        command_options={
            'build_sphinx': {
                'project': ('setup.py', name),
                'version': ('setup.py', version),
                'release': ('setup.py', release)}},
        setup_requires=['sphinx'],
    )
