from distutils.core import setup
from setuptools import find_packages

setup(name='OptiMaint',
      version='1.0',
      description='Optimisation for maintenance Bombardier',
      author='!AFK Hacktrain',
      packages=find_packages(),
      namespace_packages = ['optimaint']
     )