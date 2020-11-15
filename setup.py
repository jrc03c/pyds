from setuptools import setup

setup(
    name="python_data_science_helpers",
    version="0.0.1",    
    description="A collection of helper tools for doing data science stuff. Please don't judge me.",
    url="https://github.com/jrc03c/python-data-science-tools",
    author="jrc03c",
    author_email="jrc03c@pm.me",
    license="none",
    packages=["python_data_science_helpers"],
    install_requires=["numpy", "scipy", "pandas", "matplotlib"],

    classifiers=[
      "Topic :: Scientific/Engineering :: Mathematics",
    ],
)
