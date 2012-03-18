from sys import argv
from operator import itemgetter

from nltk.corpus import wordnet

def alliterate(word, character):
   if word[0] == character:
      return word
   results = [query.name for query in wordnet.synsets(word)]
   for result in results:
      try:
         if result[0] == character:
            return result[:result.find('.')]
      except IndexError, e:
         pass
   l = [query.lemmas[0] for query in wordnet.synsets(word)]
   for i in l:
      print i.antonyms()

   return word

class Alliterate(object):
   def __init__(self, sentence):
      self.freq = {}
      self.character = 'a'
      tokens = sentence.split(' ')
      self.firstpass(tokens=tokens)
      self.secondpass(tokens=tokens)

   def firstpass(self, tokens):
      for token in tokens:
         results = [query.name for query in wordnet.synsets(token)]
         f = {}
         for result in results:
            character = result[0]
            f[character] = f.setdefault(character, 0) + 1 
         l = [(k, v) for (k, v) in f.iteritems()]
         l.sort(key=itemgetter(1), reverse=True)
         try:
            key = l[0][0]
            self.freq[key] = self.freq.setdefault(key, 0) + 1
         except Exception, e:
            pass
      print self.freq
      m = [(k, v) for (k, v) in self.freq.iteritems()]
      m.sort(key=itemgetter(1), reverse=True)
      try:
         self.character = m[0][0]
      except Exception, e:
         pass

   def secondpass(self, tokens):
      results = [alliterate(word=token, character=self.character) for token in tokens]
      print ' '.join(results)

 
def main(argv=None):
   sentence = ''
   character = 'a'
   try:
      character = argv[1][0]
   except Error, e:
      pass

   while True:
      if 'exit' in sentence:
         break
      sentence = raw_input('Type a sentence: ')
      Alliterate(sentence)
      #tokens = sentence.split(' ')
      #results = [alliterate(word=token, character=character) for token in tokens]
      #print ' '.join(results)
      

if __name__ == '__main__':
   main(argv=argv)
