import os
import json
import pprint
from googleapiclient.discovery import build
api_key = os.environ.get('YT_API_KEY')

youtube = build('youtube', 'v3', developerKey=api_key)
channel_request = youtube.search().list(
    part='snippet',
    q="Women",
    type="video",
    channelId='UCPro_5C3SzJzZDVKPgKMuoQ'
)

comments = youtube.commentThreads().list(
    part='replies',
    videoId='LR44sgkBgmU'
).execute()['items']

channel_response = channel_request.execute()
channel = channel_response['items']
# print(json.dumps(channel_response['items'], sort_keys=True, indent=3))
# pprint.pprint(channel)
pprint.pprint(comments)

