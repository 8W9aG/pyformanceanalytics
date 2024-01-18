"""Setup pyformanceanalytics."""
from setuptools import setup, find_packages
from pathlib import Path
import typing

readme_path = Path(__file__).absolute().parent.joinpath('README.md')
long_description = readme_path.read_text(encoding='utf-8')


def install_requires() -> typing.List[str]:
    """Find the install requires strings from requirements.txt"""
    requires = []
    with open(
        Path(__file__).absolute().parent.joinpath('requirements.txt'), "r"
    ) as requirments_txt_handle:
        requires = [
            x
            for x in requirments_txt_handle
            if not x.startswith(".") and not x.startswith("-e")
        ]
    return requires


setup(
    name='pyformanceanalytics',
    version='0.0.1',
    description='A python wrapper around the PerformanceAnalytics R code.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3',
    ],
    keywords='r performanceanalytics',
    url='https://github.com/8W9aG/scrapy-bigquery',
    author='Will Sackfield',
    author_email='will.sackfield@gmail.com',
    license='GPL2',
    install_requires=install_requires(),
    zip_safe=False,
    packages=find_packages()
)
