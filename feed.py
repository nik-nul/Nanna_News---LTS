#!/bin/python3
import re
import urllib.parse
import datetime
import zoneinfo
import urllib


import os
os.system("pandoc ./html/latest.html --to 'markdown_strict' -o ./tmp.md")
today = os.popen("TZ=Asia/Urumqi date '+%F'").read()[:-1]
filename = f"./tmp.md" 

with open(filename, 'r', encoding='utf-8') as file:
    content = file.read()


pattern = r'^## (.+)$\n([\s\S]+?)(?=\n## |\Z)'
matches = re.finditer(pattern, content, re.MULTILINE)

result = {}
for match in matches:
    title = match.group(1).strip()
    content = match.group(2).strip()
    if title != "讲座" and "ngoing" not in title:
        content = content.replace("<", "").replace(">", "").replace("\n", "\n<br>")
    result[title] = content

url = f"https://nik-nul.github.io/news/{today}"

import feedgen.feed

fg = feedgen.feed.FeedGenerator()
fg.title(f"南哪消息 {filename[:-3]}")
fg.description("南哪大专集约化信息发布")
fg.id("https://nik-nul.github.io/rss.xml")
fg.author({"name": "南哪小报编辑部", "email": "231220103@smail.nju.edu.cn"})
fg.pubDate(datetime.datetime.now(tz=zoneinfo.ZoneInfo("Asia/Shanghai")))
fg.copyright("TO BE DETERMINED")
fg.skipHours(list(range(1, 22)))
fg.webMaster("231220103@smail.nju.edu.cn (nik_nul)")
fg.managingEditor("231508004@smail.nju.edu.cn (sakiko)")
fg.language("zh")
fg.ttl(1300)

for k, v in result.items():
    fe = fg.add_entry()
    fe.title(k)
    fe.content(v, type="html")
    fe.guid(url + "#" + urllib.parse.quote(k), permalink=True)
    fe.link({"href": url + "#" + urllib.parse.quote(k), "rel": "self"})

fg.link([{"href": "https://nik-nul.github.io/news/rss.xml", "rel": "self"}, {"href": url, "rel":"alternate"}])
fg.rss_file("./feed/rss.xml")

fg.link([{"href": "https://nik-nul.github.io/news/feed.atom", "rel": "self"}, {"href": url, "rel":"alternate"}], replace=True)
fg.atom_file("./feed/feed.atom")