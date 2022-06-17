from setuptools import setup, find_packages


def requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='auth_server',
    version='0.1.0',
    author='Mirko Mälicke',
    author_email='mirko@hydrocode.de',
    install_requires=requirements(),
    description='101 Auth Server',
    long_description=readme(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
)