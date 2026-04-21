
import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "Sofía", "Carlos", "María"],
    "Edad": [20, 22, 19, 21, 23],
    "Carrera": ["Ingeniería", "Derecho", "Medicina", "Ingeniería", "Derecho"]
}

df = pd.DataFrame(datos)

print("DataFrame completo:")
print(df)

print("\nEstudiantes de Ingeniería:")
print(df[df["Carrera"] == "Ingeniería"])


print("\nMayores de 20 años:")
print(df[df["Edad"] > 20])


print("\nDerecho y mayores de 21:")
print(df[(df["Carrera"] == "Derecho") & (df["Edad"] > 21)])

df["Mayor_de_edad"] = df["Edad"] >= 21

print("\nDataFrame con nueva columna:")
print(df)

print("\nSolo mayores de edad (>=21):")
print(df[df["Mayor_de_edad"] == True])


print("\nColumna Edad:")
print(df["Edad"])


print("\nPromedio de edad:")
print(df["Edad"].mean())

print("\nCantidad por carrera:")
print(df["Carrera"].value_counts())
