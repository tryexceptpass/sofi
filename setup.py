from setuptools import setup, find_packages
from os import path


# Get the long description from the README file
with open(path.join('.', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    author="tryexceptpass",
    author_email="cmedina@tryexceptpass.org",

    name="sofi",
    version="0.3.8",

    description="Desktop and Web GUI framework based on WebSockets",
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/tryexceptpass/sofi",

    packages=find_packages(),
    package_data={
        'sofi': ['app/main.html', 'app/_sofi.js'],
        'test': ['test.png']
    },

    install_requires=['websockets'],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'hypothesis'],

    license="MIT",
    classifiers=['License :: OSI Approved :: MIT License',
                 'Framework :: AsyncIO',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Multimedia',
                 'Topic :: Multimedia :: Graphics',
                 'Topic :: Software Development :: User Interfaces',

                 'Programming Language :: Python :: 3 :: Only',
                 'Programming Language :: Python :: 3.6',

                 'Development Status :: 4 - Beta',
                 ],
    keywords='websockets javascript bootstrap gui unity3d desktop html',

    project_urls={
        'Gitter Chat': 'https://gitter.im/try-except-pass/sofi',
        'Say Thanks!': 'https://saythanks.io/to/tryexceptpass',
        'Source': 'https://github.com/tryexceptpass/sofi',
        'Documentation': 'http://sofi-gui-framework.readthedocs.io/en/latest/',
    },
)
