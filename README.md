<div style="text-align: justify">

# Verificador de estructuras WHILE en lenguaje JAVA

## Definición de Reglas

El lenguaje para evaluar estructuras __WHILE__ es __JAVA__, esto también implica evaluar 
sus respectivas reglas para nombrar funciones, variables y constantes.

## Requerimientos de la estructura

Para que la estructura sea considerada con una notación válida se requerirá que esté presente la palabra reservada while
en minúsculas, seguida de su respectivo par de paréntesis que contengan la condición a evaluar.

La condición deberá ser simple con solo un par de variables o valores a comparar, las operaciones lógicas posibles 
abarcan __Mayor que (>), Menor que (<), Mayor o igual que (>=), Menor o igual que (<=), Igual que (==), diferente que (!=)__

También será posible evaluar valores boleanos como _TRUE_ o _FALSE_.

El cuerpo o contenido del ciclo deberá contener operaciones algebraicas o de asignación, se dará por hecho que todas las
variables a utilizar en el cuerpo de la estructura ya están inicializadas, por lo tanto; no tomará en cuenta la declaración de variables.
Tampoco tomará en cuenta la inclusión de otras estructuras correspondientes en JAVA (Ciclos WHILE anidados, ciclos for, ciclos do-While, estructuras switch-case, estructuras if o if-else, etc).

## Tipos de datos permitidos

Para resolver las asignaciones se podrán tomar en cuenta distintos tipos de datos primitivos y los __Strings__.

* int
* float
* char
* bool

## Ejemplo de una estructura WHILE válida
```
    while(variable1 != variable2){
    
        variable1 = b;
        b = b + 1;
        b = 10;
        c = c;
        c = a/0;
        variable2 = false;
        string = "String";
    
    } 
    
```

# Uso del programa.

Cada que el programa se inicia, llama el contenido del archivo _instructions.txt_ y lo carga dentro del contenedor de 
texto dentro del programa.

## Botones
El botón OK guarda el contenido de la caja de texto dentro del archivo .txt con nombre _instructions_.

El botón Analizar manda el contenido de la caja de texto a revisión del autómata, indiferente del resultado mostrará una
ventana emergente con el resultado del análisis.

Se puede salir del programa presionando el botón _Salir_ o simplemente cerrando la ventana como lo haría con cualquier otro programa


</div>