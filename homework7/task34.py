# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод:
# пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод:
# Парам пам-пам


# def find_rhythm(poem):
#     list_of_phrases = poem.split()
#     rhythm_of_first_phrase = sum_of_vovels_in_phrase(list_of_phrases[0])
#     print(list_of_phrases[0], rhythm_of_first_phrase)
#     for i in range(1, len(list_of_phrases)):
#         print(list_of_phrases[i], sum_of_vovels_in_phrase(list_of_phrases[i]))
#         if sum_of_vovels_in_phrase(list_of_phrases[i]) != rhythm_of_first_phrase:
#             return 'Пам парам'
#     return 'Парам пам-пам'
#
# def sum_of_vovels_in_phrase(phrase):
#     list_of_vowel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
#     count = 0
#     for i in phrase:
#         count = count + 1 if i in list_of_vowel_letters else count
#         # if i in list_of_vowel_letters:
#         #     count += 1
#     return count

def find_rhythm(poem):
    list_of_vowel_letters = ['а', 'о', 'э', 'е', 'и', 'ы', 'у', 'ё', 'ю', 'я']
    list_of_vovels_in_phrase = [''.join(filter(lambda x: x in list_of_vowel_letters, phrase)) for phrase in poem.split()]
    # print(list_of_vovels_in_phrase)
    rhythm_of_first_phrase = len(list_of_vovels_in_phrase[0])
    for i in range(1, len(list_of_vovels_in_phrase)):
        if len(list_of_vovels_in_phrase[i]) != rhythm_of_first_phrase:
            return 'Пам парам'
    return 'Парам пам-пам'

vinnies_poem = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
print(find_rhythm(vinnies_poem))

