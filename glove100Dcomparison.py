from all_wordsim import AllWordSim

class WordSim100D():
    def __init__(self):
        self.allWordSim = AllWordSim()
    def addBest(self,text):
        return "Best: " + text
    def run(self):
        a50 = self.allWordSim.all_wordsim("new_embeddingsGlove100D/a-50D.txt", "data/word-sim/")
        algo50 = self.allWordSim.all_wordsim("new_embeddingsGlove100D/algo50D.txt", "data/word-sim/")
        glove100 = self.allWordSim.all_wordsim("glove.6B/glove.6B.100d.txt", "data/word-sim/")

        for i in range(len(algo50)):
            tempList = [float(algo50[i][4]), float(glove100[i][4]), float(a50[i][4])]
            maxValue = max(tempList)
            maxIndex = tempList.index(maxValue)
            if (maxIndex == 0): algo50[i][4] = self.addBest(algo50[i][4])
            elif (maxIndex == 1): glove100[i][4] = self.addBest(glove100[i][4])
            else: a50[i][4] = self.addBest(a50[i][4])

        print("Results for Glove Embeddings 100D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in glove100:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for Algo50D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in algo50:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for A-50D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in a50:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])
