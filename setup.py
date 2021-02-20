from setuptools import find_packages, setup

with open("requirements.txt") as reqs:
    install_requires = reqs.readlines()

setup(
    name="dojo-toolkit",
    version="0.5.0",
    url="https://github.com/grupy-sanca/dojo-toolkit",
    author="Grupy-Sanca",
    description="A Toolkit for Python Coding Dojos",
    long_description=open('README.rst').read(),
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={"gtk": ["pgi==0.0.11.1"]},
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'dojo=dojo_toolkit.__main__:main',
        ]
    },
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python :: 3',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
)
