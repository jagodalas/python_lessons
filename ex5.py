#  1- sprwadzi w int co to jest fibbonchi sequence
# 2 znalezc implementacje fibbonachi sequence w pythonie
a = 0
b = 1
for x in range (0,10):
    #temp = a 
    #a = b

    #b = temp + b
    a,b = b, a + b
    print b
