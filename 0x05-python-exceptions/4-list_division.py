#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_lenghth):
    new_list = []
    for i in range(list_lenghth):
        try:
            division = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            division = 0
        except ZeroDivisionError:
            print("division by 0")
            division = 0
        except IndexError:
            print("out of range")
            division = 0
        finally:
            new_list.append(division)
    return new_list
