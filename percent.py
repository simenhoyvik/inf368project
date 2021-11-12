def percentImprovement(before,after):
    return(100*(after - before) / before)

def calcAverage(beforeList, afterList):
    sum = 0
    length = len(beforeList)
    for i in range(length):
        sum += percentImprovement(beforeList[i],afterList[i])
    return round(sum / length,2)


glove300 = [70.26,73.75,63.32,65.01,76.62,41.18,37.05,30.51,60.54,57.26,66.38,56.13,46.46]
algo150 = [68.86,75.2,61.52,64.41,74.88,41.81,37.95,40.6,65.97,60.58,70.71,54.0,51.28]
a150 = [73.68,76.40,63.19,65.76,75.33,44.16,40.23,30.28,67.11,61.55,72.19,58.27,46.96]

print("Glove300 - algo150: ", calcAverage(glove300,algo150))
print("Glove300 - a150: ", calcAverage(glove300,a150))
print("Algo150 - a150: ", calcAverage(algo150,a150), "\n")

glove200 = [66.56,71.01,61.99,62.12,71.26,38.95,34.03,28.45,57.42,54.48,62.91,52.21,50.03]
algo100 = [72.26,74.01,61.32,61.97,76.37,41.08,36.37,35.51,62.66,57.51,66.73,49.55,48.7]
a100 = [78.22,74.64,62.75,63.35,75.41,42.54,38.13,28.15,66.04,60.69,72.0,52.05,48.36]

print("Glove200 - algo100: ", calcAverage(glove200,algo100))
print("Glove200 - a100: ", calcAverage(glove200,a100))
print("Algo100 - a100: ", calcAverage(algo100,a100),"\n")

glove100 = [62.71,68.09,61.94,58.05,69.07,36.64,29.76,30.23,52.9,49.55,60.37,45.43,47.24]
algo50 = [67.3,71.02,63.45,58.52,67.74,38.25,29.33,34.29,62.33,60.2,65.4,40.81,46.05]
a50 = [77.13,71.68,60.89,58.82,75.62,39.77,30.51,17.5,62.15,58.77,68.94,57.96,38.9]

print("Glove100 - algo50: ", calcAverage(glove100,algo50))
print("Glove100 - a50: ", calcAverage(glove100,a50))
print("Algo50 - a50: ", calcAverage(algo50,a50),"\n")