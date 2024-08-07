import setuptools

# This represents the text which will be displayed in the PyPI page if the package is uploaded
with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()


REPO_NAME = 'roman-numerals'
VERSION = '0.0.0'
AUTHOR_USER_NAME = 'BogdanKandra'
AUTHOR_EMAIL = 'bogdan.kandra@gmail.com'
SRC_DIR = 'scripts'


setuptools.setup(
    name=REPO_NAME,
    version=VERSION,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description='Converts Roman numerals to integers and vice versa',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    package_dir={'': SRC_DIR},  # This is the root directory of the package
    packages=setuptools.find_packages(where=SRC_DIR),
)
