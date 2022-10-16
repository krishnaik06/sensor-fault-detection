import re
from setuptools import find_packages,setup
from typing import List
def get_requirements()-> List[str]:
    """
    This function will return the list of requirements
    Returns:
        List[str]: return all the libraries needs to be installed
    """
    requirement_list:List[str]=[]
    return requirement_list


setup(
    name="sensor",
    version="0.0.1",
    author="Krish",
    author_email="krishnaik06@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)