import io

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

def transcribe_file(speech_file):
	client = speech.SpeechClient()

	with io.open(speech_file, 'rb') as audio_file:
		content = audio_file.read()

	audio = types.RecognitionAudio(content=content)
	config = types.RecognitionConfig(
		encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
		sample_rate_hertz=16000,
		language_code='en-US')

	response = client.recognize(config, audio)

	print(response)
	
	for result in response.results:
		print(u'Transcript: {}'.format(result.alternatives[0].transcript))