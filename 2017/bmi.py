#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
high=1.75
weight=80.5
bmi=weight/(high*high)
'''
print('BMI測試工具')

while True:
	heigh=float(input('請輸入身高(M,例如1.75):'))
	weight=float(input('請輸入體重(KG,例如80):'))

	if heigh<0 or weight<0:
		print('身高或體重輸入有誤,請重新輸入.')

	else:
		bmi=weight/(heigh*heigh)

		if bmi<18.5:
				print('您的BMI爲:%.2f'%bmi,'體重過輕')
		elif bmi<25:
				print('您的BMI爲:%.2f'%bmi,'正常')
		elif bmi<28:
				print('您的BMI爲:',bmi,'過胖')
		elif bmi<32:
				print('您的BMI爲:',bmi,'肥胖')
		else:
				print('您的BMI爲:',bmi,'嚴重肥胖')
	print('點擊Enter繼續,Ctrl+C退出')
	input()

