first_number = input(
    "enter a number: "
    )
second_number = input(
    "enter another number: "
)
arithmetc_sign = input(
    "enter an arithmetic sign (+,-,*,/,%): "
)


if arithmetc_sign == "+":
    print(first_number ,arithmetc_sign ,second_number," = ",int(first_number) + int(second_number))
elif arithmetc_sign == "-":
    print(first_number ,arithmetc_sign ,second_number," = ",int(first_number) - int(second_number))
elif arithmetc_sign == "*":
    print(first_number ,arithmetc_sign ,second_number," = ",int(first_number) * int(second_number))
elif arithmetc_sign == "/":
    print(first_number ,arithmetc_sign ,second_number," = ",int(first_number) / int(second_number))
elif arithmetc_sign == "%":
    print(first_number ,arithmetc_sign ,second_number," = ",int(first_number) % int(second_number))
else:
    print("invalid arithmetic sign")

