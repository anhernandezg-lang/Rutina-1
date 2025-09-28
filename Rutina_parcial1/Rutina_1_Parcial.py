#PARCIAL 1
gene_list = [] #Aquí voy a guardar los nombres de cada gen
start_list = [] #Posiciones de inicio
end_list = [] #Posicioones del final
length_list = [] #Longitud de cada gen

file_name= 'gene_bartonella.gb' #Descargué este archivo por que mi proyecto de maestría es con este gen.
output_file = 'genes.tsv'#Formato de salida que voy a tener

# Imprimir encabezado en pantalla
print('gene', 'inicio', 'final', 'longitud', sep="\t")
#Abrir y leer el archivo line por linea con ayuda del ciclo "for" y condicional "if"
with open(file_name, mode='rt') as file:
    for line in file:
        if 'gene' in line:  # buscamos las líneas que contienen "gene"
            line = line.strip() #Eliminamos espacios y saltos de linea

            if line.startswith('gene'): #Confirmar que la linea inice con "gene"
                # Selección de posiciones
                line = line.replace('complement(', '')
                line = line.replace(')', '')
                line = line.replace('gene            ', '')
                #print(line)

                # Separar inicio y final
                temp = line.split("..")
                inicio = int(temp[0])
                final = int(temp[1])
                longitud = final - inicio
                #print(temp)

                # Guardar el valor del gen
                gene = next(file).strip()[7:-1]

                # Guardamos en lista
                gene_list.append(gene)
                start_list.append(inicio)
                end_list.append(final)
                length_list.append(longitud)

                # Mostrar en pantalla
                print(gene, inicio, final, longitud, sep="\t")

# Escribir archivo TSV
with open(output_file, "w") as out:
    out.write("gene\tinicio\tfinal\tlongitud\n")
    for g, i, f, l in zip(gene_list, start_list, end_list, length_list):
        out.write(f"{g}\t{i}\t{f}\t{l}\n")


