# Set Game
A Python implementation of the Game: Set

## Prerequisite
Python ~= 3.8.10 <br/>
You can download Python using this link: https://www.python.org/downloads/

## Installation
1. Clone the project
```
git clone https://github.com/ACRacusa/set-game.git
```
2. Go to the project directory
```
cd set-game
```
3. Install necessary python packages. Itertools and Random are automatically installed upon installing Python
```
pip install pandas
```
4. Start the Python project
```
python3 setgame.py
```

## Game Rules
1. Start with a deck of cards, each of which has a certain number of shapes, different colors, and shadings
2. Deal out 12 cards and start looking for a **Set**
    - A **Set** is a collection of three cards that have **all the same** or **all different** patterns.
        1. They all have the same number or have three different numbers.
        2. They all have the same shape or have three different shapes.
        3. They all have the same shading or have three different shadings.
        4. They all have the same color or have three different colors.
    - If no Set exists in the drawn cards, deal out three more cards. Repeat until a set occurred.

## Game Mechanics
- There is a total of 81 cards in the deck.
- Each card displays an image with **Four** features:
    - Shape
        - Oval
        - Squiggles
        - Diamonds
    - Color
        - Red
        - Green
        - Purple
    - Number
        - 1
        - 2
        - 3
    - Shading
        - Filled
        - Outlined
        - Striped
- The goal of the game is to collect as many sets as possible until there's no more possible sets in the game table.
