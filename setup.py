from setuptools import setup, find_packages

setup(
    name="BioFetcher",
    version="0.1.1",
    description="A package to download PDB and EMDB files and process protein/map data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Chenwei Zhang",
    author_email="chwzhan@gmail.com",
    url="https://github.com/chenwei-zhang/BioFetcher.git",
    packages=find_packages(),
    install_requires=[
        "requests",
        "argparse",
    ],
    entry_points={
        'console_scripts': [
            'biofetcher=scripts.run_downloader:main',  # Command `biofetcher` runs `main()` in `run_downloader.py`
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
