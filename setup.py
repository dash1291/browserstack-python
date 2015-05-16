from setuptools import setup


setup(
    name='browserstack',
    version='0.0.1',
    author="Ashish Dubey",
    author_email="ashish.dubey91@gmail.com",
    packages=['browserstack', ],
    license='MIT',
    long_description='Python wrapper for BrowserStack REST API.',
    install_requires=['requests', ],
)
