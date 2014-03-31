from urllib2 import urlopen
from json import load, dumps

url = 'http://api.npr.org/query?apiKey=' 
key = ''
url = url + key
url += '&numResults=1&format=json&id=1007' #1007 is science
url += '&requiredAssets=text,audio,image'

response = urlopen(url)
json_obj = load(response)

# uncomment 3 lines below to see JSON output to file
f = open('output.json', 'w')
f.write(dumps(json_obj, indent=4))
f.close()

for story in json_obj['list']['story']:
	print "TITLE: " + story['title']['$text'].encode('utf-8') + "\n"
	print "DATE: " + story['storyDate']['$text'].encode('utf-8') + "\n"
	print "TEASER: " + story['teaser']['$text'].encode('utf-8') + "\n"

	if 'byline' in story:
		print "BYLINE: " + story['byline'][0]['name']['$text'].encode('utf-8') + "\n"

	if 'show' in story:
		print "PROGRAM: " + story['show'][0]['program']['$text'].encode('utf-8') + "\n"

		print "NPR URL: " + story['link'][0]['$text'].encode('utf-8') + "\n"
		print "IMAGE: " + story['image'][0]['src'] + "\n"

		if 'caption' in story:
			print "IMAGE CAPTION: ", story['image'][0]['caption']['$text'].encode('utf-8') + "\n"

		if 'producer' in story:
			print "IMAGE CREDIT: " + story['image'][0]['producer']['$text'].encode('utf-8') + "\n"

		print "MP3 AUDIO: " + story['audio'][0]['format']['mp3'][0]['$text'].encode('utf-8') + "\n"	

	#loop through and print each paragraph
	for paragraph in story['textWithHtml']['paragraph']:
		print paragraph['$text'].encode('utf-8') + " \n"