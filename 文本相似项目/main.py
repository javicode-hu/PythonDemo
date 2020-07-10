import codecs

import jieba
import jieba.analyse
import get_all_content

#jieba分词
def words2vec(words1=None, words2=None):
    v1 = []
    v2 = []
    tag1 = jieba.analyse.extract_tags(words1, withWeight=True)
    tag2 = jieba.analyse.extract_tags(words2, withWeight=True)
    tag_dict1 = {i[0]: i[1] for i in tag1}
    tag_dict2 = {i[0]: i[1] for i in tag2}
    merged_tag = set(tag_dict1.keys()) | set(tag_dict2.keys())
    for i in merged_tag:
        if i in tag_dict1:
            v1.append(tag_dict1[i])
        else:
            v1.append(0)
        if i in tag_dict2:
            v2.append(tag_dict2[i])
        else:
            v2.append(0)
    return v1, v2

#利用余弦相似度公式计算相似度
def cosine_similarity(vector1, vector2):
    dot_product = 0.0
    normA = 0.0
    normB = 0.0
    for a, b in zip(vector1, vector2):
        dot_product += a * b
        normA += a ** 2
        normB += b ** 2
    if normA == 0.0 or normB == 0.0:
        return 0
    else:
        return round(dot_product / ((normA ** 0.5) * (normB ** 0.5)) * 100, 2)

#返回相似度
def cosine(str1, str2):
    vec1, vec2 = words2vec(str1, str2)
    return cosine_similarity(vec1, vec2)



#获取学生id
def get_num():
    num = []
    stu = get_all_content.get_dict()
    for item in stu:
        num.append(item[0])
    return num


def main():
    num = get_num()
    while(num):
        i = num[0]
        num.pop(0)
        for j in num:
            try:
                fa = codecs.open('user_txt\\{}.txt'.format(i), "r", encoding='utf8', errors='ignore')
                fb = codecs.open('user_txt\\{}.txt'.format(j), "r", encoding='utf8', errors='ignore')
                content_a = fa.read()
                content_b = fb.read()
                fa.close()
                fb.close()
                rate = cosine(content_a, content_b)
                with open('result.csv', 'a', encoding='utf-8') as f:
                    f.write(i+','+j+','+str(rate)+'\n')
                    print(i,j,rate)
            except FileNotFoundError:
                continue
    print('分析完成！')


main()