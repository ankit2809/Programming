tweet = "This is a sweet tweet from India"
positive_words = ['good','sweet','nice']
negative_words = ['bad','wrong']
words= tweet.split(' ')
for word in words:
    if word in positive_words: 
        print(word)