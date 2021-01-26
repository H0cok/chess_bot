import telebot
from telebot import types
# "♔♕♗♘♙♖♚♛♝♞♟♜"
bot = telebot.TeleBot('1564531492:AAFpmRadFXfGsQ8II0BUgsBbs0oIQyVZJC4')
games = {}


class Figure:
    def __init__(self, fig):
        self.fig = fig
        self.is_moved = False


class Pawn(Figure):
    def __init__(self, fig):
        super().__init__(fig=fig)
        self.is_two_steps = False
        self.is_two_steps_r = False


class King(Figure):
    def __init__(self, fig):
        super().__init__(fig)
        self.is_attacked = False

    def set_is_attacked(self):
        if self.is_attacked:
            self.is_attacked = False
        else:
            self.is_attacked = True


class Bishop(Figure):
    def __init__(self, fig):
        super().__init__(fig=fig)
        self.possible_p_p = True
        self.possible_p_m = True
        self.possible_m_p = True
        self.possible_m_m = True


class Queen(Figure):
    def __init__(self, fig):
        super().__init__(fig=fig)
        self.possible_p_p = True
        self.possible_p_m = True
        self.possible_m_p = True
        self.possible_m_m = True
        self.possible_p_p1 = True
        self.possible_p_m1 = True
        self.possible_m_p1 = True
        self.possible_m_m1 = True

def new_board():
    desk = {
        "move": True,
        "touch": False,
        "moved": True,
        "touched": {"fig": None,
                    "pos": None},
        "board": {"extra": Figure(" ")},
        "pawn": False
    }
    for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        for p in ['1', '2', '3', '4', '5', '6', '7', '8']:
            if p == '2':
                desk["board"][i + p] = Pawn("♙")
            elif p == '7':
                desk["board"][i + p] = Pawn("♟")
            else:
                desk["board"][i+p] = Figure(" ")
    desk["board"]["b1"] = Figure('♘')
    desk["board"]["g1"] = Figure('♘')
    desk["board"]["a1"] = Bishop('♖')
    desk["board"]["h1"] = Bishop('♖')
    desk["board"]["c1"] = Bishop('♗')
    desk["board"]["f1"] = Bishop('♗')
    desk["board"]["d1"] = Queen('♕')
    desk["board"]["e1"] = King('♔')

    desk["board"]["b8"] = Figure('♞')
    desk["board"]["g8"] = Figure('♞')
    desk["board"]["a8"] = Bishop('♜')
    desk["board"]["h8"] = Bishop('♜')
    desk["board"]["c8"] = Bishop('♝')
    desk["board"]["f8"] = Bishop('♝')
    desk["board"]["d8"] = Queen('♛')
    desk["board"]["e8"] = King('♚')
    return desk


