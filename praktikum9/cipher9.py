# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "pycryptodome",
# ]
# ///

import marimo

__generated_with = "0.20.4"
app = marimo.App(app_title="Eksplorasi Hash dan Digital Signature")


@app.cell
def __():
    import marimo as mo
    import hashlib
    import time
    from Crypto.PublicKey import RSA
    from Crypto.Signature import pkcs1_15
    from Crypto.Hash import SHA256
    return RSA, SHA256, hashlib, mo, pkcs1_15, time


@app.cell
def __(mo):
    style_element = mo.Html(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap');
        
        :root {
            --progress-bg: #e2e8f0;
            --progress-border: #cbd5e1;
            --bar-md5-bg: #3b82f6;
            --bar-sha-bg: #ec4899;
            --benchmark-bg: #f8fafc;
            --benchmark-border: #e2e8f0;
        }
        
        @media (prefers-color-scheme: dark) {
            :root {
                --progress-bg: #0f172a;
                --progress-border: #1e293b;
                --bar-md5-bg: #60a5fa;
                --bar-sha-bg: #f472b6;
                --benchmark-bg: #0f172a;
                --benchmark-border: #1e293b;
            }
        }
        
        .marimo-output * {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        }
        
        .crypto-card {
            background: #ffffff;
            border: 1px solid #e2e8f0;
            border-radius: 12px;
            padding: 20px;
            margin: 16px 0;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
            color: #0f172a;
            transition: all 0.2s ease;
        }
        
        .benchmark-box {
            flex: 1;
            min-width: 150px;
            background: var(--benchmark-bg);
            border: 1px solid var(--benchmark-border);
            padding: 16px;
            border-radius: 12px;
            text-align: center;
        }
        
        .card-title {
            font-size: 1rem;
            font-weight: 700;
            color: #4f46e5;
            margin-bottom: 12px;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }
        
        .register-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 16px;
            margin-top: 16px;
        }
        
        .reg-box {
            background: #f8fafc;
            border: 1px solid #e2e8f0;
            border-radius: 10px;
            padding: 14px;
            text-align: center;
        }
        
        .reg-box-highlighted {
            border: 2px solid #4f46e5;
            background: #f5f3ff;
            --highlight-color: #4f46e5;
        }
        
        .reg-name {
            font-weight: 700;
            font-size: 1.1rem;
            color: #0d9488;
            margin-bottom: 6px;
        }
        
        .reg-hex {
            font-family: 'JetBrains Mono', monospace;
            font-size: 1rem;
            font-weight: 700;
            color: #0f172a;
            background: #f1f5f9;
            padding: 4px 10px;
            border-radius: 6px;
            display: inline-block;
            margin-bottom: 6px;
            border: 1px solid #e2e8f0;
        }
        
        .reg-bin {
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.75rem;
            color: #475569;
            word-break: break-all;
        }
        
        .progress-container {
            background: #f1f5f9;
            border-radius: 20px;
            height: 12px;
            width: 100%;
            overflow: hidden;
            margin: 8px 0;
            border: 1px solid #e2e8f0;
        }
        
        .progress-bar {
            height: 100%;
            border-radius: 20px;
            transition: width 0.8s cubic-bezier(0.4, 0, 0.2, 1);
        }
        
        .progress-md5 {
            background: #3b82f6;
        }
        
        .progress-sha {
            background: #ec4899;
        }
        
        .metric-value {
            font-size: 1.5rem;
            font-weight: 700;
            color: #0f172a;
            font-family: 'JetBrains Mono', monospace;
        }
        
        .badge-success {
            background: #dcfce7;
            color: #15803d;
            border: 1px solid #bbf7d0;
            padding: 12px 16px;
            border-radius: 10px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .badge-danger {
            background: #fee2e2;
            color: #b91c1c;
            border: 1px solid #fecaca;
            padding: 12px 16px;
            border-radius: 10px;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .code-nonlinear {
            color: #be123c;
            font-weight: 600;
        }

        .code-success {
            color: #15803d;
            font-weight: 600;
        }

        .speed-alert {
            margin-top: 16px; 
            font-size: 0.95rem; 
            text-align: center; 
            color: #15803d; 
            background: #f0fdf4; 
            padding: 8px; 
            border-radius: 8px;
            border: 1px solid #bbf7d0;
        }

        /* Mode Gelap (Dark Mode) */
        @media (prefers-color-scheme: dark) {
            .crypto-card {
                background: #1e293b;
                border-color: #334155;
                color: #f8fafc;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.2);
            }
            .card-title {
                color: #818cf8;
            }
            .reg-box {
                background: #0f172a;
                border-color: #1e293b;
            }
            .reg-box-highlighted {
                border-color: #818cf8;
                background: rgba(129, 140, 248, 0.1);
                --highlight-color: #a5b4fc;
            }
            .reg-name {
                color: #2dd4bf;
            }
            .reg-hex {
                color: #f8fafc;
                background: #1e293b;
                border-color: #334155;
            }
            .reg-bin {
                color: #94a3b8;
            }
            .progress-container {
                background: #0f172a;
                border-color: #1e293b;
            }
            .progress-md5 {
                background: #60a5fa;
            }
            .progress-sha {
                background: #f472b6;
            }
            .metric-value {
                color: #f8fafc;
            }
            .badge-success {
                background: rgba(16, 185, 129, 0.15);
                color: #34d399;
                border-color: rgba(16, 185, 129, 0.3);
            }
            .badge-danger {
                background: rgba(239, 68, 68, 0.15);
                color: #f87171;
                border-color: rgba(239, 68, 68, 0.3);
            }
            .code-nonlinear {
                color: #fda4af;
            }
            .code-success {
                color: #4ade80;
            }
            .speed-alert {
                color: #a7f3d0;
                background: rgba(16, 185, 129, 0.1);
                border-color: rgba(16, 185, 129, 0.2);
            }
        }
        </style>
        """
    )
    style_element
    return (style_element,)


@app.cell
def __(mo):
    mo.md(
        """
        # Eksplorasi Hash & Digital Signature
        **Praktikum Keamanan Komputer - Modul 9**
        """
    )
    return


@app.cell
def __(mo):
    mo.md("## Bagian 1: Visualisasi Langkah Kerja MD5")
    return


@app.cell
def __(mo):
    # Selector untuk fungsi nonlinear MD5
    func_select = mo.ui.dropdown(
        options={
            "F(B, C, D) = (B & C) | (~B & D) - Round 1": "F",
            "G(B, C, D) = (B & D) | (C & ~D) - Round 2": "G",
            "H(B, C, D) = B ^ C ^ D - Round 3": "H",
            "I(B, C, D) = C ^ (B | ~D) - Round 4": "I"
        },
        value="F(B, C, D) = (B & C) | (~B & D) - Round 1",
        label="Pilih Fungsi Putaran"
    )
    
    # Input register awal dalam heksadesimal
    a_input = mo.ui.text(value="AAAA0000", label="Register A (Hex)")
    b_input = mo.ui.text(value="1111AAAA", label="Register B (Hex)")
    c_input = mo.ui.text(value="00002222", label="Register C (Hex)")
    d_input = mo.ui.text(value="1234ABCD", label="Register D (Hex)")

    # Input pesan blok X[k], konstanta T[i], dan nilai pergeseran s
    x_input = mo.ui.text(value="B0B0B0B0", label="Sub-blok X[k] (Hex)")
    t_input = mo.ui.text(value="D76AA478", label="Konstanta T[i] (Hex)")
    s_input = mo.ui.number(start=1, stop=31, step=1, value=7, label="Shift s (bits)")

    mo.vstack([
        func_select,
        mo.md("### Input Register & Parameter:"),
        mo.hstack([
            mo.vstack([a_input, b_input, c_input, d_input]),
            mo.vstack([x_input, t_input, s_input])
        ])
    ])
    return (
        a_input, b_input, c_input, d_input,
        func_select, s_input, t_input, x_input
    )


@app.cell
def __(a_input, b_input, c_input, d_input, func_select, mo, s_input, t_input, x_input):
    # Parsing input heksadesimal
    try:
        a_val = int(a_input.value, 16)
        b_val = int(b_input.value, 16)
        c_val = int(c_input.value, 16)
        d_val = int(d_input.value, 16)
        x_val = int(x_input.value, 16)
        t_val = int(t_input.value, 16)
        s_val = int(s_input.value)
        parse_err = False
    except ValueError:
        parse_err = True

    if parse_err:
        result_md5_step = mo.md("⚠️ **Format Hex tidak valid.** Harap gunakan karakter hexadecimal (0-9, A-F).")
    else:
        # Pilihan Fungsi Nonlinear
        f_type = func_select.value
        if f_type == "F":
            func_val = (b_val & c_val) | (~b_val & d_val)
            expr_str = "(B & C) | (~B & D)"
        elif f_type == "G":
            func_val = (b_val & d_val) | (c_val & ~d_val)
            expr_str = "(B & D) | (C & ~D)"
        elif f_type == "H":
            func_val = b_val ^ c_val ^ d_val
            expr_str = "B ^ C ^ D"
        else:
            func_val = c_val ^ (b_val | ~d_val)
            expr_str = "C ^ (B | ~D)"
        
        func_val &= 0xFFFFFFFF

        # Penjumlahan modulo 2^32
        sum_val = (a_val + func_val + x_val + t_val) & 0xFFFFFFFF

        # Rotasi kiri s bit
        rotated = ((sum_val << s_val) | (sum_val >> (32 - s_val))) & 0xFFFFFFFF

        # Update nilai register setelah langkah ini selesai
        new_a = d_val
        new_b = (b_val + rotated) & 0xFFFFFFFF
        new_c = b_val
        new_d = c_val

        # Membuat output penjelasan visual
        result_md5_step = mo.Html(
            f"""
            <div class="crypto-card">
                <div class="card-title">Kalkulasi MD5: {f_type}(B,C,D)</div>
                <div style="font-size: 0.95rem; margin-bottom: 16px;">
                    Fungsi Nonlinear: <code class="code-nonlinear">{expr_str}</code> &rarr; <code>0x{func_val:08X}</code> (<code style="font-size: 0.85rem;">{func_val:032b}</code>)<br/>
                    Modulo Sum: <code>A + {f_type} + X[k] + T[i]</code> &rarr; <code>0x{sum_val:08X}</code><br/>
                    Rotate Left (<<< {s_val}): &rarr; <code class="code-success">0x{rotated:08X}</code>
                </div>
                
                <div class="card-title" style="font-size: 0.9rem; border-top: 1px solid rgba(128,128,128,0.15); padding-top: 16px; margin-top: 16px;">
                    Transisi Nilai Register
                </div>
                
                <div class="register-grid">
                    <div class="reg-box">
                        <div class="reg-name">A</div>
                        <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">Awal: 0x{a_val:08X}</div>
                        <div class="reg-hex">0x{new_a:08X}</div>
                        <div class="reg-bin">{new_a:032b}</div>
                    </div>
                    <div class="reg-box reg-box-highlighted">
                        <div class="reg-name" style="color: var(--highlight-color);">B (Updated)</div>
                        <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">Awal: 0x{b_val:08X}</div>
                        <div class="reg-hex" style="color: var(--highlight-color);">0x{new_b:08X}</div>
                        <div class="reg-bin">{new_b:032b}</div>
                    </div>
                    <div class="reg-box">
                        <div class="reg-name">C</div>
                        <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">Awal: 0x{c_val:08X}</div>
                        <div class="reg-hex">0x{new_c:08X}</div>
                        <div class="reg-bin">{new_c:032b}</div>
                    </div>
                    <div class="reg-box">
                        <div class="reg-name">D</div>
                        <div style="font-size: 0.75rem; color: #64748b; margin-bottom: 4px;">Awal: 0x{d_val:08X}</div>
                        <div class="reg-hex">0x{new_d:08X}</div>
                        <div class="reg-bin">{new_d:032b}</div>
                    </div>
                </div>
            </div>
            """
        )
    result_md5_step
    return (
        a_val, b_val, c_val, d_val, expr_str, f_type, func_val,
        new_a, new_b, new_c, new_d, parse_err, result_md5_step,
        rotated, sum_val, s_val, t_val, x_val
    )


@app.cell
def __(mo):
    mo.md("## Bagian 2: Analisis Avalanche Effect & Kinerja Hash")
    return


@app.cell
def __(mo):
    # Input untuk perbandingan efek avalanche
    txt1_input = mo.ui.text_area(value="Politeknik", label="Teks Input 1")
    txt2_input = mo.ui.text_area(value="politeknik", label="Teks Input 2")
    
    mo.hstack([txt1_input, txt2_input])
    return txt1_input, txt2_input


@app.cell
def __(hashlib, mo, txt1_input, txt2_input):
    t1 = txt1_input.value.encode()
    t2 = txt2_input.value.encode()

    # MD5 Hashing
    md5_1 = hashlib.md5(t1).hexdigest()
    md5_2 = hashlib.md5(t2).hexdigest()
    
    # SHA-256 Hashing
    sha_1 = hashlib.sha256(t1).hexdigest()
    sha_2 = hashlib.sha256(t2).hexdigest()

    # Perhitungan perbedaan bit (Hamming Distance)
    def hamming_distance(hex1, hex2):
        bin1 = bin(int(hex1, 16))[2:].zfill(len(hex1) * 4)
        bin2 = bin(int(hex2, 16))[2:].zfill(len(hex2) * 4)
        return sum(c1 != c2 for c1, c2 in zip(bin1, bin2)), bin1, bin2

    h_dist_md5, b_md5_1, b_md5_2 = hamming_distance(md5_1, md5_2)
    h_dist_sha, b_sha_1, b_sha_2 = hamming_distance(sha_1, sha_2)

    pct_md5 = (h_dist_md5 / 128) * 100
    pct_sha = (h_dist_sha / 256) * 100

    avalanche_html = mo.Html(
        f"""
        <div class="crypto-card">
            <div class="card-title">Analisis Efek Avalanche (Hamming Distance)</div>
            
            <div style="margin-bottom: 20px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="font-weight: 600;">MD5 (128-bit)</span>
                    <span class="metric-value" style="font-size: 1.1rem; color: #3b82f6;">{h_dist_md5} / 128 bit ({pct_md5:.2f}%)</span>
                </div>
                <div style="background: var(--progress-bg); border-radius: 20px; height: 12px; width: 100%; overflow: hidden; margin: 8px 0; border: 1px solid var(--progress-border);">
                    <div style="width: {pct_md5}%; height: 100%; border-radius: 20px; background: var(--bar-md5-bg); transition: width 0.8s ease;"></div>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #475569; word-break: break-all; margin-top: 4px;">
                    H1: {md5_1.upper()}<br>H2: {md5_2.upper()}
                </div>
            </div>
            
            <div style="margin-top: 20px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 6px;">
                    <span style="font-weight: 600;">SHA-256 (256-bit)</span>
                    <span class="metric-value" style="font-size: 1.1rem; color: #ec4899;">{h_dist_sha} / 256 bit ({pct_sha:.2f}%)</span>
                </div>
                <div style="background: var(--progress-bg); border-radius: 20px; height: 12px; width: 100%; overflow: hidden; margin: 8px 0; border: 1px solid var(--progress-border);">
                    <div style="width: {pct_sha}%; height: 100%; border-radius: 20px; background: var(--bar-sha-bg); transition: width 0.8s ease;"></div>
                </div>
                <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #475569; word-break: break-all; margin-top: 4px;">
                    H1: {sha_1.upper()}<br>H2: {sha_2.upper()}
                </div>
            </div>
        </div>
        """
    )
    avalanche_html
    return (
        b_md5_1, b_md5_2, b_sha_1, b_sha_2, h_dist_md5, h_dist_sha,
        hamming_distance, md5_1, md5_2, pct_md5, pct_sha, sha_1, sha_2,
        t1, t2, avalanche_html
    )


@app.cell
def __(mo):
    # Benchmark Kinerja Hashing
    benchmark_btn = mo.ui.button(
        label="Jalankan Benchmark Kecepatan Hashing",
        value=0,
        on_click=lambda value: value + 1,
    )
    benchmark_btn
    return (benchmark_btn,)


@app.cell
def __(benchmark_btn, hashlib, mo, time):
    benchmark_res = ""
    if benchmark_btn.value:
        large_data = b"KeamananKomputer" * 500000 # ~8 MB
        
        # MD5 Speed Test
        start = time.time()
        for _ in range(10):
            hashlib.md5(large_data).digest()
        md5_dur = time.time() - start
        
        # SHA-256 Speed Test
        start = time.time()
        for _ in range(10):
            hashlib.sha256(large_data).digest()
        sha_dur = time.time() - start
        
        benchmark_res = mo.Html(
            f"""
            <div class="crypto-card" style="margin-top: 16px;">
                <div class="card-title">Hasil Kecepatan Pemrosesan (~80MB data)</div>
                <div style="display: flex; gap: 24px; flex-wrap: wrap;">
                    <div class="benchmark-box">
                        <div style="font-size: 0.85rem; color: #475569; margin-bottom: 6px;">Kecepatan MD5</div>
                        <div class="metric-value" style="color: #3b82f6;">{md5_dur:.4f} s</div>
                    </div>
                    <div class="benchmark-box">
                        <div style="font-size: 0.85rem; color: #475569; margin-bottom: 6px;">Kecepatan SHA-256</div>
                        <div class="metric-value" style="color: #ec4899;">{sha_dur:.4f} s</div>
                    </div>
                </div>
                <div class="speed-alert">
                    MD5 <strong>{sha_dur/md5_dur:.1f}x lebih cepat</strong> dibandingkan SHA-256
                </div>
            </div>
            """
        )
    else:
        benchmark_res = mo.md("")
    benchmark_res
    return (benchmark_res,)


@app.cell
def __(mo):
    mo.md("## Bagian 3: Simulasi Digital Signature (RSA + SHA-256)")
    return


@app.cell
def __(mo):
    # Pilihan parameter kunci
    key_size_select = mo.ui.dropdown(
        options={"1024 bit": 1024, "2048 bit": 2048},
        value="1024 bit",
        label="Pilih Ukuran Kunci RSA"
    )
    
    msg_input = mo.ui.text_area(
        value="Dokumen Transaksi Finansial Senilai Rp 10.000.000",
        label="Isi Dokumen/Pesan Asli",
        rows=3
    )
    
    # Input pesan untuk diuji (untuk simulasi tampering)
    msg_test = mo.ui.text_area(
        value="Dokumen Transaksi Finansial Senilai Rp 10.000.000",
        label="Dokumen yang Diterima (untuk Verifikasi)",
        rows=3
    )

    mo.vstack([
        key_size_select.style(width="180px"),
        mo.hstack([
            msg_input.style(width="100%"),
            msg_test.style(width="100%")
        ], gap=3)
    ], gap=1)
    return key_size_select, msg_input, msg_test


@app.cell
def __(RSA, SHA256, key_size_select, mo, msg_input, msg_test, pkcs1_15, time):
    # Generate RSA Keys
    t_start = time.time()
    rsa_key = RSA.generate(key_size_select.value)
    gen_duration = time.time() - t_start
    
    priv_key = rsa_key
    pub_key = rsa_key.publickey()

    # Perhitungan hash pesan asli
    encoded_msg = msg_input.value.encode()
    h_msg = SHA256.new(encoded_msg)
    
    # Proses penandatanganan (Signing) menggunakan Private Key
    signature = pkcs1_15.new(priv_key).sign(h_msg)

    # Proses Verifikasi
    encoded_test = msg_test.value.encode()
    h_test = SHA256.new(encoded_test)
    
    verification_success = False
    try:
        pkcs1_15.new(pub_key).verify(h_test, signature)
        verification_success = True
    except (ValueError, TypeError):
        verification_success = False

    status_class = "badge-success" if verification_success else "badge-danger"
    status_icon = "🟢" if verification_success else "🔴"
    status_text = (
        "TANDA TANGAN VALID — Integritas data terjamin dan pengirim terautentikasi."
        if verification_success
        else "TANDA TANGAN TIDAK VALID — Terdeteksi manipulasi data atau kunci tidak cocok!"
    )
    
    signature_html = mo.Html(
        f"""
        <div class="crypto-card">
            <div class="card-title">Metrik Kunci & Signature</div>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-bottom: 20px;">
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 14px; border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.8rem; color: #475569;">Waktu Kunci RSA</div>
                    <div class="metric-value" style="font-size: 1.4rem; color: #d97706;">{gen_duration:.4f} s</div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 14px; border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.8rem; color: #475569;">Panjang Kunci</div>
                    <div class="metric-value" style="font-size: 1.4rem; color: #2563eb;">{len(bin(rsa_key.n)) - 2} bit</div>
                </div>
                <div style="background: #f8fafc; border: 1px solid #e2e8f0; padding: 14px; border-radius: 10px; text-align: center;">
                    <div style="font-size: 0.8rem; color: #475569;">Ukuran Signature</div>
                    <div class="metric-value" style="font-size: 1.4rem; color: #7c3aed;">{len(signature)} byte</div>
                </div>
            </div>
            
            <div style="margin-bottom: 20px; padding: 12px; background: #f1f5f9; border: 1px solid #e2e8f0; border-radius: 8px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #475569; word-break: break-all;">
                <strong>Signature Hex:</strong> 0x{signature.hex().upper()[:64]}...
            </div>
            
            <div class="{status_class}">
                <span style="font-size: 1.3rem;">{status_icon}</span>
                <span>{status_text}</span>
            </div>
        </div>
        """
    )
    signature_html
    return (
        encoded_msg, encoded_test, gen_duration, h_msg, h_test, priv_key,
        pub_key, rsa_key, signature, signature_html, t_start,
        verification_success
    )


if __name__ == "__main__":
    app.run()
