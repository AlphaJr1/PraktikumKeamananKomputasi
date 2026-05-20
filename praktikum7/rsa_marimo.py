import marimo

__generated_with = "0.23.5"
app = marimo.App()


@app.cell(hide_code=True)
def _():
    import marimo as mo
    import math
    from Crypto.PublicKey import RSA
    from Crypto.Cipher import PKCS1_OAEP
    import binascii
    import pandas as pd

    return PKCS1_OAEP, RSA, binascii, mo, pd


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Eksperimen 1 & 2: RSA Manual
    Bagian ini mengimplementasikan algoritma RSA dari awal untuk melihat proses matematis dasar.
    - **Eksperimen 1** berfokus pada observasi pembentukan kunci dari parameter bilangan prima awal.
    - **Eksperimen 2** berfokus pada observasi proses transformasi teks menjadi array numerik selama operasi modular.
    """)
    return


@app.cell(hide_code=True)
def _():
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def multiplicative_inverse(e, phi):
        d = 0
        x1 = 0
        x2 = 1
        y1 = 1
        temp_phi = phi

        while e > 0:
            temp1 = temp_phi // e
            temp2 = temp_phi - temp1 * e
            temp_phi = e
            e = temp2

            x = x2 - temp1 * x1
            y = d - temp1 * y1

            x2 = x1
            x1 = x
            d = y1
            y1 = y

        if temp_phi == 1:
            return d + phi
        return None

    def generate_keypair(p, q):
        n = p * q
        phi = (p - 1) * (q - 1)

        e = 3
        g = gcd(e, phi)
        while g != 1 and e < phi:
            e += 2
            g = gcd(e, phi)

        d = multiplicative_inverse(e, phi)
        return ((e, n), (d, n))

    def encrypt_manual(pk, plaintext):
        key, n = pk
        cipher = [(ord(char) ** key) % n for char in plaintext]
        return cipher

    def decrypt_manual(pk, ciphertext):
        key, n = pk
        plain = [chr((char ** key) % n) for char in ciphertext]
        return ''.join(plain)

    return decrypt_manual, encrypt_manual, generate_keypair


@app.cell(hide_code=True)
def _(mo):
    # Parameter input untuk perhitungan manual
    p_input = mo.ui.number(value=61, label="Bilangan Prima p")
    q_input = mo.ui.number(value=53, label="Bilangan Prima q")
    pesan_input = mo.ui.text(value="HELLO", label="Pesan")

    mo.hstack([p_input, q_input, pesan_input])
    return p_input, pesan_input, q_input


@app.cell(hide_code=True)
def _(
    decrypt_manual,
    encrypt_manual,
    generate_keypair,
    mo,
    p_input,
    pd,
    pesan_input,
    q_input,
):
    p = int(p_input.value)
    q = int(q_input.value)
    pesan = pesan_input.value

    public_key, private_key = generate_keypair(p, q)
    pesan_enkripsi = encrypt_manual(public_key, pesan)
    pesan_dekripsi = decrypt_manual(private_key, pesan_enkripsi)

    n = p * q
    phi = (p - 1) * (q - 1)
    e = public_key[0]
    d = private_key[0]

    df_enc = pd.DataFrame({
        "Karakter": list(pesan),
        "ASCII (P)": [ord(c) for c in pesan],
        "Rumus": [f"{ord(c)}^{e} mod {n}" for c in pesan],
        "Ciphertext (C)": pesan_enkripsi,
    })

    df_dec = pd.DataFrame({
        "Ciphertext (C)": pesan_enkripsi,
        "Rumus": [f"{c}^{d} mod {n}" for c in pesan_enkripsi],
        "ASCII Hasil": [ord(c) for c in pesan],
        "Karakter Asli": list(pesan),
    })

    _ui = mo.vstack([
        mo.md(f"""
        ### Hasil Perhitungan Manual

        **Parameter Kunci:**
        - Bilangan Prima $p$: `{p}`
        - Bilangan Prima $q$: `{q}`
        - Modulus $n$: `{n}`
        - Public Key $(e, n)$: `{public_key}`
        - Private Key $(d, n)$: `{private_key}`

        ---

        **Data Proses Kriptografi:**
        - Pesan Awal: `{pesan}`
        - Ciphertext Numerik: `{pesan_enkripsi}`
        - Teks Dekripsi: `{pesan_dekripsi}`
        """),
        mo.accordion({
            "Detail Perhitungan Matematis": mo.vstack([
                mo.md(f"""
                **1. Pembentukan Kunci:**
                - Modulus $n = p \\times q = {p} \\times {q} = {n}$
                - Totient $\\phi(n) = (p-1)(q-1) = {p - 1} \\times {q - 1} = {phi}$
                - Public Exponent $e$ bernilai sedemikian sehingga $1 < e < \\phi(n)$ dan $gcd(e, \\phi(n)) = 1$. Didapatkan nilai $e = {e}$
                - Private Key $d$ sebagai invers multiplikatif dari $e \\pmod{{\\phi(n)}}$. Didapatkan nilai $d = {d}$
                """),
                mo.md("**2. Operasi Enkripsi (Per Karakter):**"),
                mo.ui.table(df_enc, selection=None),
                mo.md("**3. Operasi Dekripsi (Per Karakter):**"),
                mo.ui.table(df_dec, selection=None)
            ])
        })
    ])

    _ui
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Eksperimen 3: Implementasi Pustaka PyCryptodome
    Bagian ini memperlihatkan operasi algoritma RSA menggunakan pustaka standar industri dengan panjang kunci besar dan skema padding OAEP.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    # Parameter input pustaka
    ukuran_kunci_input = mo.ui.dropdown(
        options=["1024", "2048", "3072", "4096"], 
        value="2048", 
        label="Ukuran Kunci (bit)"
    )
    pesan_industri_input = mo.ui.text(
        value="Data Rahasia Klasifikasi A", 
        label="Pesan Rahasia"
    )

    mo.hstack([ukuran_kunci_input, pesan_industri_input])
    return pesan_industri_input, ukuran_kunci_input


@app.cell(hide_code=True)
def _(PKCS1_OAEP, RSA, binascii, mo, pesan_industri_input, ukuran_kunci_input):
    ukuran_kunci = int(ukuran_kunci_input.value)
    key = RSA.generate(ukuran_kunci)
    pesan_industri = pesan_industri_input.value.encode()

    cipher_rsa = PKCS1_OAEP.new(key.publickey())
    ciphertext_industri = cipher_rsa.encrypt(pesan_industri)

    decipher_rsa = PKCS1_OAEP.new(key)
    decrypted_industri = decipher_rsa.decrypt(ciphertext_industri)

    _ui2 = mo.vstack([
        mo.md(f"""
        ### Hasil Implementasi PyCryptodome

        **Konfigurasi Parameter:**
        - Panjang Kunci Bit: `{ukuran_kunci}`
        - Mode Padding: `PKCS#1 OAEP`

        ---

        **Data Proses Kriptografi:**
        - Plaintext Teks: `{pesan_industri_input.value}`
        - Ciphertext Format Hex (Awal 64 Karakter): `{binascii.hexlify(ciphertext_industri)[:64].decode()}...`
        - Panjang Bytes Ciphertext: `{len(ciphertext_industri)}`
        - Dekripsi Teks: `{decrypted_industri.decode()}`
        """),
        mo.accordion({
            "Mekanisme Skema OAEP": mo.md(f"""
            Perbedaan utama penggunaan mode OAEP dibandingkan algoritma dasar matematis:

            **1. Injeksi Padding (OAEP):**
            Data `{pesan_industri_input.value}` tidak mengalami proses operasi eksponensial secara langsung. Sistem menyisipkan elemen acak (padding) sehingga duplikasi proses enkripsi pada data yang identik akan memberikan hasil *ciphertext* yang unik.

            **2. Komputasi Bilangan Skala Besar:**
            Komputasi dieksekusi pada bilangan yang setara dengan rentang `{ukuran_kunci}` bit, mencegah kerentanan terhadap serangan *brute-force* konvensional.

            **3. Ekstraksi Padding:**
            Proses *unpadding* secara otomatis dijalankan setelah kalkulasi *decryption* selesai untuk memisahkan antara elemen data asli dengan elemen acak.
            """)
        })
    ])

    _ui2
    return


if __name__ == "__main__":
    app.run()
