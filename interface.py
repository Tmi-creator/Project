def interface():
    print("Приветствую тебя, странник! Если желаешь сыграть в пвп, жми 1, если против мобов - 2.")
    choice1 = int(input())
    if (choice1 == 1):
        print("1 на 1(1), командное(2) или ффа(3)?")
        choice2 = int(input())
        if (choice2 == 1):
            print(
                "Ну, да начнется бой!\nВыберете персонажа для битвы:\nВоин-1\nМаг-2\nРазбойник-3\nПаладин-4\nОхотник-5\nЧернокнижник-6\nШаман-7\nДруид-8\nЖрец-9\n")
            choice3 = int(input())

            choice4 = int(input())

            units = {
                1: Warrior,
                2: Mage,
                3: Rogue,
                4: Paladin,
                5: Hunter,
                6: Warlock,
                7: Shaman,
                8: Druid,
                9: Priest

            }

            while choice3 not in units:
                print("Incorrect choice.")
                choice3 = int(input())
            p1 = units[choice3]
            while choice4 not in units:
                print("Incorrect choice.")
                choice4 = int(input())
            p2 = units[choice4]
            while (p1.hp != 0 or p2.hp != 0):
                print(
                    "p1 turn, 1 - обычная атака,\n 2 - использование 1 способности,\n 3 - использование второй способности, и\n 4 - использование 3 способности\n")
                print(p1.hp, p1.cur_atk, p1.mana, "- p1")
                print(p2.hp, p2.cur_atk, p2.mana, "- p2")
            choices = {
                1: p1.attack(p2)
                2: p1.first_skill(p2)
                3: p1.second_skill(p2)
                4: p1.third_skill(p2)
                5: p2.attack(p1)
                6: p2.first_skill(p1)
                7: p2.second_skill(p1)
                8: p2.third_skill(p1)
            }
            t1 = int(input())
            t2 = int(input())
            choices.get(t1)
            choices.get(t2 + 4)


if (__name__ == __main__):
    run.interface()
