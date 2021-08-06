from googletrans import Translator
import os.path


def convert(target_lang):
    translator = Translator()
    relative_path = os.path.abspath(os.path.dirname(__file__))
    fw = open(relative_path + '/files/translations/' + target_lang + '.properties', "w", encoding="utf-8")
    with open(relative_path + '/files/en.properties') as f:
        for line in f:
            splited = line.split('=')
            translated = translator.translate(splited[1], dest=target_lang)
            converted = splited[0] + "=" + translated.text
            print(converted)
            fw.write(converted + "\n")
    fw.close()


if __name__ == '__main__':
    convert('hi')
