from grid import grid_to_string
from game_parser import parse
from player import Player
def test_grid():
    
    testing_grid = parse(['**X**\n', '*F W*\n', '*1 1*', '**Y**'])
    testing_player = Player("A")
    """Player position set test."""
    testing_player.row = 0
    testing_player.col = 2
    assert grid_to_string(testing_grid,testing_player) == ('**A**\n*F W*\n*1 1*\n**Y**'+ "\n\nYou have 0 water buckets."),"Player position did not change to Start"
    print("passed")

    """Water bucket update test."""
    testing_player.row = 1
    testing_player.col = 3
    grid_to_string(testing_grid,testing_player)
    assert testing_player.num_water_buckets == 1,"Did not add water bucket when player on Water cell"
    print("passed")
    
    
    testing_player.row = 1
    testing_player.col = 1
    grid_to_string(testing_grid,testing_player)
    
    assert testing_player.num_water_buckets == 0,"Did not subtract water bucket when player on Fire cell"
    print("passed")


    """Remaining teleport functionality and win/loose tested in game as it handles the steps taken by player -
    and makes changes as required to game_board attribute hence more meaningful to handle teleports in game.py."""


def run_tests():
    test_grid()

run_tests()

