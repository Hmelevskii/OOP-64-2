# задание 1
from colorama import init, Fore, Back, Style 
# Эта библиотека нужна для изменение цвета строк в терминале, особого смысла в ней нет, просто красивый вывод кода
init(autoreset=True)
print(Fore.RED + 'красный цвет')
print(Fore.YELLOW + 'желтый цвет')
print(Fore.BLACK + 'черный цвет')

# задание 2
def numbers(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return[i, j]
    return []

nums = [2, 7, 11, 15]
target = 9

num = numbers(nums, target)
print(f'два индекса, которые в сумме дают число {target}: {num}')