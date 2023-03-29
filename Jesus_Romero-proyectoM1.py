# #Calculadora de indice de masa corporal.

nombre = input('Ingrese su nombre: ')
while not nombre.isalpha():
    print('!DATO INVALIDO¡')
    nombre = input('Ingrese su nombre: ')
    
apellpaterno = input('Ingrese su apellido paterno: ')
while not apellpaterno.isalpha():
    print('!DATO INVALIDO¡')
    apellpaterno = input('Ingrese su apellido paterno: ')
  
apellmaterno = input('Ingrese su apellido materno: ')
while not apellmaterno.isalpha():
    print('!DATO INVALIDO¡')
    apellmaterno = input('Ingrese su apellido materno: ') 

edad = input('Ingrese su edad en años cumplidos: ')
while not edad.isdigit():
    print('!DATO INVALIDO¡')
    edad = (input('Ingrese su edad en años cumplidos: '))

while True:
    try:
        peso = float(input('Ingrese su peso en kilogramos: '))
        break
    except ValueError:
        print('!DATO INVALIDO¡')


while True:
    try:
        estatura = float(input('Ingrese su estatura: '))
        break
    except ValueError:
        print('!DATO INVALIDO¡')

imc = (peso / (estatura**2))
print(f'Nombre comprero del paciente: {nombre.title()} {apellpaterno.title()} {apellmaterno.title()}')
print(f'Edad: {edad}.')
print(f'Con un peso de {peso} Kg.',end='')
print(' Y una estatura de ' + str(estatura) + ' metros.')
print('Su IMC es: ' +'{:.2f}'.format(imc)) # el resultado de IMC se dedondea a 2 decimales.

if imc < 18.9:
    print('!Come todos los tamales posibles, estas desapareciendo¡\n')

elif imc >= 18.9 and imc <= 24.99:
    print('!Su peso normal¡\n')

elif imc >= 25 and imc <= 29.99:
    print('!Tiene sobrepeso¡\n')

elif imc >=30 and imc <= 34.99:
    print('!Cuenta con obesidad leve¡\n')

elif imc >=35 and imc <= 39.99:
    print('!Estas medio obeso, bajale a los tacos¡\n')  

elif imc >=40:
    print('!Visite a su doctor lo antes posible¡\n! Su obesidad es mordiba¡\n')      

print('Alimentese saludablemente.')
