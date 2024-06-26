from setuptools import setup, find_packages
from codecs import open
from os import path


__author__ = "Vincenzo (Enzo) Nicosia"
__license__ = "GPL"
__email__ = "katolaz@yahoo.it"


here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

with open(path.join(here, "requirements.txt"), encoding="utf-8") as f:
    requirements = f.read().splitlines()


setup(
    name="multired",
    version="0.2",
    license="GPL",
    description="Structural reduction of multilayer networks",
    url="https://github.com/KatolaZ/multired",
    author="Vincenzo (Enzo) Nicosia",
    author_email="katolaz@yahoo.it",
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 4 - Beta",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: GPL",
        "Operating System :: POSIX :: Other",
        "Operating System :: MacOS",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    keywords=" ",
    install_requires=requirements,
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require={},
    packages=find_packages(
        exclude=["*.test", "*.test.*", "test.*", "test", "multired.test", "multired.test.*"]
    ),
)
