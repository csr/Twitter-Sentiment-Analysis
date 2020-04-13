import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

knownWordsScores = {} # scores from the AFINN-111.txt file
tweetScores = {}
unknownWordsScores = {} # new words found in tweets 

# Fill dictionary containing scores for known words
def initializeScores(fp):
    for line in fp:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      knownWordsScores[term] = int(score)  # Convert the score to an integer.

# Get sentiment score of each tweet
def scoreTweets(tweets):
	for tweet in tweets:
		tweetScore = 0
		for word in tweet.split():
			if word in knownWordsScores:
				tweetScore += knownWordsScores[word]
		tweetScores[tweet] = tweetScore
		# print(str(tweetScores[tweet]) + ' tweet score for tweet: ' + tweet)

# For every tweet, score the terms that do not have a score yet
def rateNewTerms(tweets):
	for tweet in tweets:
		tweetScore = tweetScores[tweet]
		# print(str(tweetScores[tweet]) + ' tweet score for tweet: ' + tweet)
		for word in tweet.split():
			if word not in knownWordsScores:
				if word not in unknownWordsScores:
					# Case 1: we never found this term, creating array
					unknownWordsScores[word] = [tweetScore]
					# print('first time seeing this word, adding tweet score: ' + str(tweetScore))
				# Case 2: we've already found this term once, append tweet score to array
				else:
					# print('NOT first time seeing this word, adding tweet score: ' + str(tweetScore))
					unknownWordsScores[word].append(tweetScore)

def printScores():
	for i, (key, scores) in enumerate(unknownWordsScores.items()):
		# Skip words with multiple words
		if ' ' not in key:
			average = 0
			for score in scores:
				average += score
			average /= len(scores) 
			print(key + ' ' + str(average))

def getTweets(fp):
	tweets = []
	for line in fp:
		data = json.loads(line)
		# Only parse tweets with text
		if "text" in data:
			tweets.append(data['text'])
	return tweets

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    initializeScores(sent_file)

    tweets = getTweets(tweet_file)
    scoreTweets(tweets)
    rateNewTerms(tweets)

    printScores()

if __name__ == '__main__':
    main()
