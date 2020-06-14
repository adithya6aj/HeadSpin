
#open the text file in read mode
file = open("text.txt", "r") 
#create an empty dictionary for storing words and count as key value pair
contents = dict() 
  
for line in file: 
    line = line.strip() 
    words = line.split(" ")  
    # Iterate over each word in line 
    for word in words: 
        # Check if the word is already in dictionary 
        if word in contents: 
            # Increment count of word by 1 
            contents[word] = contents[word] + 1
        else: 
            # Add the word to dictionary with count 1 
            contents[word] = 1
  
# Print the contents of dictionary 
for key in list(contents.keys()): 
    print(key, ":", contents[key]) 
                    
        
