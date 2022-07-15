**DESCRIPCIÓN** 📍
```text
El método window.confirm() muestra un cuadro de diálogo modal con un mensaje opcional y dos botones Aceptar/Cancelar
```
**SINTAXIS** 📍
```js
confirm([message])
```
**ARGUMENTOS** 📍
```text
🔸 message: El texto que mostrará el cuadro de diálogo emergente (opcional)
```
**EJEMPLO** 📍
```js
/**
 * Esta función valida la acción del usuario.
 */
const confirmarRespuesta =  () => {
  if (window.confirm("¿Estás seguro que quieres cerrar la página?")){
    window.open("exit.html", "¡Gracias por tu visita!");
  }
}
```
**VER EN CODEPEN 👇**
⚓ https://codepen.io/EniDev911/pen/jOzVzeK

