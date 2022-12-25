import setuptools
from pathlib import Path

setuptools.setup(
    name = 'gym_mazegame',
    version = '0.0.1',
    author="Group14",
    author_email="ccchen@link.cuhk.edu.hk",
    description = 'This is our aist1110 gym game project.',
    
    url ="https://github.com/WYXG233/AIST1110project",
    
    packages=setuptools.find_namespace_packages(
                     include=["gym_maze", "gym_maze.*"], ),
    install_requires = ["gym", "pygame", "numpy", "colorama", "pandas", "tqdm", "matplotlib"],
    include_package_data=True
)
