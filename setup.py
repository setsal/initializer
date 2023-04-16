import subprocess

from setuptools import Command, setup
from setuptools.command.install import install


class InitCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        subprocess.call(['echo', 'hi'])
        # Set up git commit hooks
        # import pre_commit.main as pre_commit
        # pre_commit(['install'])
        # # Do additional setup here


setup(
    name='ult-initializer',
    version='0.1.0',
    packages=['ult-initializer'],
    install_requires=[
        'clang-format',    # for C/C++ formatting
        'yapf',    # for Python formatting
        'pre-commit',    # for pre-commit hooks
    ],
    cmdclass={
        'init': InitCommand,
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
