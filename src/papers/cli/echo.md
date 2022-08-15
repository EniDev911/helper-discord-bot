:penguin: EᑕᕼO

```fix
Este comando es uno de los comandos más utilizados. Se utiliza en los script de Bash y en los archivos por lotes para mostrar el texto de estado en un archivo o en tu terminal
```

🆂🅸🅽🆃🅰🆇🅸🆂 📍

```fix
echo [ opciones ][ string ]
```

🅾🅿🅲🅸🅾🅽🅴🆂 📍

```r
🔸-e: Permite que el comando echo considere las secuencias de escape en la cadena.
🔸-n: Muestra la salida sin salto de línea.
🔸-"": Interpreta las variables (Ej: echo "$PWD").
🔸-'': No interpreta las variable.
🔸string: Cadena de texto.
```

🅴🅹🅴🅼🅿🅻🅾 📍
Mostrar un mensaje de error colocando el texto en color rojo:

```bash
echo -e "\033[031m- Se detectó un error"
```

Otra forma sería declarar los colores en variables y usarlas después:

```bash
red="\033[31m"
reset="\033[0m"
echo -e "${red}Se detectó un error.\n${reset}El equipo se recuperó del error."
```
