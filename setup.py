from setuptools import setup, find_packages
import re
import os.path


def read_version():
    with open("quamash/__init__.py", "r", encoding="utf-8") as file:
        return re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)


def read_authors_and_emails():
    with open("quamash/__init__.py", "r", encoding="utf-8") as file:
        author_str = re.search(r'^__author__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)
        groups = re.findall(r'(.+?) <(.+?)>(?:,\s*)?', author_str)
        authors = [x[0].strip() for x in groups]
        emails = [x[1].strip() for x in groups]
    return authors, emails


def read_url():
    with open("quamash/__init__.py", "r", encoding="utf-8") as file:
        return re.search(r'^__url__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)


def read_license():
    with open("quamash/__init__.py", "r", encoding="utf-8") as file:
        return re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', file.read(), re.MULTILINE).group(1)


version = read_version()
authors, emails = read_authors_and_emails()
url = read_url()
license_name = read_license()


desc_path = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(desc_path, encoding='utf8') as desc_file:
	long_description = desc_file.read()

setup(
	name='Quamash',
	version=version,
	url=url,
	author=', '.join(authors),
	author_email=', '.join(emails),
	packages=find_packages(),
	install_requires=['PyQt5>=5'],
	python_requires='>=3.5, <3.11',
	license=license_name,
	description="Optimized fork of Quamash for seamless PEP 3156 Event-Loop integration with PyQt5.",
	long_description=long_description,
	keywords=['Qt', 'asyncio', 'PyQt5'],
	classifiers=[
		'Development Status :: 3 - Alpha',
		'License :: OSI Approved :: BSD License',
		'Intended Audience :: Developers',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: MacOS :: MacOS X',
		'Operating System :: POSIX',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3 :: Only',
		'Environment :: X11 Applications :: Qt',
	],
	extras_require={
		'test': ['pytest'],
	},
)
