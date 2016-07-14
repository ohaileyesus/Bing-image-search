# Bing Image Search Via Text
This Python Flask app returns the top 3 search results for any Bing Image search by texting a Twilio designated phone number.

#Setup
1. You will first need to create an account on Twilio's website, which will give you an Auth Token and Account SID, both of which you will need to operate this app. In addition, you will need to obtain a phone number. 
2. You will need to install ngrok and run a session. Set your ngrok forwarding url as the webhook url for your phone number's SMS HTTP GET response.
3. Obtain a Bing API key.
