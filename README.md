# i18n-properties-file-conversion-python
Python utility to convert .properties file to many other languages to support i18n

### Lib we are using is googletrans 4.0.0-rc1
Googletrans is a free and unlimited python library that implemented Google Translate API. This uses the Google Translate Ajax API to make calls to such methods as detect and translate.
Compatible with Python 3.6+.

### Other options - (translate 3.6.1)
Translate is a simple but powerful translation tool written in python with with support for multiple translation providers. By now we offer integration with Microsoft Translation API, Translated MyMemory API, LibreTranslate, and DeepL’s free and pro APIs


### How to execute
- Step 1: Install dependencies
```shell
pip install -r requirements.txt
```

- Step 2: Select paths for .properties file in `main.py`


### Sample
- Source (en -> auto-detectable)
```properties
hello=Hello!
welcome=Welcome to my app
welcome1=Welcome to my app
welcome2=Welcome to my app
welcome3=Name field
```

- Target (hi)
```properties
hello=नमस्कार!
welcome=मेरे ऐप में आपका स्वागत है
welcome1=मेरे ऐप में आपका स्वागत है
welcome2=मेरे ऐप में आपका स्वागत है
welcome3=नाम फ़ील्ड
```