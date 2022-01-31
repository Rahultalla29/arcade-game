from game_parser import parse
import cells

def test_parse():
    valid_input = ['**X**\n', '*F W*\n', '*1 1*', '**Y**']
    no_x = ['*****\n', '*F W*\n', '**Y**']
    no_y = ['**X**\n', '*F W*\n', '*****']
    no_matching_teleport = ['**X**\n', '*F1W*\n', '**Y**']
    not_list = "I am a string"
    not_list_of_strings = ["string",0,8,0.44,"string"]
    invalid_letter = ['**X**\n', '*H W*\n', '**Y**']
    
    """Invalid letter in config. test."""
    try:
        parse(invalid_letter)
        
    except ValueError as error:
        assert type(error) == ValueError, "ValueError of invalid letter in input not detected"
        print("passed")

    """Invalid no. of X in config. test."""
    try:
        parse(no_x)
    except ValueError as error:
        assert type(error) == ValueError, "ValueError of no start (X) not detected"
        print("passed")

    """Invalid no. of Y in config. test."""
    try:
        parse(no_y)
    except ValueError as error:
        assert type(error) == ValueError, "ValueError of no End (Y) not detected"
        print("passed")

    """Invalid no. of Teleport in config. test."""
    try:
        parse(no_matching_teleport)
    except ValueError as error:
        assert type(error) == ValueError, "ValueError of no matching teleport pads not detected"
        print("passed")
    
    
    
    try:
        parse(not_list)
    except TypeError as error:
        assert type(error) == TypeError, "TypeError of invalid type of input not detected"
        print("passed")
    
    """Invalid type of inout test."""
    try:
        parse(not_list_of_strings)
    except TypeError as error:
        assert type(error) == TypeError, "TypeError of invalid type of elements in input list not detected"
        print("passed")
    
    """Conversion of cells in config. test."""
    output_from_valid_in  = parse(valid_input)
    
    assert output_from_valid_in[0][0].display == "*" and type(output_from_valid_in[0][0]) == cells.Wall,"Did not convert to Wall cell and incorrect display attribute"
    print("passed")
    assert output_from_valid_in[0][2].display == "X" and type(output_from_valid_in[0][2]) == cells.Start,"Did not convert to Start cell and incorrect display attribute"
    print("passed")
    assert output_from_valid_in[1][1].display == "F" and type(output_from_valid_in[1][1]) == cells.Fire,"Did not convert to Fire cell and incorrect display attribute"
    print("passed")
    assert output_from_valid_in[2][1].display == "1" and type(output_from_valid_in[2][1]) == cells.Teleport,"Did not convert to Teleport cell and incorrect display attribute"
    print("passed")
    assert output_from_valid_in[3][2].display == "Y" and type(output_from_valid_in[3][2]) == cells.End,"Did not convert to End cell and incorrect display attribute"
    print("passed")
    assert output_from_valid_in[1][3].display == "W" and type(output_from_valid_in[1][3]) == cells.Water,"Did not convert to Water cell and incorrect display attribute"
    print("passed")
    
 
def run_tests():
    test_parse()

run_tests()