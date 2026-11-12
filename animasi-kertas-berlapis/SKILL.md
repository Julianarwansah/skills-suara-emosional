---
name: "animasi-kertas-berlapis"
description: "Pakai saat user ingin membuat video Shorts gaya kertas berlapis + cahaya (diorama potongan kertas, paralaks, cahaya emas, ambience + senandung vokal tanpa alat musik) seperti serial KISAH PARA NABI."
---

# Animasi kertas berlapis + cahaya (v1, Nov 2026)

Bicara Bahasa Indonesia santai. Semua lokal dan gratis, digambar pycairo tanpa aset luar. Hasil 1080x1920, 30 fps.
Gaya ini lahir di serial KISAH PARA NABI (`$SERIAL_ROOT/serial animasi kisah nabi/`).
Untuk alur serial penuh (suara narator cara D, naskah, build, paket unggah, jadwal Repliz) pakai skill
`serial-animasi`; skill ini hanya mengatur GAYA GAMBAR dan BUNYI. Doc Project: `kisah-nabi/SETELAN_SERI.md`
dan `kisah-nabi/RENCANA_SERI.md` (keputusan di sana menang atas skill ini).

## 0. Urutan kerja
1. Baca doc Project seri (kalau ada) dan `proyek/kertas.py` + `proyek/contoh_gaya.py` di folder kisah nabi.
   Serial baru: salin dua file itu ke `proyek/` seri baru, jangan menulis ulang dari nol.
2. **Contoh 5 detik dulu** sebelum episode penuh (`python proyek/contoh_gaya.py video5 video/Contoh_5detik.mp4`),
   kirim dengan SendUserFile, tunggu user bilang oke.
3. Tulis kode di container (`pip install pycairo numpy scipy --break-system-packages`, font Poppins sudah ada),
   cek lembar frame (0, tengah, puncak, akhir) dengan mata sendiri, baru kirim ke Mac (device_commit_files).
4. Semua hasil jadi disimpan di folder seri: `video/`, `sampul/`, `dokumen/`, `naskah/`.

## 1. Resep tampilan kertas (fungsi di `kertas.py`)
- `lembar(c, jalur, warna, bayang, tepi, y0, y1)` = selembar kertas. Tiga hal yang membuatnya terbaca kertas:
  1) **bayangan jatuh**: bentuk yang sama digambar 5x, tiap kali digeser 3,5 px ke atas, hitam-ungu alpha 0,055;
  2) **gradasi tipis** dari warna x1,10 (atas) ke x0,78 (bawah);
  3) **tebal kertas**: garis 7 px warna x1,45 alpha 0,30 di tepi, dipotong ke dalam bentuk (clip).
- `punggung(seed, dasar, amp, kasar)` + `jalur_punggung()` = garis bukit/gunung dari jumlah sinus acak (tetap per
  seed). Gunung jauh kasar 1,2-1,5; bukit pasir 0,5-0,8.
- `cakram()` untuk matahari/bulan sebagai 3-4 cincin kertas bertumpuk (warna makin terang ke tengah) + `pendar()`.
- `awan()` = kotak bulat + 6 lingkaran, tanpa garis tepi. Pohon, sungai, tebing: path sendiri lalu `lembar()`.
- `serat(c)` (serat kertas, soft-light) dan `vinyet(c)` dipanggil SEKALI di akhir tiap frame, sebelum teks.
- Warna: 6 lapis dari jauh ke dekat makin gelap dan makin jenuh. Palet fajar yang disetujui: langit
  `#2A2260 → #8A4F8E → #F6B27A`; lapis `#6B5AA0, #4F4288, #C8794C, #A5583A, #5A2F4A, #231531`; sungai `#3E7FA6`.
  Malam: langit `#0E0C2A → #221A4C`, lapis ungu tua. Warna merek zamrud `#1FA887`, cahaya emas `#F5C75C`,
  teks krim `#FAF2E0`.

## 2. Kedalaman dan gerak
- `Kamera(zoom, gx, gy)`; `kam.masuk(c, z)` ... `kam.keluar(c)` dengan z 0 (langit) sampai 1 (paling dekat).
  Lapis dekat membesar dan bergeser lebih cepat = paralaks. Satu adegan 4-6 dtk: zoom 0,07-0,10, geser 50-80 px.
- Selalu ada yang hidup di tiap lapis: bintang berkedip, awan hanyut berlawanan arah, daun kurma berayun
  (`sin(t*1.3)`), kilau sungai, burung kertas lewat, kabut tipis di lembah, butir cahaya naik.
