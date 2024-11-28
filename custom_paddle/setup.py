from setuptools import setup, find_packages

setup(
    name="custom paddle",
    version="0.1.0",  
    author="Nguyen Thanh Long",
    author_email="longnt.vie@gmail.com",  
    description="custom paddlepaddle v2.5.2",  
    long_description=open("README.md").read(),  
    long_description_content_type="text/markdown",  
    url="https://github.com/optivisionlab/docbusiness", 
    packages=find_packages(), 
    install_requires=[
        "numpy",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7', 
)
