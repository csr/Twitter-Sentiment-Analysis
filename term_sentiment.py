import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

scores = {} # initialize an empty dictionary

def initializeScores():
    afinnfile = open("AFINN-111.txt")
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def parseTweets(fp):
	for line in fp:
		data = json.loads(line)
		if "text" in data:
			tweet = data
			text = tweet['text']
			score = 0
			for word in text.split():
				if word in scores:
					score += scores[word]
			# If we detect a positive or negative score
			# then update all the words scores
			for word in text.split():
				if word not in scores:
					scores[word] = score

def printScores():
	for i, (key, score) in enumerate(scores.items()):
	    print(key + ' ' + str(score))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    initializeScores()
    parseTweets(tweet_file)
    printScores()

if __name__ == '__main__':
    main()
