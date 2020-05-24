# Sad upset blue down melancholy somber bitter troubled
# Angry mad enraged irate irritable wrathful outraged infuriated
# Happy cheerful content elated joyous delighted lively glad
# Confused disoriented puzzled perplexed dazed befuddled
# Excited eager thrilled delighted
# Scared afraid fearful panicked terrified petrified startled
# Nervous anxious jittery jumpy tense uneasy apprehensive

1.Write code to find out how many lines are in the file emotion_words.txt as shown above. Save this value to the variable num_lines. Do not use the len method.

# solution_1
fileref = open("emotion_words.txt","r")
p = fileref.readlines()
num_lines = 0
for line in p:
    num_lines += 1
    #print(line.strip())
print(num_lines)
fileref.close()
