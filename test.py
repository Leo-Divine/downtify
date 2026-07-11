import syncedlyrics

# Fetch synced lyrics using a search term (Artist - Title)
# Use 'synced_only=True' to ensure it returns LRC formatted timestamps
lrc_lyrics = syncedlyrics.search("Rick Astley - Never Gonna Give You Up", synced_only=True)

if lrc_lyrics:
    print(lrc_lyrics)
else:
    print("Synced lyrics not found.")
