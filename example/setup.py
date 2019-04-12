from setuptools import find_packages, setup

setup(
    name="mysite",
    version="0.1.0.dev0",
    packages=find_packages(),
    install_requires=[
        "Django>=2.2,<2.3",
        "whitenoise",
    ],
)