def murkup_maker(message, pawn):
    markup = types.InlineKeyboardMarkup(row_width=10)
    a1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a1"].fig, callback_data="a1")
    b1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b1"].fig, callback_data="b1")
    c1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c1"].fig, callback_data="c1")
    d1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d1"].fig, callback_data="d1")
    e1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e1"].fig, callback_data="e1")
    f1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f1"].fig, callback_data="f1")
    g1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g1"].fig, callback_data="g1")
    h1 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h1"].fig, callback_data="h1")
    markup.row(a1, b1, c1, d1, e1, f1, g1, h1)
    a2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a2"].fig, callback_data="a2")
    b2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b2"].fig, callback_data="b2")
    c2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c2"].fig, callback_data="c2")
    d2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d2"].fig, callback_data="d2")
    e2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e2"].fig, callback_data="e2")
    f2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f2"].fig, callback_data="f2")
    g2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g2"].fig, callback_data="g2")
    h2 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h2"].fig, callback_data="h2")
    markup.row(a2, b2, c2, d2, e2, f2, g2, h2)
    a3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a3"].fig, callback_data="a3")
    b3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b3"].fig, callback_data="b3")
    c3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c3"].fig, callback_data="c3")
    d3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d3"].fig, callback_data="d3")
    e3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e3"].fig, callback_data="e3")
    f3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f3"].fig, callback_data="f3")
    g3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g3"].fig, callback_data="g3")
    h3 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h3"].fig, callback_data="h3")
    markup.row(a3, b3, c3, d3, e3, f3, g3, h3)
    a4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a4"].fig, callback_data="a4")
    b4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b4"].fig, callback_data="b4")
    c4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c4"].fig, callback_data="c4")
    d4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d4"].fig, callback_data="d4")
    e4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e4"].fig, callback_data="e4")
    f4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f4"].fig, callback_data="f4")
    g4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g4"].fig, callback_data="g4")
    h4 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h4"].fig, callback_data="h4")
    markup.row(a4, b4, c4, d4, e4, f4, g4, h4)
    a5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a5"].fig, callback_data="a5")
    b5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b5"].fig, callback_data="b5")
    c5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c5"].fig, callback_data="c5")
    d5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d5"].fig, callback_data="d5")
    e5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e5"].fig, callback_data="e5")
    f5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f5"].fig, callback_data="f5")
    g5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g5"].fig, callback_data="g5")
    h5 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h5"].fig, callback_data="h5")
    markup.row(a5, b5, c5, d5, e5, f5, g5, h5)
    a6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a6"].fig, callback_data="a6")
    b6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b6"].fig, callback_data="b6")
    c6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c6"].fig, callback_data="c6")
    d6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d6"].fig, callback_data="d6")
    e6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e6"].fig, callback_data="e6")
    f6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f6"].fig, callback_data="f6")
    g6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g6"].fig, callback_data="g6")
    h6 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h6"].fig, callback_data="h6")
    markup.row(a6, b6, c6, d6, e6, f6, g6, h6)
    a7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a7"].fig, callback_data="a7")
    b7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b7"].fig, callback_data="b7")
    c7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c7"].fig, callback_data="c7")
    d7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d7"].fig, callback_data="d7")
    e7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e7"].fig, callback_data="e7")
    f7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f7"].fig, callback_data="f7")
    g7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g7"].fig, callback_data="g7")
    h7 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h7"].fig, callback_data="h7")
    markup.row(a7, b7, c7, d7, e7, f7, g7, h7)
    a8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["a8"].fig, callback_data="a8")
    b8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["b8"].fig, callback_data="b8")
    c8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["c8"].fig, callback_data="c8")
    d8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["d8"].fig, callback_data="d8")
    e8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["e8"].fig, callback_data="e8")
    f8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["f8"].fig, callback_data="f8")
    g8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["g8"].fig, callback_data="g8")
    h8 = types.InlineKeyboardButton(games[message.chat.id]["board"]["h8"].fig, callback_data="h8")
    markup.row(a8, b8, c8, d8, e8, f8, g8, h8)
    if pawn:
        q = types.InlineKeyboardButton("Q", callback_data="Q")
        k = types.InlineKeyboardButton("K", callback_data="K")
        r = types.InlineKeyboardButton("R", callback_data="R")
        b = types.InlineKeyboardButton("B", callback_data="B")
        markup.row(q, k, r, b)
    return markup


def move(pos: str, num, let):
    number = int(pos[1]) + num
    letter = chr(ord(pos[0]) + let)
    if 1 > int(number) or int(number) > 8 or 97 > ord(letter) or ord(letter) > 104:
        return "extra"
    return letter + str(number)


def possible_move(id, pos):
    if games[id]["board"][pos].fig == " " and pos != "extra":
        games[id]["board"][pos].fig = "○"
        games[id]["moved"] = True


def is_attacked(message, pos):
    return True


