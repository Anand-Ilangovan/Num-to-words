class NumberToWords:
    def __init__(self):
        self.units = [" Zero "," one"," two"," three", " four", " five", " six", " seven", " eight", " nine"]
        self.teens = ["", " eleven", " twelve", " thirteen", " fourteen", " fifteen", " sixteen", " seventeen", " eighteen", " nineteen"]
        self.tens = ["", " ten", " twenty", " thirty", " forty", " fifty", " sixty", " seventy", " eighty", " ninety"]

    def less_than_hun(self, num):
        if num == 0:
            return "Zero"
        elif 1 <= num <= 9:
            return self.units[num]
        elif 11 <= num <= 19:
            return self.teens[num % 10]
        elif 10 <= num <= 90 and num % 10 == 0:
            return self.tens[num // 10]
        elif 21 <= num <= 99:
            return self.tens[num // 10] + " " + self.units[num % 10]

    def less_than_tho(self, num):
        num = int(num)
        if num < 100:
            return self.less_than_hun(num)
        a = num // 100
        b = num % 100
        if b == 0:
            return self.units[a] + " Hundred  "
        else:
            return self.units[a] + " Hundred " + self.less_than_hun(b)

    def less_than_lak(self, num):
        if num < 1000:
            return self.less_than_tho(num)
        a = num // 1000
        b = num % 1000
        if 1 <= a <= 9:
            if b == 0:
                return self.units[a] + " Thousand  "
            else:
                return self.less_than_hun(a) + " Thousand " + self.less_than_tho(b)
        elif b == 0:
            return self.tens[a // 10] + " Thousand  "
        else:
            return self.less_than_hun(a) + " Thousand " + self.less_than_tho(b)

    def less_than_cro(self, num):
        if num < 100000:
            return self.less_than_lak(num)
        a = num // 100000
        b = num % 100000
        if 1 <= a <= 9:
            if b == 0:
                return self.units[a] + " Lakh  "
            else:
                return self.less_than_hun(a) + " Lakh " + self.less_than_lak(b)
        elif b == 0:
            return self.tens[a // 10] + " Lakh  "
        else:
            return self.less_than_hun(a) + " Lakh " + self.less_than_lak(b)

    def less_than_100_cro(self, num):
        if num < 1000000:
            return self.less_than_cro(num)
        a = num // 10000000
        b = num % 10000000
        if 1 <= a <= 9:
            if b == 0:
                return self.units[a] + " Crore  "
            else:
                return self.less_than_lak(a) + " Crore" + self.less_than_cro(b)
        elif b == 0:
            return self.tens[a // 10] + " Crore  "
        else:
            return self.less_than_lak(a) + " Crore " + self.less_than_cro(b)

    def num_to_words(self, num):
        try:
            if num == '':
                return "Zero " + self.decimal(num)
            elif num == '-':
                return "Minus Zero "
            num = int(num)
            if num < 0:
                return "Minus" + self.num_to_words(abs(num))
            if num < 100:
                return self.less_than_hun(num)
            elif num < 1000:
                return self.less_than_tho(num)
            elif num < 100000:
                return self.less_than_lak(num)
            elif num < 10000000:
                return self.less_than_cro(num)
            else:
                return self.less_than_100_cro(num)
        except(TypeError) as t:
            return 'Number Out Of Range'
        except(ValueError) as v:
            return 'Not a valid Number'
        except(IndexError) as e:
            return "index out of range"

    def decimal(self, num):
        dec = ''
        for i in str(num):
            dec += self.units[int(i)]
        return dec


while True:
    num = input("Enter the Number: ")
    number_to_words = NumberToWords()
    if num.__contains__('.'):
        if num.startswith('-'):
            num, num1 = num.split(sep='.')
            if num1:
                print("" + number_to_words.num_to_words(num) + " Point " + number_to_words.decimal(num1))
            elif num1=='':
                print(" Minus Zero Point Zero ")
            else:
                print("Minus " + number_to_words.num_to_words(num))
        else:
            num, num1 = num.split(sep='.')
            if num:
                if num1:
                    print(number_to_words.num_to_words(num) + " Point " + number_to_words.decimal(num1))

                else:
                    print(number_to_words.num_to_words(num))
            else:
                if num1:
                    print("Zero Point " + number_to_words.decimal(num1))
                else:
                    print("zero")
    else:
        print(number_to_words.num_to_words(num))
