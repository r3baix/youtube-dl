# Script for downloading Youtube playlists
import os
# Define whitch playlist to download
playlists = {
"LIKES": "https://www.youtube.com/playlist\?list\=PL-Ql7jAS5Ia4wo53vTQC2pdzu23gssgpT",
"GROOVY": "https://www.youtube.com/playlist?list=PL-Ql7jAS5Ia7F_ZM-P-EKPtzk5AIvzqOF",
"TECHNO_HOUSE": "https://www.youtube.com/playlist?list=PL-Ql7jAS5Ia6ddPiuzxSP10KKILVSsWS6",
"HOUSE": "https://www.youtube.com/playlist?list=PL-Ql7jAS5Ia5s9y7UC_saNECqibh1k4bf",
"HARD_TECHNO": "https://www.youtube.com/playlist?list=PL-Ql7jAS5Ia75JVduIWFeUZkJK68KOGX2"
}
# command : yt-dlp --download-archive /path/downloaded.txt --no-post-overwrites  --embed-thumbnail -ciwx --audio-format mp3 -o "/path/%(title)s.%(ext)s" --yes-playlist URL_PLAYLSIT
root_folder = os.path.expanduser("~") + "/Music/"
for playlist, url in playlists.items():
    path = root_folder + playlist
    if not os.path.exists(path):
        os.mkdir(path)
    print(f"Downloading {playlist}...")
    os.system('yt-dlp --download-archive ' + path + '/downloaded.txt ' + '--no-post-overwrites  --embed-thumbnail -ciwx --audio-format mp3 -o "' + path + '/%(title)s.%(ext)s" --yes-playlist ' + url)
    print(f"DONE {playlist}")
print("***Download Finished***")

