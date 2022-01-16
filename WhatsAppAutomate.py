import pywhatkit

print("---------!!!!!!!_______!!!!!!!----------")
print("+++++------WHATSAPP MESSENGER------+++++")
print()
ph = input("Enter the Phone Number>> ")
mess = input("Enter the Message>> ")
hr = int(input("Enter the time>> \nhr>> "))
mi = int(input("min>> "))
pywhatkit.sendwhatmsg(ph, mess, hr, mi)