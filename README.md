# CombustiblePy
Un script simple para calcular costo de un viaje sin pegarme a valores que pueden cambiar.
## El script se llama calcular.py y se usa así
Usa numeros reales para los datos y le asocia un texto con medidas con el siguente comando, reemplazando lo que esta entre "<>" y esos mismos "<>":
```bash
./calcular.py -p <precio_de_combustible> "<divisa>" -d <distancia_a_recorrer> "<unidad_de_distancia>" --rend <distancia_sin_gastar> "<unidad_de_autonomia>" -t <tarifas> "<divisa>"
```
## Divisas aceptadas hasta el momento
* ars, Pesos Argentinos
* usd, Dolares Estadounidenses
* mxn, Pesos Mexicanos
* eur, Euros
* cob, Pesos Colombianos
* btc, Bitcoins
* sats, Satoshis (fraccion de Bitcoin desde 0.00000001 BTC hasta 0.99999999 BTC)
### Ante la duda ejecutar
```bash
./calcular.py --ayuda
```

