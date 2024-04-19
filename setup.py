import os
from setuptools import setup

README = """
See the README on `GitHub
<https://github.com/uw-asa/uw-restclients-mazevo>`_.
"""

version_path = "uw_mazevo/VERSION"
VERSION = open(os.path.join(os.path.dirname(__file__), version_path)).read()
VERSION = VERSION.replace("\n", "")

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="UW-RestClients-Mazevo",
    version=VERSION,
    packages=["uw_mazevo"],
    author="UW Academic & Student Affairs",
    author_email="asahelp@uw.edu",
    include_package_data=True,
    install_requires=[
        "UW-RestClients-Core",
    ],
    license="Apache License, Version 2.0",
    description=("A library for connecting to the Mazevo API"),
    long_description=README,
    url="https://github.com/uw-asa/uw-restclients-mazevo",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
)
