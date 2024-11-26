# API Prognozy Cen Laptopów

Ten projekt udostępnia API oparte na modelu uczenia maszynowego do przewidywania cen laptopów na podstawie specyfikacji technicznych. API zostało stworzone w oparciu o Flask i wykorzystuje wytrenowany model PyCaret. Umożliwia ono wysyłanie danych wejściowych i otrzymywanie prognoz cenowych.

## Funkcjonalności

- **API Flask**: Obsługuje dane wejściowe i zwraca prognozy.
- **Integracja z modelem PyCaret**: Wykorzystuje pipeline do przetwarzania danych i prognozowania.
- **Docker**: Ułatwione wdrażanie i zarządzanie środowiskiem.
- **Skrypt testowy**: Zawiera skrypt do testowania działania API.

## Pliki projektu

- **`server.py`**: Główna aplikacja Flask obsługująca zapytania do API.
- **`test.py`**: Skrypt testowy wysyłający dane wejściowe do API i wypisujący wyniki.
- **`model.pkl`**: Wytrenowany model PyCaret, wykorzystywany do prognoz.
- **`requirements.txt`**: Lista zależności Python potrzebnych do uruchomienia aplikacji.
- **`Dockerfile`**: Plik Docker automatyzujący budowę obrazu kontenera dla aplikacji.

## Jak uruchomić projekt?

### 1. Klonowanie repozytorium
Skopiuj projekt na swój lokalny komputer:
```bash
git clone <URL_DO_REPOZYTORIUM>
cd <NAZWA_FOLDERU_PROJEKTU>
```

# Laptop Price Prediction API

## Uruchomienie projektu

### 1. Uruchomienie lokalne (Python)

1. Utwórz wirtualne środowisko:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
   
2.Zainstaluj zależności:
```bash
 pip install -r requirements.txt

   ```

3.Uruchom serwer Flask:
```bash
 python server.py
   ```

Domyślnie API działa pod adresem <http://127.0.0.1:5000>.

### 2\. Uruchomienie za pomocą Dockera

1. Zbuduj obraz Dockera:
```bash
 docker build -t laptop-price-prediction .

   ```
2. Uruchom kontener:
```bash
 docker run -p 5000:5000 laptop-price-prediction

   ```
API będzie dostępne pod adresem <http://127.0.0.1:5000>.

### 3\. Testowanie API

Uruchom skrypt testowy:
```bash
 python test.py

   ```
Skrypt wysyła przykładowe dane do API i wypisuje prognozowaną cenę laptopa.

Struktura danych wejściowych
----------------------------

Dane wejściowe do API powinny być w formacie JSON i zawierać następujące pola:
```bash
 {
  "RAM": 16,
  "Storage": 512,
  "Screen": 15.6,
  "Brand": "Dell",
  "CPU": "Intel Core i7",
  "GPU": "NVIDIA GTX 1650",
  "Storage type": "SSD",
  "Status": "New",
  "Model": "XPS 15"
}

   ```
Przykładowa odpowiedź API
```bash
 {
  "predictions": [750.5]
}

   ```
Problemy i rozwiązania
----------------------

1.  **Błąd:** `ModuleNotFoundError: No module named 'catboost'`\
    **Rozwiązanie:**\
    Upewnij się, że `catboost` jest zainstalowany:
```bash
 pip install catboost

   ```

2.   **Błąd:** `HTTPConnectionPool(host='127.0.0.1', port=5000)`\
    **Rozwiązanie:**\
    Upewnij się, że serwer Flask działa pod adresem `127.0.0.1:5000`.

3.  **Błąd:** `"None of [Index([...])] are in the [columns]"`\
    **Rozwiązanie:**\
    Sprawdź, czy dane wejściowe zawierają wszystkie wymagane pola.
