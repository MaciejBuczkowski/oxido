import os
from dotenv import load_dotenv
from openai import OpenAI

#ładowanie kluczu api
load_dotenv()

OPENAI_KEY = os.getenv('OPENAI_KEY')
client = OpenAI(api_key = OPENAI_KEY)

#ładowanie tekst artykułu
with open('Zadanie dla JJunior AI Developera - tresc artykulu.txt','r') as f:
    artykul = f.read()
    
f.close()
    
#tworzenie promptu
prompt = f'''Napisz kod HTML artykułu zgodny z poniższymi wytycznymi:
- Nie zmieniać treści tekstu
- Nie umieszczaj znaczników ```html ani ``` w odpowiedzi. Zwróć sam kod HTML bez dodatkowych formatowań.
- Użyj odpowiednich tagów HTML do strukturyzacji treści, takich jak nagłówki, akapity, listy, itd.
- W miejscach, gdzie warto wstawić grafiki, użyj tagu <img> z atrybutem src="image_placeholder.jpg". Do każdego obrazka dodaj atrybut alt z dokładnym opisem promptu do wygenerowania grafiki.
- Pod każdą grafiką dodaj podpis, używając odpowiedniego tagu HTML (np. <figcaption>).
Kod ma zawierać wyłącznie zawartość przeznaczoną do wstawienia pomiędzy tagami <body> i </body>. Nie dodawaj znaczników <html>, <head>, ani <body>.
Nie używaj CSS ani JavaScript. Skup się wyłącznie na czystym HTML.
Treść artykułu: {artykul}.'''

response = client.chat.completions.create(
    model='gpt-4o',
    messages= [
        {'role':'user','content': prompt}                                    
    ])


#zapisywanie odpowiedzi
with open('artykul.html','w') as res:
    res.write(response.choices[0].message.content)

res.close()