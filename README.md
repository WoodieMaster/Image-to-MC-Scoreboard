# Image to MC Scoreboards

This is a little program that converts images into mcfunction files, that generate the same image in minecraft scoreboard displays

## About
While watching [PhoenixSCLive](https://www.twitch.tv/phoenixsclive), where he used the same method to display images, I came up with the idea to automate it, and here it is!

## Overview
- The project is written in python 3.12
- The entire code is located in the main.py file
- Supports all common image formats (More details in the PIL package)
- The project converts the given image into a .mcfunction file that can be placed in a mc datapack to display the image in the scoreboard display
- The mc_test folder uses the image conversion to update the display to the item that you're currently holding in minecraft
- Used packages:
  - [numpy](https://numpy.org)
  - [PIL](https://pillow.readthedocs.io/en/stable/)


## Installation
Download the code from github.
In the future I might add the project to pip, but I this is not yet planned

## Usage
### main.py
Call the file with the following arguments (use - to ignore a specific argument):
- The path to the image you want to convert
- The output path (if this path is not given, it will print the code to the console instead of writing it to a file)
- The name of the scoreboard you want to use for display (defaults to "display")
- The alignment: true for left aligned and false for right aligned (defaults to false)
### test.py
Before running the file change the following variables:
- MC_VERSION defines the version of minecraft you want to get the images from
- WORLD defines the name of the world you want to put the datapack into
- DATAPACK is the name of the datapack where the display should happen

and move the datapack_example folder in the datapack folder of your world (you might rename the datapack)

**Important:**

This script will extract the version.jar file of the minecraft version you specified, when it wasn't already extracted. If you don't want that either extract it yourself or get the images from somewhere else