from setuptools import setup, find_packages

setup(
    name="footballmvp",  # lowercase recommended
    version="0.1.0",
    package_dir={"": "src"},             # tell setuptools to look in src/
    packages=find_packages(where="src"),  # find packages only under src/
    install_requires=[
        "requests>=2.32",
        "pandas>=2.2",
        "numpy>=2.1",
        "beautifulsoup4>=4.12",
        "selenium>=4.32",
        "pyspark>=3.5",
    ],
    author="Drue Staples",
    author_email="druestaples@gmail.com",
    description="Analytical tool to determine top performing football players (MVP) across leagues and tournaments.",
    url="https://github.com/DrueStaples08/FootballMVP",
    classifiers=[
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
