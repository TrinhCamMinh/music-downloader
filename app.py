import streamlit as st
import os
import time
from music_downloader import download_as_mp3

# Page config
st.set_page_config(page_title="Mom's Music Downloader", page_icon="🎵")

st.title("🎵 Mom's Music Downloader")
st.markdown("""
Welcome! Paste your song titles below (one per line), and I'll find them on YouTube and convert them to MP3 for your stereo.
""")

# Input for song titles
titles_input = st.text_area("Paste song titles here:", height=200, placeholder="Example:\nQueen - Bohemian Rhapsody\nBeatles - Hey Jude")

# Output directory selection (default to 'downloads')
output_folder = "downloads"

if st.button("🚀 Start Downloading"):
    if not titles_input.strip():
        st.error("Please enter at least one song title.")
    else:
        titles = [t.strip() for t in titles_input.split('\n') if t.strip()]
        st.info(f"Processing {len(titles)} songs...")
        
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        results = []
        
        for i, title in enumerate(titles):
            status_text.text(f"Searching and downloading: {title}...")
            
            # Use the local downloader
            success, message = download_as_mp3(title, output_folder)
            
            if success:
                results.append(f"✅ {title} -> {message}")
            else:
                results.append(f"❌ {title} -> Failed: {message}")
            
            progress_bar.progress((i + 1) / len(titles))
            
        st.success("All downloads finished!")
        
        # Show summary
        st.subheader("Summary")
        for res in results:
            st.write(res)
            
        # Provide info on where files are
        st.info(f"Files are saved in the `{output_folder}` folder.")

st.markdown("---")
st.caption("Built with ❤️ for Mom and Brother")
