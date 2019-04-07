#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:47:30 2019

@author: Yssubhi
"""

import random

rand_q  = ['''Could you explain the {0} of {1} to me?''',
           '''That sounds interesting. I would like to know more about {0} of {1}''',
           '''{0}? What an exciting topic! Explain {0} of {1} to me?''',
           '''Never thought about {0} of {1}! Tell me more!''',
           '''Wuaw, {0} of {1}? So much to learn. Hit me!''']

rand_e = ['''Hmm, could you elaborate on that?''',
          '''Could you try explaining it another way?''',
          '''I got a bit confused. Sorry! Wanna go again?''',
          '''Ooooooooh. Actually. I got nothing. Give me another chance''']
                    

rand_a = ['''Cool!''',
          '''Got it!''',
          '''Interesting!''',
          '''You always so smart''',
          '''ooooooooooh. Facinating''']

question_format = random.choice(rand_q)

elaborate_format = random.choice(rand_e)

appraise_format = random.choice(rand_a)

