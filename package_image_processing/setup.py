from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_image_processing_DiO",
    version="0.0.2",
    author=" jcbneves",
    author_email="jcbneves@gmail.com",
    description="Test version Image processing package using skimage. This project belongs to Karina Tiemi Kato.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcbneves/Lab-project-DIO-cria-o-de-pacotes-de-processamento-de-imagens-em-Pytho.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)
