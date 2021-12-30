# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="opensea",
    version="0.2.0",
    description="wrapper library for opensea api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://opensea.readthedocs.io/", # TASKETE KUDASAI :(
    author="Ankush Singh",
    author_email="ankush4singh@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=["requests"]
)
