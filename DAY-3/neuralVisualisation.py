import matplotlib.pyplot as plt

plt.figure(figsize=(6,4))

# Input Layer
plt.scatter([1,1],[1,2],s=500)

# Hidden Layer
plt.scatter([3,3,3],[0.5,1.5,2.5],s=500)

# Output Layer
plt.scatter([5],[1.5],s=500)

plt.title("Simple Neural Network")
plt.axis('off')
plt.show()