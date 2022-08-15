🅼🅺🅳🅸🆁

```fix
Una forma sencilla de crear carpetas, si aún no existen
```

🆂🅸🅽🆃🅰🆇🅸🆂 📍

```fix
mkdir [ opciones ]...
mkdir "Nombre con espacios"
```

🅾🅿🅲🅸🅾🅽🅴🆂 📍

```r
🔸-p, --parents: No hay error si existe, crea directorios principales según sea necesario.
🔸-v, --verbose: Imprime un mensaje para cada directorio creado
```

🅴🅹🅴🅼🅿🅻🅾 📍
Crea el siguiente árbol de carpetas:

```bash
mkdir -p -v proyecto/assets/{css,js,img}
```

```ini
 📂 proyecto [carpeta raíz]
  |-- 📂 assets [subcarpeta de proyecto]
    |-- 📂 css [subcarpeta de assets]
    |-- 📂 img [subcarpeta de assets]
    |-- 📂 js [subcarpeta de assets]
```
