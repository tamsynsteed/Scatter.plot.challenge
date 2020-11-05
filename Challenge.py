import matplotlib.pyplot as plt
x=[14.2,16.5,11.8,15.3,18.8,22.5,19.5]
y=[220,330,190,340,410,445,415]

plt.scatter(x,y)
plt.xlabel("Temperature")
plt.ylabel("Price in  (R)")
plt.title("Soup Sales In Relation To Temperature")
plt.show()
