import setuptools
from setuptools.extension import Extension
from Cython.Build import cythonize
import numpy
import matplotlib.pyplot

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='bioinfo_tools',  
    version='0.1',
    author="Demetrio Magatti",
    description="Package containing simple functions used for a first approach to the bioinformatics world",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
    ]
)
