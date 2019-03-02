Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> s=set()
>>> s
set()
>>> s.add(7)
>>> s
{7}
>>> s.add(67)
>>> s
{67, 7}
>>> s=[1,1,2,3,2,1,56,3]
>>> set(s)
{56, 1, 2, 3}
>>> 2<9
True
>>> 2>=78
False
>>> a=True
>>> a
True
>>> a=3
>>> b=67
>>> a>b
False
>>> b=None
>>> a<b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a<b
TypeError: '<' not supported between instances of 'int' and 'NoneType'
>>> b
>>> 
