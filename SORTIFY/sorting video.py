import cv2
import os
import shutil

def play_videos_from_folder(input_folder, output_folder):
    
    os.makedirs(output_folder, exist_ok=True)


    videos = [f for f in os.listdir(input_folder) if f.lower().endswith(('.mp4', '.avi', '.mkv'))]

    if not videos:
        print("No video files found in the folder.")
        return

    video_index = 0  

    while video_index < len(videos):
        video = videos[video_index]
        video_path = os.path.abspath(os.path.join(input_folder, video)) 
        target_path = os.path.abspath(os.path.join(output_folder, video)) 

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Error opening video file {video}")
            video_index += 1
            continue

        print(f"Playing {video}. Press 'Alt' to move, 'q' to skip, 'Space' to pause/resume, 'k' for previous video.")

        paused = False  

        while cap.isOpened():
            if not paused:
                ret, frame = cap.read()
                if not ret:
                    break

                
                frame = cv2.resize(frame, (640, 360))  

                
                cv2.imshow('Video Player', frame)

           
            key = cv2.waitKey(30) & 0xFF

            if key == ord('q'):  
                print(f"Skipping {video}")
                break
            elif key == ord(' '):  
                paused = not paused
                if paused:
                    print("Paused. Press 'Space' to resume.")
                else:
                    print("Resumed playback.")
            elif key == ord('k'):  
                print("Going to the previous video.")
                video_index = max(video_index - 1, 0)  
                cap.release()
                break
            elif key == 18: 
                try:
                    
                    shutil.move(video_path, target_path)
                    print(f"Moved {video} to {output_folder}")
                except Exception as e:
                    print(f"Failed to move {video}: {e}")
                break

        cap.release()
        if key != ord('k'):  
            video_index += 1

    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_folder = r'F:\aaaa'  # Replace with the path to your video folder
    output_folder = r'C:\Users\Dipak\Desktop\sakshi\sorted nigh'  # Replace with the path to your target folder

    play_videos_from_folder(input_folder, output_folder)
