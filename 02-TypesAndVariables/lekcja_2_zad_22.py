amount = 15.84
vat = amount*0.23

# {:20.2f}
# 20 ilosc znakow do zapisu czesci calkowitej

string_template = """Amount  : {:20.2f} zł 
VAT 23% : {:20.2f} zł"""

print(string_template.format(amount, vat))


print("Test: {:6.20f}".format(2))
