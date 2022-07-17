```fix
El método 𝘸𝘪𝘯𝘥𝘰𝘸.𝘤𝘰𝘯𝘧𝘪𝘳𝘮() muestra un cuadro de diálogo modal con un mensaje opcional y dos botones Aceptar/Cancelar
```
🆂🅸🅽🆃🅰🆇🅸🆂 📍
```js
confirm([message])
```
🅰🆁🅶🆄🅼🅴🅽🆃🅾🆂 📍
```c
🔸 message: "El texto que mostrará el cuadro de diálogo emergente"
```
🅴🅹🅴🅼🅿🅻🅾 📍
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

