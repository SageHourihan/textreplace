from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='textreplace',
      version='1.0',
      description='Command line tool',
      long_description=readme(),
      url='https://github.com/SageHourihan/textreplace.git',
      author='Sage Hourihan',
      author_email='samiho97@gmail.com',
      license='MIT',
      packages=['textreplace'],
      entry_points = {
        'console_scripts': ['text-replace=textreplace.command_line:main'],
    }
)