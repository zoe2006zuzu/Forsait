# TODO Напишите функцию find_common_participants
def find_common_participants(gr1, gr2, r='|'):
    participants1=gr1.split(r)
    print(participants1)
    participants2=gr2.split(r)
    spisok = list(set(participants1) & set(participants2))
    spisok.sort()
    return spisok
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
# TODO Провеьте работу функции с разделителем отличным от запятой
otvet = find_common_participants(participants_first_group, participants_second_group)
print(otvet)