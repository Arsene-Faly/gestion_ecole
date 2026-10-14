
import requests

URL = "http://127.0.0.1:5000/auth/register"

users = [
    {
        "email": f"user{i:02d}@gmail.com",
        "password": "User1234",
        "confirm_password": "User1234"
    }
    for i in range(1, 11)
]

session = requests.Session()

for user in users:
    email = user["email"]

    try:
        response = session.post(
            URL,
            data=user,
            allow_redirects=False,
            timeout=10
        )

        # Vérifier si le serveur a répondu
        if response.status_code in (301, 302, 303, 307, 308):
            print(f"[À VÉRIFIER] {email} - Redirection vers "
                  f"{response.headers.get('Location')}")

        elif response.status_code == 200:
            print(f"[À VÉRIFIER] {email} - Page reçue, "
                  "création non confirmée")

        else:
            print(f"[ÉCHEC] {email} - Code HTTP "
                  f"{response.status_code}")

    except requests.exceptions.ConnectionError:
        print(f"[ACCÈS REFUSÉ] {email} - Serveur inaccessible")

    except requests.exceptions.Timeout:
        print(f"[DÉLAI DÉPASSÉ] {email} - Serveur trop lent")

    except requests.exceptions.RequestException as erreur:
        print(f"[ERREUR] {email} - {erreur}")
