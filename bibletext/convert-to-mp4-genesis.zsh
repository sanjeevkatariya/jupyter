ffmpeg -loop 1 -i genesis.webp -i genesis.mp3 -c:a aac -b:a 128k -c:v libx264 -tune stillimage -shortest -pix_fmt yuv420p -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" genesis.mp4
