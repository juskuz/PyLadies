def arb_2_rom(number):
    rom=""
    d=[
        [900, 1000, "M", "CM"],
        [400, 500, "D", "CD"],
        [90, 100, "C", "XC"],
        [40, 50, "L", "XL"],
        [9, 10, "X", "IX"],
        [4, 5, "V", "IV"]
    ]
    for l in d:
        if number >=l[0]:
            dig = number //(l[1])
            rom += l[2] * dig
            if dig == 0:
                rom += l[3]
                dig += 1
            number -= dig * (l[1])
    rom += "I" * number
    return rom

print(arb_2_rom(123))
print(arb_2_rom(1164))
print(arb_2_rom(3338))