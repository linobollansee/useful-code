import yt_dlp

def download_youtube_channel():
    print("YouTube Channel Downloader")

    # Prompt user for channel URL
    channel_url = input("Enter the YouTube channel URL: ")

    try:
        # Options for yt-dlp
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',  # Best video & audio
            'outtmpl': './%(uploader)s/%(title)s.%(ext)s',  # Save in channel folder
            'merge_output_format': 'mp4',  # Merge into MP4
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',
            }],
            'quiet': False,  # Show progress
            'progress_hooks': [lambda d: print(f"Downloading: {d.get('filename', 'Unknown')} - {d['status']}")],
            'cookiefile': 'cookies.txt',  # Use cookies for authentication
            'retries': 10,  # Retry failed downloads
            'fragment_retries': 10,  # Retry broken fragments
            'continue': True,  # Resume downloads
            'noplaylist': False,  # Download full playlist (channel)
            'ignoreerrors': True,  # Continue even if some videos fail
        }

        print("\nDownloading... This may take some time depending on the channel size.")
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([channel_url])

        print("Download complete! All videos saved in the specified directory.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_youtube_channel()
