# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()


setup(name='HCPyTools',
      version='0.1.7',
      maintainer='Levi Thatcher',
      maintainer_email='levi.thatcher@healthcatalyst.com',
      license='proprietary',
      description='Tools for healthcare machine learning',
      long_description=readme(),
      url='http://healthcare.ai/',
      packages=[
          'hcpytools',
      ],
      install_requires=[
          'numpy>=1.11.2+mkl',
          'scipy>=0.18.1',
          'scikit-learn>=0.18',
          'pandas>=0.19.0',
          'matplotlib>=2.0.0b4',
          'pyodbc>=3.0.10',
      ],
      tests_require=[
          'nose',
      ],
      test_suite='nose.collector',
      zip_safe=False,
      classifiers=[
          "Development Status :: 1 - Planning",
          "Intended Audience :: Healthcare Industry",
          "Intended Audience :: Developers",
          "License :: Other/Proprietary License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.2",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Software Development :: Libraries :: Python Modules",
      ],
      include_package_data=True)
