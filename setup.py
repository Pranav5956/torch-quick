import setuptools

with open("README.md") as readme:
    long_description = readme.read()


setuptools.setup(
    name='torch-quick',
    version='0.0.1',
    packages=setuptools.find_packages(),
    url='https://github.com/Pranav5956/torch-quick',
    license='License',
    author='Pranav Balaji',
    author_email='pranavbalaji01@gmail.com',
    description='Provides a quick, robust and customizable training pipeline, along with utilities for model prototyping, training and testing.',
    long_description=long_description
)