from distutils.core import setup

setup(
    name='Shopify Install',
    version='1.0',
    description='Django App to install Shopify App',
    author='Igor Sobreira',
    author_email='igor@igorsobreira.com',
    url='https://github.com/igorsobreira/shopify_install',
    packages=['shopify_install', 'shopify_install.migrations'],
)
