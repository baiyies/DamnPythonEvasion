from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='Just Test',
    ext_modules=cythonize(module_list="execute.py"),
)