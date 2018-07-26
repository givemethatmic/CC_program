# coding = utf-8


def auto_range(x, y):
    if x >= y:
        return range(y + 1, x)
    else:
        return range(x + 1, y)


class Pao:
    name = 'Pao'

    @classmethod
    def move(cls, get_pos_x, get_pos_y, board):
        if cls.pos_x == get_pos_x:
            for a in auto_range(cls.pos_y, get_pos_y):
                if type(board[get_pos_x][a]).__name__ == 'type':
                    if type(board[get_pos_x][get_pos_y]).__name__ == 'type':
                        cls.pos_y = get_pos_y
                        break
                    else:
                        return True
            cls.pos_y = get_pos_y
        elif cls.pos_y == get_pos_y:
            for a in auto_range(cls.pos_x, get_pos_x):
                if type(board[a][get_pos_y]).__name__ == 'type':
                    if type(board[get_pos_x][get_pos_y]).__name__ == 'type':
                        cls.pos_x = get_pos_x
                        break
                    else:
                        return True
            cls.pos_x = get_pos_x
        else:
            return True


class JuRed1:
    pos_x = 0
    pos_y = 0
    name = 'Ju'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, get_pos_x, get_pos_y, board):
        if cls.pos_x == get_pos_x:
            for a in auto_range(cls.pos_y, get_pos_y):
                if type(board[get_pos_x][a]).__name__ == 'type':
                    return True
            cls.pos_y = get_pos_y
        elif cls.pos_y == get_pos_y:
                for a in auto_range(cls.pos_x, get_pos_x):
                    if type(board[a][get_pos_y]).__name__ == 'type':
                        return True
                cls.pos_x = get_pos_x
        else:
            return True


class JuRed2:
    pos_x = 8
    pos_y = 0
    name = 'Ju'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, get_pos_x, get_pos_y, board):
        if cls.pos_x == get_pos_x:
            for a in auto_range(cls.pos_y, get_pos_y):
                if type(board[get_pos_x][a]).__name__ == 'type':
                    return True
            cls.pos_y = get_pos_y
        elif cls.pos_y == get_pos_y:
                for a in auto_range(cls.pos_x, get_pos_x):
                    if type(board[a][get_pos_y]).__name__ == 'type':
                        return True
                cls.pos_x = get_pos_x
        else:
            return True


class MaRed1:
    pos_x = 1
    pos_y = 0
    name = 'Ma'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class MaRed2:
    pos_x = 7
    pos_y = 0
    name = 'Ma'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class XiangRed1:
    pos_x = 2
    pos_y = 0
    name = 'Xng'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class XiangRed2:
    pos_x = 6
    pos_y = 0
    name = 'Xng'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class ShiRed1:
    pos_x = 3
    pos_y = 0
    name = 'Shi'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if 3 <= x <= 5 and 0 <= y <= 2:
            if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
                cls.pos_x = x
                cls.pos_y = y
            else:
                return True
        else:
            return True


class ShiRed2:
    pos_x = 5
    pos_y = 0
    name = 'Shi'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if 3 <= x <= 5 and 0 <= y <= 2:
            if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
                cls.pos_x = x
                cls.pos_y = y
            else:
                return True
        else:
            return True


class BingRed:
    name = 'bng'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if cls.pos_y <= 4:
            if x == cls.pos_x and y == cls.pos_y + 1:
                cls.pos_y = y
            else:
                return True
        else:
            if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and y == cls.pos_y:
                cls.pos_x = x
            elif x == cls.pos_x and y == cls.pos_y + 1:
                cls.pos_y = y
            else:
                return True


class BingRed1(BingRed):
    pos_x = 0
    pos_y = 3


class BingRed2(BingRed):
    pos_x = 2
    pos_y = 3


class BingRed3(BingRed):
    pos_x = 4
    pos_y = 3


class BingRed4(BingRed):
    pos_x = 6
    pos_y = 3


class BingRed5(BingRed):
    pos_x = 8
    pos_y = 3


class Jiang:
    pos_x = 4
    pos_y = 0
    name = 'Jag'
    color = 'red'
    colorRGB = (255, 0, 0)

    @classmethod
    def move(cls, x, y, board):
        if 3 <= x <= 5 and 0 <= y <= 2:
            if x == cls.pos_x and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
                cls.pos_y = y
            elif y == cls.pos_y and (x == cls.pos_x + 1 or x == cls.pos_x - 1):
                cls.pos_x = x
            else:
                return True
        else:
            return True


class PaoRed1(Pao):
    pos_x = 1
    pos_y = 2
    color = 'red'
    colorRGB = (255, 0, 0)


