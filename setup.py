import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='dbug12',  
     version='0.1',
     author="Fabian Melendez",
     author_email="fabian.melendez.a@gmail.com",
     description="Python API for D-Bug12 compatible boards",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/mlndz28/d-bug12",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 2",
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: POSIX ::Linux",
     ],
     entry_points = {
        'console_scripts': ['dbug12=dbug12.cli:main'],
    }
 )