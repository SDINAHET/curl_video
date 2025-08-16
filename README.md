# curl_video
https://github.com/SDINAHET/curl_video.git
```bash
curl ascii.live/rick
```

```bash
wget https://archive.org/download/mov-bbb/mov_bbb.mp4 -O bunny_10s.mp4
```

```bash
sudo apt install ffmpeg jp2a
```

```bash
ffmpeg -i bunny_10s.mp4 -vf scale=80:40,format=gray -r 10 frame_%04d.png
for f in frame_*.png; do
    jp2a --width=80 "$f" >> frames.txt
    echo "===FRAME===" >> frames.txt
done
```
