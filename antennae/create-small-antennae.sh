cd small
rm base.snp scaled.snp rotated-*.snp shifted-*.snp small-antennae.snp
magalie out=base.snp ndisk=3000 nbulge=1000 nhalo=16000 mbulge=1/3 mhalo=16/3
snapscale in=base.snp out=scaled.snp mscale=1/5 rscale=1/12 vscale=1.549193338
snaprotate in=scaled.snp out=rotated-1.snp theta=-60,30 order=xz
snaprotate in=scaled.snp out=rotated-2.snp theta=-60,210 order=xz
snapshift in=rotated-1.snp out=shifted-1.snp rshift=-0.4715564761791193,-0.3884990711187128,0 vshift=0.5807543868265013,-0.24773172614949923,0
snapshift in=rotated-2.snp out=shifted-2.snp rshift=0.4715564761791193,0.3884990711187128,0 vshift=-0.5807543868265013,0.24773172614949923,0
snapstack in1=shifted-1.snp in2=shifted-2.snp out=small-antennae.snp zerocm=false
