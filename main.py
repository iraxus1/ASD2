from queue import PriorityQueue
from writeandread import readTxt
from writeandread import writeFileByte
from writeandread import writeFileStr
from node import Node


# zliczane znakow
def countFrequency(text):
    frequency = {}
    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency


# tworzenie drzewa
def createTree(text):
    occurences = countFrequency(text)
    nodes = PriorityQueue()
    for c in occurences.keys():  # dodajemy do listy
        node = Node(occurences[c], c)
        nodes.put(node)
    rootNode = None  # korzen drzewa
    while nodes.qsize() > 1:
        n1 = nodes.get()  # pobieramy pierwszy najmniejszy element
        n2 = nodes.get()  # pobieramy nastepny najmniejszy element
        # jeżeli oba liście mają tą samą wartość, a jeden z nich jest kontenerem, to powinien on być traktowany jako większy element
        if n1.value == n2.value and not n1.isLeaf():
            pom = n1  # dlatego w takiej sytuacji podmieniamy wskaźniki
            n1 = n2
            n2 = pom
        # tworzymy liść-kontener, który będzie przechowywać dwa powyższe elementy i sumę ich wartości
        parent = Node(n1.value + n2.value, "")
        rootNode = parent  # aktualny korzen
        parent.left = n1  # dodajemy dzieci
        parent.right = n2
        nodes.put(parent)  # dodajemy go do PriorityQueue
    return rootNode  #zwracamy korzeń


# kodowanie
def encryption(node, str, txt):
    if node is None:  # koniec
        return txt  # przerywamy
    if node.isLeaf():  # jeżeli przechowuje on znak
        slownik = node.character + " : " + str + "\n"  # przenoszenie do slownika
        writeFileStr(slownik)  # zapis do pliku
        txt = txt.replace(node.character, str)  # podmiana znaku w tekście z zakodowaną wartościa
    txt = encryption(node.left, str + "0", txt)  # podmiana dla lewej części drzewa
    txt = encryption(node.right, str + "1", txt)  # podmiana dla prawej części drzewa
    return txt


word = readTxt("tekst_genertaor.txt")  # wczytywanie
rootNode = createTree(word)
word = encryption(rootNode, "", word)
writeFileByte(word)  # zapisywanie do pliku
