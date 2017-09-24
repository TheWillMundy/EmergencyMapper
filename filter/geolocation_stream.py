# import _____

geoloc_list = []

for tweet_data in tweets:
    geoloc = (tweet_data[0], tweet_data[1])
    geoloc_list.append(geoloc)

geolocations = open('geolocations.csv', 'w')
geolocations.write(geoloc_list)
geolocations.close()
