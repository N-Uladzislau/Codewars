'''
"scissors", "paper" --> "Player 1 won!"
"scissors", "rock" --> "Player 2 won!"
"paper", "paper" --> "Draw!"
'''
# Let's play! You have to return which player won! In case of a draw return Draw!.
rules = [
    [0, 2, 1],
    [1, 0, 2],
    [2, 1, 0]
]
index = {
    'scissors': 0,
    "paper": 1,
    'rock': 2  
}
actions = ['scissors', "paper", "rock"]
def rps(p1, p2):
    p1i = actions.index(p2)
    p2i = actions.index(p1)
    winner = rules[p1i][p2i]
    if winner == 0:
        return "Draw!"
    return f"Player {winner} won!"

def rps1(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return "Player 1 won!"
    if beats[p2] == p1:
        return "Player 2 won!"
    return "Draw!"