import os

def create_sample_videos(num_videos, directory):
    """
    Creates a specified number of sample .mp4 files named "new-video-x.mp4"
    where 'x' is a sequential number.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    for i in range(1, num_videos + 1):
        filename = f"new-video-{i}.mp4"
        filepath = os.path.join(directory, filename)
        
        # Create an empty .mp4 file
        with open(filepath, "wb") as file:
            pass

    return f"{num_videos} sample .mp4 files have been created in '{directory}'."

# Example usage: create 5 sample .mp4 files in the 'videos' directory
create_sample_videos(50, "../New-Videos")
