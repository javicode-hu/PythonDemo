from lxml import etree
html = etree.parse('hello.html')

# result = html.xpath('//li//span')#获取 <li> 标签下的所有 <span> 标签
# print (result)
# result = html.xpath('//li/a[@href="link1.html"]')#获取 <li> 标签下 href 为 link1.html 的 <a> 标签
# print (result)

# result = html.xpath('//li[last()]/a/@href')#获取最后一个 <li> 的 <a> 的 href
# print result

# result = html.xpath('//li/a//@class')#获取 <li> 标签下的所有 class，不包括 <li>
# print (result)
# result = html.xpath('//li/@class')#获取 <li> 标签的所有 class
# print (result)
# result = html.xpath('//li[last()-1]/a') # 获取倒数第二个元素的内容
# print(result[0].text)
# result = html.xpath('//*[@class="bold"]')   #获取 class 为 bold 的标签名
# print(result[0].tag)

