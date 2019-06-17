import setuptools
with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='example-pkg-roughael',
    version='0.0.2',
    author='Raphael Holzer',
    author_email="raphael.holzer@me.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rasql/cv-tutorial",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)