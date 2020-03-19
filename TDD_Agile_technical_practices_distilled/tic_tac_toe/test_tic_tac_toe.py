from pathlib import Path
import pytest
import tic_tac_toe

"""
Tic Tac Toe rules
X always goes first.
Players alternate placing X’s and O’s on the board.
Players cannot play on a played position.
A player with three X’s or O’s in a row (horizontally, vertically, diagonally) wins.
If all nine squares are filled and neither player achieves three in a row, the game is a draw.
"""


SCRIPT_NAME = 'tic_tac_toe.py'


def test_tic_tac_toe_exists():
    assert Path(SCRIPT_NAME).is_file()


def test_when_player_selects_a_position_already_used_by_other_player_program_exits():
    input_values = [1, 1]

    def mock_input(s):
        return input_values.pop(0)

    tic_tac_toe.input = mock_input

    try:
        tic_tac_toe.main()
    except tic_tac_toe.PositionAlreadyPlayed:
        pass
    else:
        raise AssertionError("Expected a position not used")


def test_when_player_x_gets_tic_tac_toe_wins(caplog):
    input_values = [1, 4, 2, 5, 3]

    def mock_input(s):
        return input_values.pop(0)

    tic_tac_toe.input = mock_input
    with pytest.raises(SystemExit) as exc:
        tic_tac_toe.main()
        assert 'Player X wins' in caplog.text
        assert exc.value.code == 0


def test_when_player_o_gets_tic_tac_toe_wins(caplog):
    input_values = [1, 4, 2, 5, 7, 6]

    def mock_input(s):
        return input_values.pop(0)

    tic_tac_toe.input = mock_input
    with pytest.raises(SystemExit) as exc:
        tic_tac_toe.main()
        assert 'Player O wins' in caplog.text
        assert exc.value.code == 0
