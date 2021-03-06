# clock widget

A simple fun clock widget improved from an example code in the PyQT5 package and portable for Linux, iOS and Windows. 

Developed by Python3.62 and PyQT5. 

## Synopsis

Clock Widget is an analog clock controlled by mouse to display the current time. It's designed to be movable and expandable anytime and anywhere all around the desktop screen.

## Code

The widget written by Python 3.6.2 in Ubuntu 16.04 and Windows 7. The codes are lite and compacted, easy to update and maintain by your own.

## Prerequisition Installation

PyQT5 is well bundled with Python 3.x so it's required to check the python version before install the QT5 libraries though here is a discussion about how to install PyQT5 for python python 2.x.<br>
https://stackoverflow.com/questions/25589103/how-to-install-pyqt5-on-windows-for-python-2

Please be advised you probably need to check your system type to download/install the proper python. For example, this clock widget is compiled by 64 bit system and yet for x86.

To check the python version, open the terminal or cmd and type python or python --version to see the version before compile the clock widget.

$ python --version
Python 3.6.2

C:\>python (in windows)
Python 3.6.2 (v3.6.2:5fd33b5, Mar  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

## Installation

In order to run this widget you are recommended to search the following systems/utilities/tools existence in your system or install them beforehand if not.

* Linux Ubuntu 16.04 / OS2 / Windows 7
* Python 3.6.2
* PyQT5
* pip
* cx_Freeze
* Python IDE, eg. Wings, PyCharm, Vim... (optional)
* Inno Setup (optional) 

## Test and Run (Windows)

EXE pack:
1. copy the codes to your local directory 
2. change diretory to your local directory
3. under the directory type: <br>
   python setup.py build
4. when the compile command fired, cx_Freeze will follow the schema in setup.py to build an executable file inside build/exe.win-amd64-3.6
5. run the compiled file clock.exe inside the exe directory to see the clock widget

MSI pack:
1. run the following command to pack as a msi:<br>
    python setup.py bdist_msi
2. Analog Clock-0.2-amd64.msi will be generated in the dist folder
3. You're probably interested to customize the msi installation by this topic: <br>
   https://stackoverflow.com/questions/17307934/creating-msi-with-cx-freeze-and-bdist-msi-for-pyside-app

Note: you also can pack the files as a installer by Inno setup. see http://www.jrsoftware.org/isinfo.php for more information if you are interested.

## Snapshots

* Widget on top<br>
![on top](https://github.com/joechiu/clock/blob/master/ss01.png?raw=true "widget on top snapshot")

* Expandable to screen<br>
![expand to screen](https://github.com/joechiu/clock/blob/master/ss02.png?raw=true "expandable to screen by mouse wheel snapshot")

* Side menu<br>
![side menu](https://github.com/joechiu/clock/blob/master/ss03.png?raw=true "side menu snapshot")

## Resources

Images and Icons:<br>
http://www.iconarchive.com/tag/clock

PyQT5 examples:<br>
https://github.com/baoboa/pyqt5/tree/master/examples

## Contributors

You are free to update these tools to make them more helpful.

## License

A short snippet describing the license (MIT, Apache, etc.)