def take(message, pos, fig):
    positions = []
    return_set = []
    if fig.fig == "♙":
        positions = [move(pos, 1, 1), move(pos, 1, -1)]
    elif fig.fig == "♟":
        positions = [move(pos, -1, 1), move(pos, -1, -1)]
    elif fig.fig == "♝" or fig.fig == "♗":
        for i in range(1, 8):
            if fig.possible_m_p:
                if games[message.chat.id]["board"][move(pos, -i, i)].fig != "○":
                    fig.possible_m_p = False
                    positions.append(move(pos, -i, i))
            if fig.possible_p_p:
                if games[message.chat.id]["board"][move(pos, i, i)].fig != "○":
                    fig.possible_p_p = False
                    positions.append(move(pos, i, i))
            if fig.possible_m_m:
                if games[message.chat.id]["board"][move(pos, -i, -i)].fig != "○":
                    fig.possible_m_m = False
                    positions.append(move(pos, -i, -i))
            if fig.possible_p_m:
                if games[message.chat.id]["board"][move(pos, i, -i)].fig != "○":
                    fig.possible_p_m = False
                    positions.append(move(pos, i, -i))
        fig.possible_p_m = True
        fig.possible_p_p = True
        fig.possible_m_m = True
        fig.possible_m_p = True
    elif fig.fig == "♖" or fig.fig == "♜" :
        for i in range(1, 8):
            if fig.possible_m_p:
                if games[message.chat.id]["board"][move(pos, 0, i)].fig != "○":
                    fig.possible_m_p = False
                    positions.append(move(pos, 0, i))
            if fig.possible_p_p:
                if games[message.chat.id]["board"][move(pos, 0, -i)].fig != "○":
                    fig.possible_p_p = False
                    positions.append(move(pos, 0, -i))
            if fig.possible_m_m:
                if games[message.chat.id]["board"][move(pos, i, 0)].fig != "○":
                    fig.possible_m_m = False
                    positions.append(move(pos, i, 0))
            if fig.possible_p_m:
                if games[message.chat.id]["board"][move(pos, -i, 0)].fig != "○":
                    fig.possible_p_m = False
                    positions.append(move(pos, -i, 0))
        fig.possible_p_m = True
        fig.possible_p_p = True
        fig.possible_m_m = True
        fig.possible_m_p = True
    elif fig.fig == "♘" or fig.fig == "♞":
            positions.append(move(pos, 2, -1))
            positions.append(move(pos, 2, 1))
            positions.append(move(pos, -2, -1))
            positions.append(move(pos, -2, 1))
            positions.append(move(pos, 1, -2))
            positions.append(move(pos, 1, 2))
            positions.append(move(pos, -1, -2))
            positions.append(move(pos, -1, 2))
    elif fig.fig == "♕" or fig.fig == "♛":
        for i in range(1, 8):
            if fig.possible_m_p:
                if games[message.chat.id]["board"][move(pos, 0, i)].fig != "○":
                    fig.possible_m_p = False
                    positions.append(move(pos, 0, i))
            if fig.possible_p_p:
                if games[message.chat.id]["board"][move(pos, 0, -i)].fig != "○":
                    fig.possible_p_p = False
                    positions.append(move(pos, 0, -i))
            if fig.possible_m_m:
                if games[message.chat.id]["board"][move(pos, i, 0)].fig != "○":
                    fig.possible_m_m = False
                    positions.append(move(pos, i, 0))
            if fig.possible_p_m:
                if games[message.chat.id]["board"][move(pos, -i, 0)].fig != "○":
                    fig.possible_p_m = False
                    positions.append(move(pos, -i, 0))

            if fig.possible_m_p1:
                if games[message.chat.id]["board"][move(pos, -i, i)].fig != "○":
                    fig.possible_m_p1 = False
                    positions.append(move(pos, -i, i))
            if fig.possible_p_p1:
                if games[message.chat.id]["board"][move(pos, i, i)].fig != "○":
                    fig.possible_p_p1 = False
                    positions.append(move(pos, i, i))
            if fig.possible_m_m1:
                if games[message.chat.id]["board"][move(pos, -i, -i)].fig != "○":
                    fig.possible_m_m1 = False
                    positions.append(move(pos, -i, -i))
            if fig.possible_p_m1:
                if games[message.chat.id]["board"][move(pos, i, -i)].fig != "○":
                    fig.possible_p_m1 = False
                    positions.append(move(pos, i, -i))
        fig.possible_p_m = True
        fig.possible_p_p = True
        fig.possible_m_m = True
        fig.possible_m_m = True
        fig.possible_p_m1 = True
        fig.possible_p_p1 = True
        fig.possible_m_m1 = True
        fig.possible_m_p1 = True
    if fig.fig == "♚" or fig.fig == "♔":
        positions.append(move(pos, -1, 1))
        positions.append(move(pos, -1, -1))
        positions.append(move(pos, 1, -1))
        positions.append(move(pos, 1, 1))
        positions.append(move(pos, 0, 1))
        positions.append(move(pos, 0, -1))
        positions.append(move(pos, 1, 0))
        positions.append(move(pos, -1, 0))


    for i in positions:
        if games[message.chat.id]["move"]:
            if games[message.chat.id]["board"][i].fig in "♚♛♝♞♟♜":
                return_set.append(i)
        else:
            if games[message.chat.id]["board"][i].fig in "♔♕♗♘♙♖":
                return_set.append(i)
    return return_set


