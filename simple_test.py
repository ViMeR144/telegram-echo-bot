import requests

def test_bot():
    token = '6158315214:AAHLZ71hGuVElic6snIagpZSRJ-XGvUtmKs'
    url = f'https://api.telegram.org/bot{token}/getMe'
    
    try:
        response = requests.get(url)
        print(f"Статус ответа: {response.status_code}")
        print(f"Ответ: {response.json()}")
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == '__main__':
    test_bot() 