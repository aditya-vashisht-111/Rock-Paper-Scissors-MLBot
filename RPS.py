# The strategy uses a dictionary to track the frequency of patterns
# We store 'play_order' in the default argument to persist state without global variables
def player(prev_play, opponent_history=[], play_order={}):
    
    # 1. Handle the start of a match
    # If prev_play is empty, it's the first game against a new bot.
    # We reset our memory so previous bots don't confuse the new game.
    if not prev_play:
        prev_play = 'R'
        opponent_history.clear()
        play_order.clear()

    # 2. Update History
    opponent_history.append(prev_play)
    
    # 3. N-Gram Logic (Look back 5 moves)
    prediction = 'P' # Default fallback prediction

    # We need at least 5 moves to start building the pattern 'key'
    if len(opponent_history) > 4:
        # Take the last 5 moves and add them to our dictionary of patterns
        last_five = "".join(opponent_history[-5:])
        
        if last_five in play_order:
            play_order[last_five] += 1
        else:
            play_order[last_five] = 1
        
        # Now, let's predict the NEXT move based on the immediate last 4 moves
        potential_plays = [
            "".join(opponent_history[-4:]) + "R",
            "".join(opponent_history[-4:]) + "P",
            "".join(opponent_history[-4:]) + "S",
        ]

        # Find which of these potential next patterns has occurred most often in the past
        sub_order = {
            k: play_order.get(k, 0)
            for k in potential_plays
        }

        # The prediction is the last character of the most frequent pattern
        prediction = max(sub_order, key=sub_order.get)[-1:]

    # 4. Return the counter move
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]