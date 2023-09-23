# Pytube Library Markup Notes

 ## Introduction
pytube is a Python library that allows you to interact with and manipulate YouTube videos.
 It provides features for downloading videos, extracting metadata, and working with video streams.

# Installation
You can install pytube using pip:
```
 pip install pytube
```
## Basic Usage

### Importing the Library
```
import pytube

```
### Creating a YouTube Instance

```
video_url = 'https://www.youtube.com/watch?v=your_video_id_here'
youtube = pytube.YouTube(video_url)
```
### Accessing Video Streams
```
stream = youtube.streams.get_highest_resolution()

```
### Downloading a Video
```
stream.download(output_path='your_output_directory')
```
## Additional Features

### Getting Video Metadata
```
title = youtube.title
author = youtube.author
views = youtube.views
```


### Official Documentation: https://pytube.io/en/latest/