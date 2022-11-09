class Calc:

    def addition_int(self, x, y):
        return x + y

    def addition_int_array(self, int_array):
        y = 0
        for x in int_array:
            y += x

        return y

    def validate_result(self, x, y):
        if x == y:
            return True
        else:
            return False
