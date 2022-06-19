import bitcoin

import hashlib

header = bitcoin.getblock(bitcoin.getblockhash(bitcoin.getblockcount()))['data']

print (header)
