from setuptools import setup, find_packages

setup(
    name="FootballMVP",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",   # Add your dependencies here
        "pandas"
    ],
    author="Drue Staples",
    description="Short description of your tool",
    url="https://github.com/your-username/your-repo",
    classifiers=[
        "Programming Language :: Python :: 3.12.4",
    ],
)
