# Standar Kualitas Animasi (playbook lintas genre, hasil sesi 2026-11-05)

Baca ini tiap kali membangun atau memperbaiki episode. Isinya pelajaran yang sudah TERBUKTI jalan
di Mac user; jangan rombak struktur yang sudah terkunci, tambah secara aditif.

## 1. Pustaka komponen, bukan adegan sekali pakai
- Semua bentuk dasar hidup di satu modul komponen (contoh: `proyek/pustaka_kn.py` serial kisah nyata):
  peta + proyeksi lon/lat, tokoh generik `orang(jenis, pose, barang)`, gunung api (meletus/lava/salju/
  runcing), kolom abu berbenjol, awan panas, laut + dinding tsunami ber-busa, pantai, sawah, desa,
  pohon tumbuh (fase 0..1), mata air, perahu/rakit rompong/kapal penumpang/kapal kargo, efek cuaca
  (abu/salju/hujan/petir/asap/api), kartu dokumen (koran/berkas+cap/garis waktu/angka besar).
- Adegan per episode = komposisi komponen + argumen. Adegan yang muncul di beberapa beat WAJIB punya
  arg fase (`kapal_terbakar:0.35` → `:1.0`) supaya tidak identik; pertumbuhan/kehancuran diikat ke
  fase episode, bukan ke durasi beat.
- Tokoh: kartun ±4-5 kepala, kaki + sepatu terlihat, leher pendek; jenis tokoh = kamus CIRI (baju,
  celana, penutup kepala, janggut, kacamata, bungkuk, kecil); siluet 0..1 untuk jarak jauh/kilas balik.
- Uji komponen dengan `uji_pustaka.py` (lembar komponen) dan `uji_pustaka.py nama1,nama2` (lembar
  adegan) SEBELUM build penuh; perbaiki yang mentah di level komponen, bukan di tiap adegan.

## 2. Meta per episode (tanpa merusak episode lama)
- `> sepia:` daftar adegan kilas balik; `> goyang:` `nama=a0,a1,amp; ...`; keduanya dibaca render.py
  dengan fallback ke bawaan serial sehingga episode lama tetap identik.
- Adegan generik membaca meta: `stempel` (lokasi/rentang/pin/peta_sorot), `kutipan`/`kutipan_oleh`,
  `angka` (arg `ANGKA;;LABEL;;SUB`, dihitung naik bila digit), `kartu_pilih`/`kartu_tanya`
  (tanya/pilihan/follow). Teks kartu WAJIB auto-fit lebar (`teks_pas`) supaya tidak terpotong.

## 3. Hook 0-3 detik & sampul clickbait (isi tetap enak sampai akhir)
- Hook layar: maks 3 baris, satu baris kunci dalam kotak warna merek; baris pertama narasi = momen
  paling aneh (bukan intro/salam); angka boleh digit DI LAYAR, diucapkan pakai huruf.
- Pola hook terbukti: akhir dulu ("Besoknya dia benar meninggal jam tiga"), kalimat "kamu", aturan
  yang dilanggar, dan "tidak ada X padahal Y" (tentara berbaris melawan musuh yang tidak ada).
- Sampul: adegan di keadaan paling dramatis/akhir + judul maks 2 baris (auto-size ≤900 px) + baris
  kunci dalam kotak kuning miring sedikit + pil "EP n" + nama seri; semua teks di zona y 300-1640.
- Clickbait boleh kuat TAPI setiap angka di hook/sampul harus lolos verifikasi (kisah nyata: ≥2 sumber);
  isi video harus membayar janji hook di 5 detik pertama dan tetap mengalir sampai akhir.

## 4. Audio: lapisan, bukan satu loop
- Musik dasar + **strings `gesek_pad`** (attack lambat, vibrato halus) sejak intensitas ≥2.
- Transisi: `riser` 1,2 dtk masuk adegan tegang (letusan/tsunami/kebakaran/reveal), `swell` masuk
  adegan penutup/tenang (stempel/kartu). Hening total 0,9 dtk sebelum reveal (horor).
