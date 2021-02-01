from main import *

class dec:
    def __init__(self, _self):
        self.entry = int(setup._input(_self))
        setup.insert(_self, self.dec_to_bin(), self.dec_to_hex())


    def dec_to_bin(self):
        print("dec_to_bin")
        return bin(self.entry)

    def dec_to_hex(self):
        print("dec_to_hex")
        return hex(self.entry)

class Hex:
    def __init__(self, _self):
        self.entry = str(setup._input(_self))
        self.h = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.output = 0
        self._self = _self
        setup.insert(_self, self.hex_to_dec(), self.hex_to_bin())

    def power(self, input2, power):
        print(f"power {power}")
        if power == 0:
            return input2
        else:
            return int(input2 * 16 ** power)

    def hex_to_dec(self):
        print("hex_to_dec")
        # uitfilteren 0x
        input = ""
        for place in range(2, len(self.entry)):
            input = input + self.entry[int(place)]

        # omdraaien caracters
        input2 = ""
        for place in range(int(len(input) - 1), -1, -1 ):
            input2 = input2 + input[place]

        print(input2)   # debugging

        if len(input2) > 32:
            setup.ERROR(self._self, "OUT OF RANGE", "MAX DIGITS:32")
        else:

            for place in range(0, len(input2)):
                for number in range(0, 10):
                    if input2[place] == "a":
                        self.h[place] = self.power(10, place)
                        break

                    elif input2[place] == "b":
                        self.h[place] = self.power(11, place)
                        break

                    elif input2[place] == "c":
                        self.h[place] = self.power(12, place)
                        break

                    elif input2[place] == "d":
                        self.h[place] = self.power(13, place)
                        break

                    elif input2[place] == "e":
                        self.h[place] = self.power(14, place)
                        break

                    elif input2[place] == "f":
                        self.h[place] = self.power(15, place)
                        break

                    elif input2[place] == str(number):
                        self.h[place] = self.power(number, place)
                        break


                    setup.ERROR(self._self, "SYNTAX ERROR", "")
                    

            for i in range(0, len(input2)):
                self.output += self.h[i]

            return self.output




    def hex_to_bin(self):
        print("hex_to_bin")
        return bin(self.output)

class Bin:
    def __init__(self, _self):
        self.entry = str(setup._input(_self))
        self.output = 0
        self._self = _self
        setup.insert(_self, self.bin_to_dec(), self.bin_to_hex())

    def bin_to_dec(self):
        print("bin_to_dec")

        # uitfilteren 0b
        input = ""
        for place in range(2, len(self.entry)):
            input = input + self.entry[int(place)]

        # omdraaien caracters
        input2 = ""
        for place in range(int(len(input) - 1), -1, -1):
            input2 = input2 + input[place]

        print(input2)  # debugging

        for place in range(0, len(input2)):
            if input2[place] != 1 or input2[place] != 0:
                self.output += int(input2[int(place)]) * int(2 ** place)
            else:
                setup.ERROR(self._self, "SYNTAX ERROR", "ONLY USE 1 AND 0")

        return self.output



    def bin_to_hex(self):
        return hex(int(self.output))

