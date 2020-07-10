import numpy as np
from snownlp import SnowNLP
import matplotlib.pyplot as plt
import sys

# f = open('review-rating1.txt', 'r', encoding='UTF-8',errors='ignore')
# list = f.readlines()
# sentimentslist = []
# for i in list:
#     s = SnowNLP(i)
#     # print s.sentiments
#     sentimentslist.append(s.sentiments)
# plt.hist(sentimentslist, bins=np.arange(0, 1, 0.01), facecolor='g')
# plt.xlabel('Sentiments Probability')
# plt.ylabel('Quantity')
# plt.title('Analysis of Sentiments')
# plt.show()
def read_and_analysis(input_file, output_file):
  f = open(input_file, encoding='UTF-8',errors='ignore')
  fw = open(output_file,'w')
  while True:
    line = f.readline()
    if not line:
      break
    lines = line.strip().split("\t")
    if len(lines) < 2:
      continue

    s = SnowNLP(lines[1])
    # s.words 查询分词结果
    seg_words = ""
    for x in s.words:
      seg_words += "_"
      seg_words += x
    # s.sentiments 查询最终的情感分析的得分
    fw.write(lines[0] + "\t" + lines[1] + "\t" + seg_words + "\t" + str(s.sentiments) + "\n")
  fw.close()
  f.close()

if __name__ == "__main__":
  input_file = "review-rating1.txt"
  output_file = "result.txt"
  read_and_analysis(input_file, output_file)
