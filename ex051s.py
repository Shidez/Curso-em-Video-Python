print('Progressão aritmética')

primeiro=int(input("Primeiro elemento: "))
razao = int(input("Razao: "))

ultimo = primeiro + (11-1)*razao

for var in range(primeiro, ultimo, razao):
    print(var)