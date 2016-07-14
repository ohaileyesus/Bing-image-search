from flask import Flask, request
from twilio.rest import TwilioRestClient
from py_bing_search import PyBingImageSearch

client = TwilioRestClient("[ACCOUNT_SID]", "[AUTH_TOKEN]")

app = Flask(__name__)

@app.route("/")
def test():
	msg_body = request.values.get('Body', None)
	
	client.messages.create(
		to = request.values.get('From', None),
		from_= '[ENTER PHONE NUMBER]',
		body = '',
		media_url = imageLookup(msg_body,0))

	client.messages.create(
		to = request.values.get('From', None),
		from_= '[ENTER PHONE NUMBER]',
		body = '',
		media_url = imageLookup(msg_body,1))

	client.messages.create(
		to = request.values.get('From', None),
		from_= '[ENTER PHONE NUMBER]',
		body = '',
		media_url = imageLookup(msg_body,2))
			
	return 'photo'


def imageLookup(msg_body, iteration):
	bing_image = PyBingImageSearch('[ENTER YOUR API KEY]', msg_body)
	first_three_results = bing_image.search(limit=3, format='json') #1-50
	return (first_three_results[iteration].media_url)
	

app.run()
