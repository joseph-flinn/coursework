import subprocess

import click


@click.command()
@click.argument('path', default='snakeeyes')
def cli(path):
    """
    Run a test coverage report.

    :param path: Test coverage path
    :return: Subprocess call result
    """
    cmd = f'py.test --cov-report term-missing --cov {path}'
    return subprocess.call(cmd, shell=True)
