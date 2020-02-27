import os

host = "200.33.171."

i = 1
total = 0

while i < 256:
    respuesta = os.system("ping " + host + str(i))
    
    if respuesta == 0:
        print(host + str(i) + " está funcionando")
        total = total + 1
    else:
        print(host + str(i) + " no está funcionando")
    i = i + 1

print("Finalizado, número total de hosts en el ITM: " + total)