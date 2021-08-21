from glob import glob
from os.path import splitext
from os.path import basename
from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="mondrian-python3",
    version="0.1.0",
    license="",
    description="",
    author="MaskTap, Inc.",
    url="",
    packages=["mondrian-python3", "mondrian-python3.utils"],
    # packages=find_packages("mondrian-python3"),
    # package_dir={"": "mondrian-python3"},
    #     py_modules=[splitext(basename(path))[0] for path in glob(
    #         "mondrian-python3/*.py") + glob("mondrian-python3/utils/*.py")],
    #     include_package_data=True,
    zip_safe=False,
    # install_requires=_requires_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
