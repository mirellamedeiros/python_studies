#var bubble_sort_classic = function (array) {
#var length = array.length;
#for (var i = 0; i <comprimento; i ++) {
#  for (var j = 0; j <comprimento - i - 1; j ++) {
#    if (matriz [j]> matriz [j + 1]) {
#      array.swap (j, j + 1);
#    }
#  }
#}
#array de retorno;
#};

def bubble_sort(list1):
  # Outer loop for traverse the entire list
  for i in range(0, len(list1) - 1):
    for j in range(len(list1) - 1):
      if (list1[j] > list1[j + 1]):
        temp = list1[j]
        list1[j] = list1[j + 1]
        list1[j + 1] = temp
  return list1


list1 = [5, 3, 8, 6, 7, 2]
print("The unsorted list is: ", list1)
# Calling the bubble sort function
print("The sorted list is: ", bubble_sort(list1))


# sem variáveis temporárias
def bubble_sort(list1):
  # Loop externo para percorrer toda a lista
  para
  i
  no
  intervalo(0, len(lista1) - 1):
  para
  j
  no
  intervalo(len(lista1) - 1):
  if (lista1[j] > lista1[j + 1]):
    # aqui não estamos usando a variável temporária
    lista1[j], lista1[j + 1] = lista1[j + 1], lista1[j]


# lista de retorno 1

lista1 = [5, 3, 8, 6, 7, 2]
print("A lista não classificada é:", lista1)
# Chamando a função de classificação por bolha
print("A lista classificada é:", bubble_sort(list1))