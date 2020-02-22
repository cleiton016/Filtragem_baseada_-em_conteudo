import math

d1 = "Is this the real life? \
Is this just fantasy? \
Caught in a landslide \
No escape from reality"

d2 = "Love of my life, you've hurt me \
You've broken my heart \
And now you leave me"

d3 = "I live inside my own world of make-believe \
Kids, screaming in their cradles, profanities \
I see the world through eyes covered in ink and bleach \
Cross out the ones who heard my cries and watched me weep"

d4 = "One thing, I don't know why \
It doesn't even matter how hard you try \
Keep that in mind, I designed this rhyme \
To explain in due time (all I know)"

def separar(arg):
    return arg.split(' ')

bow_d1 = separar(d1)
bow_d2 = separar(d2)
bow_d3 = separar(d3)
bow_d4 = separar(d4)

unique_words = set(bow_d1).union(set(bow_d2)).union(set(bow_d3)).union(set(bow_d4))
#print(unique_words)
print('--------------------',len(unique_words))
def cont_word(bow_d, unique_words):
    tc_d = dict.fromkeys(unique_words,0)
    #print(tc_d)
    for i in bow_d:
        tc_d[i] += 1
    return tc_d
tc_d1 = cont_word(bow_d1, unique_words)
tc_d2 = cont_word(bow_d2, unique_words)
tc_d3 = cont_word(bow_d3, unique_words)
tc_d4 = cont_word(bow_d4, unique_words)

def frequencia(bow_d, tc_d):
    tf_d = {}
    total = float(len(bow_d))
    for i, y in tc_d.items():
        tf_d[i] = y / total
    return tf_d
tf_d1 = frequencia(bow_d1, tc_d1)
tf_d2 = frequencia(bow_d2, tc_d2)
tf_d3 = frequencia(bow_d3, tc_d3)
tf_d4 = frequencia(bow_d4, tc_d4)
#print(tf_d1)

def frequencia_inversa(unique_words, *documents):
    N = len(documents)
    idf = dict.fromkeys(unique_words,0)
    for d in documents:
        for w, c in d.items():
            if c > 0:
                idf[w] += 1
    for w, c in idf.items():
        idf[w] = math.log(N / float(c))

    return idf

idf = frequencia_inversa(unique_words,tc_d1,tc_d2,tc_d3,tc_d4)

def mutiplica_idf(tf_d, _idf):
    tf_idf_d = {}
    for w, c in tf_d.items():
        tf_idf_d[w] = c * _idf[w]
    return tf_idf_d
tf_idf_d1 = mutiplica_idf(tf_d1, idf)
tf_idf_d2 = mutiplica_idf(tf_d1, idf)
tf_idf_d3 = mutiplica_idf(tf_d1, idf)
tf_idf_d4 = mutiplica_idf(tf_d2, idf)



def distancia_entre_doc(unique_words, d1,d2):
    ds = []
    for w in unique_words:
        dif = d1[w] - d2[w]
        ds.append(dif * dif)
    soma = 0
    for i in ds:
        soma += 1
    return math.sqrt(soma)

print(distancia_entre_doc(unique_words,tf_idf_d1,tf_idf_d3))
print(distancia_entre_doc(unique_words,tf_idf_d1,tf_idf_d2))
print(distancia_entre_doc(unique_words,tf_idf_d1,tf_idf_d4))
print(distancia_entre_doc(unique_words,tf_idf_d2,tf_idf_d3))
print(distancia_entre_doc(unique_words,tf_idf_d2,tf_idf_d4))
print(distancia_entre_doc(unique_words,tf_idf_d3,tf_idf_d4))
