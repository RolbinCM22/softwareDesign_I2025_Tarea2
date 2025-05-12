# softwareDesign_I2025_Tarea2
En el presente repositorio se desarrolla la tarea 2 del curso de Diseño de Software, la cual consiste en la refactorización de codigo basado en buenas practicas de programación.

# Problemas de diseño
1- No cuenta con interfaces
2- Modularizar, porque hay alto acoplamiento, cada funcion depende de la otra 
3- Redundancia de codigo no se aplica DRY, se redunda en los tipos de datos entre vehiculos y flota
4- La clase flota posee más de una responsabilidad, al generar informes 
5- La funcion generar reporte se encarga de dos funcionalidades, 1 hace los calculos, dos de imprimir 
