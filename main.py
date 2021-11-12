import os
import sys

from a_and_algo import A_And_Algo
from glove100Dcomparison import WordSim100D
from glove200Dcomparison import WordSim200D
from glove300Dcomparison import WordSim300D

def generateAllEmbeddings():
    '''
    This method creates all embeddings needed for this research.
    The embeddings will be stored in the different text files.
    '''
    a_and_algo = A_And_Algo()
    a_and_algo.trainA("glove.6B/glove.6B.300d.txt", "new_embeddingsGlove300D/a-150D.txt", 150)
    a_and_algo.trainAlgo("glove.6B/glove.6B.300d.txt", "new_embeddingsGlove300D/algo150D.txt", 150)
    a_and_algo.trainA("glove.6B/glove.6B.200d.txt", "new_embeddingsGlove200D/a-100D.txt", 100)
    a_and_algo.trainAlgo("glove.6B/glove.6B.200d.txt", "new_embeddingsGlove200D/algo100D.txt", 100)
    a_and_algo.trainA("glove.6B/glove.6B.100d.txt", "new_embeddingsGlove100D/a-50D.txt", 50)
    a_and_algo.trainAlgo("glove.6B/glove.6B.100d.txt", "new_embeddingsGlove100D/algo50D.txt", 50)

def compareAllEmbeddings():
    '''
    This method is comparing different embedding reductions. 300, 200 and 100.
    '''
    wordSim300D = WordSim300D()
    wordSim300D.run()
    wordSim200D = WordSim200D()
    wordSim200D.run()
    wordSim100D = WordSim100D()
    wordSim100D.run()

if __name__ == '__main__':
    #Making the system print to file instead of console.
    original_stdout = sys.stdout

    #Opening file to print to.
    with open('main.txt', 'w') as f:
        sys.stdout = f
        generateAllEmbeddings()
        compareAllEmbeddings()
        os.system('python percent.py')
        sys.stdout = original_stdout