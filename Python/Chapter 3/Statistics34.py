from statistics import mean, median, multimode

data = [9, 11, 22, 34, 17, 22, 34, 22, 40]


print("Mean:", round(mean(data), 2))
print("Median:", median(data))
print("Mode(s):", multimode(data))  

data_with_extra_34 = data + [34]

print("\nDataset with extra 34:", data_with_extra_34)
print("Mean:", round(mean(data_with_extra_34), 2))
print("Median:", median(data_with_extra_34))
print("Mode(s):", multimode(data_with_extra_34))

