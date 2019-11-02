import os

# playlist
import googleapiclient.discovery

# spreadsheet
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#to go faster, comment the input lines below and hard codes values here
global PLID
global GSheetID
global worksheetIndex
global column
global offset

def initSheet():
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client.secret.json', scope)
    client = gspread.authorize(creds)
    return client.open_by_key(GSheetID).get_worksheet(worksheetIndex)

def initPlaylist(nextPageToken = ""):
    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = "AIzaSyCHvlL7SzcBvbjP9vm92qxH9-F07dDFPmA"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)
    if nextPageToken == "":
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=PLID
        )
    else:
        request = youtube.playlistItems().list(
            part="snippet,contentDetails",
            maxResults=50,
            playlistId=PLID,
            pageToken=nextPageToken
        )
    results = request.execute()
    return results

# To go faster, comment those lines and hardcode values up top
print("Welcome to the worksheet updater !", end="\n")
PLID = input("enter the playlist ID (must be in unlisted or public): ")
GSheetID = input("enter the ID of the google sheets document (you can find it in the URL): ")
worksheetIndex = int(input("enter the index of the worksheet you'd like me to edit (starts at 0): "))
column = input("What column shoud I put the songs in ? (for exemple, 'A' to indicate first column): ")
offset = int(input("by how many rows should I be offset ? (for exemple, '0' indicates starting at the first row): "))

sheet = initSheet()
token = ""
compteur = 0
currentResults = initPlaylist(token)
while True:
    for element in currentResults["items"]:
        compteur += 1
        print("{}. {}".format(compteur, element), end="\n")
        sheet.update_acell("{}{}".format(column, offset + compteur), '=HYPERLINK("https://youtube.com/watch?v=' + element["contentDetails"]["videoId"] + '"; "' + element["snippet"]["title"].replace('"', "'") + '")')
    if not "nextPageToken" in currentResults:
        break
    token = currentResults["nextPageToken"]
    currentResults = initPlaylist(token)