**Constantes**
Para declarar una variable constante (inmutable) use `const` en vez de `let`:
```js
const PI = 3.1416;
```
Las variables declaradas utilizando `const` no pueden ser alteradas. Al intentarlo causaría un error:

```js
const myBirthday = '05.11.1990';
myBirthday = '01.01.2001'; // ¡ERROR!}
```