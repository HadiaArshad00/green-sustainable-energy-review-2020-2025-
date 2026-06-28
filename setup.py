"""
Setup script for the Green and Sustainable Energy Review project.
This is primarily a document repository, but structured as a Python package
for reproducibility and extensibility.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="green-sustainable-energy-review",
    version="1.0.0",
    author="Hadia Arshad",
    author_email="",  # Add your email if desired
    description="A Comprehensive Review of Green and Sustainable Energy Technologies (2020-2025)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/hadia-arshad/green-sustainable-energy-review-2020-2025",
    project_urls={
        "Bug Tracker": f"https://github.com/hadia-arshad/green-sustainable-energy-review-2020-2025/issues",
        "Zenodo": f"https://doi.org/10.5281/zenodo.20782240",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Energy",
        "License :: OSI Approved :: Creative Commons Attribution 4.0 International",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)
