echo '/^\\begin{document}/ {print; found=1; next} found && /^% HEAD END/ {print "\\title{南哪消息' $(TZ=Etc/UTC date "+%F") '}\\maketitle"; print; found=0; next} found {next} {gsub(/section/, "subsection"); gsub(/\\centerline{\\huge/, "\\section{"); gsub(/\\begin{multicols}\{2\}/, ""); gsub(/\\end{multicols}/, ""); print; }' > pat
awk -f pat ./tex/000.tex > ./tex/tmp.tex
cp mailhead.html ./tex/
cp pandoc.css ./tex/
cd tex
python3 ../fix_for_pandoc.py
pandoc tmp.tex -s -o ./latest.md
pandoc --toc ./latest.md -s -V colorlinks=true -V linkcolor=blue -V urlcolor=red -V toccolor=gray --css pandoc.css -H mailhead.html --embed-resources -o ../tmp.html
cd ..
python3 ./link.py ./tmp.html
