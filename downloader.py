from pytube import YouTube
import os
from tqdm import tqdm

def download_video(url):
    try:
        video = YouTube(url)
        stream = video.streams.get_highest_resolution()
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        file_size = stream.filesize
        print("Downloading...")
        # Use tqdm to display the progress bar
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=stream.default_filename) as progress_bar:
            stream.download(output_path=download_path, filename_prefix='tmp_', 
                            filename=stream.default_filename, 
                            skip_existing=False)
            progress_bar.update(file_size)
        
        # Once the download is complete, rename the file to remove the 'tmp_' prefix
        file_name = stream.default_filename
        os.rename(os.path.join(download_path, f"tmp_{file_name}"), 
                  os.path.join(download_path, file_name))
        
        print("Download completed successfully!")
        print("Video saved at Downloads folder")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    url = input("Enter the URL of the video you want to download: ")
    download_video(url)

if __name__ == "__main__":
    main()
