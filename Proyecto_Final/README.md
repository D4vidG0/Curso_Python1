**Autor: DAVID GONZALEZ** 

**Nombre del proyecto: Juego de 21 (BLACKJACK)** 

---

## Descripción del proyecto

Este proyecto consiste en una aplicacion para un juego de cartas llamado "21", aka BlackJack. Ademas cuenta con una base de datos de usuarios y puede observarse las estadisticas de dicho usuario. La aplicacion es para solo 1 jugador y realiza la partida contra la "Casa" que es manejada por la computadora. 

## Diseño de la solución

Para la solucion de este proyecto, me base en las lecciones y el ejemplo visto en clase. Cree un modulo para: la carta, la baraja, la mano del jugador y la casa, la mesa, las reglas, los archivos txt, jugadores y el main. En total son 8 modulos que constituyen la totalidad del programa. 

Decidi realizar esta arquitectura porque es mas facil separar los conceptos como por ejemplo un modulo para la carta y otro para la baraja. Tambien decidi crear el modulo de mesa que representa como si fuera la mesa donde se reparten las cartas y el modulo jugador sirve para reunir todo lo relacionado al jugador: eleccion del jugador, repartir cartas,partidas de jugador, etc. Otro modulo importante es el de logs, en el cual me base en las tareas anteriores y este modulo agrupa todo lo relacionado con la creacion y lectura de los archivos txt. Por ultimo el modulo Main, es el modulo principal donde esta el menu principal y desde este modulo se llaman a las demas funciones. 

A continuacion se presenta una descripcion de cada modulo:

### Carta:

Con este modulo se crea la clase carta y le entra al valor y el palo, y esta a su vez devuelve el valor con su repectivo palo. 

### Baraja

Este modulo, nos crea la clase Baraja, tomando los valores y palos de una lista que se encuentra en el modulo y une los valores con el palo. Tambien se define el metodo barajar, el cual baraja el mazo con el metodo shuffle. 

Se define tambien el metodo repartir_carta y lo que hace es tomar el primer elemento de la lista y simula como cuando se reparten las cartas de un mazo. 

Tambien aqui cree el metodo print_mazo para imprimir el mazo y realizar pruebas. Decidi dejar este modulo porque puede ser util para corregir errores en el codigo a futuro o tambien por si se decide expandir el codigo con otras funciones. 

### Mano

Este modulo es para crear tanto la mano del jugador como de la casa y se crea la clase Mano. Cree un diccionario con los valores y palos, de esta manera las K, Q y J con valor de 10. Tambien cree el metodo mostrar_mano para imprimir la mano del jugador o de la casa. Dentro de este metodo cree la variable esbot para definir que es un "bot" o en otras palabras para representar a la computadora y me muestra una carta tapada. 

Otro metodo es agregar_carta, el cual agrega la carta y la guarda en una lista. Tambien guarda el valor de la carta. 

El metodo valor_mano se creo para sacar el valor de la mano y que se vaya sumando cada carta nueva que se agregue. 

Por ultimo, el metodo valor_carta me guarda al valor de cada carta en una lista y la regresa solo con los valores (sin palo).

### Mesa

Este metdoo simula la mesa donde se reparten las cartas. Cree la clase Juego, donde se guardan las manos del jugador y de la Casa y a su vez se reparten 2 cartas para simular cuando se reparten las primeras cartas. 

### Jugador

Este modulo es el mas extenso y aqui cree varias funciones para simular todo lo relacionado al jugador. Cree la funcion repartir_jugador para preguntarle al jugador si desea mas carta. Aca tambien viene lo de las manos especiales, las cuales se asignaron los valores de 210,211 como indicadores de que el jugador tiene una mano especial. Esta funcion recibe la mano el jugador y el mazo. 

Con la funcion repartir_casa que recibe una mano de la Casa y el mazo, y simula la logica que debe de seguir la compu. La logica es que si tiene menor que 14 que pida otra carta. Tambien si la carta que recibio no suma en total 17, entonces pide otra carta y al final retorna el valor de la mano. 

Esta funcion elegir_usuario simula el menu y dentro de la misma se puede escoger un usuario nuevo o un usuario existente. Para esto, se obtiene los usuario del modulo logs, donde esta el archivo txt llamado base de datos y contiene una lista de todos los usuarios. 

Por ultimo, la funcion Partida simula ya la partida contra la computadora. Dentro de esta funcion vienen las manos especiales y si no se cumple con eso, reparte a la casa y determina quien gana utilizando el modulo de reglas. 

### Reglas

