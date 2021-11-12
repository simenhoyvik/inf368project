from all_wordsim import AllWordSim

class WordSim300D():
    def __init__(self):
        self.allWordSim = AllWordSim()
    def addBest(self,text):
        '''
        :return: the input text with the word best appended in front
        '''
        return "Best: " + text
    def run(self):
        '''
        This method calculated all compariosons for 300 to 150 dimension reduction.
        The method is also printing the results.
        :return:
        '''
        algo150 = self.allWordSim.all_wordsim("new_embeddingsGlove300D/algo150D.txt", "data/word-sim/")
        glove300 = self.allWordSim.all_wordsim("glove.6B/glove.6B.300d.txt", "data/word-sim/")
        algo150testing = self.allWordSim.all_wordsim("new_embeddingsGlove300D/a-150D.txt", "data/word-sim/")

        for i in range(len(algo150)):
            tempList = [float(algo150[i][4]),
                        float(glove300[i][4]),
                        float(algo150testing[i][4])]
            maxValue = max(tempList)
            maxIndex = tempList.index(maxValue)
            if (maxIndex == 0): algo150[i][4] = self.addBest(algo150[i][4])
            elif (maxIndex == 1): glove300[i][4] = self.addBest(glove300[i][4])
            else: algo150testing[i][4] = self.addBest(algo150testing[i][4])

        print("Results for Glove Embeddings 300D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in glove300:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for Algo150D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in algo150:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])

        print("Results for A_150D")
        print('=================================================================================')
        print("%6s" % "Serial", "%20s" % "Dataset", "%15s" % "Num Pairs", "%15s" % "Not found", "%15s" % "Rho")
        print('=================================================================================')

        for item in algo150testing:
            print("%6s" % item[0], "%20s" % item[1], "%15s" % item[2], "%15s" % item[3], "%15s" % item[4])