from setuptools import setup, find_packages
import quamash
import re
import os.path

groups = re.findall(r'(.+?) <(.+?)>(?:,\s*)?', quamash.__author__)
authors = [x[0].strip() for x in groups]
emails = [x[1].strip() for x in groups]

desc_path = os.path.join(os.path.dirname(__file__), 'README.rst')
with open(desc_path, encoding='utf8') as desc_file:
	long_description = desc_file.read()

setup(
	name='Quamash PyQt5',
	version=quamash.__version__,
	url=quamash.__url__,
	author=', '.join(authors),
	author_email=', '.join(emails),
	packages=find_packages(),
	install_requires=['PyQt5>=5'],
	python_requires='>=3.5, <=3.10',
	license=quamash.__license__,
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
