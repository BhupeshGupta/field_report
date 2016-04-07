from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='field_report',
    version=version,
    description='Management Of Mobile Repoting Clients',
    author='Arun Logistics',
    author_email='info@arungas.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
