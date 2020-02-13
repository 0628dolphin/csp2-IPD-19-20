####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E2'
strategy_name = 'BBC'
strategy_description = 'Collude every 3rd turn, and betray on the other turns'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    #On the first turn they should always betray
    if len(my_history) == 0:
        return 'b'

    #On every 3rd turn they should try and collude
    elif len(my_history)%3 == 0:
      return 'c'

    #All other turns they should betray
    else:
        return 'b'
    