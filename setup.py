from setuptools import setup, find_packages

setup(
    name="custompaddle-gpu",  
    version="0.1.0", 
    author="Long Nguyen",  
    author_email="longnt.vie@gmail.com",  
    description="A custom version of paddlepaddle-gpu v2.5.2",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown", 
    url="https://github.com/optivisionlab/docbusiness",  
    packages=find_packages(),
    install_requires=[
        
    ],  
    python_requires=">=3.6",
)