def touch(message, pos):
    if games[message.chat.id]["pawn"]:
        # "♔♕♗♘♙♖♚♛♝♞♟♜"
        if pos == "Q" and games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♛")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "K" and games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♞")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "B" and games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♝")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "R" and games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♜")
            games[message.chat.id]["pawn"] = False
            return True
        if pos == "Q" and not games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♕")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "K" and not games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♘")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "B" and not games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♗")
            games[message.chat.id]["pawn"] = False
            return True
        elif pos == "R" and not games[message.chat.id]["move"]:
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure("♖")
            games[message.chat.id]["pawn"] = False
            return True
        else:
            return False

    fig = games[message.chat.id]["board"][pos]
    if games[message.chat.id]["touched"]["fig"] is not None:

        if games[message.chat.id]["touched"]["fig"].fig == "♙" and \
                not games[message.chat.id]["touched"]["fig"].is_moved and pos[1] == "4":
            if games[message.chat.id]["board"][move(pos, 0, 1)].fig == "♟":
                games[message.chat.id]["board"][move(pos, 0, 1)].is_two_steps = True
                games[message.chat.id]["board"][move(pos, 0, 1)].is_two_steps_r = True
            if games[message.chat.id]["board"][move(pos, 0, -1)].fig == "♟":
                games[message.chat.id]["board"][move(pos, 0, -1)].is_two_steps = True

        if games[message.chat.id]["touched"]["fig"].fig == "♟" and \
                not games[message.chat.id]["touched"]["fig"].is_moved and pos[1] == '5':
            if games[message.chat.id]["board"][move(pos, 0, 1)].fig == "♙":
                games[message.chat.id]["board"][move(pos, 0, 1)].is_two_steps = True
                games[message.chat.id]["board"][move(pos, 0, 1)].is_two_steps_r = True
            if games[message.chat.id]["board"][move(pos, 0, -1)].fig == "♙":
                games[message.chat.id]["board"][move(pos, 0, -1)].is_two_steps = True

        if fig.fig == "○":
            if games[message.chat.id]["touched"]["fig"].fig == "♙" and\
                    games[message.chat.id]["touched"]["pos"][0] != pos[0]:
                games[message.chat.id]["board"][move(pos, -1, 0)] = Figure(" ")
                games[message.chat.id]["touched"]["fig"].is_two_steps = False

            if games[message.chat.id]["touched"]["fig"].fig == "♟" and\
                    games[message.chat.id]["touched"]["pos"][0] != pos[0]:
                games[message.chat.id]["board"][move(pos, 1, 0)] = Figure(" ")
                games[message.chat.id]["touched"]["fig"].is_two_steps = False

            if games[message.chat.id]["touched"]["fig"].fig == "♔":
                if pos == "c1":
                    games[message.chat.id]["board"]["d1"] = games[message.chat.id]["board"]["a1"]
                    games[message.chat.id]["board"]["a1"] = Figure(" ")
                if pos == "g1":
                    games[message.chat.id]["board"]["f1"] = games[message.chat.id]["board"]["h1"]
                    games[message.chat.id]["board"]["h1"] = Figure(" ")

            if games[message.chat.id]["touched"]["fig"].fig == "♚":
                if pos == "c8":
                    games[message.chat.id]["board"]["d8"] = games[message.chat.id]["board"]["a8"]
                    games[message.chat.id]["board"]["a8"] = Figure(" ")
                if pos == "g8":
                    games[message.chat.id]["board"]["f8"] = games[message.chat.id]["board"]["h8"]
                    games[message.chat.id]["board"]["h8"] = Figure(" ")
            games[message.chat.id]["move"] = not games[message.chat.id]["move"]
            games[message.chat.id]["board"][pos] = games[message.chat.id]["touched"]["fig"]
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure(" ")
            games[message.chat.id]["board"][pos].is_moved = True
        elif fig.fig == " ":
            pass

        elif pos == games[message.chat.id]["touched"]["pos"]:
            pass

        elif pos in take(message, games[message.chat.id]["touched"]["pos"], games[message.chat.id]["touched"]["fig"]):
            games[message.chat.id]["board"][games[message.chat.id]["touched"]["pos"]] = Figure(" ")
            games[message.chat.id]["board"][pos] = games[message.chat.id]["touched"]["fig"]
            games[message.chat.id]["move"] = not games[message.chat.id]["move"]
            games[message.chat.id]["moved"] = True

        for i in games[message.chat.id]["board"]:
            if games[message.chat.id]["board"][i].fig == "○":
                games[message.chat.id]["board"][i].fig = " "
        games[message.chat.id]["touched"]["fig"] = None

        return True

    else:
        games[message.chat.id]["moved"] = False
        if fig.fig == "♙":
            if games[message.chat.id]["move"]:
                games[message.chat.id]["touched"]["pos"] = pos
                games[message.chat.id]["touched"]["fig"] = fig
                games[message.chat.id]["touch"] = True
                possible_move(message.chat.id, move(pos, 1, 0))
                if not fig.is_moved:
                    possible_move(message.chat.id, move(pos, 2, 0))
                if fig.is_two_steps:
                    if not fig.is_two_steps_r:
                        possible_move(message.chat.id, move(pos, 1, 1))
                    else:
                        possible_move(message.chat.id, move(pos, 1, -1))
                return True

        if fig.fig == "♟":
            if not games[message.chat.id]["move"]:
                games[message.chat.id]["touched"]["pos"] = pos
                games[message.chat.id]["touched"]["fig"] = fig
                games[message.chat.id]["touch"] = True
                possible_move(message.chat.id, move(pos, -1, 0))
                if not fig.is_moved:
                    possible_move(message.chat.id, move(pos, -2, 0))
                if fig.is_two_steps:
                    if not fig.is_two_steps_r:
                        possible_move(message.chat.id, move(pos, -1, 1))
                    else:
                        possible_move(message.chat.id, move(pos, -1, -1))

                return True
        if fig.fig == "♔" and games[message.chat.id]["move"]:
            if not fig.is_moved:
                if (not games[message.chat.id]["board"]["a1"].is_moved) and\
                        games[message.chat.id]["board"]["b1"].fig == " " and\
                        games[message.chat.id]["board"]["c1"].fig == " " and\
                        games[message.chat.id]["board"]["d1"].fig == " " and\
                        is_attacked(message, "b1") and is_attacked(message, "a1") and\
                        is_attacked(message, "c1") and is_attacked(message, "d1") and is_attacked(message, "e1"):
                    possible_move(message.chat.id, move(pos, 0, -2))
                if (not games[message.chat.id]["board"]["h1"].is_moved) and\
                        games[message.chat.id]["board"]["g1"].fig == " " and\
                        games[message.chat.id]["board"]["f1"].fig == " " and\
                        is_attacked(message, "h1") and is_attacked(message, "g1") and\
                        is_attacked(message, "f1") and is_attacked(message, "e1"):
                    possible_move(message.chat.id, move(pos, 0, 2))
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            possible_move(message.chat.id, move(pos, 1, -1))
            possible_move(message.chat.id, move(pos, 1, 1))
            possible_move(message.chat.id, move(pos, -1, -1))
            possible_move(message.chat.id, move(pos, -1, 1))
            possible_move(message.chat.id, move(pos, 0, -1))
            possible_move(message.chat.id, move(pos, 0, 1))
            possible_move(message.chat.id, move(pos, 1, 0))
            possible_move(message.chat.id, move(pos, -1, 0))
            return True

        if fig.fig == "♚" and not games[message.chat.id]["move"]:
            if not fig.is_moved:
                if (not games[message.chat.id]["board"]["a8"].is_moved) and \
                        games[message.chat.id]["board"]["b8"].fig == " " and \
                        games[message.chat.id]["board"]["c8"].fig == " " and \
                        games[message.chat.id]["board"]["d8"].fig == " " and \
                        is_attacked(message, "b8") and is_attacked(message, "a8") and \
                        is_attacked(message, "c8") and is_attacked(message, "d8") and is_attacked(message, "e8"):
                    possible_move(message.chat.id, move(pos, 0, -2))
                if (not games[message.chat.id]["board"]["h8"].is_moved) and\
                        games[message.chat.id]["board"]["g8"].fig == " " and\
                        games[message.chat.id]["board"]["f8"].fig == " " and\
                        is_attacked(message, "h8") and is_attacked(message, "g8") and\
                        is_attacked(message, "f8") and is_attacked(message, "e8"):
                    possible_move(message.chat.id, move(pos, 0, 2))
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            possible_move(message.chat.id, move(pos, 1, -1))
            possible_move(message.chat.id, move(pos, 1, 1))
            possible_move(message.chat.id, move(pos, -1, -1))
            possible_move(message.chat.id, move(pos, -1, 1))
            possible_move(message.chat.id, move(pos, 0, -1))
            possible_move(message.chat.id, move(pos, 0, 1))
            possible_move(message.chat.id, move(pos, 1, 0))
            possible_move(message.chat.id, move(pos, -1, 0))
            return True

        if (fig.fig == "♗" and games[message.chat.id]["move"]) or\
                (fig.fig == "♝"and not games[message.chat.id]["move"]):
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            for i in range(1, 8):
                if fig.possible_m_p:
                    if games[message.chat.id]["board"][move(pos, -i, i)].fig != " ":
                        fig.possible_m_p = False
                    possible_move(message.chat.id, move(pos, -i, i))
                if fig.possible_p_p:
                    if games[message.chat.id]["board"][move(pos, i, i)].fig != " ":
                        fig.possible_p_p = False
                    possible_move(message.chat.id, move(pos, i, i))
                if fig.possible_m_m:
                    if games[message.chat.id]["board"][move(pos, -i, -i)].fig != " ":
                        fig.possible_m_m = False
                    possible_move(message.chat.id, move(pos, -i, -i))
                if fig.possible_p_m:
                    if games[message.chat.id]["board"][move(pos, i, -i)].fig != " ":
                        fig.possible_p_m = False
                    possible_move(message.chat.id, move(pos, i, -i))
            fig.possible_p_m = True
            fig.possible_p_p = True
            fig.possible_m_m = True
            fig.possible_m_p = True
            return True
        if (fig.fig == "♘" and games[message.chat.id]["move"]) or \
                (fig.fig == "♞" and not games[message.chat.id]["move"]):
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            possible_move(message.chat.id, move(pos, 2, -1))
            possible_move(message.chat.id, move(pos, 2, 1))
            possible_move(message.chat.id, move(pos, -2, -1))
            possible_move(message.chat.id, move(pos, -2, 1))
            possible_move(message.chat.id, move(pos, 1, -2))
            possible_move(message.chat.id, move(pos, 1, 2))
            possible_move(message.chat.id, move(pos, -1, -2))
            possible_move(message.chat.id, move(pos, -1, 2))
            return True
        if (fig.fig == "♖" and games[message.chat.id]["move"]) or \
                (fig.fig == "♜" and not games[message.chat.id]["move"]):
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            for i in range(1, 8):
                if fig.possible_m_p:
                    if games[message.chat.id]["board"][move(pos, 0, i)].fig != " ":
                        fig.possible_m_p = False
                    possible_move(message.chat.id, move(pos, 0, i))
                if fig.possible_p_p:
                    if games[message.chat.id]["board"][move(pos, 0, -i)].fig != " ":
                        fig.possible_p_p = False
                    possible_move(message.chat.id, move(pos, 0, -i))
                if fig.possible_m_m:
                    if games[message.chat.id]["board"][move(pos, i, 0)].fig != " ":
                        fig.possible_m_m = False
                    possible_move(message.chat.id, move(pos, i, 0))
                if fig.possible_p_m:
                    if games[message.chat.id]["board"][move(pos, -i, 0)].fig != " ":
                        fig.possible_p_m = False
                    possible_move(message.chat.id, move(pos, -i, 0))
            fig.possible_p_m = True
            fig.possible_p_p = True
            fig.possible_m_m = True
            fig.possible_m_p = True
            return True
        if (fig.fig == "♕" and games[message.chat.id]["move"]) or \
                (fig.fig == "♛" and not games[message.chat.id]["move"]):
            games[message.chat.id]["touched"]["pos"] = pos
            games[message.chat.id]["touched"]["fig"] = fig
            games[message.chat.id]["touch"] = True
            for i in range(1, 8):
                if fig.possible_m_p:
                    if games[message.chat.id]["board"][move(pos, 0, i)].fig != " ":
                        fig.possible_m_p = False
                    possible_move(message.chat.id, move(pos, 0, i))
                if fig.possible_p_p:
                    if games[message.chat.id]["board"][move(pos, 0, -i)].fig != " ":
                        fig.possible_p_p = False
                    possible_move(message.chat.id, move(pos, 0, -i))
                if fig.possible_m_m:
                    if games[message.chat.id]["board"][move(pos, i, 0)].fig != " ":
                        fig.possible_m_m = False
                    possible_move(message.chat.id, move(pos, i, 0))
                if fig.possible_p_m:
                    if games[message.chat.id]["board"][move(pos, -i, 0)].fig != " ":
                        fig.possible_p_m = False
                    possible_move(message.chat.id, move(pos, -i, 0))

                if fig.possible_m_p1:
                    if games[message.chat.id]["board"][move(pos, -i, i)].fig != " ":
                        fig.possible_m_p1 = False
                    possible_move(message.chat.id, move(pos, -i, i))
                if fig.possible_p_p1:
                    if games[message.chat.id]["board"][move(pos, i, i)].fig != " ":
                        fig.possible_p_p1 = False
                    possible_move(message.chat.id, move(pos, i, i))
                if fig.possible_m_m1:
                    if games[message.chat.id]["board"][move(pos, -i, -i)].fig != " ":
                        fig.possible_m_m1 = False
                    possible_move(message.chat.id, move(pos, -i, -i))
                if fig.possible_p_m1:
                    if games[message.chat.id]["board"][move(pos, i, -i)].fig != " ":
                        fig.possible_p_m1 = False
                    possible_move(message.chat.id, move(pos, i, -i))
            fig.possible_p_m = True
            fig.possible_p_p = True
            fig.possible_m_m = True
            fig.possible_m_p = True
            fig.possible_p_m1 = True
            fig.possible_p_p1 = True
            fig.possible_m_m1 = True
            fig.possible_m_p1 = True
            return True

        if not games[message.chat.id]["moved"]:
            games[message.chat.id]["touch"] = False
            games[message.chat.id]["touched"]["fig"] = None
            games[message.chat.id]["touched"]["pos"] = None
            games[message.chat.id]["moved"] = True

    return False


@bot.message_handler(commands=['game'])
def game(message):
    games[message.chat.id] = new_board()
    markup_first = murkup_maker(message, False)
    bot.send_message(message.chat.id, 'White move', reply_markup=markup_first)
    @bot.callback_query_handler(func=lambda call: True)
    def callback_query(call):
        if touch(message, call.data) and games[message.chat.id]["moved"]:
            for i in games[message.chat.id]["board"]:
                if i[1] == "1" and games[message.chat.id]["board"][i].fig == "♟":
                    games[message.chat.id]["pawn"] = True
                    games[message.chat.id]["touched"]["pos"] = i
                if i[1] == "8" and games[message.chat.id]["board"][i].fig == "♙":
                    games[message.chat.id]["pawn"] = True
                    games[message.chat.id]["touched"]["pos"] = i
            markup = murkup_maker(message, games[message.chat.id]["pawn"])
            if games[message.chat.id]["move"]:
                txt = "White move"
            else:
                txt = "Black move"
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, reply_markup=markup,
                                  text=txt)


bot.polling()