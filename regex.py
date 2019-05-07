# 正则表达式  小写属于该范畴，大写属于非该范畴
import re

"""
字符

语法 	说明 	表达式案例 	完整匹配字符串
一般字符 	匹配自身 	abc 	abc
. 	匹配任意除换行符\n外的字符。在DOTALL模式中也能匹配换行符 	a.c 	abc
\ 	转义字符，使后一个字符表示字符本身。 	a.c 	a.c
[...] 	选取字符范围 	a[bcd]e 	abe 或 ace 或 ade

预定义字符集（可以写在字符集[...]中）

\d 	数字:[0-9] 	a\dc 	a1c
\D 	非数字:[^0-9] 	a\Dc 	abc
\s 	空白字符:[<空格>\t\r\n\f\v] 	a\sc 	a c
\S 	非空白字符:[^<空格>\t\r\n\f\v] 	a\Sc 	abc
\w 	单词字符:[A-Za-z0-9_] 	a\wc 	abc
\W 	非单词字符:[^A-Za-z0-9_] 	a\Wc 	a c

数量词（用在字符或(...)之后）

语法 	说明 	表达式案例 	完整匹配字符串
* 	匹配前一个字符0次或无限次。 	abc* 	abccc
+ 	匹配前一个字符1次或无限次。 	abc+ 	abccc
? 	匹配前一个字符0次或1次。 	abc? 	abc 或 ab
{m} 	匹配前一个字符m次。 	ab{2}c 	abbc

"""


def run():
    # d数字 s空白字符 w单词字符（含数字）
    # *匹配前一个字符0次或无限次 +匹配前一个字符1次或无限次 ？匹配前一个字符0次或1次 {m}匹配前一个字符m次
    # result = re.match("a\D", "abc")
    result = re.match("a{3}\d{3}\w{4}", "aaa123bddccc")
    print(result.group())


if __name__ == '__main__':
    run()
