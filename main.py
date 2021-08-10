from googletrans import Translator
import os.path


def convert(target_lang):
    translator = Translator()
    relative_path = os.path.abspath(os.path.dirname(__file__))
    fw = open(relative_path + '/files/translations/' + target_lang + '.properties', "w", encoding="utf-8")
    with open(relative_path + '/files/en.properties') as f:
        i = 1
        for line in f:
            splited = line.split('=')
            translated_text = ''
            if len(splited) == 2:
                try:
                    translated = translator.translate(splited[1], dest=target_lang)
                    translated_text = splited[0] + "=" + translated.text
                except IndexError as ie:
                    translated_text = splited[0] + "="

            print(str(i) + '> ' + translated_text)
            fw.write(translated_text + "\n")
            i = i + 1
    fw.close()


if __name__ == '__main__':
    convert('hi')
