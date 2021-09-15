from os import name
from setuptools import setup, find_packages


setup(
    name="inputhandler",
    version="1.0",
    author="DaHunterTime",
    description="A (basic) cross-platform python input handler",
    url="https://github.com/DaHunterTime/InputHandler",
    project_urls={
        "Bug Tracker": "https://github.com/DaHunterTime/InputHandler/issues",
    },
    packages=find_packages(),
    python_requires=">=3.7",
)
