# Ensures that we can install a package with pip install package

from setuptools import setup

setup(
    name='ppg',
    version='0.2',
    description='Testing installation of Package',
    # py_modules=["ppack"],
    # package_dir={'': '.'},
    url='#',
    author='Mike Huls',
    author_email='mike_huls@hotmail.com',
    license='MIT',
    packages=['ppg'], # same as name
    zip_safe=False,
    install_requires=['wheel', 'requests'],  # external packages as dependencies
)
