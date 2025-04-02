def main():
    apples = int(input("Сколько у вас яблок? "))
    people = int(input("Сколько человек? "))
    if people > 0:
        apples_per_person = apples // people
        remaining_apples = apples % people
        print(f"Каждый получит по {apples_per_person} яблок(а), остаток: {remaining_apples} яблок(а).")
    else:
        print("На ноль делить нельзя!")

if __name__ == "__main__":
    main()
