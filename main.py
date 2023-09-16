import pandas as pd
date = pd.read_excel("lab_pi_101.xlsx")
KolOtm = date.shape[0]
KoiOtmPI101 = date['Группа'].str.contains('ПИ101').sum()
NunberStud = date['Личный номер студента']
NunberStud1 = []
for i in NunberStud:
    if i not in NunberStud1:
        NunberStud1.append(1)
StudLast = len(NunberStud1)        
KolStudPI101 = len(date[date['Группа'] == 'ПИ101']['Личный номер студента'].unique())
NunberP101 = date.loc[date['Группа'] == 'ПИ101', 'Личный номер студента'].unique()
Control =date['Уровень контроля'].unique()
Years = date['Год'].unique()
print ('В исходном датасете содержалось оценок', KolOtm, 'из них', KoiOtmPI101, 'оценок относятся к группе ПИ101')
print ('В датасете находятся оценки', KolStudPI101,'студентов со следующими личными номерами (по ПИ101):', NunberP101)
print ('Используемые формы контроля:', Control)  
print ('Данные представлены по следующим учебным годам:', Years)