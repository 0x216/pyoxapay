from setuptools import setup, find_packages

setup(
    name='pyoxapay',
    version='0.1.0',
    author='Maksim L',
    author_email='0x216@pm.me',
    packages=find_packages(),
    description='An asynchronous Python client for the OxaPay API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/0x216/pyoxapay',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        'aiohttp',
    ],
)
