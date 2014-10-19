from setuptools import setup

setup(name='httpsync',
        version='0.1.1',
        description='HTTP Sync Client',
        author='Henry Stern',
        author_email='stern@fsi.io',
        url='https://github.com/farsightsec/httpsync',
        scripts=['httpsync'],
        install_requires=['requests', 'python-librsync'],
        )
