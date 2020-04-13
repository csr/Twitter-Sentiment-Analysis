import sys
import json

scores = {} # initialize an empty dictionary

def initializeScores(fp):
    for line in fp:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

# To parse the data in output.txt you want to apply the function json.loads to every line in the file.
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
			print(score)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    initializeScores(sent_file)
    parseTweets(tweet_file)

if __name__ == '__main__':
    main()
