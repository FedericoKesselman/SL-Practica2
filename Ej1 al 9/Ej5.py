article = """ título: Experiences in Developing a Distributed Agentbased Modeling Toolkit with Python Version 3
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented
details of large-scale complex systems. However, the specialized
knowledge required for developing such ABMs creates barriers to wider
adoption and utilization. Here we present our experiences in
developing an initial implementation of Repast4Py, a Python-based
distributed ABM toolkit. We build on our experiences in developing ABM
toolkits, including Repast for High Performance Computing (Repast
HPC), to identify the key elements of a useful distributed ABM
toolkit. We leverage the Numba, NumPy, and PyTorch packages and the
En este ejemplo se debe informar:
Python C-API to create a scalable modeling system that can exploit the
largest HPC resources and emerging computing architectures. """

special_characters = (',', '@', '-', '(', ')', '!', '1', '2', '3', 
                      '4', '5', '6', '7', '8', '9', '0')
for character in special_characters:
        if (character in article):
            article = article.replace (character, '')

tittle = []
tittle = article.split('\n', 1)[0]
tittle = tittle.split (' ')

if len(tittle) > 11:
    print ('Title NOT Ok')
else:
    print ('Title OK')

from collections import Counter
sentences = article.split('\n', 1)[1]
sentences = sentences.split('.')
counter_sentences = Counter()

for sentence in sentences:
    words = sentence.split(' ')

    if len(words) <= 12:
        counter_sentences['facil de leer'] += 1
    elif len(words) >= 13 and len(words) <= 17:
        counter_sentences['aceptale para leer'] += 1
    elif len(words) >= 18 and len(words) <= 25:
        counter_sentences['dificil leer'] += 1 
    else:
        counter_sentences['muy dificil'] += 1 

print ('Conteo de facilidad de lectura: ', counter_sentences)

