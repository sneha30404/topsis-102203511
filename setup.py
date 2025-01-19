from setuptools import setup, find_packages

setup(
    name='topsis-102203511',
    version='1.0.0',
    description='Python implementation of TOPSIS for multi-criteria decision-making',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Sneha',
    author_email='sneha30404@gmail.com',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.5',
        'pandas>=1.1.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
