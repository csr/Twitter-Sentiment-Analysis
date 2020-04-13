import sys
import json

reload(sys)
sys.setdefaultencoding('utf8')

frequencies = {}

def getTweets(fp):
  tweets = []
  for line in fp:
    data = json.loads(line)
    # Only parse tweets with text
    if "text" in data:
      tweets.append(data['text'])
  return tweets

def parseTweetsAndReturnTotalNumberOfTerms(tweets):
  totalNumberOfTerms = 0

  for tweet in tweets:
    for word in tweet.split():
      totalNumberOfTerms += 1
      if word in frequencies:
        frequencies[word] += 1
      else:
        frequencies[word] = 1 
  return totalNumberOfTerms

def main():
    global totalNumberOfTerms

    tweet_file = open(sys.argv[1])
    tweets = getTweets(tweet_file)

    totalNumberOfTerms = parseTweetsAndReturnTotalNumberOfTerms(tweets)

    # Print frequency
    for i, (term, frequency) in enumerate(frequencies.items()):
      result = float(frequency)/float(totalNumberOfTerms)
      print(term + ' ' + str(result))

if __name__ == '__main__':
    main()
