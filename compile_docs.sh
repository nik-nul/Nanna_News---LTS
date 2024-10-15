#!/bin/bash
# sudo apt-get install -y imagemagick # cannot cahced
# sudo mkdir /usr/share/ghostscript/9.55.0/iccprofiles
# sudo cp ./icc/* /usr/share/ghostscript/9.55.0/iccprofiles/
# sudo cp ./icc/* /usr/share/color/icc/ghostscript/
# sudo cp ./policy/policy.xml /etc/ImageMagick-6/policy.xml
cd tex
lualatex -interaction=nonstopmode -jobname=latest --output-directory=../pdfs './000.tex'
cd ..
# convert -density 300 ./pdfs/latest.pdf -append ./imgs/latest.png
echo '/^\\begin{document}/ {print; found=1; next} found && /^% HEAD END/ {print "\\title{南哪消息' $(TZ=Asia/Urumqi date "+%F") '}\\maketitle"; print; found=0; next} found {next} {gsub(/section/, "subsection"); gsub(/\\centerline{\\huge/, "\\section{"); gsub(/\\begin{multicols}\{2\}/, ""); gsub(/\\end{multicols}/, ""); print; }' > pat
awk -f pat ./tex/000.tex > ./tex/tmp.tex
cat header.html <(echo '<style>#textbox {display: flex;justify-content: space-between;}</style><div id="textbox"><p class="alignleft"><a href="https://nik-nul.github.io/news/"><svg fill="#0645ad" height="20px" width="20px" version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 469.411 469.411" xml:space="preserve"><g><g><path d="M397.305,207.826c-67.733-59.947-161.493-61.12-194.56-59.307V74.706c0-5.867-4.8-10.667-10.667-10.667c-2.453,0-4.907,0.853-6.827,2.453L3.918,215.826c-4.587,3.733-5.227,10.453-1.493,15.04c0.427,0.533,0.96,0.96,1.493,1.493l181.333,149.333c4.587,3.733,11.307,3.093,15.04-1.493c1.6-1.92,2.453-4.267,2.453-6.827v-77.013c34.667-8,175.147-30.507,246.613,103.36c1.813,3.52,5.44,5.653,9.387,5.653c3.413,0,6.72-1.6,8.853-4.693c1.28-1.813,1.813-4.053,1.813-6.293C469.305,312.999,445.091,250.279,397.305,207.826z M260.558,269.159c-41.067,0-70.72,8.427-71.467,8.64c-4.587,1.28-7.68,5.44-7.68,10.24v62.72l-153.92-126.72l153.92-126.72v62.72c0,5.867,4.8,10.667,10.667,10.667c0.427,0,0.853,0,1.28-0.107c1.173-0.107,115.2-12.907,189.76,53.227c35.2,31.147,56.213,75.2,62.72,130.987C391.758,284.306,315.811,269.159,260.558,269.159z"/></g></g></svg></a></p><p class="aligncenter">订阅群：<a href="https://qm.qq.com/q/FGX1VYCrGS">962626571</a></p><p class="alignright"><i>Last Update: ' $(TZ=Asia/Shanghai LC_TIME=C date) '</i></p></div><div style="clear: both;"></div><link rel="alternate" type="application/rss+xml" title="RSS" href="https://nik-nul.github.io/news/rss.xml"/><link href="https://nik-nul.github.io/news/rss.xml" type="application/atom+xml" rel="alternate" title="Atom" /><a href="https://nik-nul.github.io/news/feed.atom"><img src="https://nik-nul.github.io/news/validator/atom.svg" alt="Subscribe Via Atom" width="30" height="30" /></a><a href="http://validator.w3.org/feed/check.cgi?url=https%3A//nik-nul.github.io/news/feed.atom"><img src="https://nik-nul.github.io/news/validator/valid-atom.png" alt="[Valid Atom 1.0]" title="Validate my Atom 1.0 feed" /></a><a href="http://validator.w3.org/feed/check.cgi?url=https%3A//nik-nul.github.io/news/rss.xml"><br><a href="https://nik-nul.github.io/news/rss.xml"><img src="https://nik-nul.github.io/news/validator/rss.svg" alt="Subscribe Via RSS" width="30" height="30" /></a><a href="http://validator.w3.org/feed/check.cgi?url=https%3A//nik-nul.github.io/news/rss.xml"><img src="https://nik-nul.github.io/news/validator/valid-rss-rogers.png" alt="[Valid RSS]" title="Validate my RSS feed" /></a>') > ./tex/h
cd tex
# awk '{ gsub(/longtable/, "table"); print $0 }' tmp.tex > tmpp.tex
python3 ../fix_for_pandoc.py
pandoc tmp.tex -s -o ../html/latest.md
pandoc --toc ../html/latest.md -s -V colorlinks=true -V linkcolor=blue -V urlcolor=red -V toccolor=gray --css ../pandoc.css -H h --embed-resources -o ../html/latest.html
python3 ../link.py ../html/latest.html
pandoc ../html/latest.html --to 'markdown_strict+pipe_tables' -o ../README.md
# cp ./html/latest.html ./README.md
# tail ./html/latest.html -n +2 > ./README.md
# cp ./html/latest.html ./README.md
cd ..
python3 ./feed.py
rm ./html/latest.md ./tex/tmp.tex ./tex/tmpp.tex ./pdfs/latest.out ./pdfs/latest.log ./pdfs/latest.aux ./tex/h tmp.md
dtm=$(TZ=Asia/Urumqi date '+%F')
cp ./README.md ./md/$dtm.md
cp ./README.md ./md/latest.md
cat status.md ./md/latest.md > ./README.md
cp ./pdfs/latest.pdf ./pdfs/$dtm.pdf
# cp ./imgs/latest.png ./imgs/$dtm.png
cp ./html/latest.html ./html/$dtm.html
cp ./tex/000.tex ./tex/$dtm.tex