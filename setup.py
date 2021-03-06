#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name="wikitools",
    version="0.1",
    packages=find_packages(),
    namespace_packages=['wikitools'],
    install_requires=[
        'suds'
    ],
    entry_points={
        'console_scripts': [
            'clone_wiki=wikitools.clone_page:main',
            'clone_wiki_news=wikitools.clone_news:main',
            'clone_wiki_news_hid=wikitools.clone_news_hid:main',
            'delete_wiki_page=wikitools.delete_page:main',
        ]
    }
)