- Kejadian baru tiap 3-5 detik. Pindah adegan dengan crossfade 0,5-0,6 dtk (gambar adegan baru ke surface
  terpisah lalu `paint_with_alpha`).

## 3. Cahaya (pengganti sosok)
- `sinar()` = trapesium bergradasi mode ADD, 3-4 berkas dengan lebar berbeda dan denyut `0.85+0.15*sin`.
- Cincin cahaya melebar di tanah (elips, skala y 0,28), butir cahaya naik (`pendar` kecil + titik putih).
- Nama tokoh: huruf besar berspasi warna emas terang + bayangan gelap, muncul naik 24 px.
- **Untuk kisah nabi (wajib):** sosok nabi, malaikat, dan Iblis TIDAK digambar. Nabi = cahaya emas + nama +
  "'alaihis salam"; malaikat = berkas cahaya; Iblis = nyala api gelap. Kaum/orang biasa boleh siluet kertas
  tanpa wajah. Tidak ada suara yang memerankan mereka, semua lewat narator. Tiap naskah punya blok sumber
  (surat + ayat); hanya Al-Qur'an dan hadis sahih; riwayat lemah/israiliyat tidak dipakai.

## 4. Teks di layar
- `label_seri()` kecil berspasi di y 150. `teks_hook()` di y 300-560, baris kunci dalam kotak zamrud, sudah
  tampil di frame 0. `subtitle()` garis dasar y 1430, lebar maks 820 px, maks 2 baris, outline gelap 13 px,
  kata aktif emas. Di episode asli waktu kata mengikuti timeline suara, bukan perkiraan.
- Zona aman: x 90-930, y 220-1500. Poppins tidak punya huruf Arab dan panah.

## 5. Bunyi: ambience + senandung vokal, TANPA alat musik (`contoh_gaya.py`)
- `senandung(f0, dur, vokal, seed)`: deret harmonik + forman vokal ('m', 'u', 'a') + vibrato ±0,4% + napas.
  Dengung dasar D3 + D3 (sedikit sumbang) + A3 + D4, masuk langsung di detik 0 (bukan fade-in dari nol).
- Motif seri (hijaz): **D4 – Eb4 – F#4 – G4 – F#4 – D4**, satu suara lembut, dipakai di semua episode dan
  diaransemen ulang (lebih rendah untuk sedih, dua suara untuk puncak).
- `angin()` dua lapis kiri-kanan; tambah air, api, pasir, langkah, petir sesuai adegan (derau tersaring).
- Cahaya turun: desis naik 1,6 dtk + dentum lembut 58 Hz + kilau udara. Bukan lonceng atau piano.
- `gema()` boleh untuk senandung, **jangan pernah untuk narasi**. Akhir: ekor dipotong supaya loop mulus.
- Narator KISAH PARA NABI = suara cewek khidmat (calon E, "ibu dewasa, nada rendah"), referensi terkunci
  `_kerja/ref_narator_E.wav`. Setelan di `proyek/bank_suara.json`: `N` speed 0.90 narasi biasa,
  `N2` speed 0.84 momen Iblis/puncak, tanpa gaung. **Jangan audisi ulang** — resep 3 tahap lengkap
  (OmniVoice voice design -> VoxCPM2 rasa khidmat -> OmniVoice kloning) ada di skill `suara-emosional-serial`.
- Mix: -18 LUFS (loudnorm), true peak ≤ -1,5 dBTP; saat ada narasi, senandung ±12 dB di bawah suara.
- Kalau user minta perkusi/musik, itu keputusan baru: tanya dulu, catat di SETELAN_SERI.

## 6. Pelajaran (jangan diulang)
- Bingkai tebing simetris kiri-kanan + gundukan di tengah terbaca seperti VAS. Pakai bingkai tidak simetris
  (satu tebing besar, satu rendah) dan gundukan lebar yang menyatu dengan tanah.
- Jangan `scale(0)` di cairo; mulai dari 0,01.
- Render di container ±9 dtk per detik video; pipe frame BGRA ke ffmpeg (libx264 crf 17, yuv420p, AAC 44,1 kHz).
- File yang dikirim ulang ke path sama di Mac bisa tetap versi lama: cek ukuran/md5.

## 7. Cek sebelum kirim
Frame 0 sudah ada gambar kuat + hook; tidak ada sosok nabi/malaikat/Iblis; tiap lapis punya bayangan dan tepi;
tidak ada >5 dtk tanpa kejadian; teks di zona aman; bunyi terdengar sejak detik 0; durasi dan ukuran benar.
Setelah user menyetujui perubahan gaya, perbarui skill ini dan `kisah-nabi/SETELAN_SERI.md`.