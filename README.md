# Python-Naval-Battle
A simple Naval Battle game made in python
Sure! Here's the translation of the entire text into English:

## 1. Introduction
Currently, one of the industries that generates the most revenue worldwide is the gaming industry, which plays a significant role in spreading technology innovations, both in hardware and software. Taking this into account, Blizzard Entertainment, one of the largest game publishers and developers, earning over 8 billion dollars annually, contacted the best software development team in Bahia, the MI Algoritmos class from the Universidade Estadual de Feira de Santana (UEFS), to create an innovative and accessible Battleship game with the following features:

- Game boards with a size of 10x10
- Each player will have 6 ships:
  - 1 large
  - 2 medium
  - 3 small
- Each player will take one shot per round, and for each hit, they will get an extra shot
- All shots, whether hits or misses, will be marked on the second board
- The first player will be the computer, and the location of its ships (on the first board) and its shots on the opponent's ships (on the second board) will be randomly generated
- The second player will use the keyboard to indicate the location of their ships (on the first board) at the beginning of the game and their shots on the opponent's ships (on the second board) in each round
- The game will end when one of the players manages to sink all of their opponent's ships
- At the beginning and end of each round, both boards will be presented to the players

The MI Algoritmos team successfully developed a 100% functional and accessible application that fulfills all the requirements provided by Blizzard Entertainment. The game provides freedom and ease of use for users to position and orient their ships, as well as to fire shots within their chosen area on the board. The graphical interface is designed for user understanding, with messages tailored to enhance the overall user experience.

## 2. Methodology
The MI Algoritmos class split into groups to find the best approach for the functionality of the program. Each member of the team worked separately on their code, but the functionalities were very similar. Throughout the sessions, we decided on the methods that would yield the best performance for the application. Initially, we researched concepts of modularization and functions, and we decided to use the 'Random' library to configure how the Bot would play, mainly using 'Randint,' and we also discussed the use of 'Choice' for selecting the Bot's orientation. We even considered using the "Time" library with the 'Sleep' option for the Bot to make its moves at a steady pace.

Next, we defined the necessary functions for the application's functionality, and we concluded with the main functions listed in the table below:

| Function                          | Description                                                                             |
|-----------------------------------|-----------------------------------------------------------------------------------------|
| Create Board                      | Function to create the game board                                                     |
| Display Board                    | Function to display the game board                                                    |
| Place Ships (Player and Computer) | Function to position the ships on the board, either by player input or randomly by the computer |
| Formation of Main Matrices       | Function to form the main matrices (one for the computer and one for the player)       |
| Ship Placement (Graphics)        | Function to visually display the ships on the board                                    |
| Shoot Function                   | Function to handle the shots and their results                                         |
| Game End Check                   | Function to check if the game has ended                                               |
| Main Function (optional)         | Main function to manage the game flow                                                 |

We then implemented these necessary functions for the application, using them as listed in the table above. In the sessions, we also discussed the concept of a Ghost Matrix for the computer's board, which would hide the positions of its ships. However, due to time constraints and unexpected issues with my code and computer, I didn't implement this Ghost Matrix, especially since it was not required in the topics listed in the Introduction.

## 3. Results and Discussions
### 3.1 Results
In this section, I will provide detailed explanations of all the solutions and results. However, for better understanding, I will divide the discussions into different topics.

#### 3.1.1 How to Use the Program
Upon starting the application, the user will see the game board already formatted, prompting them to position the large ship (4x1 or 1x4). The user is asked to enter the row [1-10], followed by the column [1-10], and lastly, the orientation [Vertical or Horizontal], as shown in the image below:


In this input, the large ship is positioned, and the process continues until all ships are placed on the board. If there is any overlap or if a ship goes beyond the board's boundaries, the code will prompt an error message and ask the user to enter a valid position. Once all the ships are placed, the game will begin, and the computer will make a random shot on the player's board. Afterward, the player's board and the computer's board will be displayed, showing the player's ship locations and the shots fired by the computer. The user will then have the option to fire a shot at a chosen coordinate, and messages will indicate whether it's a hit, miss, or if an extra shot is available. The game will continue in this loop until one of the players sinks all of the opponent's ships. The game will then announce the winner.

#### 3.1.2 How the Program Functions
Each function contains a complex system of conditions to be fulfilled. The system begins with the creation of a 10x10 matrix, which is then formatted correctly for

 better visualization. Instead of using a dictionary of letters for numbers, the code uses rows and columns with numbers from 1 to 10 for simplicity. However, there were some dictionaries used in the program, such as the 'Key-Lock' dictionary for ship sizes: 'Large': 4, 'Medium': 3, 'Small': 2. This allows for easy manipulation of ship sizes in the subsequent functions. 

Next, there are functions for placing the player's and computer's ships. The placement function is divided into three parts: a general function for placing ships, a function for the player to choose the position and orientation, and another for randomly placing the computer's ships. The placement function handles the positioning of the ships, using the primary placement function and position function to ensure that no ship goes beyond the boundaries of the board and that there is no overlap. The display board function is also used to update the board according to the 6 ships being placed.

The player's shooting function is then configured to eliminate the computer's ships, which is necessary for victory in the game. The main function, 'battleship()', calls all the other functions, organizes the boards, determines the order of play (always starting with the computer), and includes specific logic such as the extra shot. This function displays hits, misses, and both boards, as well as checking the necessary conditions for the game to end only when one side emerges victorious.

### 3.1.3 Errors and Tests
Due to the large number of functions and substantial code revisions in a short amount of time, there were various errors, particularly in ship placement. Issues included infinite loops with incorrect positions and logic mismatches in several parts of the code. One error I encountered was the improper formation of the computer's board, which occasionally failed to register shots correctly at specific coordinates. Due to the time constraints, I decided to remove the implementation of the ghost matrix, and thus the computer's board was fully formed, resulting in efficient tracking of shots. Another error involved the rows being identified as numbers rather than letters. Due to time limitations, I decided to keep the coordinates as numbers rather than letters.

## 4. Conclusion
In conclusion, the project successfully adhered to the requirements and objectives proposed by the problem statement. Although the game may not be the most exciting in isolation due to the visibility of the computer's board, it fulfills the specified requirements and operates as intended. The report also provides suggestions for future improvements, such as implementing the Ghost Matrix for the computer's board to enhance the player's experience and changing the row indices to letters (A to J) for a more authentic Battleship game feel. Additionally, a better format for the boards and text can be considered to avoid confusion.

Overall, the Battleship game project showcases functional and accessible gameplay while following the outlined requirements.
