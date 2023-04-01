#Segunda Parte
##Problema 1 
###Paso1: Enteder el Problema

Es un programa que recibe una frase del usuario y nos dice si esta frase se puede leer de igual forma de derecha a izquierda y viceversa. Es decir que se tenga el mismo significado si se leen en ambos sentidos. 

###Paso2: Planear

El programa ocupa interfaz de usuario y los inputs son la frase y el output la respuesta si es un palindromo

Para este paso ocupamos el pseudocodigo. 

1. El usuario debe ingresar la frase. 
2. El programa debe de leer la frase de derecha a izquierda.
5. El programa debe guardar la ubicacion de cada letra y su valor. 
3. El programa debe luego leer la frase de izquierda a derecha.
8. El programa debe guardar la ubicacion de cada letra y su valor. 
4. El programa debe comparar si la frase es la misma al comparar que cada letra sea igual con su respectiva ubicacion de derecha a izquierda y viceversa. 
5. Si la frase es la misma el programa imprime que la frase es un palindromo
6. Si la frase es diferente, el programa imprime que la frase no es un palindromo. 


###Paso3: Dividir y conquistar

En este caso el problema es pequeno, pero se podria uno de los subproblemas podria ser guardar la ubicacion de cada letra y su valor. Y otro subproblema es comparar si la frase es la misma al comparar que cada letra sea igual con su respectiva ubicacion de derecha a izquierda y viceversa.
   

##Problema 2
###Paso1: Enteder el Problema

Se requiere un programa que borre los logs de un servidor excepto si tiene la palabra Error. Si los logs contienen la palabra Error, se debe copiar el log al directorio "Errores" e enviar un correo al administrador. 

###Paso2: Planear

No ocupa interfaz de usuario y los inputs son los logs y el output es el log que tenga la palabra error. 

Para eso ocupamos el pseudocodigo.

1. El programa debe de leer los logs constantemente. 
2. El programa debe buscar la palabra Error en los logs. 
3. Si encuentra la palabra Error, debe copiar ese log y guardarlo. 
7. El programa debe abrir el directorio Errores.
5. Debe copiar el log al directorio de Errores
6. Una vez copiada debe enviar un correo al administrador
4. De lo contrario debe de seguir leyendo los logs. 

###Paso3: Dividir y conquistar

Uno de los subproblemas es buscar la palabra Error y el otro subproblema es buscar el directorio y enviar el correo. 


##Problema 3
###Paso1: Enteder el Problema

El usuario ingresa un numero entero y el programa debe verificar si los digitos de este numero se pueden ordenar de forma que sea multiplo de 5. Por ejemplo, el numero 51 que si se cambia el orden de los digitos a 15, este ya es multiplo de 5. Para que sea multiplo de 5, el numero debe terminar en 5 o 0. 

###Paso2: Planear

El programa SI ocupa interfaz de usuario y el input es el numero que ingresa el usuario y los outputs son el nuevo numero multiplo de 5 o la respuesta de que no se puede reordenar para que sea multiplo de 5. 

Para eso ocupamos el pseudocodigo.

1. El usuario debe ingresar un numero. 
2. El programa debe leer los digitos de ese numero
3. El programa debe determinar si el numero tiene un 0 o un 5. 
7. Si tiene numero 0 o 5, debe colocar cualquiera de esos digitos de ultimo.
5. Luego debe imprimir el nuevo numero que es multiplo de 5
6. En caso contrario que no tengo 0 o 5, debe imprimir que no puede arreglarse para que sea multiplo de 5. 

###Paso1: Dividir y conquistar

Uno de los subproblemas seria encontrar el 0 o el 5 y el otro subproblema es colocar estos digitos de ultimo en el numero. 
