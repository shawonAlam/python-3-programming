
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