This project is a modified version of https://github.com/vyraun/Half-Size, such that
many methods is not implemented by me. The main changes is done in the python files
a_and_algo, all_wordsim, glove100Dcomparison, glove200Dcomparison, glove300Dcomparison
and main.

For running the project, you have to have a python interpretor with the
libraries listed in requirements.txt installed. You also need to download 
the original pre-trained glove embeddings which you can download from
https://nlp.stanford.edu/projects/glove/.

For reproducing all results from the report, run the main.py script. This script
will print all results to the main.txt. This scirpt will take a while when running
on a personal computer. It took between 0.5 to 1 hour to excecute on mine.

Percent.py is calculating the average improvement from the results. These are collected
from main.txt and hard coded in a list. This could be automized if more time were given.

If you want to apply our algorithm on a pretrained word embeddings. Create a script,
create a object of the class A_And_Algo, call the method trainA() and pass in the path
to where your original embeddings are stored, path to where the new embeddings should
be stored, and the final dimensions as int. 

Enjoy!
