import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tomplotlib",
    version="1.2.0",
    scripts=["tomplotlib/tpl.py"],
    author="Tom George",
    author_email="tom.george.20@ucl.ac.uk",
    description="A package which formats matplotlib plots and contains some other useful functions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TomGeorge1234/tomplotlib",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["matplotlib", "numpy"],
)
