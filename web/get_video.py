import sys
from you_get import common as you_get       #导入you-get库

directory = r'../static/img/video/'                         #设置下载目录
url = 'https://www.bilibili.com/video/BV1QL411H7Ws/?spm_id_from=333.337.search-card.all.click&vd_source=5a2cc1a2e09a7be731e9121ce27a605b'      #需要下载的视频地址
sys.argv = ['you-get','-l','-o',directory,url]
#sys传递参数执行下载，就像在命令行一样；‘-l’是指按列表下载，如果下载单个视频，去掉‘-l’即可；‘-o’后面跟保存目录。
you_get.main()