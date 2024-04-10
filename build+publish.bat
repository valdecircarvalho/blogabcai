git pull
git add .
git commit -m "update source"
git push
hugo --cleanDestinationDir
git add .
git commit -m "site publishing"
git push
