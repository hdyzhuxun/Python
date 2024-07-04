进口要求
进口关于
进口时间
本地=时间。strftime(" %Y.%m.%d ")
url =' http://cn.bing.com/'
con =请求。得到(全球资源定位器(Uniform Resource Locator))
内容= con。文本
reg =r"(az/hprichbg/rb/。*?。jpg)"
a = re。芬达尔(注册，内容，回复。S)[0]
打印(a)
picUrl = url + a
读取=请求。得到(皮库尔)
f =打开(%s.jpg '%本地，wb ')
f.写(阅读。内容)
f.关闭()
