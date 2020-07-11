
# 1. Run this to get all the required depenceies. Ironically you will have to install the setuptools dependecy for this to work by running: "pip install --upgrade setuptools" first.

# 2. once setuptools is installed run the command "python setup.py sdist" to get all the dependencies

# install dependecies automatically in a new environment
from setuptools import setup, find_packages
setup(
	name="crypto_speed_test",
	version="1.0",
	packages=find_packages()
)