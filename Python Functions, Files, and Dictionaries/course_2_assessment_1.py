1.The textfile, travel_plans.txt, contains the summer travel plans for someone with some commentary. Find the total number of characters in the file and save to the variable num.


fileref = open("travel_plans.txt","r")
fileRead = fileref.read()
num = len(fileRead) 
print(num)


2.We have provided a file called emotion_words.txt that contains lines of words that describe emotions. Find the total number of words in the file and assign this value to the variable num_words.

fileref = open("emotion_words.txt","r")
fileRead = fileref.readlines()
num_words = 0
for line in fileRead:
    for word in line.split():
        num_words += 1
print(num_words)
fileref.close()

      
3.Assign to the variable num_lines the number of lines in the file school_prompt.txt.

fileref = open("school_prompt.txt","r")
fileRead = fileref.readlines()
num_lines = 0
num_lines += len(fileRead)
print(num_lines)
fileref.close()

4.Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

fileref = open("school_prompt.txt","r")
fileread = fileref.read()
beginning_chars = ""
for c in fileread[0:30]:
    beginning_chars += c
print(beginning_chars)
    


5.Challenge: Using the file school_prompt.txt, assign the third word of every line to a list called three.

fileref = open("school_prompt.txt","r")
fileRead = fileref.readlines()
three = []
for line in fileRead:
    line = line.strip().split()
    three.append(line[3-1])
print(three)
    
6.Challenge: Create a list called emotions that contains the first word of every line in emotion_words.txt.


fileref = open("emotion_words.txt","r")
fileRead = fileref.readlines()
emotions = []
for line in fileRead:
    line = line.strip().split()
    emotions.append(line[1-1])
print(emotions)
    


7.Assign the first 33 characters from the textfile, travel_plans.txt to the variable first_chars.

fileref = open ("travel_plans.txt", "r")
fileRead = fileref.read()

first_chars = ""
for c in fileRead[0:33]:
    first_chars += c
print(first_chars)

8.Challenge: Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.


fileref = open("school_prompt.txt","r")
fileRead = fileref.readlines()

p_words = []
for line in fileRead:
    line = line.strip().split()
    for word in line:
        for alf in word:
            if alf == "p":
                p_words.append(word)
                break
print(p_words)

9.

      

      
