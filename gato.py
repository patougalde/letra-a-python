x=["1","o","1","o","1","o","1","o","1","o"]
posicion=int(input("ingresa la posicion de tiro"))
turno=input("ingresa 'x' o 'o'")
x[posicion]=turno
gato=f"{x[0]}|{x[1]}|{x[2]}|\n{x[3]}|{x[4]}|{x[5]}|\n{x[6]}|{x[7]}|{x[8]}|"
print(gato)