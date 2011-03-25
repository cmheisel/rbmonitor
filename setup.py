from setuptools import setup, find_packages

setup(
    name="rbmonitor",
    version=__import__("rbmonitor").__version__,
    author="Chris Heisel",
    author_email="chris@heisel.org",
    description=("Utility to modify Review Board reviews via its API"),
    long_description=open("README.rst").read(),
    url="http://github.com/cmheisel/rbmonitor",
    zip_safe=False,
    include_package_data=True,
    packages=find_packages(),
    classifiers=[
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",

    ]
)
