```fix
Una forma sencilla de obtener una entrada de un usuario mediante el método => 𝘸𝘪𝘯𝘥𝘰𝘸.𝘱𝘳𝘰𝘮𝘱𝘵()
```

🆂🅸🅽🆃🅰🆇🅸🆂 📍
```fix
prompt(text, [default])
```

🅰🆁🅶🆄🅼🅴🅽🆃🅾🆂 📍

```r
🔸text: "El texto que mostrará el cuadro de diálogo emergente"
🔸default: "Valor predeterminado que tendrá el campo de texto" (opcional)
```

🅴🅹🅴🅼🅿🅻🅾 📍

```js
/** 🖳︎☟︎
 * Esta función saluda a un usuario.
 * @param {String} nombre : El nombre del usuario
 * @param {String} apellido : El apellido del usuario
 */
const saludarUsuario = (nombre, apellido) => {
  let formateado = `Un gusto ${nombre} ${apellido}, bienvenido a mi sitio web`;
  alert(formateado);
};

nombre = prompt("¿Cuál es tu nombre?", "nombre");
apellido = prompt("¿Cuál es tu apellido?", "apellido");

saludarUsuario(nombre, apellido);
```

🅲🅾🅳🅴🅿🅴🅽 👇
https://codepen.io/EniDev911/pen/jOzVzeK ⚓

