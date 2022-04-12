# -*- coding: utf-8 -*
from josephus_iter import JosephusCircle


if __name__ == "__main__":
    number, step, start = map(int, input("请输入参与游戏人数,步长和开始位置（用空格隔开）：").split())
    josephus_list = list(range(1, number+1))
    print("约瑟夫环人员弹出顺序：")
    for person in JosephusCircle(josephus_list, step, start):
        print(person)