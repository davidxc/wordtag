"""Tests the part of speech tagging and 
  the part of speech number of occurrences counting."""

from __future__ import absolute_import
from __future__ import unicode_literals

import unittest

from word_tag.business import tag_text

class TestTagging(unittest.TestCase):
    """Part of speech tagging sometimes differs
        depending on the context of the word and the tagger.
        This is basic testing."""
         
    def setUp(self):
        self.sentence = "He likes to read books about expressive languages."
        self.paragraph = """The sea otter swam in the sea for a while. It slowly drifted on the waves, eating
        a clam that it had found."""
        
        """Parts of speech for self.sentence - He(PRP) likes(VBZ) to(TO) read(VB) books(NNS) about(IN)
           expressive(JJ) languages(NNS) ./."""
        
        """Parts of speech for self.paragraph - The(DT) sea(NN) otter(NN) swam(NN) in(IN) the(DT) sea(NN)
           for(IN) a(DT) while(NNP). It(NNP) slowly(RB) drifted(VBD) on(IN) the(DT) waves(NNS) ,/, eating(VBG)
           a(DT) clam(NN) that(WDT) it(PRP) had(VBD) found(VBN) ./."""
           
    def test_sentence(self):
        counter_tags = tag_text(text=self.sentence, use_averages=False)[1]
        self.assertEqual(counter_tags['PRP'], 1)
        self.assertEqual(counter_tags['VBZ'], 1)
        self.assertEqual(counter_tags['TO'], 1)
        self.assertEqual(counter_tags['VB'], 1)
        self.assertEqual(counter_tags['NNS'], 2)
        self.assertEqual(counter_tags['IN'], 1)
        self.assertEqual(counter_tags['JJ'], 1)
        self.assertEqual(counter_tags['words'], 8)
        self.assertEqual(counter_tags['sentences'], 1)
        
    def test_sentence_averages(self):
        counter_tags = tag_text(text=self.sentence, use_averages=True)[1]
        self.assertEqual(counter_tags['PRP'], 1)
        self.assertEqual(counter_tags['VBZ'], 1)
        self.assertEqual(counter_tags['TO'], 1)
        self.assertEqual(counter_tags['VB'], 1)
        self.assertEqual(counter_tags['NNS'], 2)
        self.assertEqual(counter_tags['IN'], 1)
        self.assertEqual(counter_tags['JJ'], 1)
        self.assertEqual(counter_tags['words'], 8)
        self.assertEqual(counter_tags['sentences'], 1)
    
    def test_paragraph(self):
        counter_tags = tag_text(text=self.paragraph, use_averages=False)[1]
        self.assertEqual(counter_tags['DT'], 5)
        self.assertEqual(counter_tags['NN'], 5)
        self.assertEqual(counter_tags['IN'], 3)
        self.assertEqual(counter_tags['NNP'], 2)
        self.assertEqual(counter_tags['RB'], 1)
        self.assertEqual(counter_tags['VBD'], 2)
        self.assertEqual(counter_tags['NNS'], 1)
        self.assertEqual(counter_tags['VBG'], 1)
        self.assertEqual(counter_tags['WDT'], 1)
        self.assertEqual(counter_tags['PRP'], 1)
        self.assertEqual(counter_tags['VBN'], 1)
        self.assertEqual(counter_tags['words'], 23)
        self.assertEqual(counter_tags['sentences'], 2)
        
    def test_paragraph_averages(self):
        counter_tags = tag_text(text=self.paragraph, use_averages=True)[1]
        self.assertEqual(counter_tags['DT'], 2.5)
        self.assertEqual(counter_tags['NN'], 2.5)
        self.assertEqual(counter_tags['IN'], 1.5)
        self.assertEqual(counter_tags['NNP'], 1)
        self.assertEqual(counter_tags['RB'], 0.5)
        self.assertEqual(counter_tags['VBD'], 1)
        self.assertEqual(counter_tags['NNS'], 0.5)
        self.assertEqual(counter_tags['VBG'], 0.5)
        self.assertEqual(counter_tags['WDT'], 0.5)
        self.assertEqual(counter_tags['PRP'], 0.5)
        self.assertEqual(counter_tags['VBN'], 0.5)
        self.assertEqual(counter_tags['words'], 11.5)
        self.assertEqual(counter_tags['sentences'], 2)
        

         
if __name__ == '__main__':
    unittest.main()    
        
