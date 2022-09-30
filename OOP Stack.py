

NULL_POINTER=-1
class Stack():
    def __init__(self, max_capacity):
        self.__top = NULL_POINTER
        self.__free = 0
        self.__size = 0
        self.__items = ["" for i in range(max_capacity)]


    def print_stack(self):
        print(self.__items)


    def push(self,new_item):
        if self.__size <len(self.__items):
            self.__items[self.__free] = new_item
            self.__top = self.__free
            self.__free+=1
            self.__size+=1
        else:
            print("no more space")

students = Stack(3)
students.print_stack()

students.push("Nelson")
students.push("Stephen")
students.push("Moodi")
students.push("Kemp")
students.print_stack()



# def Pop():
#  if TopPointer < 0 :
#   return -1
#  else:
#  Value = DataStack(TopPointer)
#   TopPointer= TopPointer – 1
#   return Value


