import whisper
import os

# Path to the folder containing videos
videos_dir = r"/pathto/folder/"

# Load the Whisper model
model = whisper.load_model("large")

# Process each video in the videos folder
for video_file in os.listdir(videos_dir):
    if video_file.endswith(('.mp4', '.mkv', '.avi')):  # Add any other video formats you might have
        file_path = os.path.join(videos_dir, video_file)
        print("Converting ", file_path)
        # Transcribe the audio from the video file
        result = model.transcribe(file_path)
        
        # Create the output text file path with the same name as the video file
        output_file = os.path.join(videos_dir, f"{os.path.splitext(video_file)[0]}.txt")
        
        # Save the transcription to a text file
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(result["text"])
        
        print(f"Transcription saved to {output_file}")
