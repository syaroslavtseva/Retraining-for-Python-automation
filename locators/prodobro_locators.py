class ProDobroLocators:
    FUNDS_LINK = "Фонды"
    SEARCH_INPUT = "css=.relative.w-full input"
    KLYUCH_DOBRA_TEXT = "Ключ добра"
    FUND_SITE_LINK = "Сайт фонда"
    
    ANIMALS_BUTTON_SCRIPT = '''() => {
        const button = document.evaluate(
            '//button[text()="Животные"]',
            document,
            null,
            XPathResult.FIRST_ORDERED_NODE_TYPE,
            null
        ).singleNodeValue;
        button?.click();
    }'''