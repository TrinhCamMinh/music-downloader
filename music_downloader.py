import os
import yt_dlp

def download_as_mp3(query, output_dir="downloads"):
    """
    Searches for a video title and downloads it as an MP3 file.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'default_search': 'ytsearch',
        'noplaylist': True,
        'quiet': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # We pass 'ytsearch1:' to ensure it searches by title and picks the first result
            search_query = f"ytsearch1:{query}"
            info = ydl.extract_info(search_query, download=True)
            if 'entries' in info and len(info['entries']) > 0:
                video_info = info['entries'][0]
                return True, video_info.get('title', 'Unknown Title')
            else:
                return False, "No results found"
    except Exception as e:
        return False, str(e)

if __name__ == "__main__":
    # Test
    success, message = download_as_mp3("Never Gonna Give You Up")
    print(f"Success: {success}, Message: {message}")
