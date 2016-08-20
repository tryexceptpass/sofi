from setuptools import setup, find_packages

setup(
    author = "tryexceptpass",
    author_email = "tryexceptpass@users.noreply.github.com",

    name = "sofi",
    version = "0.1.1",

    description = "GUI layer for Python based on WebSockets Bootstrap and D3.js",
    long_description="Sofi is a Python 3 system that will generate the necessary HTML and JavaScript code typically needed to produce a single-page application and serve it up through WebSockets.\n\nThe webpage functions as a dumb user interface layer on top of your python code by exposing a simple command and event system that allows for communications back and forth with the python logic. The UI itself is generated using Bootstrap components, and enabled by D3.js for processing events and DOM changes.",

    url = "https://github.com/tryexceptpass/sofi",

    packages = find_packages(),
    package_data = {
            'sofi': ['app/main.html', 'app/sofi.js']
    },

    install_requires = [ 'autobahn' ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'hypothesis'],

    license = "MIT",
    classifiers = [ 'License :: OSI Approved :: MIT License',
                   # ADD MORE CLASSIFIERS!
                    'Development Status :: 4 - Beta',
                  ],
    keywords = [ 'websockets', 'javascript', 'bootstrap', 'gui' ]

)
