import setuptools

with open("README.md", "r") as desc:
    long_description = desc.read()

setuptools.setup(
    name="csv_intersection",
    version="1.0.0",
    author="Swapnal Shahil",
    author_email="swapnalsahil@gmail.com",
    description="CSV intersection",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/swapnalshahil/csv_intersection",
    keywords= ["csv", "intersection", "csv_intersection", "tsv", "tsv_intersection", "common data" ,"data visualization"],
    packages=setuptools.find_packages(),
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['python-csv'],
    python_requires='>=3.6',
    project_urls={
        'Bug Reports': 'https://github.com/swapnalshahil/csv_intersection/issues',
        'Source': 'https://github.com/swapnalshahil/csv_intersection',
    }
)
