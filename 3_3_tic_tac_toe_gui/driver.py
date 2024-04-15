import math
from tic_tac_toe import alpha_beta_search
from utility import utility
import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QTableWidget , QHeaderView ,\
     QStyledItemDelegate , QTableWidgetItem , QDialog , QPushButton , QLabel , QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi
from time import sleep
from threading import Thread

class IconDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(IconDelegate, self).initStyleOption(option, index)
        size = option.rect.size()
        size.setWidth(130)
        size.setHeight(85)
        option.decorationSize = size

class error_msg(QDialog):
    def __init__(self):
        super(error_msg, self).__init__()
        loadUi('error_msg.ui', self)
        self.ok_button = self.findChild(QPushButton , "ok_btn")
        self.ok_button.clicked.connect(self.close)

class tic_tac_toe_GUI(QMainWindow):
    def __init__(self):
        global starter , difficulty
        super().__init__()
        loadUi('gui.ui', self)
        self.setWindowTitle("Tic Tac Toe")
        self.state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
        self.user_row = None
        self.user_col = None
        self.start_button = self.findChild(QPushButton , "start_btn")
        self.starterE = self.findChild(QLineEdit , "starter")
        self.difficultyE = self.findChild(QLineEdit , "difficulty")
        self.useless1 = self.findChild(QLabel , "label")
        self.useless2 = self.findChild(QLabel , "label_2")
        self.start_button.clicked.connect(self.set_start_vars)
        self.player_one_choice = {}
        self.player_two_choice = {}
        self.turn = 1
        self.error = error_msg()
        self.tic_tac_toe = self.findChild(QTableWidget , "tic_tac_toe")
        self.result = self.findChild(QLabel , "result_label")
        self.tic_tac_toe.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tic_tac_toe.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tic_tac_toe.horizontalHeader().hide()
        self.tic_tac_toe.verticalHeader().hide()
        self.delegate = IconDelegate(self.tic_tac_toe)
        self.tic_tac_toe.pressed.connect(self.set_table_widget_event)
        self.show()
    
    def set_start_vars(self):
        self.starter = self.starterE.text()
        self.difficulty_level = self.difficultyE.text()
        self.start_button.setVisible(False)
        self.starterE.setVisible(False)
        self.difficultyE.setVisible(False)
        self.useless2.setVisible(False)
        self.useless1.setVisible(False)
        self.setFixedSize(379, 385)
        Thread(target=self.run_game).start()

    def run_game(self):
                        if(self.starter == "computer"):

                            if(self.difficulty_level == "easy"):
                                depth_limit_2 = 0
                                print("\ngame starts at easy difficulty")
                            else:
                                depth_limit_2 = math.inf

                            depth_limit_1 = math.inf

                            while True:
                                if(self.isterminal() == True):
                                    break

                                sleep(2)
                                move = alpha_beta_search(self.state, 'max', depth_limit_1)
                                self.state[move[0]][move[1]] = 1
                                self.set_circle(move[0] , move[1])

                                if(self.isterminal() == True):
                                    break

                                sleep(2)
                                opponent_move = alpha_beta_search(self.state, 'min', depth_limit_2)
                                self.state[opponent_move[0]][opponent_move[1]] = -1
                                self.set_x(opponent_move[0] , opponent_move[1])
                        else:
                            if(self.difficulty_level == "easy"):
                                depth_limit = 0
                                print("\ngame starts at easy difficulty")
                            else:
                                depth_limit = math.inf
                            while True:
                                if(self.isterminal() == True):
                                    break
                                
                                while self.user_row == None and self.user_col == None:
                                    ...
                                
                                row, col = self.user_row , self.user_col
                                self.user_row = self.user_col = None
                                while((row > 2) or (row < 0) or (col > 2) 
                                    or (col < 0) or (self.state[row][col] != 0)):
                                    print("\nyour input is wrong.please try again\n")
                                    while self.user_row == None and self.user_col == None:
                                       ...
                                    row, col = self.user_row , self.user_col
                                    self.user_row = self.user_col = None

                                self.state[row][col] = 1
                                self.set_circle(row,col)
                                if(self.isterminal() == True):
                                    break
                                sleep(1)
                                opponent_move = alpha_beta_search(self.state, 'min', depth_limit)
                                self.state[opponent_move[0]][opponent_move[1]] = -1
                                self.set_x(opponent_move[0] , opponent_move[1])

    def set_table_widget_event(self,item):
        row = item.row()
        column = item.column()
        if (row,column) in self.player_one_choice or (row,column) in self.player_two_choice:
            self.error.show()
        else:
            if self.turn==1:
                self.user_row = row
                self.user_col = column
                self.set_circle(row,column)
            else:
                self.set_x(row,column)

    def get_player_one_choices(self):
        return list(self.player_one_choice.keys())
    
    def get_player_two_choices(self):
        return list(self.player_two_choice.keys())
    
    def get_all_choice(self):
        return self.get_player_one_choices() + self.get_player_two_choices()

    def isCellEmpty(self , row , col):
        return not ((row,col) in self.player_one_choice or (row,col) in self.player_two_choice)
    
    def cells_to_fill_winner(self , start , end):
        if start[0]==end[0]:
            return (start,(start[0],1),end)
        elif start[1]==end[1]:
            return (start,(1,start[1]),end)
        elif abs(start[0]-end[0])==2 and abs(start[1]-end[1])==2:
            return (start,(1,1),end)

    def set_result(self , start_cell = None, end_cell = None, winner = 1):
        if winner==1:
            cells = self.cells_to_fill_winner(start_cell,end_cell)
            for row,col in cells:
              self.tic_tac_toe.removeCellWidget(row,col)
              item = QTableWidgetItem(QIcon("green_circle.png"), "")
              self.tic_tac_toe.setItem(row,col,item)
              self.tic_tac_toe.setItemDelegateForColumn(col, self.delegate)
            self.result.setText("Player one is winner")
        elif winner==2:
            cells = self.cells_to_fill_winner(start_cell,end_cell)
            for row,col in cells:
              self.tic_tac_toe.removeCellWidget(row,col)
              item = QTableWidgetItem(QIcon("green_x.png"), "")
              self.tic_tac_toe.setItem(row,col,item)
              self.tic_tac_toe.setItemDelegateForColumn(col, self.delegate)
            self.result.setText("Player two is winner")
        else:
            self.result.setText("No one is winner")

    def set_circle(self , row , col):
        self.player_one_choice[(row,col)] = None
        item = QTableWidgetItem(QIcon("circle.png"), "")
        self.tic_tac_toe.setItem(row,col,item)
        self.tic_tac_toe.setItemDelegateForColumn(col, self.delegate)
        self.turn = 2

    def set_x(self , row , col):
        self.player_two_choice[(row,col)] = None
        item = QTableWidgetItem(QIcon("x.png"), "")
        self.tic_tac_toe.setItem(row,col,item)
        self.tic_tac_toe.setItemDelegateForColumn(col, self.delegate)
        self.turn = 1
    
    def search_element(self , item):
        output = []
        for x in range(len(self.state)):
            for y in range(len(self.state[0])):
                if self.state[x][y] == item:
                    output.append([x,y])
        return output

    def isterminal(self):
        utility_result = utility(self.state)
        if(utility_result != 'not_terminal'):
            if(utility_result == 1):
                out = self.search_element(1)
                out = sorted(out , key = lambda x : x[0] + x[1])
                self.set_result(out[0] , out[-1])
            elif(utility_result == -1):
                out = self.search_element(-1)
                out = sorted(out , key = lambda x : x[0] + x[1])
                self.set_result(out[0] , out[-1] , winner = 2)
            else:
                self.set_result(winner = -1)
            return True
        return False

app = QApplication(sys.argv)
my_form = tic_tac_toe_GUI()
sys.exit(app.exec_())