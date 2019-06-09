# Program 1
# Read weights (lbs.) of Nstudents into a list and convert these weights to kilograms in a separate list using
# loops and list
Lbs = []
Kgs = []
n = int(input("Enter the number of students:"))
for i in range(n):
    num = int(input('Enter the value to be inserted:'))
    Lbs.append(num)
    kilograms = num * 0.454
    Kgs.append(kilograms)
    
print("Weights in Lbs") 
print("*" * 50)
print(Lbs)
print("*" * 50)

print("Weights in Kgs") 
print("#" * 50)
print(Kgs)
print("#" * 50)
      


# Program 2
# Return every other char of a given string starting with first using a function named “string_alternative
def string_alternative(input):
    return input[::2]


word = input("Enter the word:")
output = string_alternative(word)
print(output)    


# Program 3
# find the wordcountin a file for each line and thenprint the output.Finally store the output back to the file
fileName = input("Enter the name of file:")
word_frequency = {}

file = open(fileName, 'r')                              # Opening the file
text_string = file.read().lower()                       # Reading the contents of the file
des = text_string.strip("!()-[]{};:'\,<>./?@#$%^&*_~ ")
desired = des.split(" ")                                # Splitting the words using Space

for word in desired:                                    # Counting the occuring of each word
    count = word_frequency.get(word, 0)
    word_frequency[word] = count + 1

frequency_list = word_frequency.keys()                  # Creating a list of words and their count

for words in frequency_list:
    print(words, word_frequency[words])