# PyTomato
![PyTomato logo](logo.png)

A very simple pomodoro timer made with python

## Functions
A pomodoro timer is a timer inspired by the [pomodoro technique](https://en.wikipedia.org/wiki/Pomodoro_Technique). The application will allow you to start a 25 minutes timer and during this time you are supposed to work, followed by a short break of 5 minutes. For now, the time for the work period and the break period cannot be changed, but I'm planning on adding this feature in future versions.

## How to run

### Windows
On windows, just download the zip file and extract it. Then make sure to <mark>keep the executable file inside of the folder</mark> and just double click on it to open the application

### Linux

On linux you can do two things:
#### Wine
You can use Wine on linux machines to run windows executable. To install wine check the official [Wine repo](https://github.com/wine-mirror/wine).
Firstly navigate to the timer folder. Then just type in your terminal: 
``` 
wine timer.exe
```

#### Python execution
If you don't have Wine installed, you can just download the source code, and run the timer.py file (If you have python installed on your machine). You can run it in two ways:

In the terminal type:

```
python timer.py
```
or: 
```
python3 timer.py
```
In alternative you can make the python file executable with chmod. First of all add this line at the top of the python file:
```
#!/usr/bin/python
```
Then run the chmod command:
```
chmod +x timer.py
```
And then you can run it:
```
./timer.py
```


## Conlusion
You can download the executable from [here](). Windows Defender or your antivirus will probably block the execution, but you can add an exception in your antivirus settings. If you don't trust the application, you can always check the source code from the main branch of the repo.
