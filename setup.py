from setuptools import setup, find_packages

setup(
    name='Shopify Install',
    version='1.0',
    description='Django App to install Shopify App',
    author='Igor Sobreira',
    author_email='igor@igorsobreira.com',
    url='https://github.com/igorsobreira/shopify_install',
    packages=find_packages(),
    install_requires=['requests'],
)
