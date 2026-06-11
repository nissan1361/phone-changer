def vopros(tekst, varianty):
    print(f"\n{tekst}")
    for i, v in enumerate(varianty, 1):
        print(f"  {i}. {v}")
    while True:
        try:
            vybor = int(input("  >>> "))
            if 1 <= vybor <= len(varianty):
                return vybor
            print(f"  Введите число от 1 до {len(varianty)}")
        except ValueError:
            print("  Введите число")

def rekomendovat(budzhet, kamera, igry, batareya, ekosistema, kompakt):
    kategorii = []

    if budzhet <= 1:
        kategorii.append("бюджетный")
    elif budzhet == 2:
        kategorii.append("средний")
    elif budzhet == 3:
        kategorii.append("выше среднего")
    else:
        kategorii.append("флагманский")

    if ekosistema == 2:
        kategorii.append("ios")
    else:
        kategorii.append("android")

    if kamera >= 4 or (kamera >= 3 and budzhet >= 3):
        kategorii.append("камерафон")
    if igry >= 4:
        kategorii.append("игровой")
    if batareya >= 4:
        kategorii.append("с мощным аккумулятором")
    if kompakt == 1:
        kategorii.append("компактный")

    print("\n" + "=" * 60)
    print("        ПОДБОР СМАРТФОНА ПО ВАШИМ ПАРАМЕТРАМ")
    print("=" * 60)

    if "ios" in kategorii:
        print("\n  Рекомендации iPhone:")
        if budzhet <= 1:
            print("  • iPhone SE (2022) — лучший бюджетный вход в экосистему Apple")
            print("  • iPhone 13 (б/у или со скидкой) — отличный вариант за свои деньги")
        elif budzhet == 2:
            print("  • iPhone 15 — отличная камера, USB-C, Dynamic Island")
            print("  • iPhone 14 Plus — большой экран и хорошая автономность")
        elif budzhet == 3:
            print("  • iPhone 16 Pro — титан, новая камера, мощный процессор")
            print("  • iPhone 16 — отличный баланс цены и возможностей")
        else:
            print("  • iPhone 16 Pro Max — максимум возможностей Apple")
            print("  • iPhone 16 Pro — лучший компактный флагман")
            if kamera >= 4:
                print("  • Камера Pro Max — лучшая в своём классе для фото и видео")

    print("\n  Рекомендации Android:")
    if budzhet <= 1:
        if batareya >= 4:
            print("  • Xiaomi Redmi Note 14 — отличная автономность, ёмкий аккумулятор")
            print("  • Samsung Galaxy A16 — хорошая батарея и долгие обновления")
        else:
            print("  • Xiaomi Redmi Note 14 — лучший вариант за свои деньги")
            print("  • Samsung Galaxy A15 — стабильная работа и хороший экран")
        print("  • Motorola Moto G85 — чистый Android, карта памяти, разъём 3.5 мм")
    elif budzhet == 2:
        if kamera >= 3:
            print("  • Google Pixel 8a — лучшая камера в среднем сегменте")
            print("  • Samsung Galaxy A55 — хороший экран, защита IP67")
        else:
            print("  • OnePlus Nord 4 — быстрая зарядка, хорошая производительность")
            print("  • Poco X7 Pro — отличное соотношение цена/производительность")
        if kompakt == 1:
            print("  • Google Pixel 8a — компактный корпус с отличной камерой")
    elif budzhet == 3:
        print("  • Google Pixel 9 — лучшая камера, чистый Android, долгие обновления")
        print("  • OnePlus 13 — молниеносная зарядка, отличный экран")
        print("  • Samsung Galaxy S25 — компактный флагман с хорошей камерой")
        if igry >= 4:
            print("  • OnePlus 13 — лучшая производительность в играх в этом сегменте")
    else:
        print("  • Samsung Galaxy S25 Ultra — лучший экран, S-Pen, камера-зум")
        print("  • Xiaomi 16 Pro — мощная камера Leica, быстрая зарядка")
        if igry >= 4:
            print("  • ASUS ROG Phone 9 — лучший игровой смартфон без компромиссов")
            print("  • Samsung Galaxy S25 Ultra — флагманская производительность для любых игр")
        if kamera >= 4:
            print("  • Samsung Galaxy S25 Ultra — 200 МП камера, лучший зум")
            print("  • Xiaomi 16 Pro — камера Leica с профессиональными режимами")
        if kompakt == 1:
            print("  • Samsung Galaxy S25 — компактный флагман без урезаний")

    print("\n" + "-" * 60)
    print("  💡 Совет: перед покупкой подержите телефон в руках в магазине.")
    print("  💡 Сравните цены в разных магазинах и проверьте наличие чехлов")
    print("      и защитного стекла для выбранной модели.")
    print("-" * 60)


def main():
    print("=" * 60)
    print("   КАКОЙ СМАРТФОН ВАМ ПОДОЙДЁТ?")
    print("   Ответьте на несколько вопросов —")
    print("   программа подберёт лучшие варианты.")
    print("=" * 60)

    budzhet = vopros(
        "Какой у вас бюджет?",
        [
            "до 20 000 ₽ — нужен надёжный бюджетный телефон",
            "20 000 – 40 000 ₽ — хороший средний сегмент",
            "40 000 – 70 000 ₽ — выше среднего, почти флагман",
            "от 70 000 ₽ — флагман без компромиссов",
        ],
    )

    kamera = vopros(
        "Насколько важна камера?",
        [
            "не важно — сфоткать документы и всё",
            "средне — иногда снимаю на отдыхе",
            "важно — люблю фотографировать",
            "очень важно — снимаю фото/видео постоянно",
            "критически важно — увлекаюсь мобильной фотографией",
        ],
    )

    igry = vopros(
        "Как часто вы играете в игры на телефоне?",
        [
            "не играю вообще",
            "редко — казуальные игры",
            "иногда — нетребовательные игры",
            "часто — современные игры на средних настройках",
            "постоянно — хочу максимум графики и FPS",
        ],
    )

    batareya = vopros(
        "Насколько важна автономность?",
        [
            "не важно — всегда есть розетка",
            "средне — хватает на день",
            "важно — хочется полтора дня без подзарядки",
            "очень важно — телефон живёт в руках весь день",
            "критически важно — розетки рядом нет часами",
        ],
    )

    ekosistema = vopros(
        "Какая экосистема вам ближе?",
        [
            "Android — гибкость, свобода настройки",
            "iPhone — всё работает из коробки, связка с Mac/iPad",
        ],
    )

    kompakt = vopros(
        "Какой размер телефона предпочитаете?",
        [
            "компактный — чтобы удобно лежал в одной руке",
            "обычный или большой — для видео и игр",
        ],
    )

    rekomendovat(budzhet, kamera, igry, batareya, ekosistema, kompakt)


if __name__ == "__main__":
    main()
