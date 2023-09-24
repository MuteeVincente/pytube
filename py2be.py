import pytube

# Ask the user to enter url of the Youtube.

video_url = input('Enter url: ')

#Create an instance of Youtube video

video_instance = pytube.YouTube(video_url)
stream = video_instance.streams.get_highest_resolution()

#download

video1= stream.download()

print(video1.title)

