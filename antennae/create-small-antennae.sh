cd small
rm *
magalie out=base.snp ndisk=3000 nbulge=1000 nhalo=16000 mbulge=1/3 mhelo=16/3
snaprotate in=base.snp out=rotated-1.snp theta=30,-60 order=z,x
snaprotate in=base.snp out=rotated-2.snp theta=-150,-60 order=z,x
snapshift in=base.snp out=shifted-1.snp rshift=-10,0,0 vshift=0,-0.3,0
snapshift in=base.snp out=shifted-2.snp rshift=10,0,0 vshift=0,0.3,0
snapstack in1=shifted-galaxy-1.snp in2=shifted-galaxy-2.snp out=small-galaxy-merger.snp zerocm=true
