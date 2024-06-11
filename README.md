# Flappybird-Game-
Implementaion of the game Flappy Bird using PyGame. 
The game has two options the manual mode: where the user can play and the game and an AI mode where the user can watch a neural network train to play the game. 
For the AI mode a neural network is used to control weather a bird should jump or not where the neural network has three inputs, 1 hidden layer with 5 neurons and a single output to tell the bird to jump or not. 
The three inputs are:
- the horzontial distance from the bird's center to the center of the gap between the pipes, so the bird times when exactly to jump
- vertical distance from the bird's center to the center of the gap between the pipes so the birds decides weather to jump or not
- vertical distance from the bird's center to the coin within the gap between pipes which helps the bird decide weather to risk getting the coin or ignoring it if getting the coin comes with risk of crashing with the pipe.

A genetic algorithm is applied where after all birds die , their fitness scores get evaluated and the birds with highest fitness get to breed and pass their neural net weights to their offspring . Some of the other birds with lower fitness get discarded while others have mutations introduced to their weights to increase exploration for a better neural net. 
