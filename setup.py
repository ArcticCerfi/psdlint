from setuptools import setup, find_packages

setup(
    name="psdlint",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["cli"],  
    install_requires=[
        "psd-tools", 
    ],
    entry_points={
        "console_scripts": [
            "psdlint=cli:main",
        ],
    },
)