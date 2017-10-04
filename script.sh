for i in {1..9}
do
  cd lesson$i
  mv assignment$i.md README.md
  cd ..
done
