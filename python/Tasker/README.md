# Tasker

A simple tool in python that helps organize several tasks as groups/containers/singletasks in a configuration file (*.json format), and will let interactively execute the desired one. As a simple example: To work with Project-A you need to set the environment variables in a specific way, and again to work with Project-B, those variables need to be reset to different values. So you could simply organize the two different variants into groups in the configuration file and execute them interactively. If you think this sounds like your problem, then this tool is for you. The advantage of this tool is that it can be extended with new modules. This is not limited to environment variables alone. 

# Terminology
The following description is all you need to use the tool. Please refer to the **tasker.json** file for further details.
## SingleTask
A single executable task. Cannot be broken down further.

## TaskGroup
A group of SingleTasks that are all executed together. 

## TaskContainer
A way to organize multiple TaskGroups/SingleTasks. The tool will interatively display all the configured options here and based on user input will executed the specified task (could be either SingleTask/TaskGroup).

# How to add a new module

# Supported operating systems
Depending on the module you may create the tool will work either in Windows only, Linux only or may be both. In the current form given all the dependencies as listed below are present, this works only under Windows.

# Dependencies
The tool in general requires the following modules to be installed.
* Colorama
* importlib

# Module Dependencies
1. EnvVar
   1. inreg
   1. win32gui
   1. win32con

