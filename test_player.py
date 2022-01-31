#This module  is collectively tested in the test_game where the water bucket and row and col modification are tested.
#Also since the Player class's display attribute is fixed through out the game. It is not tested.
from player import Player

def test_player():

    testing_player = Player("A")
    """Intial player position at zero test."""
    assert testing_player.row == 0, "Coordiante does not start at zero"
    print("passed")
    assert testing_player.col == 0, "Coordiante does not start at zero"
    print("passed")
    
    """Water bucket update function test."""
    testing_player.mod_num_water_buckets("+")
    assert testing_player.num_water_buckets == 1, "Water bucket did not increase by one"
    print("passed")
    testing_player.mod_num_water_buckets("-")
    assert testing_player.num_water_buckets == 0, "Water bucket did not decrease by one"
    print("passed")
    
    """Input validity test."""
    try :
        testing_player.mod_num_water_buckets("9")
    except Exception as error:
        h = str(error)
        assert h == "Please enter - or + ","Invalid input not detected"
        print("passed")

    """Player move function test."""
    previous = testing_player.row
    testing_player.move("w")
    assert (previous - 1) == testing_player.row, "Did not modify row correctly"
    print("passed")

    previous = testing_player.row
    testing_player.move("s")
    assert (previous + 1) == testing_player.row, "Did not modify row correctly"
    print("passed")

    previous = testing_player.col
    testing_player.move("a")
    assert (previous - 1) == testing_player.col, "Did not modify col correctly"
    print("passed")

    previous = testing_player.col
    testing_player.move("d")
    assert (previous + 1) == testing_player.col, "Did not modify col correctly"
    print("passed")

    previous_coord = (testing_player.row,testing_player.col)
    testing_player.move("e")
    assert previous_coord == (testing_player.row,testing_player.col), "Modified coordinates when waiting turn "
    print("passed")


def run_tests():
    test_player()
run_tests()