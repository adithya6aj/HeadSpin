# HeadSpin
HeadSpin Assignment



1. 5x5 Soduku Solution Checking

- **Platforms used**

- Windows 10
- Python 3.6.8
- No extra packages required

- **To run the program**

- Open cmd and locate to the program root directory
- Run: python sudoku.py
- Input the elements of sudoku one by one followed by hitting Enter after each entry till it displays the complete 5x5 sudoku

- **How does the algorithm works**

- First it checks for the sum in each row if found that any of the rows doesn&#39;t satisfy the condition of being sum equals to 15 it     breaks the loop and return False.
- If the above step goes fine, it then checks for the same condition of the sum equals 15 but for column.
- After verifying the sum, the program then checks whether there is any repeating element along the rows. The same procedure does for a   column if there is no repetition along the rows.
- What is here to notice is that the program goes to the subsequent steps only if the just previous step is satisfied, otherwise the       program exits and returns False.
- If every step goes fine, then the program returns True ensuring that the 5x5 sudoku solution is a valid one.

2. Addition of element to the nth position

- **Platforms used**

- Windows 10
- Python 3.6.8

- **To run the program**

- Open cmd and locate to the program root directory
- Run: python element\_add.py
- First it asks for the position, so give the visible position of the list to which the new element has to be inserted
- When it asks for the element give the inserting element

- **How does the algorithm works**

- The program works with the basic idea of python list slicing
- First it checks whether user input position is beyond the list range or not, if yes, it displays a warning information
- Else, It creates two halves of the list, the first half consisting of the elements before the position and the second half with the     elements after the position
- After that program adds the element to the last position of the first half and then combine with the second half to generate a new       output list
- Output is a print function which displays the new list

3. Count the occurrence of words inside a text file

- **Platforms used**

- Windows 10
- Python 3.6.8

- **To run the program**

- Open cmd and locate to the program root directory
- Run: python count\_words.py
- Ensure that the text file is in the program root directory itself, if not, give the entire path of the text file

- **How does the algorithm works**

- First it segregates each word by separating the lines followed by space
- If uses a dictionary for storing the word and the number of its occurrence inside the file as key-value pair
- For each repetition of a specific word rather it increments the number of occurrences associated with it
- The output is a print function which displays each word and its number of occurrences
