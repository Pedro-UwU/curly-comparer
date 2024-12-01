from setuptools import setup, find_packages
setup(
    name='curly_comparer',
    version='0.1.0',
    author='Pedro Lopez',
    author_email='pdihax@gmail.com',
    description='A little package with string comparison tools',
    packages=find_packages(),
    license='Apache License 2.0',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache Software License'
    ],
    install_requires=['numpy>=2.1'],
    python_requires='>=3.10'
)
