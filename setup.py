from setuptools import setup


setup(
    name='browserstack',
    version='0.0.1',
    author="Ashish Dubey",
    author_email="ashish.dubey91@gmail.com",
    packages=['browserstack', ],
    license='MIT',
    description="Python wrapper for BrowserStack REST API.",
    long_description=open('README.md', 'r').read(),
    install_requires=['requests', ],
)
