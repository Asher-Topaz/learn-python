str = 'X-DSPAM-Confidence:0.8475'

str2 = str.find(':')
print(str2)

str3 = str[str2+1 :]
print(float(str3))

type_of_value= type(str3)
print(type_of_value)


