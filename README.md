**Extracción de genes de Bartonella tribocorum**
Este proyecto contiene un script en Python para procesar un archivo GenBank (.gb) y extraer información de los genes, incluyendo la posición de inicio, posición final y longitud de cada uno.
El resultado se muestra en pantalla y también se guarda en un archivo de salida en formato tabulado (.tsv), listo para abrirse en Excel u otras herramientas.
**Descripción**
El script lee el archivo línea por línea, detecta las líneas que contienen la palabra gene, limpia el texto para quedarse solo con las posiciones, separa inicio y fin, calcula la longitud de cada gen.
Toda la información se organiza en una tabla.
**Requisitos**
Python 3.x
Un archivo GenBank válido  "gene_bartonella.gb"
