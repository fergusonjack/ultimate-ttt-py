import pytest
from uttt import TicTacToe, MoveOutsideSubBoardError, MoveOutsideMainBoardError

def test_whenInitSizeIsStringThenExceptionRaised():
    with pytest.raises(ValueError):
        TicTacToe("mustFail")

# We only support size 3 boards for now
def test_whenInitSizeNot3ExceptionRaised():
    with pytest.raises(ValueError):
        TicTacToe(4)

    with pytest.raises(ValueError):
        TicTacToe(2)

def test_whenNoInitSizeGivenThenSizeIs3():
    assert TicTacToe()._board_size == 3

def test_whenBoardSize3ThenMainBoardHas3x3SubBoards():
    board = TicTacToe(3)._board
    assert areBoardDimensionXbyX(board, 3) == True

def test_whenBoardSize3ThenAllSubBoardsHave3x3Squares():
    board = TicTacToe(3).board
    #Check that each subboard has 3 rows
    for board_x in range(1, 3):
        for board_y in range(1, 3):
            #This is each board
            sub_board = board[board_x][board_y]
            assert areBoardDimensionXbyX(sub_board, 3) == True

def test_whenBoardSize3Then0x0IsOutOfBounds():
    assert False

def test_whenBoardSize3Then3x3IsInBounds():
    assert False

def whenBoardIsPrettyPrintedThenItIsRenderedCorrectly():
    TicTacToe(3).pretty_print_board()

def areBoardDimensionXbyX(board, x):
    if not len(board) == x:
        return False

    for row in board:
        if not len(row) == x:
            return False

    return True

def test_whenMoveIsOutOfMainBoardBoundsThenExceptionRaised():
    with pytest.raises(MoveOutsideMainBoardError):
        TicTacToe(3).play_square_in_sub_board(1,2,3,4)

def whenMaxMovesExceededThenBoardIsFull():
    assert False

def whenWinnerGetsSetOrBoardIsFullThenBoardIsFinished():
    assert False

def whenBoardIsFullAndMoveAttemptedThenExceptionRaised():
    assert False

def whenRowFilledThenRowCheckReturnsWon():
    assert False

def whenRowNotFilledThenRowCheckReturnsNotWon():
    assert False

def whenColumnFilledThenColumnCheckReturnsWon():
    assert False

def whenColumnNotFilledThenColumnCheckReturnsNotWon():
    assert False

#Do both here?
def whenDiagonalFilledThenDiagonalCheckReturnsWon():
    assert False

def whenDiagonalNotFilledThenDiagonalCheckReturnsNotWon():
    assert False

def whenBoardIsFinishedAndWinnerNotSetThenSetResultToTie():
    assert False