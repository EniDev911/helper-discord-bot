**DESCRIPCIÓN** 📍
```text
Una forma sencilla de obtener una entrada de un usuario mediante el método window.prompt()
```
**SINTAXIS** 📍
```js
prompt(text, [default])
```
**ARGUMENTOS** 📍
```text
🔸 text: El texto que mostrará el cuadro de diálogo emergente
🔸 default: Valor predeterminado que tendrá el campo de texto (opcional)
```
**EJEMPLO** 📍
```js
/**
 * Esta función saluda a un usuario.
 * @param {String} nombre : El nombre del usuario
 * @param {String} apellido : El apellido del usuario
 */
const saludarUsuario =  (nombre, apellido) => {
  let formateado = `Un gusto ${nombre} ${apellido}, bienvenido a mi sitio web` 
  alert(formateado);
}

nombre = prompt("¿Cuál es tu nombre?", "nombre");
apellido = prompt("¿Cuál es tu apellido?", "apellido");

saludarUsuario(nombre, apellido)
```
**VER EN CODEPEN 👇**
⚓ https://codepen.io/EniDev911/pen/jOzVzeK
