import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

scores = {} # initialize an empty dictionary
statesScore = {} # contains scores for states

# Only add tweets which
# - have text
# - have country code == US
def getTweets(fp):
	tweets = []
	for line in fp:
		data = json.loads(line)
		# Only parse tweets with text AND location data
		if 'text' in data and 'user' in data:
			userData = data['user']
			if userData != None:
				if 'location' in userData and userData['location'] != None:
					# print(userData)
					tweets.append(data)
	return tweets

# To parse the data in output.txt you want to apply the function json.loads to every line in the file.
def parseTweets(tweets):
	for tweet in tweets:
		# print(tweet)
		score = 0
		for word in tweet['text'].split():
			if word in scores:
				score += scores[word]
		# print(score)

		# Get country code
		countryCode = tweet['user']['location'].split(', ')
		# print(countryCode)
		if (len(countryCode) == 2 and countryCode[1] in states):
			statesScore[countryCode[1]] = score

def initializeScores(fp):
    for line in fp:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def main():
	sent_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	initializeScores(sent_file)

	tweets = getTweets(tweet_file)
	# print('loaded ' + str(len(tweets)) + ' tweets')
	parseTweets(tweets)

	state = ''
	maxScore = -99999

	for i, (key, score) in enumerate(statesScore.items()):
		# print('state ' + key + 'has score: ' + str(score))
		if score > maxScore:
			maxScore = score
			state = key
	
	print(state)

if __name__ == '__main__':
	main()