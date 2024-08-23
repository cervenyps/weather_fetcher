from setuptools import setup, find_packages

setup(
    name="weather_fetcher",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A package to fetch temperatures in specific cities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/weather_fetcher",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
