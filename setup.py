from setuptools import setup

import birthday

setup(
    name='birthday',
    version=birthday.__version__,
    description='Base code for Birthday Greetings kata',
    author_email='kevin@bigkevmcd.com',
    author='Kevin McDermott',
    classifiers=[],
    license='MIT',
    tests_require=['mock'],
    packages=['birthday'],
    test_suite='tests',
)
