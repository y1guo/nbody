cd regular
glnemo2 in=antennae.run.snp select=0:149999,1000000:1149999 osd=f perspective=f xrot=90 zrot=-45 wsize=3840 hsize=2160 point=f texture=t auto_ts=f texture_s=0.01 bestzoom=f ortho_range=1 play=t shot_ext=png screenshot=frame 
ffmpeg -y -i frame.%05d.png -c:v libx264 -vf fps=60 -pix_fmt yuv420p antennae.mp4
rm frame.*.png