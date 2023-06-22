import openpyxl
import os
from pathlib import Path


print('Для удаления 1-го листа введите 1 \n ')
choose_func = int(input())
path = str(input('Введите путь к папке с файлами Excel - '))
files = os.listdir(path)
savep = str(input('Введите путь сохранения файлов - '))


def remove_one_sheet():
    deleted_sheets = str(input('Введите наименование листов которые будут удалены - '))
    for i in range(len(files)):
        workbook = openpyxl.load_workbook(path + '\\' + files[i])
        if deleted_sheets in workbook.sheetnames:
            workbook.remove(workbook[deleted_sheets])
            workbook.save(savep + '\\' + files[i])


if choose_func == 1:
    remove_one_sheet()