#coding:gbk
"""
����Ŀ�ģ�ͨ���Զ��庯����ʵ��RPSLS��Ϸ���û�ͨ��������������һ��ѡ��ʯͷ/����/��/����/ʷ���ˣ�,������Զ�����һ�����ѡ�񣬸���RPSLS���򣬲������յĽ��
�������ߣ����ݷ�
����ʱ�䣺2021/05/27
"""
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
import random

player=int(input("����������ѡ��"))
number=random.randint(0,4)

if player==0:
	print("����ѡ��Ϊ��ʯͷ")
elif player==1:
	print("����ѡ��Ϊ��ʷ����")
elif player==2:
	print("����ѡ��Ϊ����")
elif player==3:
	print("����ѡ��Ϊ������")
elif player==4:
	print("����ѡ��Ϊ������")

if number==0:
	print("���Ե�ѡ��Ϊ��ʯͷ")
if number==1:
	print("���Ե�ѡ��Ϊ��ʷ����")
if number==2:
	print("���Ե�ѡ��Ϊ����")
if number==3:
	print("���Ե�ѡ��Ϊ������")
if number==4:
	print("���Ե�ѡ��Ϊ������")

if player==number:
	print("ƽ��")
elif player==4 and number==2:
	print("��Ӯ��!")
elif player==2 and number==1:
	print("��Ӯ��!")
elif player==0 and number==4:
	print("��Ӯ��!")	
elif player==0 and number==3:
	print("��Ӯ��!")
elif player==3 and number==1:
	print("��Ӯ��!")
elif player==1 and number==4:
	print("��Ӯ��!")	
elif player==4 and number==3:
	print("��Ӯ��!")			
elif player==3 and number==2:
	print("��Ӯ��!")		
elif player==2 and number==1:
	print("��Ӯ��!")			
elif player==1 and number==0:
	print("��Ӯ��!")			

elif player==2 and number==4:
	print("������")
elif player==1 and number==2:
	print("������")
elif player==4 and number==0:
	print("������")	
elif player==3 and number==0:
	print("������")
elif player==1 and number==3:
	print("������")
elif player==4 and number==1:
	print("������")	
elif player==3 and number==4:
	print("������")			
elif player==2 and number==3:
	print("������")		
elif player==1 and number==2:
	print("������")			
elif player==0 and number==1:
	print("������")		
else:
	print("Error. No Correct Name")
	

	
	



