from setuptools import setup

with open("README.md", 'r') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='scanner',
    version='1.0',
    description='Scanning module for OCR',
    license="MIT",
    long_description=LONG_DESCRIPTION,
    author='Adel Abdallah, Mykola Somov',
    author_email='',
    url="https://github.com/adelabdallah/scanner",
    packages=['scanner'],
    install_requires=[
        'Pillow',
        'pylint',
        'pytesseract',
        'opencv-python',
    ]  # UPDATE
)
