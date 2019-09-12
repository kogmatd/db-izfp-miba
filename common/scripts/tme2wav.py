#!/usr/bin/python3

import os
import sys
import numpy as np
import wave

if len(sys.argv)<3:
    print('Usage: '+sys.argv[0]+' {FILE.tme} OUTDIR')
    raise SystemExit()

encoding='>f4'
srate=22050
gain=2048

odir=sys.argv[-1]
for fn in sys.argv[1:-1]:
    ofn=os.path.join(odir,os.path.basename(fn).replace('.tme','')+'.wav')
    with open(fn,'rb') as f:
        buf=f.read()
        arr=np.frombuffer(buf[4:],encoding)
        with wave.open(ofn,'wb') as w:
            w.setnchannels(1)
            w.setsampwidth(2)
            w.setframerate(srate)
            w.writeframesraw((arr*gain).astype(np.int16).tobytes())

