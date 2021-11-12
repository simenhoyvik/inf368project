from all_wordsim import AllWordSim


class WordSim200D():
    def __init__(self):
        self.allWordSim = AllWordSim()
    def addBest(self,text):
        return "Best: " + text
    def run(self):
        a100 = self.allWordSim.all_wordsim("new_embeddingsGlove200D/a-100D.txt", "data/word-sim/")
        algo100 = self.allWordSim.all_wordsim("new_embeddingsGlove200D/algo100D.txt", "data/word-sim/")
        glove200 = self.allWordSim.all_wordsim("glove.6B/glove.6B.200d.txt", "data/word-sim/")

        for i in range(len(algo100)):
            tempList = [float(algo100[i][4]), float(glove200[i][4]), float(a100[i][4])]
            maxValue = max(tempList)
            maxIndex = tempList.index(maxValue)
            if (maxIndex == 0): algo100[i][4] = self.addBest(algo100[i][4])
            elif (maxIndex == 1): glove200[i][4] = self.addBest(glove200[i][4])
            else: a100[i][4] = self.addBest(a100[i][4])

        print("Results for Glove Embeddings 200D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in glove200:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for Algo100D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in algo100:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for A-100D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in a100:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])
