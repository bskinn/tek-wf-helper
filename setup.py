import re
from pathlib import Path

from setuptools import find_packages, setup


exec(Path("src", "tek_wf", "version.py").read_text(encoding="utf-8"))


NAME = "tek_wf"


setup(
    name=NAME,
    version=__version__,
    description="Helpers for traces from Tektronix TBS-series and similar oscilloscopes",
    # long_description=readme(),
    # long_description_content_type="text/x-rst",
    url="https://github.com/bskinn/tek-wf-helper",
    # project_urls={
    # "Changelog": "https://github.com/bskinn/tek-wf-helper/blob/main/CHANGELOG.md",
    #        "Docs": "https://tek-wf-helper.readthedocs.io/en/stable/",
    # "Thank": "https://twitter.com/btskinn",
    # "Donate": "https://github.com/sponsors/bskinn",
    # },
    license="MIT License",
    author="Brian Skinn",
    author_email="bskinn@alum.mit.edu",
    packages=find_packages("src"),
    package_dir={"": "src"},
    provides=["ttrans_fft"],
    python_requires=">=3.8",
    requires=["attrs (>=19.2)", "matplotlib", "numpy", "scipy"],
    install_requires=["attrs>=19.2", "matplotlib", "numpy", "scipy"],
    classifiers=[
        "License :: OSI Approved",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Intended Audience :: Science/Research",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Utilities",
        "Development Status :: 3 - Alpha",
    ],
)
