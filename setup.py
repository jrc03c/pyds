from setuptools import setup

setup(
    name="pyds",
    version="0.0.2",
    description="A collection of helper tools for doing data science stuff. Please don't judge me.",
    url="https://github.com/jrc03c/python-data-science-tools",
    author="jrc03c",
    author_email="jrc03c@pm.me",
    license="none",
    packages=["pyds"],
    install_requires=["numpy", "scipy", "pandas", "matplotlib"],
    classifiers=["Topic :: Scientific/Engineering :: Mathematics",],
)
