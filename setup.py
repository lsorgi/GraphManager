from setuptools import setup, find_packages

REQUIRED = [
    "numpy==1.20.1",
    "matplotlib>=3.3.4<3.4",
    "pytest==6.2.2",
    "h5py"
]

setup(name='graph_manager',
      version='0.1.0',
      author='Lorenzo Sorgi',
      author_email='lorenzosorgi77@gmail.com',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=False,
      zip_safe=False,
      install_requires=REQUIRED,
      python_requires='>=3.7'
)
