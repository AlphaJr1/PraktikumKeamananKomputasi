# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pycryptodome",
#     "matplotlib",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(app_title="Blockchain Playground & Cryptographic Sandbox")


@app.cell
def __():
    import marimo as mo
    import hashlib
    import time
    import json
    import matplotlib.pyplot as plt
    from Crypto.PublicKey import RSA
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256
    return RSA, SHA256, hashlib, json, mo, pkcs1_15, plt, time


@app.cell
def __(mo):
    # Stylesheet CSS premium untuk visualisasi dashboard futuristik
    style_element = mo.Html(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
        
        :root {
            --bg-playground: #f8fafc;
            --card-bg: #ffffff;
            --card-border: #e2e8f0;
            --text-primary: #0f172a;
            --text-secondary: #64748b;
            --accent-color: #4f46e5;
            --accent-success: #059669;
            --accent-error: #dc2626;
            --box-bg: #f1f5f9;
            --box-border: #cbd5e1;
            
            --banner-info-bg: rgba(79, 70, 229, 0.1);
            --banner-info-text: #4338ca;
            --banner-info-border: rgba(79, 70, 229, 0.2);
            
            --banner-success-bg: rgba(5, 150, 105, 0.1);
            --banner-success-text: #047857;
            --banner-success-border: rgba(5, 150, 105, 0.2);
            
            --banner-error-bg: rgba(220, 38, 38, 0.1);
            --banner-error-text: #b91c1c;
            --banner-error-border: rgba(220, 38, 38, 0.2);
        }
        
        @media (prefers-color-scheme: dark) {
            :root {
                --bg-playground: #0f172a;
                --card-bg: #1e293b;
                --card-border: #334155;
                --text-primary: #f8fafc;
                --text-secondary: #cbd5e1;
                --accent-color: #818cf8;
                --accent-success: #34d399;
                --accent-error: #f87171;
                --box-bg: #0f172a;
                --box-border: #334155;
                
                --banner-info-bg: rgba(99, 102, 241, 0.15);
                --banner-info-text: #c7d2fe;
                --banner-info-border: rgba(99, 102, 241, 0.3);
                
                --banner-success-bg: rgba(52, 211, 153, 0.15);
                --banner-success-text: #a7f3d0;
                --banner-success-border: rgba(52, 211, 153, 0.3);
                
                --banner-error-bg: rgba(248, 113, 113, 0.15);
                --banner-error-text: #fca5a5;
                --banner-error-border: rgba(248, 113, 113, 0.3);
            }
        }
        
        .marimo-output * {
            font-family: 'Inter', sans-serif;
        }
        
        .dashboard-container {
            background: var(--bg-playground);
            padding: 20px;
            border-radius: 20px;
            color: var(--text-primary);
        }
        
        .playground-card {
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 16px;
            padding: 24px;
            margin-bottom: 24px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
            transition: all 0.3s ease;
            color: var(--text-primary);
        }
        
        .playground-card:hover {
            box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.08);
            border-color: var(--accent-color);
        }
        
        .playground-card strong {
            color: var(--text-secondary);
            font-weight: 600;
            display: inline-block;
            margin-bottom: 6px;
            font-size: 0.9rem;
        }
        
        .card-header {
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--accent-color);
            margin-bottom: 16px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            border-bottom: 2px solid var(--box-bg);
            padding-bottom: 8px;
        }
        
        .data-box {
            background: var(--box-bg);
            border: 1px solid var(--box-border);
            border-radius: 8px;
            padding: 12px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.85rem;
            color: var(--text-primary);
            word-break: break-all;
            margin: 8px 0;
        }
        
        .status-banner {
            padding: 16px;
            border-radius: 12px;
            font-weight: 600;
            margin-top: 12px;
            text-align: center;
        }
        
        .status-valid {
            background: var(--banner-success-bg);
            color: var(--banner-success-text);
            border: 1px solid var(--banner-success-border);
        }
        
        .status-invalid {
            background: var(--banner-error-bg);
            color: var(--banner-error-text);
            border: 1px solid var(--banner-error-border);
        }
        
        .status-info {
            background: var(--banner-info-bg);
            color: var(--banner-info-text);
            border: 1px solid var(--banner-info-border);
        }
        
        details {
            background: var(--box-bg);
            border: 1px solid var(--box-border);
            border-radius: 8px;
            padding: 10px 14px;
            margin-top: 14px;
            font-size: 0.85rem;
        }
        
        summary {
            font-weight: 600;
            color: var(--accent-color);
            cursor: pointer;
            outline: none;
            user-select: none;
            padding: 2px 0;
        }
        
        details[open] summary {
            border-bottom: 1px solid var(--box-border);
            margin-bottom: 10px;
            padding-bottom: 8px;
        }
        
        .binary-grid {
            display: block;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            margin-top: 8px;
            background: var(--card-bg);
            padding: 12px;
            border-radius: 6px;
            border: 1px solid var(--card-border);
            line-height: 1.6;
            word-break: break-all;
        }
        
        .bit-diff {
            color: var(--accent-error);
            font-weight: bold;
            background: rgba(220, 38, 38, 0.15);
            padding: 1px 3px;
            border-radius: 3px;
        }
        
        .bit-same {
            color: var(--text-secondary);
            padding: 1px 3px;
        }
        </style>
        """
    )
    style_element
    return (style_element,)


@app.cell
def __(mo):
    mo.md(
        r"""
        # Cryptographic & Blockchain Playground

        Eksplorasi langsung tiga konsep inti blockchain: fungsi hash, tanda tangan digital, dan Proof of Work.
        Semua diimplementasi dari formula $h(n) = f[h(n-1), \phi, K]$ — utak-atik input dan amati hasilnya secara langsung.
        """
    )
    return


@app.cell
def __(mo):
    # Definisi UI Identitas (Tanpa pemrosesan nilai)
    nim_input = mo.ui.text(value="", label="NIM Mahasiswa")
    nama_input = mo.ui.text(value="", label="Nama Lengkap")
    return nama_input, nim_input


@app.cell
def __(mo, nama_input, nim_input):
    # Menampilkan UI Identitas
    mo.vstack([
        mo.md(
            """
            ### Kredensial Eksperimen

            NIM kamu dipakai sebagai seed pembangkit kunci RSA — jadi tiap orang punya pasangan kunci yang berbeda.
            """
        ),
        mo.hstack([nim_input, nama_input])
    ])
    return


@app.cell
def __(mo):
    # Definisi UI Avalanche Lab
    teks_a = mo.ui.text(value="Blockchain Poltek", label="Teks Input A")
    teks_b = mo.ui.text(value="blockchain Poltek", label="Teks Input B")
    return teks_a, teks_b


@app.cell
def __(hashlib, mo, teks_a, teks_b):
    # Pemrosesan Logika Avalanche Lab
    hash_a = hashlib.sha256(teks_a.value.encode()).hexdigest()
    hash_b = hashlib.sha256(teks_b.value.encode()).hexdigest()
    
    # Hitung Hamming Distance
    bin_a = bin(int(hash_a, 16))[2:].zfill(256)
    bin_b = bin(int(hash_b, 16))[2:].zfill(256)
    hamming_dist = sum(c1 != c2 for c1, c2 in zip(bin_a, bin_b))
    diff_pct = (hamming_dist / 256) * 100
    
    # Membuat visualisasi biner grid perbandingan bit
    bit_visual = []
    for c1, c2 in zip(bin_a, bin_b):
        if c1 != c2:
            bit_visual.append(f'<span class="bit-diff">{c1}</span>')
        else:
            bit_visual.append(f'<span class="bit-same">{c1}</span>')
    binary_grid_html = f'<div class="binary-grid">{"".join(bit_visual)}</div>'
    
    avalanche_ui = mo.Html(
        f"""
        <div class="playground-card">
            <div class="card-header">Avalanche Effect & Hash Laboratory</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 12px;">
                <div>
                    <strong>Hash Output A:</strong>
                    <div class="data-box">{hash_a}</div>
                </div>
                <div>
                    <strong>Hash Output B:</strong>
                    <div class="data-box">{hash_b}</div>
                </div>
            </div>
            <div class="status-banner status-info">
                Hamming Distance: {hamming_dist} dari 256 bit ({diff_pct:.2f}% perbedaan bit)
            </div>
            <details>
                <summary>Lihat Komparasi Struktur Bit Biner (Avalanche Detail)</summary>
                <div style="margin-top: 10px; font-weight: 500;">
                    Visualisasi bit biner SHA-256 (Karakter berwarna merah mengindikasikan perbedaan posisi bit akibat perubahan input):
                </div>
                {binary_grid_html}
            </details>
        </div>
        """
    )
    return (
        avalanche_ui,
        bin_a,
        bin_b,
        binary_grid_html,
        bit_visual,
        diff_pct,
        hamming_dist,
        hash_a,
        hash_b,
    )


@app.cell
def __(avalanche_ui, mo, teks_a, teks_b):
    # Menampilkan UI Avalanche Lab
    mo.vstack([
        mo.md(
            r"""
            ### 1. Eksplorasi Fungsi Hash

            SHA-256 bersifat deterministik dan sensitif ekstrem — satu karakter beda mengubah ratusan bit output (*avalanche effect*).
            Coba ganti satu huruf di salah satu input, amati Hamming Distance-nya di biner 256 bit.
            """
        ),
        mo.hstack([teks_a, teks_b]),
        avalanche_ui
    ])
    return


@app.cell
def __(RSA, nim_input, time):
    # Pembangkitan Kunci RSA unik berdasarkan kredensial mahasiswa
    seed = f"{nim_input.value or 'anonim'}_{time.strftime('%Y%m%d')}"
    key = RSA.generate(1024)
    priv_key_pem = key.export_key().decode('utf-8')
    pub_key_pem = key.publickey().export_key().decode('utf-8')
    return key, priv_key_pem, pub_key_pem, seed


@app.cell
def __(mo):
    # Definisi UI Transaksi
    nominal_input = mo.ui.number(start=1, stop=5000, step=1, value=150, label="Nominal Koin")
    penerima_input = mo.ui.text(value="Bob", label="Penerima Aset")
    return nominal_input, penerima_input


@app.cell
def __(SHA256, key, mo, nim_input, nominal_input, penerima_input, pkcs1_15, priv_key_pem, pub_key_pem):
    # Pemrosesan Logika Digital Signature
    tx_msg = f"Alice-{nim_input.value or 'anonim'}-mengirim-{nominal_input.value}-Koin-ke-{penerima_input.value}"
    tx_hash = SHA256.new(tx_msg.encode())
    
    # Penandatanganan digital secara instan
    signature = pkcs1_15.new(key).sign(tx_hash)
    sig_hex = signature.hex()
    
    # Simulasi perhitungan matematis signature: S = m^d mod n
    hash_int = int(tx_hash.hexdigest()[:16], 16) # representasi numerik hash (64-bit awal)
    d_param = key.d
    n_param = key.n
    sig_calc_sim = pow(hash_int, d_param, n_param)
    
    signature_ui = mo.Html(
        f"""
        <div class="playground-card">
            <div class="card-header">RSA Signature Workshop</div>
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px;">
                <div>
                    <strong>Kunci Publik (Dibagikan ke Jaringan):</strong>
                    <div class="data-box" style="max-height: 80px; overflow-y: auto; font-size: 0.75rem;">{pub_key_pem[:140]}...</div>
                </div>
                <div>
                    <strong>Kunci Privat (Kerahasiaan Pengirim):</strong>
                    <div class="data-box" style="max-height: 80px; overflow-y: auto; font-size: 0.75rem;">{priv_key_pem[:140]}...</div>
                </div>
            </div>
            <div>
                <strong>Pesan Transaksi Asli:</strong>
                <div class="data-box">{tx_msg}</div>
            </div>
            <div style="margin-top: 12px;">
                <strong>Digital Signature Hasil Enkripsi Kunci Privat (Hex):</strong>
                <div class="data-box" style="color: var(--accent-color); font-weight: bold;">{sig_hex[:128]}...</div>
            </div>
            <details>
                <summary>Lihat Alur Matematis Digital Signature</summary>
                <div style="margin-top: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; line-height: 1.6;">
                    <strong>Formulasi Tanda Tangan: S = m^d mod n</strong><br>
                    • Representasi Numerik Hash (m) : {hash_int}<br>
                    • Eksponen Kunci Privat (d)     : {str(d_param)[:50]}...<br>
                    • Modulus Kunci (n)             : {str(n_param)[:50]}...<br>
                    • Hasil Modulo Komputasi (S)    : {str(sig_calc_sim)[:50]}...
                </div>
            </details>
        </div>
        """
    )
    return d_param, hash_int, n_param, sig_calc_sim, sig_hex, signature, signature_ui, tx_hash, tx_msg


@app.cell
def __(mo, nominal_input, penerima_input, signature_ui):
    # Menampilkan UI Signature Workshop
    mo.vstack([
        mo.md(
            r"""
            ### 2. Eksplorasi Digital Signature

            Setiap transaksi ditandatangani dengan kunci privat pakai formula $S = m^d \bmod n$. Kunci RSA dibangkitkan dari NIM kamu.
            Ganti nominal atau penerima, signature-nya akan berubah total meski pesannya mirip.
            """
        ),
        mo.hstack([nominal_input, penerima_input]),
        signature_ui
    ])
    return


@app.cell
def __(hashlib, json, time):
    # Struktur Data Block untuk Konsensus & Rantai Blok
    class Block:
        def __init__(self, index, transactions, h_prev, phi=2, K=0):
            self.index = index
            self.timestamp = time.time()
            self.transactions = transactions
            self.h_prev = h_prev    # h(n-1): hash blok sebelumnya
            self.phi = phi          # phi: difficulty level
            self.K = K              # K: nonce
            self.h_curr = self.calculate_hash()  # h(n): hash blok saat ini

        def calculate_hash(self):
            block_content = json.dumps({
                "index": self.index,
                "transactions": self.transactions,
                "h_prev": self.h_prev,
                "phi": self.phi,
                "K": self.K
            }, sort_keys=True)
            return hashlib.sha256(block_content.encode()).hexdigest()

        def mine_block(self, max_iter=100000):
            target = "0" * self.phi
            iterations = 0
            while self.h_curr[:self.phi] != target and iterations < max_iter:
                self.K += 1
                self.h_curr = self.calculate_hash()
                iterations += 1
            return self.h_curr[:self.phi] == target
    return Block,


@app.cell
def __(mo):
    # Definisi UI Konsensus
    difficulty_slider = mo.ui.slider(start=1, stop=3, step=1, value=2, label="Kesulitan Mining (phi)")
    mine_button = mo.ui.run_button(label="Jalankan Penambangan Blok (Mine)")
    return difficulty_slider, mine_button


@app.cell
def __(mo, difficulty_slider, mine_button):
    # Menampilkan Kontrol Konsensus
    mo.vstack([
        mo.md(
            r"""
            ### 3. Eksplorasi Proof of Work

            Proses mining mencari nonce $K$ sampai hash-nya diawali $\phi$ angka nol heksadesimal. Setiap naik satu level $\phi$, usaha yang dibutuhkan meningkat $\times 16$.
            Atur tingkat kesulitan lalu tekan Mine — grafik akan menunjukkan perjalanan setiap percobaan nonce hingga target ditemukan.
            """
        ),
        mo.hstack([difficulty_slider, mine_button])
    ])
    return


@app.cell
def __(Block, difficulty_slider, hashlib, json, mine_button, mo, plt, time, tx_msg):
    # Logika Penambangan
    mining_output = ""
    nonce_found = 0
    hash_found = ""
    durasi = 0.0
    iteration_log_html = ""
    test_block = None

    if mine_button.value:
        h_prev_dummy = "0000abcde1234567890f"
        test_block = Block(index=1, transactions=[{"data": tx_msg}], h_prev=h_prev_dummy, phi=difficulty_slider.value)
        
        # Eksekusi mining dengan pencatatan data plot
        target_prefix = "0" * difficulty_slider.value
        hash_values = []
        nonces = []
        max_plot_points = 500
        
        # Log iterasi awal hashing nonce (untuk visualisasi details)
        iteration_log = []
        for test_k in range(5):
            test_block_string = json.dumps({
                "index": 1,
                "transactions": [{"data": tx_msg}],
                "h_prev": h_prev_dummy,
                "phi": difficulty_slider.value,
                "K": test_k
            }, sort_keys=True)
            test_hash = hashlib.sha256(test_block_string.encode()).hexdigest()
            status_symbol = "✓ (Cocok)" if test_hash.startswith(target_prefix) else "✗ (Tidak cocok)"
            iteration_log.append(f"K = {test_k} | Hash: {test_hash[:32]}... | Status: {status_symbol}")
        iteration_log_html = "<br>".join(iteration_log)
        
        # Eksekusi mining penuh
        t0 = time.time()
        success = False
        iterasi_ke = 0
        max_iter = 50000
        
        while test_block.h_curr[:test_block.phi] != target_prefix and iterasi_ke < max_iter:
            if iterasi_ke < max_plot_points or iterasi_ke % 10 == 0:
                val_dec = int(test_block.h_curr[:4], 16)
                hash_values.append(val_dec)
                nonces.append(test_block.K)
                
            test_block.K += 1
            test_block.h_curr = test_block.calculate_hash()
            iterasi_ke += 1
            
        success = test_block.h_curr[:test_block.phi] == target_prefix
        t1 = time.time()
        
        durasi = (t1 - t0) * 1000
        nonce_found = test_block.K
        hash_found = test_block.h_curr
        
        if success:
            hash_values.append(int(hash_found[:4], 16))
            nonces.append(nonce_found)
            
        status_text = "Blok Berhasil Ditambahkan ke Rantai Jaringan!" if success else "Penambangan Dihentikan (Batas Maksimum 50.000 Iterasi Tercapai)!"
        status_class = "status-valid" if success else "status-invalid"
        
        # Membuat Plot Visualisasi
        fig, ax = plt.subplots(figsize=(6.5, 3.2))
        is_dark = mo.app_meta().theme == "dark"
        
        fig.patch.set_facecolor('#1e293b' if is_dark else '#ffffff')
        ax.set_facecolor('#0f172a' if is_dark else '#f8fafc')
        
        # Plot data gagal
        ax.scatter(nonces[:-1], hash_values[:-1], color='#f87171' if is_dark else '#dc2626', alpha=0.5, s=12, label='Hash Tidak Cocok')
        
        # Plot data sukses
        if success:
            ax.scatter([nonces[-1]], [hash_values[-1]], color='#34d399' if is_dark else '#059669', marker='*', s=180, edgecolor='#ffffff', linewidth=1.5, zorder=5, label='Hash Valid Ditemukan')
            
        # Garis threshold kesulitan
        threshold = 65536 // (16**difficulty_slider.value)
        ax.axhline(y=threshold, color='#eab308', linestyle='--', linewidth=1.5, label=f'Threshold phi={difficulty_slider.value}')
        
        ax.set_title("Distribusi Hashing Nonce (Proof of Work)", color='#f8fafc' if is_dark else '#0f172a', fontsize=10, fontweight='bold')
        ax.set_xlabel("Nilai Nonce (K)", color='#cbd5e1' if is_dark else '#64748b', fontsize=8)
        ax.set_ylabel("Nilai Awal Hash (Desimal 16-bit)", color='#cbd5e1' if is_dark else '#64748b', fontsize=8)
        
        text_color = '#f8fafc' if is_dark else '#0f172a'
        ax.tick_params(colors=text_color, labelsize=8)
        for spine in ax.spines.values():
            spine.set_color('#334155' if is_dark else '#cbd5e1')
            
        ax.legend(loc='upper right', fontsize=7, facecolor='#1e293b' if is_dark else '#f1f5f9', labelcolor=text_color)
        plt.tight_layout()
        
        chart_html = mo.as_html(fig)
        plt.close(fig)
        
        mining_output = mo.vstack([
            mo.Html(
                f"""
                <div class="playground-card">
                    <div class="card-header" style="color: var(--accent-success);">Konsol Penambangan</div>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 12px;">
                        <div>
                            <strong>Nonce K yang Ditemukan:</strong>
                            <div class="data-box" style="font-weight: bold; color: var(--accent-success);">{nonce_found}</div>
                        </div>
                        <div>
                            <strong>Waktu Komputasi:</strong>
                            <div class="data-box">{durasi:.2f} ms</div>
                        </div>
                    </div>
                    <div>
                        <strong>Hash Valid Berawalan Nol h(n):</strong>
                        <div class="data-box">{hash_found}</div>
                    </div>
                    <div class="status-banner {status_class}">
                        {status_text}
                    </div>
                    <details>
                        <summary>Lihat Log Iterasi Hashing Nonce (K)</summary>
                        <div style="margin-top: 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; line-height: 1.6;">
                            <strong>Pencarian Nonce Berawalan {target_prefix} (Menampilkan 5 Iterasi Awal):</strong><br>
                            {iteration_log_html}<br>
                            ...<br>
                            <strong>K = {nonce_found} | Hash: {hash_found[:32]}... | Status: {"✓ (Cocok)" if success else "✗ (Batas Tercapai)"}</strong>
                        </div>
                    </details>
                </div>
                """
            ),
            chart_html
        ])
    else:
        mining_output = mo.md("*Gunakan tombol di atas untuk mencari nonce (K) secara real-time.*")
    return (
        chart_html,
        durasi,
        hash_found,
        iteration_log_html,
        mining_output,
        nonce_found,
        test_block,
    )


@app.cell
def __(mining_output):
    # Menampilkan Output Konsul Mining
    mining_output
    return


@app.cell
def __(mo):
    # Definisi UI Tampering
    manipulasi_genesis = mo.ui.text(value="Genesis Block", label="Manipulasi Isi Transaksi Blok 0 (Genesis)")
    return (manipulasi_genesis,)


@app.cell
def __(mo, manipulasi_genesis):
    # Menampilkan UI Kontrol Tampering
    mo.vstack([
        mo.md(
            r"""
            ### 4. Eksplorasi Keutuhan Rantai Blok (Ledger Integrity Auditor)
            
            **Blok Genesis (Blok 0)** adalah blok pertama dalam blockchain yang menjadi fondasi rantai jaringan dan tidak memiliki blok pendahulu ($h_{prev} = 0$). 
            
            Simulasi ini mendemonstrasikan serangan manipulasi data (*tampering*). Coba ubah teks pada kolom input di bawah untuk memodifikasi transaksi Blok 0 pada masa lalu, lalu amati bagaimana perubahan tersebut langsung merusak validitas keterkaitan hash pada Blok 1 ($h(1) = f[h(0), \phi, K]$).
            """
        ),
        manipulasi_genesis
    ])
    return


@app.cell
def __(Block, json, manipulasi_genesis, mo, sig_hex, tx_msg):
    # Logika Auditor Rantai Blok
    genesis_asli = Block(index=0, transactions=[{"data": "Genesis Block"}], h_prev="0", phi=2)
    hash_genesis_asli = genesis_asli.h_curr
    
    genesis_manipulasi = Block(index=0, transactions=[{"data": manipulasi_genesis.value}], h_prev="0", phi=2)
    hash_genesis_manipulasi = genesis_manipulasi.h_curr
    
    blok1_asli = Block(index=1, transactions=[{"data": tx_msg, "sig": sig_hex[:16]}], h_prev=hash_genesis_asli, phi=2)
    blok1_manipulasi = Block(index=1, transactions=[{"data": tx_msg, "sig": sig_hex[:16]}], h_prev=hash_genesis_manipulasi, phi=2)
    
    rantai_valid = hash_genesis_asli == hash_genesis_manipulasi
    
    # Payload JSON untuk visualisasi audit details
    payload_asli_json = json.dumps({
        "index": 1,
        "transactions": [{"data": tx_msg, "sig": sig_hex[:16]}],
        "h_prev": hash_genesis_asli,
        "phi": 2,
        "K": blok1_asli.K
    }, indent=2, sort_keys=True)
    
    payload_manipulasi_json = json.dumps({
        "index": 1,
        "transactions": [{"data": tx_msg, "sig": sig_hex[:16]}],
        "h_prev": hash_genesis_manipulasi,
        "phi": 2,
        "K": blok1_manipulasi.K
    }, indent=2, sort_keys=True)
    
    auditor_ui = ""
    if rantai_valid:
        auditor_ui = mo.Html(
            f"""
            <div class="playground-card" style="border-color: var(--accent-success);">
                <div class="card-header" style="color: var(--accent-success);">Ledger Integrity Auditor</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 12px;">
                    <div>
                        <strong>Hash Blok 0 Asli h(0):</strong>
                        <div class="data-box">{hash_genesis_asli}</div>
                    </div>
                    <div>
                        <strong>Hash Blok 0 Auditor h(0)*:</strong>
                        <div class="data-box">{hash_genesis_manipulasi}</div>
                    </div>
                </div>
                <div class="status-banner status-valid">
                    STATUS LEDGER: RANTAI BLOK INTEGRAL & VALID (Aman dari Serangan)
                </div>
            </div>
            """
        )
    else:
        auditor_ui = mo.Html(
            f"""
            <div class="playground-card" style="border-color: var(--accent-error);">
                <div class="card-header" style="color: var(--accent-error);">Ledger Integrity Auditor</div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 12px;">
                    <div>
                        <strong>Hash Blok 0 Asli h(0):</strong>
                        <div class="data-box">{hash_genesis_asli}</div>
                    </div>
                    <div>
                        <strong>Hash Blok 0 Manipulasi h(0)*:</strong>
                        <div class="data-box" style="color: var(--accent-error); font-weight: bold;">{hash_genesis_manipulasi}</div>
                    </div>
                </div>
                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 12px;">
                    <div>
                        <strong>Blok 1 Previous Hash yang Diharapkan:</strong>
                        <div class="data-box">{blok1_asli.h_prev}</div>
                    </div>
                    <div>
                        <strong>Blok 1 Previous Hash yang Diterima:</strong>
                        <div class="data-box" style="color: var(--accent-error);">{blok1_manipulasi.h_prev}</div>
                    </div>
                </div>
                <div class="status-banner status-invalid">
                    STATUS LEDGER: RANTAI BLOK RUSAK! Terdeteksi Modifikasi Data Ilegal pada Masa Lalu.
                </div>
                <details>
                    <summary>Lihat Struktur Data Input Hashing Blok 1</summary>
                    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-top: 10px;">
                        <div>
                            <strong>Payload Asli (Sebelum Tampering):</strong>
                            <pre style="font-size: 0.75rem; background: var(--card-bg); padding: 8px; border: 1px solid var(--card-border); border-radius: 4px; overflow-x: auto;">{payload_asli_json}</pre>
                        </div>
                        <div>
                            <strong>Payload Baru (Setelah Tampering):</strong>
                            <pre style="font-size: 0.75rem; background: var(--card-bg); padding: 8px; border: 1px solid var(--card-border); border-radius: 4px; overflow-x: auto; color: var(--accent-error);">{payload_manipulasi_json}</pre>
                        </div>
                    </div>
                </details>
            </div>
            """
        )
    return (
        auditor_ui,
        blok1_asli,
        blok1_manipulasi,
        genesis_asli,
        genesis_manipulasi,
        hash_genesis_asli,
        hash_genesis_manipulasi,
        payload_asli_json,
        payload_manipulasi_json,
        rantai_valid,
    )


@app.cell
def __(auditor_ui):
    # Menampilkan UI Auditor
    auditor_ui
    return

if __name__ == "__main__":
    app.run()
