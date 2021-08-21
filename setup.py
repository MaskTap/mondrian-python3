from glob import glob
from os.path import splitext
from os.path import basename
from setuptools import setup
from setuptools import find_packages


def _requires_from_file(filename):
    return open(filename).read().splitlines()


setup(
    name="wrapmondrian",
    version="0.1.0",
    license="",
    description="",
    author="MaskTap, Inc.",
    url="",
    packages=['wrapmondrian', 'wrapmondrian.utils'],
    # packages=find_packages("wrapmondrian"),
    # package_dir={"": "wrapmondrian"},
    
#     py_modules=[splitext(basename(path))[0] for path in glob(
#         "wrapmondrian/*.py") + glob("wrapmondrian/utils/*.py")],
#     include_package_data=True,
    zip_safe=False,
    # install_requires=_requires_from_file("requirements.txt"),
    setup_requires=["pytest-runner"],
    tests_require=["pytest", "pytest-cov"],
)
