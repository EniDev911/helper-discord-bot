```fix
El mรฉtodo ๐ธ๐ช๐ฏ๐ฅ๐ฐ๐ธ.๐ค๐ฐ๐ฏ๐ง๐ช๐ณ๐ฎ() muestra un cuadro de diรกlogo modal con un mensaje opcional y dos botones Aceptar/Cancelar
```

๐๐ธ๐ฝ๐๐ฐ๐๐ธ๐ ๐

```js
confirm([message]);
```

๐ฐ๐๐ถ๐๐ผ๐ด๐ฝ๐๐พ๐ ๐

```c
๐ธ ๐ข๐๐จ๐จ๐๐๐: "El texto que mostrarรก el cuadro de diรกlogo emergente"
```

๐ด๐น๐ด๐ผ๐ฟ๐ป๐พ ๐

```js
/**
 * Esta funciรณn valida la acciรณn del usuario.
 */
const confirmarRespuesta = () => {
  if (window.confirm("ยฟEstรกs seguro que quieres cerrar la pรกgina?")) {
    window.open("exit.html", "ยกGracias por tu visita!");
  }
};
```

**VER EN CODEPEN ๐**
โ https://codepen.io/EniDev911/pen/jOzVzeK
