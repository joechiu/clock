# clock widget

A fun clock widget compilable for Linux, OS2 and Windows. Developed by Python3.62 and PyQT5. 

## Synopsis

Clock Widget is an analog clock controlled by mouse to display the current system time. It's designed to be movable and extensible anytime and anywhere all around the desktop screen.

## Code

The widget written by Python 3.6.2 in Ubuntu 16.04 and Windows 7. The code are lite and concised, easy to update and maintain.

## Prerequisition Installation

The PyQT5 bundled with Python 3.x so you need to check the python version before install the QT5 for python. 

Please be advised you should need to check your system type to download/install the 32/64 bit Python.

To check the python version, open the terminal or cmd and type pythone or python --version to see the python before compile the clock widget.

$ python --version
Python 3.6.2

C:\>python (in windows)
Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

## Installation

In order to run these tools you would search the following systems/utilities/tools existing in your system or install them beforehand if not.

* Linux Ubuntu 16.04 / OS2 / Windows 7
* Python 3.6.2
* PyQT5
* pip
* cx_Freeze
* Python IDE, eg. Wings, PyCharm, Vim... (optional)
* Inno Setup (optional) 

## Test and Run (Windows)
1. copy the codes to your local directory 
2. change diretory to your local directory
3. under the directory type: python setup.py build
4. when the compile command fired, cx_Freeze will follow the schema in setup.py to build an executable file inside build/exe.win-amd64-3.6
5. run the compiled file clock.exe (in this example) to see the clock widget
6. this package is available to be packed as a installer by Inno setup

## Snapshots

* adb-run<br>
![adb-run](https://raw.githubusercontent.com/joechiu/adb-tools/master/snapshots/adb-run-snapshot.png "adb-run snapshot")

* adb-install<br>
![adb-install](https://raw.githubusercontent.com/joechiu/adb-tools/master/snapshots/adb-install-snapshot.png "adb-install snapshot")

* adb-uninstall<br>
![adb-uninstall](https://raw.githubusercontent.com/joechiu/adb-tools/master/snapshots/adb-uninstall-snapshot.png "adb-uninstall snapshot")

## Contributors

You are free to update these tools to make them more helpful.

## License

A short snippet describing the license (MIT, Apache, etc.)
