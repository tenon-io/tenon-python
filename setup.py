import tenon
from setuptools import setup, find_packages

requires=["requests"]

setup(
    name='tenon-python',
    version=tenon.__version__,
    description="Python wrapper for the Tenon.io API",
    license='MIT',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    keywords='tenon, tenon.io, accessibility, a11y, testing, api',
    author='Justin Stockton',
    author_email='poorgeek@gmail.com',
    url='https://github.com/poorgeek/tenon-python',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=True,
    install_requires=requires,
)
