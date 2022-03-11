cd small
rm base.snp scaled.snp rotated-*.snp shifted-*.snp antennae.snp
magalie out=base.snp ndisk=150000 nbulge=50000 nhalo=800000 mbulge=1/3 mhalo=16/3
snapscale in=base.snp out=scaled.snp mscale=1/5 rscale=1/12 vscale=1.549193338
snaprotate in=scaled.snp out=rotated-1.snp theta=-60,30 order=xz
snaprotate in=scaled.snp out=rotated-2.snp theta=-60,210 order=xz
snapshift in=rotated-1.snp out=shifted-1.snp rshift=-0.4715564761791193,-0.3884990711187128,0 vshift=0.5807543868265013,-0.24773172614949923,0
snapshift in=rotated-2.snp out=shifted-2.snp rshift=0.4715564761791193,0.3884990711187128,0 vshift=-0.5807543868265013,0.24773172614949923,0
snapstack in1=shifted-1.snp in2=shifted-2.snp out=antennae.snp zerocm=false
