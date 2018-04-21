from setuptools import setup, find_packages

setup(
    name='text_adventure',
    version='0.0.1',
    author='Inkwell',
    author_email=('StockerDE@cardiff.ac.uk'),
    packages=find_packages('src'),
    package_dir={"": "src"},
    description='A library enabling the creation of a simple text based computer game.',
)