from setuptools import setup, find_packages


setup(
    name='wp-pre-commit-hooks',
    description='Pre-commit hooks by Will Price',
    url='http://github.com/willprice/pre-commit-hooks',
    version='0.0.1',

    author='Will Price',
    author_email='will.price94@gmail.com',

    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    packages=find_packages(exclude=('tests*', 'testing*')),
    install_requires=[
        'black'
    ],
    entry_points={
        'console_scripts': [
            'black-formatter = black:main'
        ]
    }
)
