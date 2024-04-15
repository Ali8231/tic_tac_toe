import sys, os
import math
from PyQt5.QtWidgets import QApplication, QMainWindow , QTableWidget , QHeaderView ,\
     QStyledItemDelegate , QTableWidgetItem , QDialog , QPushButton , QLabel
from PyQt5.QtGui import QIcon
from PyQt5.uic import loadUi

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
        super().__init__()
        loadUi('gui.ui', self)
        self.state = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]
        starter = input("who plays against computer?(user/computer) : ")
        difficulty_level = input("\nenter difficulty level(easy/hard) : ")
        self.starter = starter
        self.difficulty_level = difficulty_level
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
    
    def run_game(self):
                        if(self.starter == "computer"):

                            if(self.difficulty_level == "easy"):
                                depth_limit_2 = 0
                                print("\ngame starts at easy difficulty")
                            else:
                                depth_limit_2 = math.inf

                            depth_limit_1 = math.inf

                            while True:

                                print_state(state)

                                if(isterminal(state) == True):
                                    break

                                time.sleep(2)
                                move = alpha_beta_search(state, 'max', depth_limit_1)
                                state[move[0]][move[1]] = 1

                                print_state(state)

                                if(isterminal(state) == True):
                                    break

                                time.sleep(2)
                                opponent_move = alpha_beta_search(state, 'min', depth_limit_2)
                                state[opponent_move[0]][opponent_move[1]] = -1


                        else:

                            if(difficulty_level == "easy"):
                                depth_limit = 0
                                print("\ngame starts at easy difficulty")
                            else:
                                depth_limit = math.inf

                            
                            while True:

                                print_state(state)

                                if(isterminal(state) == True):
                                    break

                                row, col = getMove()
                                
                                while((row > 2) or (row < 0) or (col > 2) 
                                    or (col < 0) or (state[row][col] != 0)):
                                    print("\nyour input is wrong.please try again\n")
                                    row, col = getMove()

                                state[row][col] = 1

                                print_state(state)

                                if(isterminal(state) == True):
                                    break

                                time.sleep(1)
                                opponent_move = alpha_beta_search(state, 'min', depth_limit)
                                state[opponent_move[0]][opponent_move[1]] = -1



    def set_table_widget_event(self,item):
        row = item.row()
        column = item.column()
        if (row,column) in self.player_one_choice or (row,column) in self.player_two_choice:
            self.error.show()
        else:
            if self.turn==1:
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