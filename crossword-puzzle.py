#!/bin/python3

# https://www.hackerrank.com/challenges/crossword-puzzle

import math
import os
import random
import re
import sys


def fill_word(crossword, x, y, s, isHorizontal=True):
    c = crossword[:]
    for i in range(len(s)):
        if isHorizontal:
            if c[y][x+i] == s[i] or c[y][x+i] == "-":
                c[y] = c[y][:x+i] + s[i] + c[y][x+i+1:]
            else:
                return None
        else:
            if c[y+i][x] == s[i] or c[y+i][x] == "-":
                c[y+i] = c[y+i][:x]+ s[i] + c[y+i][x+1:]
            else:
                return None
    return c


def find_slots(crossword):
    slots = []
    # Iterate rows
    rowNum = 0
    for row in crossword:
        count = 1
        for i in range(1, len(row)):
            if row[i-1] == row[i]:
                count += 1
            else:
                if row[i-1] == "-":
                    slots.append((i-count,rowNum,True,count))
                count = 1
        if row[i-1] == "-":
            slots.append((i+1-count,rowNum,True,count))
        rowNum += 1

    # Iterate cols
    for i in range(len(crossword[0])):
        count = 1
        for j in range(1,len(crossword)):
            if crossword[j-1][i] == crossword[j][i]:
                count += 1
            else:
                if crossword[j-1][i] == "-":
                    slots.append((i,j-count,False,count))
                count = 1
        if crossword[j-1][i] == "-":
            slots.append((i,j+1-count,False,count))
    return slots


def fill_recursive(crossword, hints, slots):
    if len(hints) == 0:
        return crossword
    for i in range(len(hints)):
        for j in range(len(slots)):
            if slots[j][3] == len(hints[i]):
                cur_crossword = fill_word(crossword,
                    slots[j][0], slots[j][1], hints[i], slots[j][2])
                if cur_crossword is None:
                    break
                x = fill_recursive(cur_crossword,
                    hints[:i] + hints[i + 1:],
                    slots[:j] + slots[j + 1:])
                if x: return x
        else:
            continue
        break


def crossword_puzzle(crossword, hints):
    slots = find_slots(crossword)
    filled = fill_recursive(crossword, hints, slots)
    return filled


if __name__ == '__main__':
    # crossword = [
    #     "+-++++++++",
    #     "+-++++++++",
    #     "+-------++",
    #     "+-++++++++",
    #     "+-++++++++",
    #     "+------+++",
    #     "+-+++-++++",
    #     "+++++-++++",
    #     "+++++-++++",
    #     "++++++++++"
    # ]
    # hints = "AGRA;NORWAY;ENGLAND;GWALIOR"
    # crossword = [
    #     "+-++++++++",
    #     "+-++++++++",
    #     "+-++++++++",
    #     "+-----++++",
    #     "+-+++-++++",
    #     "+-+++-++++",
    #     "+++++-++++",
    #     "++------++",
    #     "+++++-++++",
    #     "+++++-++++"
    # ]
    # hints = "LONDON;DELHI;ICELAND;ANKARA"
    crossword = [
        "+-++++++++",
        "+-------++",
        "+-++-+++++",
        "+-------++",
        "+-++-++++-",
        "+-++-++++-",
        "+-++------",
        "+++++++++-",
        "++++++++++",
        "++++++++++"
    ]
    hints = "ANDAMAN;MANIPUR;ICELAND;ALLEPY;YANGON;PUNE"

    result = crossword_puzzle(crossword, hints.split(";"))
    print('\n'.join(result))
