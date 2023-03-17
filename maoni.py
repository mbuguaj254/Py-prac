from moviepy.video.io.VideoFileClip import VideoFileClip

# Define the input video file or video link
input_video = 'mics.mp4'

# Define the starting and ending minutes for the video cut
start_minute = 1  # Start at 1 minute
end_minute = 3  # End at 3 minutes

# Load the video clip using moviepy
video_clip = VideoFileClip(input_video)

# Define the start and end times for the video cut
start_time = start_minute * 60  # Convert minutes to seconds
end_time = end_minute * 60  # Convert minutes to seconds

# Cut the video clip using moviepy
cut_video = video_clip.subclip(start_time, end_time)

# Save the cut video as a new file
cut_video.write_videofile("output.mp4")
