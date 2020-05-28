from re import search
from codecs import open as c_open
from os import path

from setuptools import setup

name = "kedro-doorstop"
here = path.abspath(path.dirname(__file__))

# get package version
package_name = name.replace("-", "_")
with c_open(path.join(here, package_name, "__init__.py"), encoding="utf-8") as f:
    version = search(r'__version__ = ["\']([^"\']+)', f.read()).group(1)

# get the dependencies and installs
with c_open("requirements.txt", "r", encoding="utf-8") as f:
    requires = [x.strip() for x in f if x.strip()]

# get test dependencies and installs
with c_open("test_requirements.txt", "r", encoding="utf-8") as f:
    test_requires = [x.strip() for x in f if x.strip() and not x.startswith("-r")]

# Get the long description from the README file
with c_open(path.join(here, "README.md"), encoding="utf-8") as f:
    readme = f.read()

setup(
    name=name,
    version=version,
    description="Kedro-Doorstop makes it easy to manage software requirements in Kedro projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/fkromer/kedro-doorstop",
    author="Florian Kromer",
    author_email="florian.kromer@mailbox.org",
    python_requires=">=3.6, <3.9",
    install_requires=requires,
    tests_require=test_requires,
    license="Apache Software License (Apache 2.0)",
    packages=["kedro_doorstop"],
    package_data={"kedro_doorstop": []},
    zip_safe=False,
    entry_points={
        "kedro.project_commands": ["doostop = kedro_doorstop.plugin:commands"]
    },
)