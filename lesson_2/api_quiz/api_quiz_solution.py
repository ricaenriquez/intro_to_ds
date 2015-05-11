import json
import requests

import json
import requests

def api_get_request(url):
    # In this exercise, you want to call the last.fm API to get a list of the
    # top artists in Spain.
    #
    # Once you've done this, return the name of the number 1 top artist in Spain.
    data = requests.get(url).text
    data = json.loads(data)
    return data[u'topartists'][u'artist'][u'name']


if __name__ == '__main__':
	# url should be the url to the last.fm api call which
	# will return find the top artists in Spain

    url = "http://ws.audioscrobbler.com/2.0/?method=geo.getTopArtists" \
          "&country=Spain&limit=1&api_key=df198ec4a4217da50ecd99aeec424a9e" \
          "&format=json"
    print api_get_request(url) 

