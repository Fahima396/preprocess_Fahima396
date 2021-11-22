import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
    name = 'preprocess_Fahima396', #this should be unique
    version = '0.0.3',
    author = 'Fahima',
    author_email = 'fahimaansari396@gmail.com',
    description = 'This is preprocessing package',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages = setuptools.find_packages(),
    classifiers = [
    'Programming Language :: Python :: 3',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent'

    ],
    python_requires = '>=3.7'
	)	