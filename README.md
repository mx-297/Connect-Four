# Connect-Four-with-MiniMax-and-Genetic-Algorithm

# Project Description

In this project, I have developed a connect four game with two players. One player is the user of the game, and the other is an AI engine which can anticipate the future moves of the player to play the best optimized move in the game. The idea behind this engine is two algorithms called minimax and genetic algorithm. Minimax is responsible for anticipating the moves of the player and minimizing their scores, then, based on that, it maximizes the move of the AI to play the best move. The role of genetic algorithm is to optimize the scores upon which the minimax algorithm decides its next move. I have developed the game framework using Pygame, a python framework for games. Also, I have used NumPy to deal with multidimensional arrays in a friendly way.

# Project Steps

  * The project was mainly divided into four main steps:
    
    * The game interface was designed by using pygame. (See screenshots below)
    
    * The Evaluation_State algorithm was implemented as follows:
    
      * Since this is a connect four game, we only have four states of the board for each player: 1-sequence, 2-sequence, 3-sequqence, and 4-sequence. For example, in          the screenshot below, this is a 3-sequence.
      <p align="center">
         <img src="https://user-images.githubusercontent.com/106694589/219944218-149df9ff-2b73-4ca2-a818-b3a0ad8f4c04.png" alt="Screenshot 2023-02-19 130905">
      </p>

      
      * Each of these sequences has a weight or a score assigned to it. This score or weight helps the mini-max algorithm to decide which move is the best to make.
      * Intuitavely, The 4-seuqence weight should be the greatest weight as it is the win-sequence for a connect-four game. 
      * Other than a 4-sequence, the function calculates a state's score by totaling the number of 1-, 2-, and 3-sequences for each participant.
      * Once these counts have been established, evalState calculates a state's score by deducting the opponent's count from the player it is assessing and putting             those values together
    
    * The Mini-Max Algorithm:
      
      * The minimax method is fundamentally applicable to any one-on-one strategic gaming scenario. 
      * The algorithm's initial stage is shown in the diagram below. It is assumed that Player X is taking the turn in a game involving only two players, Player X and         Player Y.
      <p align="center">
         <img src="https://user-images.githubusercontent.com/106694589/219944532-6b21d164-556e-4a4b-b504-19796a8112bc.png" alt="Screenshot 2023-02-19 131559">
      </p>
      
      * The Connect Four board's current state is first ingested by the algorithm. Then, it stretches out the following seven states, with each child of the current           state representing a move made by Player X into a specific column of the Connect Four board. Then, after traversing each node in Level 1, seven children are           formed for each node to represent Player Y's seven possible moves, and so on untill it reaches a terminal state (winning state or depth of the tree).
      * When a terminal state is reached, The algorithm will then start to move upwards through the tree, invoking our “Evaluation_State” function on each node to get         a score. The algorithm will select the option with the lowest score at each level, which represents Player Y's. The method chooses the action that                     "Evaluation_State" rates as the best, meaning it has the highest score out of the collection of seven options, at each level that corresponds to Player X in           order to maximize our score. 
      
    * The Genetic Algorithm:
      
      * The "Evaluation_State" function calculates a state's score by and weighing various n-sequences for each component as mentioned above.
      * These weights will be calculated optimally by a genetic algorithm instead of intuition.
      * Each player will be represented by a vector of weights representing each of the 1,2,3 sequences respectively.
      * Techniques to control those players will be devised once the fundamental concept of a player had been established in order to broaden the search for the               optimum possible collection of weight such as cross-over and mutation.
      * A cross-over strategy involves taking two players and changing some of their values. The following cross-over would then take place as illustrated in the               screenshot below:
      <p align="center">
         <img src="https://user-images.githubusercontent.com/106694589/219945136-170e60a8-14dd-4035-a8b7-985b9f2fcba6.png" alt="Screenshot 2023-02-19 132953">
      </p>
      
      * A mutation is a method which will pick one of the three weights for the player and swap it out with a random number as shown below:
      
      <p align="center">
         <img src="https://user-images.githubusercontent.com/106694589/219945237-8bce9812-6854-4a83-9e8c-daf86d1bed63.png" alt="Screenshot 2023-02-19 133225">
      </p>


* Screenshots for the game:

<p align="center">
         <img src="https://user-images.githubusercontent.com/106694589/219945376-adc3db94-58ca-4fb4-a00d-08b3f9b9cb34.png" alt="Picture1">
      </p>

      
    
      

      

