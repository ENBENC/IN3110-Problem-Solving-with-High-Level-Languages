from distutils.core import setup
import setuptools

setup(
   name='instapy',
   version='0.1.0',
   packages=setuptools.find_packages(),
   description='Sepia and grey filter',
   scripts = ['bin/script_instapy.py']
)
