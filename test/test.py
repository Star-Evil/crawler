"""
just for testing.
"""
from lxml import etree

f = open('html.txt', 'r')	# 如果文件编码为UTF-8, 记得添加参数：encoding='utf8'
text = f.read()

html = etree.HTML(text, etree.HTMLParser())
result = html.xpath('//a/text()')
print(result)

