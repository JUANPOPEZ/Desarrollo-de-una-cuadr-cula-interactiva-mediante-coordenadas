# Cuadrícula interactiva con selección de círculos mediante coordenadas

Aplicación de consola en Python que representa una cuadrícula de 8x8 círculos.
Todos los círculos inician "transparentes" (`○`) y, al ingresar una coordenada
`(X, Y)` válida, el círculo correspondiente cambia a "relleno" (`●`).

## Requisitos

- Python 3.8 o superior (no requiere librerías externas).

## Instalación

1. Clona o descarga este repositorio.
2. Verifica que tienes Python instalado:
   ```bash
   python3 --version
   ```

## Ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
python3 cuadricula_circulos.py
```

## Uso

Al iniciar, el programa muestra la cuadrícula vacía y un menú con estas opciones:

1. **Ver cuadrícula**: muestra el estado actual de la cuadrícula.
2. **Seleccionar una coordenada**: pide un valor de X (columna) y un valor de Y
   (fila), ambos entre 1 y 8, y rellena el círculo correspondiente.
3. **Ver coordenadas seleccionadas**: lista todas las coordenadas elegidas
   hasta el momento, en el orden en que fueron seleccionadas.
4. **Reiniciar cuadrícula**: vuelve todos los círculos a su estado transparente
   y borra el historial de coordenadas.
5. **Salir**: termina el programa.

### Ejemplo

Si ingresas la coordenada `(3,5)`, el círculo ubicado en la columna 3, fila 5
cambiará de `○` a `●`.

## Estructura del código

El archivo `cuadricula_circulos.py` está organizado en funciones, cada una con
una única responsabilidad:

| Función | Responsabilidad |
|---|---|
| `crear_cuadricula` | Genera la matriz inicial de círculos vacíos |
| `mostrar_cuadricula` | Imprime la cuadrícula con sus ejes de coordenadas |
| `validar_coordenada` | Comprueba que una coordenada esté dentro del rango permitido |
| `seleccionar_circulo` | Cambia un círculo a relleno y lo registra en el historial |
| `reiniciar_cuadricula` | Crea una cuadrícula nueva y vacía el historial |
| `mostrar_coordenadas_seleccionadas` | Imprime el historial de coordenadas elegidas |
| `pedir_numero_entero` | Solicita al usuario un número, validando el tipo de dato |
| `mostrar_menu` | Imprime las opciones del menú principal |
| `main` | Controla el flujo general del programa |

El código incluye comentarios detallados en cada bloque para facilitar su
comprensión y documentación.

## Recursos utilizados

- Lenguaje: Python 3 (librería estándar únicamente).
- Entorno de ejecución: terminal / consola.

