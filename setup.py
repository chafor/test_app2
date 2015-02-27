from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='test_app2',
    version=version,
    description='test',
    author='AptitudeTech',
    author_email='cfortin@brunet.cc',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
