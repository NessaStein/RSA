#!/usr/bin/env python
# -*- coding: utf-8 -*-
__Auther__ = 'M4x'

from gmpy2 import iroot

n=0x7003581fa1b15b80dbe8da5dec35972e7fa42cd1b7ae50a8fc20719ee641d6080980125d18039e95e435d2a60a4d5b0aaa42d5c13b0265da4930a874ddadcd9ab0b02efcb4463a33361a84df0c02dfbd05c0fdc01e52821c683bd265e556412a3f55e49517778079cb1c1c1c22ef8a6e0bccd5e78888ff46167a471f6bff25664a34311c5cb8d6c1b1e7ac2ab0e6676d594734e8f7013b33806868c151316d0cf762a50066c596244fd70b4cb021369aae432e174da502a806e7a8ab13dad1f1b83ac73c0e9e39648630923cbd5726225f17cc0d15afadb7d2c2952b6e092ffc53dcff2914bfddedd043bbdf9c6f6b6b5a6269c5bd423294b9deac4f268eaadb
e=0x3
c=0xb2ab05c888ab53d16f8f7cd39706a15e51618866d03e603d67a270fa83b16072a35b5206da11423e4cd9975b4c03c9ee0d78a300df1b25f7b69708b19da1a5a570c824b2272b163de25b6c2f358337e44ba73741af708ad0b8d1d7fa41e24344ded8c6139644d84dc810b38450454af3e375f68298029b7ce7859f189cdae6cfaf166e58a22fe5a751414440bc6bce5ba580fd210c4d37b97d8f5052a69d31b275c53b7d61c87d8fc06dc713e1c1ce05d7d0aec710eba2c1de6151c84d7bc3131424344b90e3f8947322ef1a57dd3a459424dd31f65ff96f5b8130dfd33111c59f3fc3a754e6f98a836b4fc6d21aa74e676f556aaa5a703eabe097140ec9d98

i = 0
while True:
    if iroot(c + i * n, 3)[1] == True:
        print "Success!"
        print iroot(c + i * n, 3)
        break
    i += 1
