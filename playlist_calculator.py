from googleapiclient.discovery import build
import isodate

def get_playlist_id_from_url(url):
    """Extracts the playlist ID from the YouTube playlist URL."""
    if "list=" in url:
        return url.split("list=")[1].split("&")[0]
    raise ValueError("Invalid playlist URL. Make sure it includes 'list='.")

def get_playlist_duration(api_key, playlist_id):
    # Initialize YouTube API client
    youtube = build('youtube', 'v3', developerKey=api_key)

    total_duration = 0

    # Paginate through playlist items
    next_page_token = None
    while True:
        playlist_items = youtube.playlistItems().list(
            part="contentDetails",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        video_ids = [item['contentDetails']['videoId'] for item in playlist_items['items']]

        # Fetch video details
        video_details = youtube.videos().list(
            part="contentDetails",
            id=",".join(video_ids)
        ).execute()

        for video in video_details['items']:
            duration = video['contentDetails']['duration']
            parsed_duration = isodate.parse_duration(duration)
            total_duration += parsed_duration.total_seconds()

        next_page_token = playlist_items.get('nextPageToken')
        if not next_page_token:
            break

    # Convert total seconds to minutes
    total_minutes = total_duration / 60
    return total_minutes

if __name__ == "__main__":
    # Your YouTube Data API Key
    API_KEY = "AIzaSyB-sD8ntpDf28dBp3Fv79QWUhTENelGBkQ"

    # Ask user for playlist URL
    playlist_url = input("Enter the YouTube playlist URL: ")

    try:
        # Extract playlist ID from URL
        playlist_id = get_playlist_id_from_url(playlist_url)

        # Calculate playlist duration
        total_minutes = get_playlist_duration(API_KEY, playlist_id)
        print(f"Total duration of the playlist: {total_minutes:.2f} minutes")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
