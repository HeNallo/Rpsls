#coding:gbk
"""
程序目的：通过自定义函数，实现RPSLS游戏，用户通过键盘输入任意一个选择（石头/剪刀/布/蜥蜴/史波克）,计算机自动生成一个随机选择，根据RPSLS规则，产生最终的结果
程序作者：熊逸凡
程序时间：2021/05/27
"""
print("欢迎使用RPSLS游戏")
print("----------------")
import random

player=int(input("请输入您的选择"))
number=random.randint(0,4)

if player==0:
	print("您的选择为：石头")
elif player==1:
	print("您的选择为：史波克")
elif player==2:
	print("您的选择为：布")
elif player==3:
	print("您的选择为：蜥蜴")
elif player==4:
	print("您的选择为：剪刀")

if number==0:
	print("电脑的选择为：石头")
if number==1:
	print("电脑的选择为：史波克")
if number==2:
	print("电脑的选择为：布")
if number==3:
	print("电脑的选择为：蜥蜴")
if number==4:
	print("电脑的选择为：剪刀")

if player==number:
	print("平局")
elif player==4 and number==2:
	print("您赢了!")
elif player==2 and number==1:
	print("您赢了!")
elif player==0 and number==4:
	print("您赢了!")	
elif player==0 and number==3:
	print("您赢了!")
elif player==3 and number==1:
	print("您赢了!")
elif player==1 and number==4:
	print("您赢了!")	
elif player==4 and number==3:
	print("您赢了!")			
elif player==3 and number==2:
	print("您赢了!")		
elif player==2 and number==1:
	print("您赢了!")			
elif player==1 and number==0:
	print("您赢了!")			

elif player==2 and number==4:
	print("您输了")
elif player==1 and number==2:
	print("您输了")
elif player==4 and number==0:
	print("您输了")	
elif player==3 and number==0:
	print("您输了")
elif player==1 and number==3:
	print("您输了")
elif player==4 and number==1:
	print("您输了")	
elif player==3 and number==4:
	print("您输了")			
elif player==2 and number==3:
	print("您输了")		
elif player==1 and number==2:
	print("您输了")			
elif player==0 and number==1:
	print("您输了")		
else:
	print("Error. No Correct Name")
	

	
	



