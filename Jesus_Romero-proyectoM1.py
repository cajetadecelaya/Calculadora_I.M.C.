# #Calculadora de indice de masa corporal.

nombre = input('Ingrese su nombre: ')
while not nombre.isalpha():
    print('!DATO INVALIDO¡')
    nombre = input('Ingrese su nombre: ')

    """Inicialmente se solicita ingresar el nombre y con el ciclo 'white' se le obrliga al usuario a ingresar
     caracteres alfanumericas """
    

apellpaterno = input('Ingrese su apellido paterno: ')
while not apellpaterno.isalpha():
    print('!DATO INVALIDO¡')
    apellpaterno = input('Ingrese su apellido paterno: ')
    """Se solicita ingresar el primer apellido y con el ciclo 'white'  y funcion '.isalpha'se le obliga al usuario a ingresar
     caracteres alfanumericas """
  

apellmaterno = input('Ingrese su apellido materno: ')
while not apellmaterno.isalpha():
    print('!DATO INVALIDO¡')
    apellmaterno = input('Ingrese su apellido materno: ') 
    """Se solicita ingresar el segundo apellido y con el ciclo 'white'  y funcion '.isalpha'se le obliga al usuario a ingresar
     caracteres alfanumericas """


edad = input('Ingrese su edad en años cumplidos: ')
while not edad.isdigit():
    print('!DATO INVALIDO¡')
    edad = (input('Ingrese su edad en años cumplidos: '))
    """Se solicita ingresar la edad y con el ciclo 'white'  y funcion '.isdigit'se le obliga al usuario a ingresar
     numeros enteros """


while True:
    try:
        peso = float(input('Ingrese su peso en kilogramos: '))
        break
    except ValueError:
        print('!DATO INVALIDO¡')
    """con esta condicional aseguramos que se ingrese numeros float para el calculo correcto de la calculadora, 
    de lo contrario no dejara pasar al siguiente bloque"""


while True:
    try:
        estatura = float(input('Ingrese su estatura: '))
        break
    except ValueError:
        print('!DATO INVALIDO¡')
    """con esta condicional aseguramos que se ingrese numeros float para el calculo correcto de la calculadora, 
    de lo contrario no dejara pasar al siguiente bloque"""


imc = (peso / (estatura**2))
print(f'Nombre comprero del paciente: {nombre.title()} {apellpaterno.title()} {apellmaterno.title()}')
print(f'Edad: {edad}.')
print(f'Con un peso de {peso} Kg.',end='')
print(' Y una estatura de ' + str(estatura) + ' metros.')
print('Su IMC es: ' +'{:.2f}'.format(imc)) # el resultado de IMC se dedondea a 2 decimales.
"""De primera instalcia, nos imprimira los datos generales ingresados por el ususario y 
    despues arroja su Indice de Masa Corporal, se especifico con '{:.2f}' que en el resultado 
    solo arrojara dos numero decimales, esto por facilidad al interpretar los datos"""


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
"""Con esta serie de condicionales lograremos definir su condicion fisica antes de imprimir un resultado"""


print('Alimentese saludablemente.')
