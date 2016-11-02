from setuptools import setup, find_packages


with open("requirements.txt") as reqs:
    install_requires = reqs.readlines()

setup(
    name="dojo-toolkit",
    version="0.4.3",
    url="https://github.com/grupy-sanca/dojo-toolkit",

    author="Grupy-Sanca",

    description="A Toolkit for Python Coding Dojos",
    long_description=open('README.rst').read(),

    packages=find_packages(),

    install_requires=install_requires,

    include_package_data=True,

    entry_points={
        'console_scripts': [
            'dojo=dojo_toolkit.main:main',
        ]
    },

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],
)
