# Gonna try to make it as a console application first


class Regularity:
    """Is used to create sequence and find regularities"""
    def __init__(self):
        """Creates new sequence"""
        self.reg = []
        print('Последовательность создана. Продолжайте вводить числа, когда захотите закончить, введите "С" или "S"')
        while True:
            number = input("Введите число: ")
            # Only integers yet >
            try:
                number = int(number)
            except ValueError:
                if number.upper() == "С" or number.upper() == "S":
                    print("Принято.")
                    break
                print("Value error occurred! Пожалуйста, введите число (int)")
                continue
            self.reg.append(number)

    def find_dependencies(self):
        if len(self.reg) < 3:
            print("Длина последовательности слишком мала.")
            # concatenate "Хотите попробовать... и т.д." /
            # offer to test low-reliable mode and ask input as answer, add 'if-else' and so on..>
            return 1
        # Could be written as the assignment at the same time as the initialization,
        # ..but I am afraid that this may be too resource-intensive
        # result = {}
        # # result must match the sample -> 'parameter': (0 or 1 for success or failure respectively, additional value)
        # result['arithmetic_progression'] = self.check_arithmetic()
        # result['geometric_progression'] = self.check_geometric()

        # removed array thing, for now would just call func's consistently
        result = self.check_arithmetic()
        if result[0] == 0:
            if result[1] == 0:
                print("Арифметическая и геометрическая прогрессия с разностью 0 или знаменателем 1")
                return 0
            print("Это арифметическая прогрессия, разность - d=" + str(result[1]))
            return 0
        result = self.check_geometric()
        if result[0] == 0:
            print("Это геометрическая прогрессия, знаменатель - r=" + str(result[1]))
            return 0

    def check_arithmetic(self):
        # find difference of potential progression
        d = self.reg[1] - self.reg[0]
        # check if it is an arithmetic progression by adding difference to the second number
        if self.reg[1] + d == self.reg[2]:
            return 0, d
        else:
            return 1, None  # follow pattern just in case, maybe it's redundant~

    def check_geometric(self):
        # find common ratio
        r = self.reg[1] / self.reg[0]
        # check if it is a geometric progression by multiplying the second number by the common ratio
        if self.reg[1] * r == self.reg[2]:
            return 0, r
        else:
            return 1, None


def start():
    reg = Regularity()
    reg.find_dependencies()


if __name__ == '__main__':
    start()