- **Setiap nama adegan punya SFX/ambien sendiri** (gemuruh+dentum+petir vulkanik; ombak+angin+
  gemericik+burung laut; jangkrik+burung+cangkul desa; api+alarm+kerumunan kapal; klik kamera+tepuk
  untuk pertemuan/press; jam tik+desir kertas untuk dokumen; dentum+ding untuk kartu angka).
  Adegan baru tanpa SFX = terasa murah; tambahkan ke pemetaan efek sebelum build.
- Room tone sangat pelan di jeda (jangan sunyi digital); narasi kering tanpa reverb; satu gain linier
  ke −17..−19 LUFS, true peak ≤ −1 dBTP; cek mono.

## 5. Loop QC yang dipakai sesi ini (urutan wajib)
1. `uji_pustaka.py` komponen & adegan baru → perbaiki di komponen.
2. Build suara → `jaga_suara` wajib 0 MELESET (kalau meleset: pendekkan kalimat / kunci seed).
3. Render → lihat `lembar.png` per episode: teks terpotong? tokoh ketimpa benda? adegan identik
   antar beat? caption menabrak subtitle/badge? Perbaiki → render ulang (suara di-cache, murah).
4. Ukur: durasi genre, LUFS, true peak; lihat sampul di ukuran kecil.
5. Baru jadwalkan (simulasi → setuju user → `--jalan`).

## 6. Jebakan yang sudah pernah memakan waktu
- Parser naskah: arg kosong (`adegan:`) dulu membuat beat HILANG; arg ganda pakai `;;` bukan `|`.
- `kotak()` butuh 6 argumen (r wajib); jangan `scale(0)`; Poppins tidak punya "→" (pakai "–").
- Angka di naskah WAJIB huruf; whisper menulis angka sebagai digit sehingga pembanding transkripsi
  harus membuang digit di kedua sisi.
- Venv render bersama bisa hilang tanpa kabar: cek path venv di `bangun.sh` sebelum build massal;
  fallback teruji = `serial animasi ojol/_env`; font Poppins dari ~/Library/Fonts.
- Render 2 bagian paralel + satu proses OmniVoice saja per mesin; rantai banyak episode pakai
  `rantai.sh` supaya kegagalan berhenti di satu tempat dan log mudah dibaca.
- Parser caption (`otomasi/status_upload.blok_dokumen`): heading catatan produksi yang memuat
  nomor episode di NAMA BERKAS ('## Cara pasang sampul (pakai sampul/Cover_Episode3.png)')
  pernah naik jadi caption publik + judul YouTube. Penjaga: lewati heading ber-kata catatan
  (`KEPALA_CATATAN`) dan nomor yang diikuti ekstensi berkas (`NOMOR_BERKAS`). Kalau jadwal
  terlanjur terkirim rusak, perbaiki di tempat lewat `PUT /public/schedule/{id}` (field
  `FIELD_PUT`), cadangkan payload lama dulu — lihat `otomasi/perbaiki_pijat_ep3.py`.
- Kartu waktu (`waktu`) tanpa argumen mencetak bawaan serial (mis. "LIMA BELAS") dan bisa
  bertabrakan dengan narasi; selalu tulis `## n | waktu:SATU` / `waktu:TIGA` sesuai kalimatnya.
- Label `> pilihan:` lebih dari ±18 karakter membuat huruf pertama tertutup badge A/B di kartu
  pilih; pakai label pendek.
- Nama helper musik BEDA per serial (mis. `riser` ada di musik sedih, tidak ada di musik horor —
  pakai `reverse_swell`); grep `^def` musik.py serial itu sebelum menambah cabang SFX.
- Naskah horor serial ber-rutinitas: beat "pagi di warung/fakta kampung" wajib ada; tanpanya
  durasi jatuh di bawah batas genre (63 dtk vs target 80–95).
- `bisikan(dur)` di musik horor: `panjang` selisih bisa melewati ujung array sehingga assignment
  envelope crash broadcast pada durasi tertentu. Kunci `panjang = min(..., n - k)`.
