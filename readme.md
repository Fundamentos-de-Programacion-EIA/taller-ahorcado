## Instrucciones para el Taller

### Objetivo

El objetivo de este taller es construir un juego de Ahorcado utilizando Python. Se practicarán conceptos como listas, diccionarios, clases, funciones, condicionales y bucles.

### Descripción de las Funciones de la Clase `Hangman`

#### Constructor

- **Propósito**: Inicializar una nueva instancia de la clase `Hangman`.
- **Parámetros**:
  - `word_list` (`str[]`): Lista de palabras entre las cuales se seleccionará una al azar para el juego.
- **Comportamiento**: Debe seleccionar una palabra al azar de `word_list`, inicializar una lista vacía para mantener las letras que el jugador ha adivinado y establecer el número de intentos restantes.
- **Salidas**: No retorna ningún valor (None).

#### Función `guess_letter`

- **Propósito**: Permitir al jugador adivinar una letra y actualizar el estado del juego.
- **Parámetros**:
  - `letter` (`str`): La letra que el jugador intenta adivinar.
- **Comportamiento**: Debe aceptar una letra como entrada, verificar si ya se ha adivinado, y en caso contrario, añadirla a la lista de letras adivinadas. Si la letra no está en la palabra secreta, debe reducir el número de intentos restantes.
- **Salidas**:
  - Retorna un valor booleano (`True` si la letra está en la palabra, `False` en caso contrario) y un mensaje de estado como cadena.

#### Función `get_display_word`

- **Propósito**: Mostrar la palabra oculta actualizada.
- **Parámetros**: Ninguno.
- **Comportamiento**: Debe retornar la palabra con guiones bajos en las posiciones de las letras que aún no se han adivinado y las letras correctas en su lugar correspondiente.
- **Salidas**:
  - Retorna la representación de la palabra secreta como una cadena, donde las letras no adivinadas se muestran como guiones bajos.

#### Función `is_game_over`

- **Propósito**: Determinar si el juego ha terminado.
- **Parámetros**: Ninguno.
- **Comportamiento**: Debe verificar si el jugador se ha quedado sin intentos o si ha adivinado todas las letras de la palabra.
- **Salidas**:
  - Retorna un valor booleano (`True` si el juego ha terminado, `False` en caso contrario) y un mensaje de estado como cadena.

#### Función `play_game`

- **Propósito**: Ejecutar el juego.
- **Parámetros**: Ninguno.
- **Comportamiento**: Debe contener el bucle principal del juego, mostrar el estado actual de la palabra, aceptar entradas del usuario y mostrar mensajes relevantes según el progreso del jugador.
- **Salidas**: Ninguna directa, pero controla el flujo del juego e imprime resultados y mensajes en la consola.
