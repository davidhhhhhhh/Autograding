from setuptools import setup, find_packages

setup(
    name="Auto-grading",  # Name of your project
    version="0.1.0",  # Initial version
    packages=find_packages(include=["StudentSimulator.ideaToText", "StudentSimulator.ideaToText.*"]),
    description="A project for Student Simulator and Idea to Text conversion.",
    author="David Dai",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11.9",
)