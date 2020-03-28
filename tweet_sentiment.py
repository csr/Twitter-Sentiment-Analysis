import sys
import json

scores = {} # initialize an empty dictionary

def initializeScores():
    afinnfile = open("AFINN-111.txt")
    for line in afinnfile:
      term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
      scores[term] = int(score)  # Convert the score to an integer.

def lines(fp):
	print(str(len(fp.readLines())))

# To parse the data in output.txt you want to apply the function json.loads to every line in the file.
def parseTweets(fp):
	print("Parsing tweets...")
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
    initializeScores()
    parseTweets(tweet_file)

if __name__ == '__main__':
    main()