En este modulo, viene todas la reglas para determinar quien gana si el Jugador o la Casa. Obtiene de la base de datos los usuarios y los guarda en una lista

### Logs

Aca en este modulo vienen todo lo relacionado a los archivos txt para guardar los usuarios y las estadisticas. Esta funcion crear_base crea el archivo base de datos.txt para guardar los usuarios. La funcion base_resultado agrega usuario a la base de datos.

La funcion obtener_usario obtiene de la base de datos los usuarios y los guarda en una lista. 

Otra funcion es estadisticas_usuario crea archivo unico de estadistica para cada usuario. Las estadisticas que se guardan son el nombre del usuario, la fecha y si gano y perdio. 

Esta funcion obtener_stats obtiene las estadisticas de cada usuario. Tambien determina si el usuario existe pero no ha jugado una partida, entonces nos tira un error. 

### Main

Este modulo es el principal y junta las funciones de los otros modulos. 

## Manual de usuario

Pequeño manual de usuario que describa cada acción que se puede realizar en la aplicación y qué _inputs_ se esperan para cada una.

Aca se presenta el manual de usuario para la aplicacion. 

### Menu Principal

- Al ingresar a la aplicacion debe de elegir si desea un juego nuevo o si quiere ver la estadisticas de un jugador.
- Si se escribe otra cosa, se tira un error y regresa al menu principal. 
- Si elegi el juego nuevo, se presentaran las opciones de si se desea un usuario nuevo o uno existente.
- Si debe elegir Salir desde este menu para salir del programa. 

### Eleccion de usuarios

- Si se elige la opcion de usuario nuevo, se tiene que indicar si desea continuar ingresando el jugador nuevo. Si elegi N (No) se regresa al menu principal. Si se eligi Y, se continua escribiendo el nombre. 
- El nombre se convertira todo a mayusculas y se guardara. Luego se da la bienvenida y se procede con la partida.
- Si se elige un usuario existente, se mostrara una lista con todos los usarios y se elegi Y para continuar y N para regresar al menu principal. 
- Si se escribe cualquier otra cosa, se muestra un error y se regresa al menu principal. 


### Partida de 21

- Una vez en la partida, se debe escoger si se desea una carta nueva o no.
- Si se pasa de 21, se presenta un mensaje de que el jugador perdio y se retorna al menu principal para que el jugador vea si desea un juego nuevo o ver las estadisticas. 
- Si el usuario decide que no quiere mas cartas, se procede con la jugada de la casa. 
- Se muestra la mano de la casa (con una carta tapada) y el valor total de la mano.
- Luego se ve quien gana, si la casa o el jugador.
- Finalmente, el programa se devuelve automaticamente al menu principal para que el jugador vea si desea un juego nuevo o ver las estadisticas. 
- Si el usuario tiene tres 7 en su mano, gana automaticamente.
- Si el usuario tiene 5 menores, gana automaticamente
- Si el usuario tiene una carta con valor de 10 (10,J,Q,K) y un A, gana automaticamente. 
- En caso de que ambos manos sean iguales, gana la casa. 

### Estadisticas de usuario

- Cuando se elegi la opcion de estadisticas de usuarios, se muestra una lista con los usuarios existentes. 
- Se debe elegir si se desea continuar o no. Si digta Y se continua con el programa, y si se digita N se regresa al menu principal. 
- Si se digita cualquier otra cosa, se muestra error y se regresa al menu principal. 
- Se muestran las siguientes estadisticas en pantalla para cada usuario: Fecha de cuando jugo, Nombre del usuario y RESULTADO de la partida (GANO o PERDIO)
- Despues se debe ingresar la palabra RETURN para regresar el menu principal. 
- Si se elegi un usuario que no existe, igual se debe ingresar RETURN para regresar al MENU principal. 

## Consideraciones especiales

Cualquier consideración o comentario adicional sobre la aplicación. Por ejemplo:

- Se debe correr la aplicacion de main para correr todo el programa.
- La carta tapada se representa como CARTA TAPADA. 
- Queria meter dentro de las estadisticas, el porcentaje de partidas ganadas pero por razones de tiempo no pude. 
- Se crea un archivo de estadisticas para cada usuario. 
- Use de base los ejemplos de la clase e Internet. 
- Tambien empece la aplicacion para varios jugadores, pero me di cuenta que era solo para un jugador. 
- Me gustaria luego mejorar la aplicacion para que acepte mas jugadores. 
- No estoy seguro de las reglas, pero creo que BlackJack es un A con una carta que valga 10.  
- Tambien queria mejorar la seccion de menus pero por tiempo no pude. 
