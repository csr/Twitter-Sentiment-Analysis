# Sentiment Analysis on Tweets

## Getting Started
Sign up for a Twitter Developer account and add your API key, API secret, Access Token Key, and Access Token Secret to `twitterstream.py` to get started. You'll need Python 2.7 and Oauth2 installed on your machine to get started.

```
api_key = "YOUR_API_KEY"
api_secret = "YOUR_API_SECRET"
access_token_key = "YOUR_ACCESS_TOKEN_KEY"
access_token_secret = "YOUR_ACCESS_TOKEN_SECRET"
```

To download a stream of tweets and check that everything is working fine, enter in the following command into the terminal:
```
python twitterstream.py > output.json
```

This will create a continous stream of tweets and save it to a file named `output.json`. To stop, press control + C on your keyboard.

## License
This directory is licensed under the MIT License.
