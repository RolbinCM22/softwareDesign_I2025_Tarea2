# Estudiante
Rolbin Castillo Matamoros - B81771
# softwareDesign_I2025_Tarea2
En el presente repositorio se desarrolla la tarea 2 del curso de Diseño de Software, la cual consiste en la refactorización de código basado en buenas practicas de programación.


## Problemas identificados
1. **Falta de interfaces:** No se utilizaban interfaces para definir contratos claros entre clases.
2. **Alto acoplamiento:** Las funciones dependían directamente unas de otras, dificultando la reutilización y el mantenimiento.
3. **Redundancia de código:** Se repetía lógica relacionada con los tipos de vehículos y sus atributos.
4. **Responsabilidades múltiples:** La clase `Fleet` tenía más de una responsabilidad, como gestionar vehículos y generar reportes.
5. **Generación de reportes acoplada:** La función `generate_report` realizaba tanto cálculos como la impresión de datos, violando el principio de responsabilidad única.

## Soluciones implementadas
1. **Uso de interfaces:** Se implementaron interfaces utilizando clases abstractas (`abc`) para definir contratos claros entre clases.
2. **Desacoplamiento:** Se separaron las responsabilidades de cálculo y presentación en la generación de reportes.
3. **Eliminación de redundancia:** Se simplificó la lógica de agregar vehículos eliminando estructuras condicionales innecesarias.
4. **Separación de responsabilidades:** La clase `Fleet` ahora se encarga únicamente de gestionar vehículos, mientras que la generación de reportes se realiza de manera desacoplada.
5. **Refactorización de `generate_report`:** Ahora devuelve los datos calculados en lugar de imprimirlos directamente, dejando la presentación a otra capa.

## Buenas prácticas aplicadas
1. **Principio de responsabilidad única (SRP):** Cada clase y función tiene una única responsabilidad.
2. **No te repitas (DRY):** Se eliminó la redundancia en la lógica de manejo de vehículos.
3. **Desacoplamiento:** Se separaron las capas de lógica de negocio y presentación.
4. **Uso de contratos claros:** Se implementaron interfaces para garantizar que las clases cumplan con los métodos esperados.
5. **Código reutilizable y mantenible:** Las funciones y clases ahora son más modulares y fáciles de probar.

## Explicación técnica de mejoras significativas

1. **Desacoplamiento de lógica de negocio y presentación:**
   - Se refactorizó la función `generate_report` para que devuelva los datos calculados en lugar de imprimirlos directamente. Esto permite que la presentación de los datos sea manejada por otra capa, siguiendo el principio de responsabilidad única (SRP) y facilitando la reutilización del código.

2. **Eliminación de redundancia en la gestión de vehículos:**
   - La función `agregar_vehiculo` fue simplificada para recibir directamente un objeto de tipo `Vehiculo`, eliminando estructuras condicionales innecesarias. Esto aplica el principio DRY (Don't Repeat Yourself) y mejora la claridad y mantenibilidad del código.

3. **Uso de interfaces para contratos claros:**
   - Se implementaron interfaces utilizando clases abstractas (`abc`) para definir métodos obligatorios como `calcular_costo` y `necesita_inspeccion`. Esto asegura consistencia en las implementaciones y mejora la escalabilidad del sistema.
