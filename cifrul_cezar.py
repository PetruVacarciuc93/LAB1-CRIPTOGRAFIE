

# ---------------------------------------------------------------------------
# Alfabetul si codificarea literelor (Tabelul 1)
# ---------------------------------------------------------------------------
ALFABET_MAJ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALFABET_MIN = "abcdefghijklmnopqrstuvwxyz"
N = len(ALFABET_MAJ)  # 26


COD = {}
for _i in range(N):
    COD[ALFABET_MAJ[_i]] = _i
    COD[ALFABET_MIN[_i]] = _i  # literele mici au acelasi cod ca cele mari


# ---------------------------------------------------------------------------
# Functii ajutatoare: validare si normalizare
# ---------------------------------------------------------------------------
def in_majuscule(text):
    """Transforma literele mici in majuscule folosind alfabetul propriu."""
    rezultat = ""
    for c in text:
        rezultat += ALFABET_MAJ[COD[c]]
    return rezultat


def text_valid(text):
    """Textul poate contine doar litere A-Z, a-z (spatiile se vor elimina)."""
    for c in text:
        if c != " " and c not in COD:
            return False
    return True


def normalizeaza(text):
    """Elimina spatiile si transforma in majuscule."""
    fara_spatii = ""
    for c in text:
        if c != " ":
            fara_spatii += c
    return in_majuscule(fara_spatii)


def cheie_valida(k):
    """Cheia k trebuie sa fie intre 1 si 25 inclusiv."""
    return 1 <= k <= N - 1


def cuvant_cheie_valid(cuvant):
    """Cheia 2: doar litere latine, lungime >= 7."""
    if len(cuvant) < 7:
        return False
    for c in cuvant:
        if c not in COD:
            return False
    return True


# ---------------------------------------------------------------------------
# Construirea alfabetului permutat (cheia a doua)
# ---------------------------------------------------------------------------
def alfabet_permutat(cuvant_cheie):
    """
    Literele cuvantului-cheie (fara repetari) se plaseaza la inceput,
    apoi urmeaza restul literelor alfabetului in ordine naturala.
    """
    cuvant = in_majuscule(cuvant_cheie)
    rezultat = ""
    for c in cuvant:
        if c not in rezultat:
            rezultat += c
    for c in ALFABET_MAJ:
        if c not in rezultat:
            rezultat += c
    return rezultat


# ---------------------------------------------------------------------------
# Criptare / decriptare
# ---------------------------------------------------------------------------
def _pozitie(alfabet, litera):
    """Pozitia (codul) unei litere in alfabetul dat."""
    for i in range(N):
        if alfabet[i] == litera:
            return i
    return -1


def cripteaza(mesaj, k, alfabet=ALFABET_MAJ):
    """c = (x + k) mod n; 'alfabet' poate fi cel permutat (Sarcina 1.2)."""
    rezultat = ""
    for litera in mesaj:
        x = _pozitie(alfabet, litera)
        rezultat += alfabet[(x + k) % N]
    return rezultat


def decripteaza(criptograma, k, alfabet=ALFABET_MAJ):
    """m = (y - k) mod n; 'alfabet' poate fi cel permutat (Sarcina 1.2)."""
    rezultat = ""
    for litera in criptograma:
        y = _pozitie(alfabet, litera)
        rezultat += alfabet[(y - k) % N]
    return rezultat


# ---------------------------------------------------------------------------
# Interfata cu utilizatorul
# ---------------------------------------------------------------------------
def citeste_cheia_k():
    """Citeste cheia numerica pana cand este valida (1..25)."""
    while True:
        valoare = input("Introduceti cheia k (numar intreg intre 1 si 25): ").strip()
        try:
            k = int(valoare)
        except ValueError:
            print("  Eroare: cheia trebuie sa fie un numar intreg. "
                  "Diapazon corect: 1 - 25.")
            continue
        if cheie_valida(k):
            return k
        print("  Eroare: cheia este in afara limitelor. Diapazon corect: 1 - 25.")


def citeste_cuvant_cheie():
    """Citeste cheia a doua pana cand este valida (doar litere, min. 7)."""
    while True:
        cuvant = input("Introduceti cheia 2 (cuvant-cheie, doar litere latine, "
                       "minim 7 caractere): ").strip()
        if cuvant_cheie_valid(cuvant):
            return cuvant
        print("  Eroare: cheia 2 trebuie sa contina DOAR litere A-Z / a-z "
              "(fara spatii sau cifre) si sa aiba cel putin 7 caractere.")


def citeste_text(eticheta):
    """Citeste mesajul/criptograma pana cand contine doar litere (A-Z, a-z)."""
    while True:
        text = input("Introduceti " + eticheta + ": ")
        if not text_valid(text):
            print("  Eroare: sunt permise doar literele A-Z si a-z "
                  "(spatiile vor fi eliminate). Incercati din nou.")
            continue
        text = normalizeaza(text)
        if text == "":
            print("  Eroare: textul nu poate fi gol.")
            continue
        return text


def meniu():
    print("=" * 56)
    print("   CIFRUL LUI CEZAR - Lucrare de laborator nr. 1")
    print("=" * 56)
    while True:
        print("\nAlegeti versiunea algoritmului:")
        print("  1 - Cezar clasic (o cheie)            [Sarcina 1.1]")
        print("  2 - Cezar cu permutare (doua chei)    [Sarcina 1.2]")
        print("  0 - Iesire")
        versiune = input("Optiunea dumneavoastra: ").strip()
        if versiune == "0":
            print("La revedere!")
            break
        if versiune not in ("1", "2"):
            print("  Eroare: alegeti 1, 2 sau 0.")
            continue

        print("\nAlegeti operatia:")
        print("  1 - Criptare")
        print("  2 - Decriptare")
        operatie = input("Optiunea dumneavoastra: ").strip()
        if operatie not in ("1", "2"):
            print("  Eroare: alegeti 1 sau 2.")
            continue

        k = citeste_cheia_k()
        alfabet = ALFABET_MAJ
        if versiune == "2":
            cuvant = citeste_cuvant_cheie()
            alfabet = alfabet_permutat(cuvant)
            print("  Alfabetul permutat:", alfabet)

        if operatie == "1":
            mesaj = citeste_text("mesajul")
            print("  Mesajul normalizat :", mesaj)
            print("  CRIPTOGRAMA        :", cripteaza(mesaj, k, alfabet))
        else:
            cript = citeste_text("criptograma")
            print("  Criptograma        :", cript)
            print("  MESAJ DECRIPTAT    :", decripteaza(cript, k, alfabet))


if __name__ == "__main__":
    meniu()
