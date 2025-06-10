import scrapetube
from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders import YoutubeAudioLoader
from langchain_community.document_loaders.parsers import OpenAIWhisperParser
import os
from dotenv import load_dotenv
from youtubevideo import YoutubeVideo

load_dotenv()

my_key_openai = os.getenv("openai_apikey")

#1 Transcription
def get_video_transcript(url):
    target_dir = "./audios/"
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    loader = GenericLoader(
        YoutubeAudioLoader(urls=[url], save_dir=target_dir),
        OpenAIWhisperParser(api_key=my_key_openai)
    )

    video_transcript_docs = loader.load()
    return video_transcript_docs

#2 Youtube Search
def get_video_for_search_term(search_term, video_count=1, sorting_criteria="relevance"):

    videos = scrapetube.get_search(query=search_term, limit=video_count, sort_by=sorting_criteria)
    videolist = list(videos)

    youtube_videos = []
    for video in videolist:
        new_video = YoutubeVideo(
            video_id=video["videoId"],
            video_title=video["title"]["runs"][0]["text"],
            video_url= "https://www.youtube.com/watch?v=" + video["videoId"],
            channel_name= video["longBylineText"]["runs"][0]["text"],
            duration = video["lengthText"]["accessibility"]["accessibilityData"]["label"],
            publish_date= video["publishedTimeText"]["simpleText"]
        )

        youtube_videos.append(new_video)
        return youtube_videos

















