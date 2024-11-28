from setuptools import setup, find_packages

setup(
    name="Custom Paddle", 
    version="0.1.0", 
    author="Long Nguyen",  
    author_email="longnt.vie@gmail.com", 
    description="Paddlepaddle version 2.5.2 has been customed",  
    url="https://github.com/optivisionlab/docbusiness",
    packages=find_packages(),  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',  # Phiên bản Python yêu cầu
)
