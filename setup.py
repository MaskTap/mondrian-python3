from glob import glob
from os.path import splitext
from os.path import basename
from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="Mondrian",
    version="0.1.0",
    license="MIT",
    description="",
    author="MaskTap, Inc.",
    url="",
    packages=["Mondrian", "Mondrian.utils"],
    zip_safe=False,
    # install_requires=_requires_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
