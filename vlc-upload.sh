
for i in ./*
do
  curl --progress-bar -F "files[]=@$i" http://miphone.local/upload.json | tee /dev/null
done
