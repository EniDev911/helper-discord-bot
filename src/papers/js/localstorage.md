```fix
Una forma sencilla de obtener una entrada de un usuario mediante el mรฉtodo => ๐ธ๐ช๐ฏ๐ฅ๐ฐ๐ธ.๐ฑ๐ณ๐ฐ๐ฎ๐ฑ๐ต()
```

๐๐ธ๐ฝ๐๐ฐ๐๐ธ๐ ๐

```fix
prompt(text, [default])
```

๐ฐ๐๐ถ๐๐ผ๐ด๐ฝ๐๐พ๐ ๐

```r
๐ธ๐ฉ๐๐ญ๐ฉ: "El texto que mostrarรก el cuadro de diรกlogo emergente"
๐ธ๐๐๐๐๐ช๐ก๐ฉ: "Valor predeterminado que tendrรก el campo de texto" (opcional)
```

๐ด๐น๐ด๐ผ๐ฟ๐ป๐พ ๐

```js
/** ๐ณ๏ธโ๏ธ
 * Esta funciรณn saluda a un usuario.
 * @param {String} nombre : El nombre del usuario
 * @param {String} apellido : El apellido del usuario
 */
const saludarUsuario = (nombre, apellido) => {
  let formateado = `Un gusto ${nombre} ${apellido}, bienvenido a mi sitio web`;
  alert(formateado);
};

nombre = prompt("ยฟCuรกl es tu nombre?", "nombre");
apellido = prompt("ยฟCuรกl es tu apellido?", "apellido");

saludarUsuario(nombre, apellido);
```
