'''Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?'''


class one:
    arr = []
    num = 0

    def find(self, i, el):
        for k in range(i, len(self.arr)):
            if el == self.arr[k]:
                print("FOUND")
                return k

        return

    def accept(self):
        self.num = int(input("Enter number to be found"))
        n = int(input("Enter array length"))
        self.arr = [None]*n
        for i in range(0, n):
            self.arr[i] = int(input("Enter number"))

    def one_pass(self):
        for i in range(0, len(self.arr)):
            dif = self.num - self.arr[i]
            if dif == 0:
                print("FOUND")
                return
            elif dif > 0:
                self.find(i, dif)


if __name__ == "__main__":
    obj = one()
    obj.accept()
    obj.one_pass()
