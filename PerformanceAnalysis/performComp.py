import ScikitImp
import KmeansImp
import time
## 1 cluster
start = time.time()
KmeansImp.segmentation("test.png", 1, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The self-implemented kmeans algorithm took " + str(end - start) + " s for 1 cluster\n")
print("================================================================================================\n")



print("\n")



start = time.time()
ScikitImp.segmentation("test.png", 1, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The Scikit-Learn kmeans algorithm took " + str(end - start) + " s for 1 cluster\n")
print("================================================================================================\n")


## 2 clusters
start = time.time()
KmeansImp.segmentation("test.png", 2, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The self-implemented kmeans algorithm took " + str(end - start) + " s for 2 clusters\n")
print("================================================================================================\n")



print("\n")



start = time.time()
ScikitImp.segmentation("test.png", 2, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The Scikit-Learn kmeans algorithm took " + str(end - start) + " s for 2 clusters\n")
print("================================================================================================\n")


## 3 clusters
start = time.time()
KmeansImp.segmentation("test.png", 3, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The self-implemented kmeans algorithm took " + str(end - start) + " s for 3 clusters\n")
print("================================================================================================\n")



print("\n")



start = time.time()
ScikitImp.segmentation("test.png", 3, "SEGtest.png")
end = time.time()
print("================================================================================================\n")
print("The Scikit-Learn kmeans algorithm took " + str(end - start) + " s for 3 clusters\n")
print("================================================================================================\n")
