from ensurepip import version
from gettext import translation
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey= os.environ['apikey']
url= os.environ['url']
version='2018-05-01'
authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    model_id= 'en-fr'
    translation= language_translator.translate(englishText, model_id=model_id).get_result()
    frenchText= json.dumps(translation, ensure_ascii=False)
    frenchText= json.loads(frenchText)["translations"][0]["translation"]
    return frenchText

def frenchToEnglish(frenchText):
    model_id= 'fr-en'
    translation= language_translator.translate(frenchText, model_id=model_id).get_result()
    englishText= json.dumps(translation, ensure_ascii=False)
    englishText= json.loads(englishText)["translations"][0]["translation"]
    return englishText

print(englishToFrench('welcome'))
print(frenchToEnglish('oui'))