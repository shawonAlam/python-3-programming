# Writing essays for school can be difficult but
# many students find that by researching their topic that they
# have more to say and are better informed. Here are the university
# we require many undergraduate students to take a first year writing requirement
# so that they can
# have a solid foundation for their writing skills. This comes
# in handy for many students.
# Different schools have different requirements, but everyone uses
# writing at some point in their academic career, be it essays, research papers,
# technical write ups, or scripts.

1.	Using the file school_prompt2.txt, find the number of characters in the file and assign that value to the variable num_char.

# solution_1
fileref = open("school_prompt2.txt" , "r")
num = fileref.read()
num_char = len(num)
print(num_char)



# This summer I will be travelling.
# I will go to...
# Italy: Rome
# Greece: Athens
# England: London, Manchester
# France: Paris, Nice, Lyon
# Spain: Madrid, Barcelona, Granada
# Austria: Vienna
# I will probably not even want to come back!
# However, I wonder how I will get by with all the different languages.
# I only know English!

2.	Find the number of lines in the file, travel_plans2.txt, and assign it to the variable num_lines.

# solution_2
fileref = open ("travel_plans2.txt","r")
fileRead = fileref.readlines()
num_lines = len(fileRead)
print(num_lines)


# Sad upset blue down melancholy somber bitter troubled
# Angry mad enraged irate irritable wrathful outraged infuriated
# Happy cheerful content elated joyous delighted lively glad
# Confused disoriented puzzled perplexed dazed befuddled
# Excited eager thrilled delighted
# Scared afraid fearful panicked terrified petrified startled
# Nervous anxious jittery jumpy tense uneasy apprehensive

3.	Create a string called first_forty that is comprised of the first 40 characters of emotion_words2.txt.

# solution_3
fileref = open("emotion_words2.txt", "r")
first_forty = ""
#c = 0
fileRead = fileref.readline()
for line in fileRead[:40]:
    #c += 1
    first_forty += line
    
print(first_forty)
#print(c)
    