class PaoRed2(Pao):
    pos_x = 7
    pos_y = 2
    color = 'red'
    colorRGB = (255, 0, 0)


class PaoGreen1(Pao):
    pos_x = 1
    pos_y = 7
    color = 'green'
    colorRGB = (0, 255, 0)


class PaoGreen2(Pao):
    pos_x = 7
    pos_y = 7
    color = 'green'
    colorRGB = (0, 255, 0)


class JuGreen1:
    pos_x = 0
    pos_y = 9
    name = 'Ju'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, get_pos_x, get_pos_y, board):
        if cls.pos_x == get_pos_x:
            for a in auto_range(cls.pos_y, get_pos_y):
                if type(board[get_pos_x][a]).__name__ == 'type':
                    return True
            cls.pos_y = get_pos_y
        elif cls.pos_y == get_pos_y:
                for a in auto_range(cls.pos_x, get_pos_x):
                    if type(board[a][get_pos_y]).__name__ == 'type':
                        return True
                cls.pos_x = get_pos_x
        else:
            return True


class JuGreen2:
    pos_x = 8
    pos_y = 9
    name = 'Ju'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, get_pos_x, get_pos_y, board):
        if cls.pos_x == get_pos_x:
            for a in auto_range(cls.pos_y, get_pos_y):
                if type(board[get_pos_x][a]).__name__ == 'type':
                    return True
            cls.pos_y = get_pos_y
        elif cls.pos_y == get_pos_y:
                for a in auto_range(cls.pos_x, get_pos_x):
                    if type(board[a][get_pos_y]).__name__ == 'type':
                        return True
                cls.pos_x = get_pos_x
        else:
            return True


class Ma:
    name = 'Ma'

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
            judge_x = int(round((x - cls.pos_x) / 2) + cls.pos_x)
            judge_y = int(round((y - cls.pos_y) / 2) + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class MaGreen1(Ma):
    pos_x = 1
    pos_y = 9
    color = 'green'
    colorRGB = (0, 255, 0)


class MaGreen2(Ma):
    pos_x = 7
    pos_y = 9
    color = 'green'
    colorRGB = (0, 255, 0)


class BingGreen:
    name = 'Zu'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, x, y, board):
        if cls.pos_y >= 5:
            if x == cls.pos_x and y == cls.pos_y - 1:
                cls.pos_y = y
            else:
                return True
        else:
            if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and y == cls.pos_y:
                cls.pos_x = x
            elif x == cls.pos_x and y == cls.pos_y - 1:
                cls.pos_y = y
            else:
                return True


class BingGreen1(BingGreen):
    pos_x = 0
    pos_y = 6


class BingGreen2(BingGreen):
    pos_x = 2
    pos_y = 6


class BingGreen3(BingGreen):
    pos_x = 4
    pos_y = 6


class BingGreen4(BingGreen):
    pos_x = 6
    pos_y = 6


class BingGreen5(BingGreen):
    pos_x = 8
    pos_y = 6


class XngGreen:
    name = 'Xng'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, x, y, board):
        if (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        elif (x == cls.pos_x + 2 or x == cls.pos_x - 2) and (y == cls.pos_y + 2 or y == cls.pos_y - 2):
            judge_x = int((x - cls.pos_x) / 2 + cls.pos_x)
            judge_y = int((y - cls.pos_y) / 2 + cls.pos_y)
            if type(board[judge_x][judge_y]).__name__ == 'type':
                return True
            cls.pos_x = x
            cls.pos_y = y
        else:
            return True


class XanGreen1(XngGreen):
    pos_x = 2
    pos_y = 9


class XanGreen2(XngGreen):
    pos_x = 6
    pos_y = 9


class ShiGreen:
    name = 'Shi'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, x, y, board):
        if 3 <= x <= 5 and 0 <= y <= 2:
            if (x == cls.pos_x + 1 or x == cls.pos_x - 1) and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
                cls.pos_x = x
                cls.pos_y = y
            else:
                return True
        else:
            return True


class ShiGreen1(ShiGreen):
    pos_x = 3
    pos_y = 9


class ShiGreen2(ShiGreen):
    pos_x = 5
    pos_y = 9


class Shuai:
    pos_x = 4
    pos_y = 9
    name = 'Sai'
    color = 'green'
    colorRGB = (0, 255, 0)

    @classmethod
    def move(cls, x, y, board):
        if 3 <= x <= 5 and 7 <= y <= 9:
            if x == cls.pos_x and (y == cls.pos_y + 1 or y == cls.pos_y - 1):
                cls.pos_y = y
            elif y == cls.pos_y and (x == cls.pos_x + 1 or x == cls.pos_x - 1):
                cls.pos_x = x
            else:
                return True
        else:
            return True
