from setuptools import setup, find_packages
import cyanobot

setup(
    name='cyanobot',
    version=cyanobot.__version__,
    author='cyanobird',
    author_email='3358851903@qq.com',
    description='A simple bot framework',
    long_description_content_type='text/markdown',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    packages=find_packages(),
    platforms=["all"],
    install_requires=[
    	'pyfiglet'
    ]
)
