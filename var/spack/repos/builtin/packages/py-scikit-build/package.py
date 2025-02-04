# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitBuild(PythonPackage):
    """scikit-build is an improved build system generator for CPython
    C/C++/Fortran/Cython extensions. It provides better support for
    additional compilers, build systems, cross compilation, and
    locating dependencies and their associated build requirements.

    The scikit-build package is fundamentally just glue between
    the setuptools Python module and CMake."""

    homepage = "https://scikit-build.readthedocs.io/en/latest/"
    pypi = "scikit-build/scikit-build-0.15.0.tar.gz"

    maintainers = ["coreyjadams"]

    version("0.15.0", sha256="e723cd0f3489a042370b9ea988bbb9cfd7725e8b25b20ca1c7981821fcf65fb9")
    version("0.12.0", sha256="f851382c469bcd9a8c98b1878bcfdd13b68556279d2fd9a329be41956ae5a7fe")
    version("0.11.1", sha256="da40dfd69b2456fad1349a894b90180b43712152b8a85d2a00f4ae2ce8ac9a5c")
    version("0.10.0", sha256="7342017cc82dd6178e3b19377389b8a8d1f8b429d9cdb315cfb1094e34a0f526")

    depends_on("py-setuptools@28.0.0:", type=("build", "run"))
    depends_on("py-setuptools@42.0.0:", when="@0.15.0:", type=("build", "run"))
    depends_on("py-setuptools-scm+toml", when="@0.15.0:", type="build")
    depends_on("py-packaging", type=("build", "run"))
    depends_on("py-wheel@0.29.0:", type=("build", "run"))
    depends_on("py-distro", when="@0.11:", type=("build", "run"))
