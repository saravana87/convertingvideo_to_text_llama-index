import cv2
import os

# Path to the video file
output_dir = r"/Output/directory/"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Load the video
cap = cv2.VideoCapture(video_path)

# Initialize variables
ret, prev_frame = cap.read()
count = 0
threshold = 0.004  # Sensitivity threshold for detecting changes
prev_perc = 0.0
frame_filename = ""
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
frames_per_minute = 30 * 60  # 1800 frames per minute
frame_skip = frames_per_minute

# Iterate through each frame
while ret:
    for _ in range(frame_skip):  # Skip the specified number of frames
        ret, _ = cap.read()
        if not ret:
            break

    ret, current_frame = cap.read()
    if not ret:
        break
    
    # Compute the difference between the current frame and the previous frame
    diff = cv2.absdiff(current_frame, prev_frame)
    
    # Convert the difference to grayscale
    gray_diff = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    
    # Calculate the percentage of different pixels
    non_zero_count = cv2.countNonZero(gray_diff)
    total_pixels = gray_diff.size
    diff_percentage = non_zero_count / total_pixels
    print("diff", diff_percentage)
    print("prev", prev_perc)
    
    # If the difference is above a certain threshold, save the frame
    if diff_percentage > threshold:
        print(frame_filename)
        frame_filename = os.path.join(output_dir, f"frame_{count}.jpg")
        cv2.imwrite(frame_filename, current_frame)
        count += 1
    
    prev_perc = diff_percentage
    prev_frame = current_frame

cap.release()
cv2.destroyAllWindows()
