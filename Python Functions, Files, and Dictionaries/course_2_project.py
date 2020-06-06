# We have provided some synthetic (fake, semi-randomly generated) twitter data in a csv file named project_twitter_data.csv which has the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet. We have also words that express positive sentiment and negative sentiment, in the files positive_words.txt and negative_words.txt.

# Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. You will create a csv file, which contains columns for the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score for each tweet. At the end, you upload the csv file to Excel or Google Sheets, and produce a graph of the Net Score vs Number of Retweets.

# To start, define a function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(x):
    for i in punctuation_chars:
        x = x.replace(i, "")
    return x

word = input("Hello! i'm shawon")
print(strip_punctuation(word))


      
#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# list of positive words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
print(positive_words)
def strip_punctuation(x):
        for i in punctuation_chars:
            x = x.replace(i, "")
        return x
def get_pos(sentence):
    no_punc_word = strip_punctuation(sentence)
    split_no_punc_word = no_punc_word.lower().split()
    pos = 0
    d = []
    for item in split_no_punc_word:
        if item in positive_words:
            pos += 1
            d.append(item)
    return pos
word = input("Hello! i'm shawon")
print(get_pos(word))
#['wonderful', 'incredible'],wonderful


# Next, copy in your strip_punctuation function and define a function called get_neg which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered negative words. Use the list, negative_words to determine what words will count as negative. The function should return a positive integer - how many occurrences there are of negative words in the text. Note that all of the words in negative_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

print(negative_words)
def strip_punctuation(x):
        for i in punctuation_chars:
            x = x.replace(i, "")
        return x
def get_neg(sentence):
    no_punc_word = strip_punctuation(sentence)
    split_no_punc_word = no_punc_word.lower().split()
    pos = 0
    #d = []
    for item in split_no_punc_word:
        if item in negative_words:
            pos += 1
            #d.append(item)
    return pos
word = "Hello! i'm shawon"
print("Negative words number are: ", get_neg(word))

# Finally, copy in your previous functions and write code that opens the file project_twitter_data.csv which has the fake generated twitter data (the text of a tweet, the number of retweets of that tweet, and the number of replies to that tweet). Your task is to build a sentiment classifier, which will detect how positive or negative each tweet is. Copy the code from the code windows above, and put that in the top of this code window. Now, you will write code to create a csv file called resulting_data.csv, which contains the Number of Retweets, Number of Replies, Positive Score (which is how many happy words are in the tweet), Negative Score (which is how many angry words are in the tweet), and the Net Score (how positive or negative the text is overall) for each tweet. The file should have those headers in that order. Remember that there is another component to this project. You will upload the csv file to Excel or Google Sheets and produce a graph of the Net Score vs Number of Retweets. Check Coursera for that portion of the assignment, if you’re accessing this textbook from Coursera.


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())
            
def get_pos(sentence):
    no_punc_word = strip_punctuation(sentence)
    split_no_punc_word = no_punc_word.lower().split()
    pos = 0
    for item in split_no_punc_word:
        if item in positive_words:
            pos += 1
    return pos


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def get_neg(sentence):
    no_punc_word = strip_punctuation(sentence)
    split_no_punc_word = no_punc_word.lower().split()
    pos = 0
    for item in split_no_punc_word:
        if item in negative_words:
            pos += 1
    return pos


def strip_punctuation(strWord):
    for charPunct in punctuation_chars:
        strWord = strWord.replace(charPunct, "")
    return strWord


twitter_data = open("project_twitter_data.csv", "r")
result_data = open("resulting_data.csv", "w")
read_twitter_data = twitter_data.read()
print("Negative words number are: ", get_neg(read_twitter_data))
print("Positive words number are: ", get_pos(read_twitter_data))

def writeInResultData(result_data):
    result_data.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
    result_data.write('\n')
    twitteLine = twitter_data.readlines()
    noHeader = twitteLine.pop(0)
    for lines in twitteLine:
        listItem = lines.strip().split(',')
        result_data.write("{},{},{},{},{}".format(listItem[1], listItem[2], get_pos(listItem[0]), get_neg(listItem[0]),(get_pos(listItem[0])-get_neg(listItem[0]))))
        result_data.write("\n")


writeInResultData(result_data)
twitter_data.close()
result_data.close()

