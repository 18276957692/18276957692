# -*- coding: utf-8 -*

class JosephusCircle(list):
    def __init__(self, people_list, step, start):
        assert step > 0
        self.people_list = people_list
        self.step = step
        self.start = start
        self.josephus_list = []

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.people_list) > 0:
            self.start = (self.start + self.step - 1) % len(self.people_list)
            self.josephus_list.append(self.people_list.pop(self.start))
            return self.josephus_list[-1]
        else:
            raise StopIteration


if __name__ == "__main__":
    number, step, start = map(int, input("请输入参与游戏人数,步长和开始位置（用空格隔开）：").split())
    josephus_list = list(range(1, number+1))
    print("约瑟夫环人员弹出顺序：")
    for person in JosephusCircle(josephus_list, step, start):
        print(person)
