
from setuptools import setup
import io
import os

from tarot.ver import get_git_version

here = os.path.abspath(os.path.dirname(__file__))


def read(*filenames, **kwargs):
   encoding = kwargs.get('encoding', 'utf-8')
   sep = kwargs.get('sep', '\n')
   buf = []
   for filename in filenames:
       with io.open(filename, encoding=encoding) as f:
           buf.append(f.read())
   return sep.join(buf)


long_description = read('README.md', 'contributing.md')

setup(
   name='tarot',
   # version=get_git_version(),
   version="0.1.0",
   url='http://github.com/arfc/tarot/',
   license='BSD 3-Clause License',
   author='Samuel G. Dotson',
   tests_require=['pytest'],
   author_email='samgdotson@gmail.com',
   description='Transient Reactor Operator',
   long_description=long_description,
   packages=['tarot',
             ],
   include_package_data=True,
   platforms='any',
   # test_suite='cairo.tests',
   classifiers=[
       'Development Status :: 1 - Planning',
       'Intended Audience :: Education',
       'Intended Audience :: Science/Research',
       'Intended Audience :: Developers',
       'License :: OSI Approved :: BSD 3-Clause',
       'Natural Language :: English',
       'Operating System :: OS Independent',
       'Programming Language :: Python',
       'Topic :: Scientific/Engineering',
       'Topic :: Scientific/Engineering :: Physics',
       'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
