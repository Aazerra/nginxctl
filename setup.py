from setuptools import setup, find_packages
from nginxctl import version

setup(
    name="nginxctl",
    version=version,
    packages=find_packages(exclude=[]),
    install_requires=[
        "click"
    ],
    entry_points={
        'console_scripts': [
            "nginxctl=nginxctl.main:cli"
        ]
    }
)
