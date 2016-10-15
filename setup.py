import os
from setuptools import setup, find_packages
import versioneer

# vagrant doesn't appreciate hard-linking
if os.environ.get('USER') == 'vagrant' or os.path.isdir('/vagrant'):
    del os.link

package_data = []
import sys
if sys.platform == 'nt':
    package_data.append([os.path.join('tools', 'magic1.dll')])

setup(
    name="csirtg_smrt",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    package_data=package_data,
    description="s.m.r.t",
    long_description="",
    url="https://github.com/csirtgadgets/csirtg-smrt-py",
    license='LGPL3',
    classifiers=[
               "Topic :: System :: Networking",
               "Environment :: Other Environment",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
               "Programming Language :: Python",
               ],
    keywords=['security'],
    author="Wes Young",
    author_email="wes@csirtgadgets.org",
    packages=find_packages(),
    install_requires=[
        'pytest-cov>=2.2.1',
        'ipaddress>=1.0.16',
        'feedparser>=5.2.1',
        'nltk==3.2',
        'requests>=2.6.0',
        'pytest>=2.8.0',
        'arrow>=0.6.0',
        'python-magic>=0.4.6',
        'pyaml>=15.8.2',
        'chardet>=2.3.0',
        'SQLAlchemy==1.0.14',
        'elasticsearch<3.0.0,>=2.0.0',
        'elasticsearch_dsl<3.0.0,>=2.0.0',
        # bug affecting bs4, py2 and cgmail
        'html5lib==1.0b8'

    ],
    scripts=[],
    entry_points={
        'console_scripts': [
            'csirtg-smrt=csirtg_smrt.smrt:main',
        ]
    },
)
