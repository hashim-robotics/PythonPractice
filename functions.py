from Dog import dog       

d1 = dog("tony", 4, "german shephard", "red")
d2 = dog("bruno", 3, "labrador")
d3 = dog("sal", 3, "lab")


d1.location = "lousiville"

d1.changeColor("blue")

#d1.printBreed("yellow")

print(d3.color)
d3.printBreed(x="brown")
print(d1.color)
print(d3.color)
print(d1.location)






