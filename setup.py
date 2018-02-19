from setuptools import setup, find_packages

setup(
    author="tryexceptpass",
    author_email="cmedina@tryexceptpass.org",

    name="sofi",
    version="0.2.0",

    description="WebSocket server and protocol for GUI layers based on WebSockets",
    long_description="Sofi is a Python 3 WebSocket server and protocol that works with clients to generate GUI applications. For websites, it generates the necessary HTML and JavaScript needed to produce a single-page application with event listeners. In conjunction with sofi-unity3d, it can drive the Unity3D game engine.",

    url="https://github.com/tryexceptpass/sofi",

    packages=find_packages(),
    package_data={
        'sofi': ['app/main.html', 'app/sofi.js'],
        'test': ['test.png']
    },

    install_requires=['autobahn'],
    python_requires='>=3.6',
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'hypothesis'],

    license="MIT",
    classifiers=['License :: OSI Approved :: MIT License',
                 # ADD MORE CLASSIFIERS!
                 'Development Status :: 4 - Beta',
                 ],
    keywords=['websockets', 'javascript', 'bootstrap', 'gui', 'unity3d']
)
