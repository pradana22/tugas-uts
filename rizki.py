# Metode Input
var = []
bny = int(input("Seberapa banyak data yang ingin diinput: "))
for x in range(bny):
  data = input("Masukkan Data ke-"+str(x+1)+"(Tekan N untuk berhenti):")
  if data == "N" or data == "n":
    break
  else:
    var.append(data)

print(var)