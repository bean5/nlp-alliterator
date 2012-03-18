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
   return word

def main():
   sentence = ''
   character = 's'
   while True:
      if 'exit' in sentence:
         break
      sentence = raw_input('Type a sentence: ')
      tokens = sentence.split(' ')
      results = [alliterate(word=token, character=character) for token in tokens]
      print ' '.join(results)
      

if __name__ == '__main__':
   main()
