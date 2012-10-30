#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Author: David Wong <davidwong.xc@gmail.com>
License: 3 clause BSD license

This module only contains the text tagging function right now.

"""

from __future__ import absolute_import
from __future__ import unicode_literals

import collections

import nltk

def tag_text(text, use_averages):
    
        text = text
        tokens = nltk.word_tokenize(text)
        tagged_tokens = nltk.pos_tag(tokens)
        
        list_tagged_tokens = ["/".join(i) for i in tagged_tokens]
        tagged_text = " ".join(list_tagged_tokens)
        
        counter_tags = collections.Counter()
        words = 0
        sentences = 0
        
        for pairs in tagged_tokens:
            counter_tags[pairs[1]] += 1
            if pairs[1] != '"' and pairs[1] != '\'\'' and pairs[1] != '``' and pairs[1] != '.' and pairs[1] != ',':
                words += 1
            if '.' in pairs[0] or '?' in pairs[0] or '!' in pairs[0]:
                sentences += 1
        
        #Check if option is selected to show averages per sentence.
                
        if use_averages:
            sentences = float(sentences)
            if sentences != 0:
                for key in counter_tags:
                    counter_tags[key] /= sentences
                words /= sentences
            
                
        counter_tags['words'] = words
        counter_tags['sentences'] = sentences
        
                
        return tagged_text, counter_tags