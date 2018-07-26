class ChessBoard:

    chess_pos = {}
    chess_select = {}
    board = []

    @classmethod
    def init(cls):
        for number1 in range(9):
            cls.board.append([])
            for number2 in range(10):
                cls.board[number1].append(number2)
                cls.chess_pos[(number1, number2)] = (160 + number1 * 40, 60 + number2 * 40)
                cls.chess_select[(160 + number1 * 40, 60 + number2 * 40)] = (number1, number2)

    @staticmethod
    def change_position(pos_x, pos_y):
        if 120 <= pos_x <= 520 and 20 <= pos_y <= 460:
            pos_x = round((pos_x - 160) / 40) * 40 + 160
            pos_y = round((pos_y - 60) / 40) * 40 + 60
        return pos_x, pos_y


if __name__ == '__main__':
    ChessBoard.init()
    print(ChessBoard.board)
    print(ChessBoard.chess_pos[0, 0])
    print(ChessBoard.board)



