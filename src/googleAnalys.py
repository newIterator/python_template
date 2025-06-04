from google.cloud import videointelligence
client = videointelligence.VideoIntelligenceServiceClient()
response = client.annotate_video(
    input_uri="./../static/IMG_0501.mp4",
    features=["PERSON_DETECTION"],
)