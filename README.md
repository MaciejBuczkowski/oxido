# Zadanie Rekrutacyjne Oxido
 
## Funkcje

- Konwertuje tekst na strukturalny kod HTML z wykorzystaniem modelu językowego OpenAI.
- Wstawia znaczniki `<img>` z zastępczymi obrazkami i opisowymi atrybutami `alt`, gdzie to odpowiednie.
- Generuje HTML zawierający tylko zawartość do umieszczenia między znacznikami `<body>`, bez znaczników `<html>`, `<head>` ani `<body>`.
- Zapisuje wygenerowany HTML do pliku, umożliwiając łatwą weryfikację i użycie.

## Wymagania

- Python 3.8 lub nowszy
- Wymagane biblioteki (instalowane przez `pip`):
  - `openai`
  - `python-dotenv`

## Instalacja

1. Sklonuj to repozytorium:
   ```bash
   git clone https://github.com/MaciejBuczkowski/oxido.git
   cd oxido
   ```
2. Zainstaluj wymagane biblioteki
    ```
    pip install -r requirements.txt
    ```
3. Stwórz plik `.env` w głównym katalogu projektu i dodaj do niego swój klucz API OpenAI
    ```
    OPENAI_KEY=twoj_klucz_api_openai
    ```
4. Upewnij się, że w katalogu projektu znajduje się plik tekstowy o nazwie `Zadanie dla JJunior AI Developera - tresc artykulu.txt`, zawierający treść artykułu

## Użycie

1. Uruchom skrypt:
    ```
    python main.py
    ```
2. Skrypt wykona następujące kroki:

- Wczyta treść artykułu z pliku `Zadanie dla JJunior AI Developera - tresc artykulu.txt`.
- Wygeneruje sformatowaną treść HTML na podstawie artykułu i zdefiniowanego promptu.
- Zapisze wynikowy kod HTML w pliku o nazwie `artykul.html`.

3. Otwórz plik `artykul.html`, aby przejrzeć wygenerowaną zawartość.

