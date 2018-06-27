from setuptools import setup, find_packages

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='passbook',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    zip_safe=False
)