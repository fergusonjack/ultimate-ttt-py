import random

from engine import MainBoardCoords, SubBoardCoords, SubBoard, Player
from players.stdout import StdOutPlayer


class Random(StdOutPlayer):
    def __init__(self):
        super().__init__()

    def get_my_move(self):  # -> Tuple[MainBoardCoords, SubBoardCoords]
        main_board_coords = self.pick_next_main_board_coords()
        sub_board = self.main_board.get_sub_board(main_board_coords)
        sub_board_coords = self.nextCoord(sub_board)
        return main_board_coords, sub_board_coords

    def pick_next_main_board_coords(self) -> MainBoardCoords:
        if self.main_board.sub_board_next_player_must_play is None:
            return random.choice(self.main_board.get_playable_coords())
        else:
            return self.main_board.sub_board_next_player_must_play

    @staticmethod
    def pick_random_sub_board_coords(sub_board: SubBoard) -> SubBoardCoords:
        return random.choice(sub_board.get_playable_coords())

    def nextCoord(self, sub_board : SubBoard):
        arr = [[-9999 for x in range(3)]for y in range(3)]
        for x in range(0 , len(sub_board.get_playable_coords())):
            arr[(sub_board.get_playable_coords()[x]).row][(sub_board.get_playable_coords()[x]).col] = self.subBoardHeuristic(sub_board, sub_board.get_playable_coords()[x])
        #print(self.main_board)
        #print(sub_board)
        #print(arr)
        #print("----------------")
        return self.getMaxValue(arr)


    def getMaxValue(self, arr):
        maxCoord = SubBoardCoords(0,0)
        maxValue = -9999

        for x in range(3):
            for y in range(3):
                if (arr[x][y] > maxValue):
                    maxCoord = SubBoardCoords(x,y)
                    maxValue = arr[x][y]

        return maxCoord

    def subBoardHeuristic(self, sub_board: SubBoard, coords):
        count = 0

        tmpBoardMe = sub_board.add_my_move(coords)

        #if the move wins me the small board -> +1
        if tmpBoardMe.is_finished:
            if tmpBoardMe.winner == Player.ME:
                count += 1

        if tmpBoardMe.is_finished and tmpBoardMe.winner == Player.OPPONENT:
            count -= 1


        if tmpBoardMe.is_finished and self.winnableBy(tmpBoardMe) == Player.OPPONENT:
            count -= 1

        if self.winnableBy(self.main_board.get_sub_board(MainBoardCoords(coords.row, coords.col))) == Player.OPPONENT:
            count -= 1

        if self.winnableBy(self.main_board.get_sub_board(MainBoardCoords(coords.row, coords.col))) == Player.ME:
            count += 1

        tmpBoardOp = sub_board.add_opponent_move(coords)
        if tmpBoardOp.is_finished and tmpBoardOp.winner == Player.OPPONENT:
            count += 1

        return count


    def winnableBy(self, subBoard : SubBoard):
        #print(subBoard)
        playable = subBoard.get_playable_coords()
        for x in range(0, len(subBoard.get_playable_coords())):
            tmpBoard = subBoard.add_opponent_move(SubBoardCoords(playable[x].row, playable[x].col))
            if tmpBoard.is_finished:
                if tmpBoard.winner == Player.ME or tmpBoard.winner == Player.OPPONENT:
                    #print(tmpBoard.winner)
                    return tmpBoard.winner
        for x in range(0, len(subBoard.get_playable_coords())):
            tmpBoard = subBoard.add_my_move(SubBoardCoords(playable[x].row, playable[x].col))
            if tmpBoard.is_finished:
                if tmpBoard.winner == Player.ME or tmpBoard.winner == Player.OPPONENT:
                    #print(tmpBoard.winner)
                    return tmpBoard.winner
        return 0

    #def checkOpWin(self, subBoard: SubBoard):
