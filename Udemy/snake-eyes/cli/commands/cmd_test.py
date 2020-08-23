import os
import subprocess

import click


@click.command()
@click.argument('path', default=os.path.join('snakeeyes', 'tests'))
@click.option('--disable-warnings', is_flag=True, help='Disables pytest warnings')
def cli(path, disable_warnings):
    """
    Run tests with Pytest.

    :param path: Test path
    :return: Subprocess call result
    """
    options = ''
    if disable_warnings:
        options += '--disable-warnings '

    cmd = f'py.test {options}{path}'
    return subprocess.call(cmd, shell=True)
