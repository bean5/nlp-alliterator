#!/usr/bin/env python
import re
from operator import itemgetter

from nltk.corpus import wordnet


class Alliterate(object):
   def __init__(self, sentence):
      self.freq = {}
      self.character = 'a'
      self.output = ''
      self.tokens = re.split(r"[^a-zA-Z]", sentence)
      self._firstpass()

   def _firstpass(self):
      for token in self.tokens:
         results = [query.name for query in wordnet.synsets(token)]
         f = {}
         for result in results:
            _result = result[:result.find('.')]
            for character in _result:
               f[character] = f.setdefault(character, 0) + 1
         l = [(k, v) for (k, v) in f.iteritems()]
         l.sort(key=itemgetter(1), reverse=True)
         try:
            key = l[0][0]
            self.freq[key] = self.freq.setdefault(key, 0) + 1
         except Exception, e:
            pass
      m = [(k, v) for (k, v) in self.freq.iteritems()]
      m.sort(key=itemgetter(1), reverse=True)
      self.characters = [c for c, f in m]
      try:
         self.character, frequency = m[0]
      except Exception, e:
         pass

   def _alliterate(self, word=''):
      if len(word) == 0: return word
      for character in self.characters:

         if character in word:
            return word
         results = [query.name for query in wordnet.synsets(word)]
         for result in results:
            try:
               _result = result[:result.find('.')]
               if character in _result:
                  return _result
            except IndexError, e:
               pass
      return word

   def __str__(self):
      output = [self._alliterate(word=token) for token in self.tokens]
      return ' '.join(output)
 
def main():
   sentence = ''
   while True:
      if 'exit' in sentence:
         break
      sentences = raw_input('Type a sentence: ')
      for sentence in sentences.split('.'):
         print "\nresults: %s" % Alliterate(sentence)
      

if __name__ == '__main__':
   main()
