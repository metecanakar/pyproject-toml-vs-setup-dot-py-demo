from setuptools import setup, find_packages

# read module requirements from requirements.txt instead of repeating the dependencies here:
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    install_requires = [r for r in requirements if not r == ""]

setup(
    name="example_project",
    version="0.1.0",
    description="An example Python project",
    author="Your Name",
    install_requires=install_requires,
    package_dir={"": "src"},
    packages=find_packages("src")   # Automatically discovers Python packages
)
