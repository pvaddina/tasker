# Tasker
A simple tool in python that helps organize several tasks as groups/containers/singletasks in a configuration file (*.json format), and will let interactively execute the desired one. As a simple example: To work with Project-A you need to set the environment variables in a specific way, and again to work with Project-B, those variables need to be reset to different values. So you could simply organize the two different variants into groups in the configuration file and execute them interactively. If you think this sounds like your problem, then this tool is for you. The advantage of this tool is that it can be extended with new modules. This is not limited to environment variables alone. 

# Usage
``` python
tasker.py [--configfile=<config-file-name>] [--exec=<option>]
```
* The arguments should be qualified with keywords. Currently supported keywords are:
** configfile --> Specify a configuration file name. If this option is not present, then the default config file is taken, "config.json". When the default one is also not available, then it will not continue
** exec --> Use this option to specify a direct command for execution. The tool will execute it and exit at the end automatically. The direct commands are specified with numerical numbers followed by '.', until the desired task is chosen. The following example will first extract the 3rd workpackage, followed by 4th task container, then the 2nd container and finally the task/taskgroup '1'. Example:  
``` python
tasker.py --configfile=config.json --exec=3.4.2.1
```
* If no config file is passed as an argument, then the default config filename, "config.json" is used

# Terminology
The following description is all you need to use the tool. Please refer to the **tasker.json** file for further details.

### SingleTask
A single executable task. Cannot be broken down further.

### TaskGroup
A group of one or more SingleTasks that are all executed together one after the other. 

### TaskContainer
A way to organize multiple TaskGroups/SingleTasks. The tool will interatively display all the configured options here and based on user input will execute the specified task (could be either SingleTask/TaskGroup).

# How to add a new module
To add a new module of your own please follow these steps:
* The class that handles your task should implement the interfaces of the class **interfaces.ISingleTask**. The mentioned class mandates implementation of two functions only.
* Place the new file in the directory **mods**
* Import the new module in the package definition file **mods/__init__.py** 

# Supported operating systems
Depending on the module you may create the tool will work either in Windows only, Linux only or may be both. In the current form given all the dependencies as listed below are present, this works only under Windows.

# Dependencies
The tool in general requires the following modules to be installed.
* Colorama
* importlib

# Module Dependencies
The modules that are supplied along with the script come with some dependencies and are listed as below:
1. EnvVar - A module that can create new environment variables or update the PATH environment variable accordingly ...
   1. inreg
   1. win32gui
   1. win32con
1. SysExec - A module that runs a program along with its arguments
   1. subprocess

