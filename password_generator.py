import random
lower_value=("abcdefghujkohlshj")
upper_value=("ABCDEFGHJIKLLJUTYRSXZV")
symbols_value=("0123456789")
Numbers_value=("{[]},.<>/?_")

all= lower_value +upper_value + symbols_value + Numbers_value

length= 10

password= "".join(random.sample(all,length))
print(password)
