class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self. age = age
tweet = parrot("tweet", 2)
twitter = parrot("twitter", 4)
print("tweet is a {}".format(tweet.species))
print("twitter is also a {}".format(twitter.species))
print("{} is {} years old".format(tweet.name, tweet.age))
print("{} is {} years old".format(twitter.name, twitter.age))