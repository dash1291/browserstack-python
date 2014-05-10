from distutils.core import setup

setup(
    name='browserstack',
    version='0.0.1',
    packages=['browserstack',],
    license='MIT',
    long_description='Python wrapper for BrowserStack REST API.',
    install_requires=['requests',],
)
