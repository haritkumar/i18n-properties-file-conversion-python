from translate import Translator


def convert(target_lang):
    translator = Translator(to_lang=target_lang)
    translation = translator.translate("This is a pen.")
    print(translation)


if __name__ == '__main__':
    convert('zh')
