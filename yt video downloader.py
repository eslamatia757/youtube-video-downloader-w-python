from pytube import YouTube #we imported the youtube file from the pytube module

link = "https://www.youtube.com/watch?v=q0ert5YP968&list=PLuXY3ddo_8nzrO74UeZQVZOb5-wIS6krJ&index=38"
#link = input("please enter your video link url:") # creaded a variable to store the video link 

video = YouTube(link) # created an object from the youtube class stores the value of the link as an constractor

#print(f"the video title is:{video.title} \n--------")
#print(f"the video description is:\n{video.description} \n-------")
#print(f"the video length is :\n{video.length}\n------")
#print (f"the video views are :{video.views}\n------")

#for stream in video.streams.filter(progressive=True, res="720p"):
#	print(stream)

#print(video.streams.get_highest_resolution())
def finish():
	print("download done")

video.streams.get_highest_resolution().download(output_path="Users/eslam/Desktop/py oob")
video.register_on_complete_callback(finish())

#from pytube import PlayList

#playlist_link = ""

#playlist = PlayList(playlist_link)

#for video in playlist.videos:
	#video.streams.get_lowest_resolution().download(output_path="")