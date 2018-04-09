# Sofi
Sofi is a **Python 3** package designed to alleviate development of cross-platform GUIs by leveraging existing technologies for rendering interfaces while keeping all of the logic in Python.

It boils down to designing a communications protocol to implement across different interface mechanisms, and using Python to direct those systems on what to display to the user, while relaying their events and inputs back to Python. The communication layer uses JSON over WebSockets, two technologies that are easy to integrate into almost any system, especially the web. Python is the glue logic for rendering engines, not the rendering engine itself.

The main package comes with a built-in implementation for creating single-page web applications. The items inside `sofi.ui` wrap [Bootstrap](https://getbootstrap.com/) widgets into Python objects which use the `__str__` method to generate the HTML and JavaScript required to have them render in the browser.

You can use these widgets as-is, which can get a little verbose, or you can build on top of each other into higher levels of abstraction to produce composite elements like responsive tables. Over time, we expect to add more and more of these widgets to the base library, making the implementation as easy as an instantiation of one of these objects.

Along the same lines, work is ongoing on a package that uses the base Sofi protocols to integrate with the [Unity3d](https://www.unity3d.com) game engine. The package is called [`sofi-unity3d`](https://github.com/tryexceptpass/sofi-unity3d) and has the end goal of doing for game engines what Bootstrap did for the web. Start with a set of pre-existing game objects and build complex user interfaces with them.

We've also been successful at creating fully contained desktop applications through the use of `PyInstaller` and `Chromium`. Delivering OS-specific executables that run as applications instead of web pages or games. For info on how we've done this, please have a look at [How to turn a Web app into a Desktop App](http://tryexceptpass.org/article/how-to-turn-a-web-app-into-a-desktop-app/).
