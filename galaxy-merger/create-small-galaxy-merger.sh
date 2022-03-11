cd small
rm *
ln -s ../../standalone-galaxy/small/small-standalone-galaxy.snp small-standalone-galaxy.snp
snapshift in=small-standalone-galaxy.snp out=shifted-galaxy-1.snp rshift=10,0,0 vshift=0,0.3,0
snapshift in=small-standalone-galaxy.snp out=shifted-galaxy-2.snp rshift=-10,0,0 vshift=0,-0.3,0
snapstack in1=shifted-galaxy-1.snp in2=shifted-galaxy-2.snp out=small-galaxy-merger.snp zerocm=true
