from pathlib import Path
import moviepy.editor

# Get file name
file_name = Path('video/')

# Convert vidio to audio with {file_name} name
video = moviepy.editor.VideoFileClip(f'{file_name}')
audio = video.audio
audio.write_audiofile(f'audio/{file_name.stem}.mp3')