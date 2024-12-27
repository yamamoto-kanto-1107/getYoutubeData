from googleapiclient.discovery import build
import pandas as pd
import re

def extract_sns_url(description):
    x=''
    instagram=''
    facebook=''

    insta_url = r'https://www.instagram.com/[^\s]+'
    face_url= r'https://www.facebook.com/[^\s]+'
    x_url=r'https://www.x.com/[^\s]+'
    twitter_url =r'https://twitter.com/[^\s]+'

    instagram = re.findall(insta_url,description)
    facebook = re.findall(face_url,description)
    x=re.findall(x_url,description)
    if len(x)  ==0:
        x = re.findall(twitter_url,description)

    sns_list={
        'insta':instagram,
        'face':facebook,
        'x':x
    }

    return sns_list

def output_youtube_detail(csv_value,category_value,count_value):
# def output_youtube_detail():
    API_KEY = 'AIzaSyC4L5XLO19nJdBIrllPTwneiidJ_7_HEOU'
    youtube = build('youtube','v3',developerKey=API_KEY)
    name=[]
    watch=[]
    count=[]
    video=[]
    insta=[]
    face=[]
    x=[]
    count_output = 0

    try:
        while True:
            if count_output == count_value:
                break
            request = youtube.search().list(
                part='snippet',
                type='video',
                videoCategoryId=category_value,
                maxResults=50
            )

            result = request.execute()
            for item in result['items']:
                channel_id = item['snippet']['channelId']

                channel_request = youtube.channels().list(
                    part='snippet,statistics,brandingSettings',
                    id = channel_id
                )
                channel_result = channel_request.execute()

                if channel_result['items']:
                    channel = channel_result['items'][0]
                    channel_name = channel['snippet']['title']
                    channel_regist_count = channel['statistics'].get('subscriberCount',0)
                    channel_all_watch_time = channel['statistics'].get('viewCount',0)
                    channel_video_count = channel['statistics'].get('videoCount',0)

                    #重複チェック
                    if channel_name in name:
                        continue

                    if int(channel_regist_count) < 5000 or 100000 < int(channel_regist_count):
                        continue

                    count_output += 1
                    name.append(channel_name)
                    watch.append(channel_all_watch_time)
                    count.append(channel_regist_count)
                    video.append(channel_video_count)

                    description = channel['snippet'].get('description', '')

                    sns_list = extract_sns_url(description)
                    if len(sns_list['insta']) == 0:
                        insta.append('-')
                    else:
                        insta.append(sns_list['insta'][0])

                    if len(sns_list['face']) == 0:
                        face.append('-')
                    else:
                        face.append(sns_list['face'][0])

                    if len(sns_list['x']) == 0:
                        x.append('-')
                    else:
                        x.append(sns_list['x'][0])

            request = youtube.search().list_next(request, result)

    except Exception as e:
        print(e)

    data_list ={
        'チャンネル名':name,
        '総視聴回数':watch,
        '登録者数':count,
        '動画本数':video,
        'facebook':face,
        'instagram':insta,
        'x':x
    }
    print(len(name))
    print(len(watch))
    print(len(count))
    print(len(video))
    print(len(face))
    print(len(insta))
    print(len(x))

    df = pd.DataFrame(data_list)
    df.to_csv(f'{csv_value}/sample.csv')
    df.to_csv('/Users/kantoyamamoto/Desktop/sample.csv')