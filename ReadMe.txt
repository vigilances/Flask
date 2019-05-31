1.app.route()装饰器

2.*arg 不定参数 tuple ，**kwargs 关键字参数 dict

3.https://github.com/CriseLYJ/Python-crawler-tutorial-starts-from-zero  爬虫（正则表达、数据处理）

4.python中extend和append区别：extend接受一个list参数，并添加到末尾；append是接受一个对象参数，并添加到末尾

5.找出单链表的倒数第K个元素：定义两个指针A、B，A先走K步，接着A、B一起走，当A走到链表尾端，这是B所指的位置就是倒数第K个元素。
class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if head == None or k == 0:
            return None
        phead = head
        pbehind = head
        for i in range(k-1):
            if phead.next == None:
                return None
            else:
                phead = phead.next
        while phead.next != None:
            phead = phead.next
            pbehind = pbehind.next
        return pbehind

6.pscp D:\Desktop\vip视频.exe root@45.77.70.45:/root/ftp/ pscp上传文件

7.