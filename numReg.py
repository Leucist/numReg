# Gonna try to make it as a console application first


class Regularity:
    """Is used to handle and modify the regularity"""
    def __init__(self):
        """Creates new regularity"""
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
        result = {}
        # result must match the sample -> 'parameter': (0 or 1 for success or failure respectively, additional value)
        result['arithmetic_progression'] = self.check_arithmetic()

    def check_arithmetic(self):
        # finding difference of potential progression
        d = self.reg[1] - self.reg[0]
        if self.reg[1] + d == self.reg[2]:
            return 0, d
        else:
            return 1, None  # follow pattern just in case, maybe it's redundant~

    def check_geometric(self):
        pass


def start():
    reg = Regularity()
    reg.find_dependencies()


if __name__ == '__main__':
    start()
