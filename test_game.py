from game import Game
from player import Player

def test_game():
    # testing grid :
    # **A**
    # *F W*
    # *1 1*
    # **Y**

    filename = "board_simple.txt"
    testing_player = Player("A")
    testing_game = Game(filename)
    
    """Does initial_player_position function set player position to start cell."""
    assert Game.initial_player_position(filename,testing_player) == ('**A**\n*F W*\n*1 1*\n**Y**'+ "\n\nYou have 0 water buckets."),"Did not set player position to start at X"
    print("passed")

    """Does it count invalid moves as part of moves."""
    Game.initial_player_position(filename,testing_player)
    testing_game.game_move(testing_player,"d")
    assert testing_game.num_of_moves == None, "Counted bumping into wall as move"
    print("passed")

    """Does get_grid function output grid from previous move."""
    testing_player.row = 1
    testing_player.col = 2
    assert testing_game.get_grid(testing_player) == ('**X**\n*FAW*\n*1 1*\n**Y**'+ "\n\nYou have 0 water buckets."),"Did not get grid from previous move"
    print('passed')
    
    Game.initial_player_position(filename,testing_player) # resetting testing_player position to X (start)
    assert testing_game.game_move(testing_player,"s") == ('**X**\n*FAW*\n*1 1*\n**Y**'+ "\n\nYou have 0 water buckets."),"Did not move player down one step"
    print("passed")

    """To check if stepping on teleport pad changes player position as expected."""
    testing_game.game_move(testing_player,"s")
    testing_game.game_move(testing_player,"d")
    assert testing_player.row == 2 and testing_player.col == 1,"Did not teleport player to matching pad"
    print("passed")
    
    """To check if stepping on end cell changes game state to False to end game in run.py."""
    testing_game.game_move(testing_player,"d")
    testing_game.game_move(testing_player,"s")
    assert testing_game.game_state == False,"Did not detect player has reached end cell Y"
    print("passed")
    
    Game.initial_player_position(filename,testing_player) # resetting testing_player position to X (start)
    
    """To check if stepping on fire cell without water buckets changes game state to False to end game in run.py."""
    testing_game.game_move(testing_player,"s")
    testing_game.game_move(testing_player,"a")
    assert testing_game.game_state == False,"Did not detect player has stepped on Fire cell without water bucket"
    print("passed")
    
    

def run_tests():
    test_game()
run_tests()