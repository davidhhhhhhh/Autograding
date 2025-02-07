from setuptools import setup, find_packages

setup(
    name="research_2024",  # Name of your project
    version="0.1.0",  # Initial version
    packages=find_packages(include=["StudentSimulator.ideaToText", "StudentSimulator.ideaToText.*"]),
    install_requires=[
        # List your dependencies here, e.g.:
        # 'numpy>=1.21.0',
        # 'pandas>=1.3.0',
    ],
    description="A project for Student Simulator and Idea to Text conversion.",
    author="Your Name",
    author_email="your.email@example.com",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)