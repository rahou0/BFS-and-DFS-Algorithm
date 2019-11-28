import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.Qt import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
from PyQt5.QtGui import QPainter, QBrush, QPen, QGuiApplication, QFont
from PyQt5.QtCore import Qt, QRectF
#creation de la class Node qui contien des valeur et 2 pointer forward and 1 pointer back
class Node:
    def __init__(self,data,x,y):
        self.left=None
        self.right=None
        self.back=None
        self.data=data
        self.x=x
        self.y=y
#cree un class element pour empiler et depiler
class Element:
    def __init__(self):
        self.value=None
        self.next=None
#class Main for l'interface
class MainWindow(QWidget):
    hello="hii"
    text="G"
    #create pile empty
    tete = Element()
    #create tree and remplire
    root = Node("S",620,140)
    def remplirlist(self):
        # left
        self.root.left = Node("A","310","240")
        self.root.left.back=self.root
        # right
        self.root.right = Node("D","910","240")
        self.root.right.back = self.root
        # left -->
        self.root.left.right = Node("D","465","340")
        self.root.left.right.back =self.root.left
        self.root.left.left = Node("B","155","340")
        self.root.left.left.back = self.root.left
        # left left -->
        self.root.left.left.left = Node("C","80","440")
        self.root.left.left.left.back = self.root.left.left
        self.root.left.left.right = Node("E","234","440")
        self.root.left.left.right.back = self.root.left.left
        self.root.left.left.right.left = Node("D","200","540")
        self.root.left.left.right.left.back = self.root.left.left.right
        self.root.left.left.right.right = Node("F","280","540")
        self.root.left.left.right.right.back = self.root.left.left.right
        self.root.left.left.right.right.right = Node("G","300","640")
        self.root.left.left.right.right.right.back = self.root.left.left.right.right
        # left right -->
        self.root.left.right.right = Node("E","550","440")
        self.root.left.right.right.back = self.root.left.right
        self.root.left.right.right.right = Node("F","590","540")
        self.root.left.right.right.right.back = self.root.left.right.right
        self.root.left.right.right.left = Node("B","510","540")
        self.root.left.right.right.left.back = self.root.left.right.right
        self.root.left.right.right.left.left = Node("C","490","640")
        self.root.left.right.right.left.left.back = self.root.left.right.right.left
        self.root.left.right.right.right.right = Node("G","610","640")
        self.root.left.right.right.right.right.back = self.root.left.right.right.right
        # right -->
        self.root.right.right = Node("E","1065","340")
        self.root.right.right.back = self.root.right
        self.root.right.left = Node("A","755","340")
        self.root.right.left.back = self.root.right
        # right left-->
        self.root.right.left.right = Node("B","830","440")
        self.root.right.left.right.back = self.root.right.left
        self.root.right.left.right.left = Node("C","790","540")
        self.root.right.left.right.left.back = self.root.right.left.right
        self.root.right.left.right.right = Node("E","870","540")
        self.root.right.left.right.right.back = self.root.right.left.right
        self.root.right.left.right.right.left = Node("F","850","640")
        self.root.right.left.right.right.left.back = self.root.right.left.right.right
        self.root.right.left.right.right.left.right = Node("G","860","740")
        self.root.right.left.right.right.left.right.back = self.root.right.left.right.right.left
        # right right-->
        self.root.right.right.right = Node("F","1140","440")
        self.root.right.right.right.back = self.root.right.right
        self.root.right.right.right.right = Node("G","1180","540")
        self.root.right.right.right.right.back = self.root.right.right.right
        self.root.right.right.left = Node("B","990","440")
        self.root.right.right.left.back = self.root.right.right
        self.root.right.right.left.left = Node("A","950","540")
        self.root.right.right.left.left.back = self.root.right.right.left
        self.root.right.right.left.right = Node("C","1030","540")
        self.root.right.right.left.right.back = self.root.right.right.left
    #ajoute le racine a la tete de la pile

    witchButtonClicked = 0
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.remplirlist()
        self.tete.value = self.root
        self.resize(1720, 980)
        self.button = QtWidgets.QPushButton("DASHBOARD", self)
        self.line = QLineEdit(self)
        self.label = QLabel(self)
        self.label.setText("RESULTS ")
        self.label.setGeometry(40,805,80,30)
        self.label.setStyleSheet("font-size: 20px;")
        self.line.setGeometry(1300,20,80,80)
        regex = QtCore.QRegExp("[A-Z_]+")
        validator = QtGui.QRegExpValidator(regex)
        self.line.setValidator(validator)
        self.line.setMaxLength(1)
        self.line.setStyleSheet("border-radius:16px;font-size: 40px;padding:10px;border: 2px solid #000")
        self.button.setGeometry(20,20,300,80)
        self.button.setStyleSheet("background-color: transparent;color: black;border: 2px solid #000;font-size: 36px;padding: 15px 32px;text-align: center;border-radius: 12px;")
        self.buttonDfsAll = QtWidgets.QPushButton("DFS ALL SOLUTIONS", self)
        self.buttonBFS = QtWidgets.QPushButton("BREADTH FIRST SEARCH", self)
        self.buttonDFS = QtWidgets.QPushButton("DEPTH FIRST SEARCH", self)
        self.buttonBfsAll = QtWidgets.QPushButton("BFS ALL SOLUTIONS", self)

        self.buttonDfsAll.setGeometry(980,20,300,80)#f44336 red
        self.buttonBFS.setGeometry(660,20,300,80)#bbdefb bleu
        self.buttonDFS.setGeometry(340,20,300,80)#4CAF50 vert
        self.buttonBfsAll.setGeometry(1400,20,300,80)#9c27b0 move
        self.buttonDfsAll.setStyleSheet(" background-color: #4CAF50;color: white;border-radius: 12px; box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19); border: none;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;")
        self.buttonBFS.setStyleSheet(" background-color: #bbdefb;color: white;border-radius: 12px;box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19); border: none;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;")
        self.buttonDFS.setStyleSheet(" background-color: #4CAF50;color: white;border-radius: 12px;box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19); border: none;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;")
        self.buttonBfsAll.setStyleSheet(" background-color: #bbdefb;color: white;border-radius: 12px;box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2), 0 6px 20px 0 rgba(0,0,0,0.19); border: none;padding: 15px 32px;text-align: center;text-decoration: none;display: inline-block;font-size: 16px;")
        self.buttonDfsAll.clicked.connect(self.DFSALL)
        self.buttonBfsAll.clicked.connect(self.BFSALL)
        self.buttonBFS.clicked.connect(self.BFS)
        self.buttonDFS.clicked.connect(self.DFS)
    #draw tree with nodes
    def painTree(self,painter):
        painter.setRenderHint(QPainter.Antialiasing)
        rectangleTree = QRectF(20.0, 120.0, 1220.0, 680.0)
        rectangleTable = QRectF(1260.0, 120.0, 440.0, 820.0)
        rectangleTable1 = QRectF(20.0, 840.0, 1220.0, 120.0)
        painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        painter.setPen(QPen(Qt.white, 3, Qt.SolidLine))
        painter.drawRoundedRect(rectangleTree, 20.0, 15.0)
        painter.drawRoundedRect(rectangleTable, 20.0, 15.0)
        painter.drawRoundedRect(rectangleTable1, 20.0, 15.0)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        font = QFont()
        font.setBold(True)
        font.setPixelSize(18)
        painter.setFont(font)
        painter.drawText(1280, 150, "Developed Node")
        painter.drawText(1450, 150, "List of Nodes")
        # lvl1
        font = QFont()
        font.setBold(True)
        font.setPixelSize(18)
        painter.setFont(font)
        painter.drawLine(640, 160, 330, 260)
        painter.drawLine(640, 160, 930, 260)
        painter.drawEllipse(QRectF(620, 140, 40, 40))
        painter.drawText(QRectF(620, 140, 40, 40), Qt.AlignCenter, "S")
        # lvl2
        # line A
        painter.drawLine(330, 260, 175, 360)
        painter.drawLine(330, 260, 485, 360)
        # line D
        painter.drawLine(930, 260, 775, 360)
        painter.drawLine(930, 260, 1085, 360)
        # position
        painter.drawEllipse(310, 240, 40, 40)
        painter.drawText(QRectF(310, 240, 40, 40), Qt.AlignCenter, "A")
        painter.drawEllipse(910, 240, 40, 40)
        painter.drawText(QRectF(910, 240, 40, 40), Qt.AlignCenter, "D")
        # lvl3
        # line B
        painter.drawLine(175, 360, 100, 460)
        painter.drawLine(175, 360, 254, 460)
        # line D
        painter.drawLine(485, 360, 570, 460)
        # line A
        painter.drawLine(775, 360, 850, 460)
        # line E
        painter.drawLine(1085, 360, 1010, 460)
        painter.drawLine(1085, 360, 1160, 460)
        # position
        painter.drawEllipse(155, 340, 40, 40)
        painter.drawText(QRectF(155, 340, 40, 40), Qt.AlignCenter, "B")
        painter.drawEllipse(465, 340, 40, 40)
        painter.drawText(QRectF(465, 340, 40, 40), Qt.AlignCenter, "D")
        painter.drawEllipse(755, 340, 40, 40)
        painter.drawText(QRectF(755, 340, 40, 40), Qt.AlignCenter, "A")
        painter.drawEllipse(1065, 340, 40, 40)
        painter.drawText(QRectF(1065, 340, 40, 40), Qt.AlignCenter, "E")

        # lvl4
        # line E
        painter.drawLine(264, 460, 220, 560)
        painter.drawLine(264, 460, 300, 560)
        # line E
        painter.drawLine(570, 460, 530, 560)
        painter.drawLine(570, 460, 610, 560)
        # line B
        painter.drawLine(850, 460, 810, 560)
        painter.drawLine(850, 460, 890, 560)
        # line B
        painter.drawLine(1010, 460, 970, 560)
        painter.drawLine(1010, 460, 1050, 560)
        # line F
        painter.drawLine(1160, 460, 1200, 560)
        # position
        painter.drawEllipse(80, 440, 40, 40)
        painter.drawText(QRectF(80, 440, 40, 40), Qt.AlignCenter, "C")
        painter.drawEllipse(234, 440, 40, 40)
        painter.drawText(QRectF(234, 440, 40, 40), Qt.AlignCenter, "E")
        painter.drawEllipse(550, 440, 40, 40)
        painter.drawText(QRectF(550, 440, 40, 40), Qt.AlignCenter, "E")
        painter.drawEllipse(830, 440, 40, 40)
        painter.drawText(QRectF(830, 440, 40, 40), Qt.AlignCenter, "B")
        painter.drawEllipse(990, 440, 40, 40)
        painter.drawText(QRectF(990, 440, 40, 40), Qt.AlignCenter, "B")
        painter.drawEllipse(1140, 440, 40, 40)
        painter.drawText(QRectF(1140, 440, 40, 40), Qt.AlignCenter, "F")

        # lvl5
        # line F
        painter.drawLine(300, 560, 320, 660)
        # line B
        painter.drawLine(530, 560, 510, 660)
        # line F
        painter.drawLine(610, 560, 630, 660)
        # line E
        painter.drawLine(890, 560, 870, 660)
        # position
        painter.drawEllipse(200, 540, 40, 40)
        painter.drawText(QRectF(200, 540, 40, 40), Qt.AlignCenter, "D")
        painter.drawEllipse(280, 540, 40, 40)
        painter.drawText(QRectF(280, 540, 40, 40), Qt.AlignCenter, "F")
        painter.drawEllipse(510, 540, 40, 40)
        painter.drawText(QRectF(510, 540, 40, 40), Qt.AlignCenter, "B")
        painter.drawEllipse(590, 540, 40, 40)
        painter.drawText(QRectF(590, 540, 40, 40), Qt.AlignCenter, "F")
        painter.drawEllipse(790, 540, 40, 40)
        painter.drawText(QRectF(790, 540, 40, 40), Qt.AlignCenter, "C")
        painter.drawEllipse(870, 540, 40, 40)
        painter.drawText(QRectF(870, 540, 40, 40), Qt.AlignCenter, "E")
        painter.drawEllipse(950, 540, 40, 40)
        painter.drawText(QRectF(950, 540, 40, 40), Qt.AlignCenter, "A")
        painter.drawEllipse(1030, 540, 40, 40)
        painter.drawText(QRectF(1030, 540, 40, 40), Qt.AlignCenter, "C")
        painter.drawEllipse(1180, 540, 40, 40)
        painter.drawText(QRectF(1180, 540, 40, 40), Qt.AlignCenter, "G")

        # lvl6
        # line F
        painter.drawLine(870, 660, 880, 760)
        # position
        painter.drawEllipse(300, 640, 40, 40)
        painter.drawText(QRectF(300, 640, 40, 40), Qt.AlignCenter, "G")
        painter.drawEllipse(490, 640, 40, 40)
        painter.drawText(QRectF(490, 640, 40, 40), Qt.AlignCenter, "C")
        painter.drawEllipse(610, 640, 40, 40)
        painter.drawText(QRectF(610, 640, 40, 40), Qt.AlignCenter, "G")
        painter.drawEllipse(850, 640, 40, 40)
        painter.drawText(QRectF(850, 640, 40, 40), Qt.AlignCenter, "F")
        # lvl7
        painter.drawEllipse(860, 740, 40, 40)
        painter.drawText(QRectF(860, 740, 40, 40), Qt.AlignCenter, "G")
    # Breadth First Search Algorithme
    def BFSearch(self,painter):
        # draw first line
        painter.drawText(1280, 180, "-")
        painter.drawText(1445, 180, "{")
        if self.root is not None:
            painter.drawText(1455, 180, self.root.data)
        painter.drawText(1465, 180, "}")
        isfound = 0
        counter = 1
        #boucle jusqu'a la file soit vide ou le but atteint
        while self.tete is not None and isfound != 1:
            painter.drawLine(1440, 140, 1440, counter * 24 + 110)
            painter.drawText(1280, counter * 20 + 180, self.tete.value.data)
            #testi si le noeud est le noeud but
            if self.tete.value.data == self.text:
                painter.drawText(1300, counter * 20 + 180, "but")
                isfound = 1
                path = Element()
                path = self.tete
                painter.drawText(60, 870,
                                 "Path to etat But : ")
                i = 15
                #boucle en ariere jusqu'a la racine pour trouve le chemin de noeud but
                while path.value is not None:
                    painter.drawText(i + 200, 870,
                                     path.value.data)
                    painter.setBrush(QColor(0, 140, 186))
                    painter.drawEllipse(int(path.value.x), int(path.value.y), 40, 40)
                    painter.drawText(QRectF(int(path.value.x), int(path.value.y), 40, 40), Qt.AlignCenter,
                                     path.value.data)
                    path.value = path.value.back
                    i=i+15
            #le cas si le noeud n'est pas le noeud but
            else:
                #mzttre le pointeur dans la tete de la file
                ptr = self.tete
                #enfile les fils de current node s'il exist
                if self.tete.value.left is not None:
                    elements = Element()
                    elements.value = self.tete.value.left
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
                if self.tete.value.right is not None:
                    elements = Element()
                    elements.value = self.tete.value.right
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
            #retirer le noeud de la file
            self.tete = self.tete.next
            ptr = self.tete
            i = 0
            painter.drawText(1445, counter * 20 + 180, "{")
            #boucle pour affiche liste des nodes
            while ptr is not None:
                painter.drawText(i * 14 + 1455, counter * 20 + 180, ptr.value.data)
                i = i + 1
                ptr = ptr.next
            painter.drawText(i * 14 + 1455, counter * 20 + 180, "}")
            if isfound == 1:
                painter.drawText(i * 14 + 1468, counter * 20 + 180, "non developpe")
            counter = counter + 1
        #le cas si on nous trouve aucune solution
        if isfound==0:
            painter.drawText(60, 870,
                             "Path to etat But : Node But n'exist pas <3 ")
    # Depth First Search Algorithme
    def DFSearch(self,painter):
        #draw first line
        painter.drawText(1280, 180, "-")
        painter.drawText(1445, 180, "{")
        if self.root.data is not None:
            painter.drawText(1455, 180, self.root.data)
        painter.drawText(1465, 180, "}")
        #this variable is used to annonce that we isfound solution! it will turn to 1 to leave the loop
        isfound = 0
        #this variable used to give new space beteween lines in GUI
        counter = 1
        #boucle jusqu'a la pile soit vide au le noeud est le but
        while self.tete is not None and isfound != 1:
            #print the current node in developped nodes liste
            painter.drawText(1280, counter * 20 + 180, self.tete.value.data)
            #test the curent node if he is the solution or not
            if self.tete.value.data == self.text:
                painter.drawText(1300, counter * 20 + 180, "but")
                isfound = 1
                #create pointer to point in the solution and move backword to initial stats
                path = Element()
                path = self.tete
                painter.drawText(60, 870,
                                 "Path to etat But : ")
                i=15
                #go back until root node and draw colored stats to show the path
                while path.value is not None:
                    painter.drawText(i+200, 870,
                                     path.value.data)
                    painter.setBrush(QColor(76, 175, 80))
                    painter.drawEllipse(int(path.value.x), int(path.value.y), 40, 40)
                    painter.drawText(QRectF(int(path.value.x), int(path.value.y), 40, 40), Qt.AlignCenter,
                                     path.value.data)
                    path.value = path.value.back
                    i=i+15
                #remove the soluion from Noeud List
                if self.tete.next is not None:
                    self.tete = self.tete.next
                else:
                    self.tete = None
            #the case that Node not the Node Goal
            else:
                #put the pointer in the head of list
                ptr = self.tete
                # remove the current Node from Noeud List
                if self.tete.next is not None:
                    self.tete = self.tete.next
                else:
                    self.tete = None
                # add Node fils xD if exist right or left in the head of the pile "stack"
                if ptr.value.right is not None:
                    elements = Element()
                    elements.value = ptr.value.right
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements
                if ptr.value.left is not None:
                    elements = Element()
                    elements.value = ptr.value.left
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements
            #put the pointer in the first element of the list to draw Node list
            ptr = self.tete
            i = 0
            painter.drawText(1445, counter * 20 + 180, "{")
            while ptr is not None:
                painter.drawText(i * 14 + 1455, counter * 20 + 180, ptr.value.data)
                i = i + 1
                ptr = ptr.next
            painter.drawText(i * 14 + 1455, counter * 20 + 180, "}")
            if isfound == 1:
                painter.drawText(i * 14 + 1468, counter * 20 + 180, "non developpe")
            counter = counter + 1
        #print error not found whene ther's no solution
        if isfound==0:
            painter.drawText(60, 870,
                             "Path to etat But : Node But n'exist pas")
    # Depth First Search ALL SOLUTIONS Algorithme
    def DFSearchALL(self, painter):
        # draw first line
        if self.root.data is not None:
            painter.drawText(1280, 180, "-")
            painter.drawText(1445, 180, "{")
            painter.drawText(1455, 180, self.root.data)
            painter.drawText(1465, 180, "}")
        # this variable is used to annonce that we isfound solution! it will turn to 1 to leave the loop
        isfound = 0
        # this variable used to give new space beteween lines in GUI
        counter = 1
        # loop used to enpiler and dipiler the list until the list get empty
        while self.tete is not None:
            # print the current node in developped nodes liste
            painter.drawText(1280, counter * 20 + 180, self.tete.value.data)
            # test the curent node if he is the solution or not
            if self.tete.value.data == self.text:
                painter.drawText(1300, counter * 20 + 180, "but")
                isfound = isfound+1
                # create pointer to point in the solution and move backword to initial stats
                path = Element()
                path = self.tete
                ptr = self.tete
                #depiler first node
                if self.tete.next is not None:
                    self.tete = self.tete.next
                else:
                    self.tete = None
                #add sont fils to the list
                if ptr.value.right is not None:
                    elements = Element()
                    elements.value = ptr.value.right
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements
                if ptr.value.left is not None:
                    elements = Element()
                    elements.value = ptr.value.left
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements

                painter.drawText(60, isfound*30+830,
                                 "Path to etat But : ")
                i = 15
                #go back to root and  draw colored stats to show the path
                while path.value is not None:
                    painter.drawText(i + 200, isfound * 30 + 830,
                                     path.value.data)
                    painter.setBrush(QColor(76, 175, 80))
                    painter.drawEllipse(int(path.value.x), int(path.value.y), 40, 40)
                    painter.drawText(QRectF(int(path.value.x), int(path.value.y), 40, 40), Qt.AlignCenter,
                                     path.value.data)
                    path.value = path.value.back
                    i = i + 15
            # the case that Node not the Node Goal
            else:
                # put the pointer in the head of list
                ptr = self.tete
                # remove the current Node from Noeud List
                if self.tete.next is not None:
                    self.tete = self.tete.next
                else:
                    self.tete = None
                # add Node fils xD if exist right or left
                if ptr.value.right is not None:
                    elements = Element()
                    elements.value = ptr.value.right
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements
                if ptr.value.left is not None:
                    elements = Element()
                    elements.value = ptr.value.left
                    if self.tete is not None:
                        elements.next = self.tete
                        self.tete = elements
                    else:
                        self.tete = elements
            # put the pointer in the first element of the list to draw Node list
            ptr = self.tete
            i = 0
            painter.drawText(1445, counter * 20 + 180, "{")
            while ptr is not None:
                painter.drawText(i * 14 + 1455, counter * 20 + 180, ptr.value.data)
                i = i + 1
                ptr = ptr.next
            painter.drawText(i * 14 + 1455, counter * 20 + 180, "}")
            counter = counter + 1
        #draw the error if ther's no solution
        if isfound == 0:
            painter.drawText(60, 870,
                             "Path to etat But : Node But n'exist pas")
    # BREADTH First Search Algorithme
    def BFSearchALL(self, painter):
        # draw first line
        painter.drawText(1280, 180, "-")
        painter.drawText(1445, 180, "{")
        if self.root is not None:
            painter.drawText(1455, 180, self.root.data)
        painter.drawText(1465, 180, "}")
        isfound = 0
        counter = 1
        #boucle jusqu'a la fin de file
        while self.tete is not None:
            painter.drawLine(1440, 140, 1440, counter * 24 + 110)
            painter.drawText(1280, counter * 20 + 180, self.tete.value.data)
            #testi si le noeud current est le node but
            if self.tete.value.data == self.text:
                painter.drawText(1300, counter * 20 + 180, "but")
                isfound = isfound+1
                path = Element()
                path = self.tete
                ptr = self.tete
                #ajouter les fils a la file
                if self.tete.value.left is not None:
                    elements = Element()
                    elements.value = self.tete.value.left
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
                if self.tete.value.right is not None:
                    elements = Element()
                    elements.value = self.tete.value.right
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
                painter.drawText(60, isfound * 30 + 830,
                                 "Path to etat But : ")
                i = 15
                #fait un retour en arrier pour obtenu le chemin et trace la route
                while path.value is not None:
                    painter.drawText(i + 200, isfound * 30+830,
                                     path.value.data)
                    painter.setBrush(QColor(0, 140, 186))
                    painter.drawEllipse(int(path.value.x), int(path.value.y), 40, 40)
                    painter.drawText(QRectF(int(path.value.x), int(path.value.y), 40, 40), Qt.AlignCenter,
                                     path.value.data)
                    path.value = path.value.back
                    i = i + 15
            #le cas ou le node n'est pas le node but
            else:
                ptr = self.tete
                if self.tete.value.left is not None:
                    elements = Element()
                    elements.value = self.tete.value.left
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
                if self.tete.value.right is not None:
                    elements = Element()
                    elements.value = self.tete.value.right
                    while ptr.next is not None:
                        ptr = ptr.next
                    ptr.next = elements
            #remove le node current est pointier sur le node suivant
            self.tete = self.tete.next
            ptr = self.tete
            i = 0
            painter.drawText(1445, counter * 20 + 180, "{")
            #draw list nodeee
            while ptr is not None:
                painter.drawText(i * 14 + 1455, counter * 20 + 180, ptr.value.data)
                i = i + 1
                ptr = ptr.next
            painter.drawText(i * 14 + 1455, counter * 20 + 180, "}")
            counter = counter + 1
        #if ther's no solution print Error
        if isfound == 0:
            painter.drawText(60, 870,
                             "Path to etat But : Node But n'exist pas <3 ")
    #function for painting
    def paintEvent(self, QPaintEvent):
        painter=QtGui.QPainter(self)
        painter.begin(self)
        self.painTree(painter)
        # Depth First Search Algorithme
        if self.witchButtonClicked==0:
            painter.end()
        if self.witchButtonClicked==1:
            self.DFSearch(painter)
            painter.end()
        #Breadth First Search Algorithme
        if self.witchButtonClicked==2:
            self.BFSearch(painter)
            painter.end()
        if self.witchButtonClicked==3:
            self.DFSearchALL(painter)
            painter.end()
        if self.witchButtonClicked==4:
            self.BFSearchALL(painter)
            painter.end()
    #when user click in BFS Button
    def BFS(self):
        self.tete=Element()
        self.tete.value=self.root
        if self.line.text()!="":
            self.text=self.line.text()
        else:
            self.line.setText("G")
        self.witchButtonClicked=2
        self.update()
    # when user click in BFS Button
    def DFS(self):
        self.tete = Element()
        self.tete.value = self.root
        if self.line.text() != "":
            self.text = self.line.text()
        else:
            self.line.setText("G")
        self.witchButtonClicked = 1
        self.update()
    # when user click in DFS ALL SOLUTIONS Button
    def DFSALL(self):
        self.tete = Element()
        self.tete.value = self.root
        if self.line.text() != "":
            self.text = self.line.text()
        else:
            self.line.setText("G")
        self.witchButtonClicked = 3
        self.update()
    # when user click in BFS ALL SOLUTIONS Button
    def BFSALL(self):
        self.tete = Element()
        self.tete.value = self.root
        if self.line.text() != "":
            self.text = self.line.text()
        else:
            self.line.setText("G")
        self.witchButtonClicked = 4
        self.update()
def main():
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()