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

```bash
wget https://download.blender.org/peach/bigbuckbunny_movies/big_buck_bunny_480p_surround-fix.avi -O bunny_short.avi

ffmpeg -i bunny_short.avi -t 2 -vf scale=80:40 -an bunny_2s.mp4

ffmpeg -i bunny_2s.mp4 -vf scale=80:40,format=gray -r 5 frame_%03d.png
for f in frame_*.png; do
    jp2a --width=80 "$f" >> frames.txt
    echo "===FRAME===" >> frames.txt
done
```

```bash
python3 server.py
```

```bash
curl http://localhost:8080/rick
```
yt-dlp -f best -o mickey_short.mp4 "https://www.youtube.com/watch?v=RUhhKb_t2gE" --download-sections "*00:00:00-00:00:05"

ffmpeg -i mickey_short.mp4 -vf scale=80:40,format=gray -r 5 frame_%03d.png
for f in frame_*.png; do
  jp2a --width=80 "$f" >> frames.txt
  echo "===FRAME===" >> frames.txt
done

sudo apt update
sudo apt install yt-dlp

sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp


yt-dlp -f best -o mickey_short.mp4 "https://www.youtube.com/watch?v=RUhhKb_t2gE" --download-sections "*00:00:00-00:00:05"


ffmpeg -i mickey_short.mp4 -vf scale=80:40,format=gray -r 5 frame_%03d.png
for f in frame_*.png; do
  jp2a --width=80 "$f" >> frames.txt
  echo "===FRAME===" >> frames.txt
done



Ton yt-dlp est trop ancien (2022.04.08) → il ne sait plus décoder YouTube (erreurs RegexNotFoundError, Precondition check failed).
Deux chemins possibles. Le plus simple : mettre à jour yt-dlp.

Option A — Mettre à jour yt-dlp (recommandé)
# 1) (facultatif) enlever l’ancienne version apt
sudo apt remove -y yt-dlp

# 2) installer la dernière release “standalone”
sudo wget https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp -O /usr/local/bin/yt-dlp
sudo chmod a+rx /usr/local/bin/yt-dlp

# 3) s’assurer que c’est bien celle-là qui est appelée
which -a yt-dlp
yt-dlp --version
hash -r   # (réinitialise le cache des chemins dans le shell)

Télécharger seulement 5 s
yt-dlp "https://www.youtube.com/watch?v=RUhhKb_t2gE" \
  --download-sections "*00:00:00-00:00:05" \
  -o "mickey_short.%(ext)s" --merge-output-format mp4 --no-playlist


Vérifie le fichier :

ffmpeg -i mickey_short.mp4

Option B — Garder l’ancien yt-dlp et couper avec ffmpeg
yt-dlp -o mickey_full.%(ext)s "https://www.youtube.com/watch?v=RUhhKb_t2gE"
ffmpeg -i mickey_full.mp4 -ss 00:00:00 -t 5 -c copy mickey_short.mp4


(souvent ça échoue avec l’ancienne version à cause des changements YouTube — d’où l’Option A)

Astuces si ça coince encore

Si which -a yt-dlp montre /usr/bin/yt-dlp avant /usr/local/bin/yt-dlp, alors tu utilises encore l’ancienne version. Soit retire celle d’apt, soit mets /usr/local/bin avant dans $PATH.

Sous WSL, garde tout côté Linux (pas dans C:\...) pour éviter des soucis de droits/chemins.

Quand tu auras mickey_short.mp4, reprends la conversion ASCII :

ffmpeg -i mickey_short.mp4 -vf "eq=contrast=1.5:brightness=0.05,scale=80:40,format=gray" -r 5 frame_%03d.png
for f in frame_*.png; do
  jp2a --width=80 "$f" >> frames.txt
  echo "===FRAME===" >> frames.txt
done
