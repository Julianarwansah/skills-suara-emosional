---
name: serial-animasi
description: Membuat, melanjutkan, atau memperbaiki episode serial animasi vertikal Indonesia (horor, komedi/lucu, sedih/relate, kisah nyata) di folder "serial animasi" Mac: naskah, suara narator OmniVoice, render pycairo 1080x1920, musik & efek sintesis, sampul clickbait, QC, paket unggah, dan jadwal Repliz. Pakai saat user minta episode baru, serial baru, perbaikan animasi/suara/backsound, thumbnail, caption, atau jadwal untuk serial animasi apa pun (PENGUMUMAN DUKA, DINAS KEBETULAN, ANAK SULUNG, KISAH NYATA NUSANTARA, dll).
---

# Serial Animasi Vertikal (satu skill untuk semua genre)

Satu pipeline untuk empat genre. Semua lokal & gratis, target FYP YouTube Shorts + TikTok + IG Reels
(satu master 1080x1920 30 fps, satu caption gabungan, satu jadwal lewat Repliz).
Akar: `$SERIAL_ROOT/`. Bicara Bahasa Indonesia santai ke user.

## 0. Metrik yang dinilai algoritma (dasar semua keputusan)
- Shorts: "viewed vs swiped away" ≥70%; lalu % ditonton & replay (loop >100% kuat).
- TikTok: retensi 3 detik pertama; kehilangan >50% di 3 dtk = mati di uji pertama.
- IG Reels: watch time + **sends per reach** (terkuat), likes, saves.
- Konsekuensi: frame & kalimat 0-2 dtk paling penting; perubahan kecil tiap 3-5 dtk; akhir menyambung
  ke awal (loop); selalu ada alasan KOMENTAR (A/B, cari sosok) dan alasan KIRIM/TAG.
- Setelah tayang minta tangkapan analitik 48 jam; simpan di "Pelajaran dari angka" SETELAN_SERI:
  swiped-away tinggi → perbaiki hook/frame 0; drop tengah → potong baris lambat; completion bagus
  tapi follow/tag kecil → perkuat cliffhanger/ajakan.

## 1. Routing genre
**Baca dulu `PETA_MESIN.md` di akar workspace** sebelum menyentuh folder serial mana pun: isinya mesin
mana yang dipakai tiap serial (A pycairo klasik / B per-episode / C Remotion), perintah build-nya,
prasyarat venv yang sudah diverifikasi hidup, gerbang QC mana yang tersedia per serial, dan celah yang
belum ada penjaganya. Jangan bangun mesin baru untuk episode baru, dan jangan asumsikan semua serial
memakai pipeline di bagian 2 (KKN, OJOL, NIGHT SHIFT, IN LOVING MEMORY bentuknya beda).

Baca referensi sesuai genre serialnya SEBELUM menulis apa pun:
- **Memilih konsep episode/serial BARU → `references/tren-format.md` dulu** (format apa yang sedang
  ramai bulan berjalan, kanal kecil mana yang meledak, gaya visual apa yang terbukti; ada tanggal
  risetnya — kalau sudah lebih dari sebulan, perbarui dengan cara di bagian 11 berkas itu).
- **Menanyakan/memperbaiki kenapa sebuah video lolos atau gagal → `references/mekanika-fyp.md`**
  (gerbang rekomendasi 3 detik → selesai → aksi, dan tuas mana yang menarik gerbang mana).
- Horor / misteri fiksi → `references/horor.md`
- Komedi / lucu → `references/lucu.md`
- Sedih / relate keluarga → `references/sedih.md`
- Kisah nyata / sejarah / dokumenter → `references/kisah-nyata.md`
- Standar kualitas gambar & suara (berlaku untuk SEMUA genre, wajib dibaca tiap build) →
  `references/kualitas-animasi.md`
Bila serial sudah ada: baca `<seri>/SETELAN_SERI.md` + `<seri>/RENCANA_SERI.md` dulu (tokoh tetap,
warna milik tokoh, running gag, motif sosok, suara pilihan user, status episode).

## 2. Pipeline (urutan wajib)
```
naskah/epN.md -> naskah_ke_lines.py -> gen_suara.py -> jaga_suara.py -> timeline.py
-> musik.py -> render.py epN 0 2 & 1 2 -> gabung.py -> sampul.py -> render.py epN lembar
```
- Satu episode: `cd "<seri>/proyek" && bash bangun.sh epN N`.
- Banyak episode: `bash rantai.sh [mulai]` (berurutan; berhenti di kegagalan pertama).
- Venv suara: `lab suara/venv` (+ `venv_omni`). Venv render: `serial animasi ojol/_env`
  (venv lama `animasi fun fact/_env` SUDAH TIDAK ADA sejak 2026-11-05; Poppins terpasang di
  ~/Library/Fonts sehingga venv pycairo mana pun bisa).
- Uji cepat tanpa suara: `python uji_gambar.py epN [no_adegan] [detik]`,
  `python uji_pustaka.py` (lembar komponen) atau `python uji_pustaka.py nama1,nama2` (lembar adegan).
- Dua `_mesin_omni` TIDAK boleh jalan bersamaan (berebut MPS): cek `pgrep -fl _mesin`; tunggu dengan
  `kill -0 PID`; jangan bunuh job serial lain.

## 3. Naskah (format bersama)
```
> suara: N   > musik: kisah|sedih|komedi|misteri   > hook: baris1 / *katakunci* / baris3
> sampul: Judul baris1 / *kata kunci* | nama_adegan[:arg]
> tanya: baris1 / *baris2?*   > pilihan: A=.. | B=..   > follow: ..
> sepia: adegan1 adegan2      > goyang: adegan=a0,a1,amp; adegan2=...
## 1 | adegan[:arg]
Kalimat narator (maks ±12 kata; angka diucapkan ditulis huruf; angka hanya di layar).
```
- Parser: `## n | adegan:arg` — arg BOLEH kosong (`adegan:`); arg ganda dipisah `;;`
  (JANGAN `|`, itu pemisah beat). Baris meta lain: `> lokasi/rentang/pin/peta_sorot/kutipan/...`.
- Target durasi per genre ada di referensinya (horor 80-95 dtk, lucu 75-90, sedih 60-100, kisah nyata 60-95).

## 4. Suara narator (pilih dengan telinga, cara D)
OmniVoice voice design → VoxCPM2 kloning + arahan emosi (Inggris) → referensi emosional →
OmniVoice kloning dari referensi itu untuk semua baris. TANPA reverb/gaung pada narasi.
- Audisi 4-5 calon (bunyi tit 1x..5x), kirim mp3 + tabel (nada median Hz, variasi semiton, transkripsi);
  user boleh memilih dengan menyebut detik → hitung tata letak file.
- Ref disimpan dengan nama BARU (kunci cache = path ref); pilih per baris dengan tag `[N2] teks` dll.
- `jaga_suara.py` wajib hijau: rentang nada per speaker + transkripsi (kemiripan ≥0,7); baris meleset
  dibuat ulang seed 21/33/47/59/71 lalu dikunci di `seed_khusus`.
- Jeda dramatis/komedi ditulis sebagai penanda di naskah (`[jeda]`, `[tahan]`, `[ketuk]`, `[pelan]`),
  bukan "..." di teks suara; timeline mengubahnya jadi sunyi sesudah baris.

## 5. Musik & efek (semua disintesis sendiri, bebas hak cipta)
- Musik −10 s.d. −11 dB di bawah narasi, duck saat bicara (kecuali horor: tanpa ducking).
- Lapisan wajib kisah/sedih: piano + pad + sub + **strings `gesek_pad`**; transisi: `riser` masuk adegan
  tegang, `swell` masuk adegan penutup/tenang; **efek suara per nama adegan** (setiap adegan baru WAJIB
  punya ambien/SFX sendiri di `efek_kisah`/`atur_umum`).
- Akhir: −17..−19 LUFS, true peak ≤ −1 dBTP, SATU gain linier (tanpa kompresor/limiter bus);
  ekor dipotong pas supaya loop ke detik 0 tidak bolong; cek juga versi mono.

## 6. Visual (pycairo, tanpa aset luar)
- Komponen pakai ulang hidup di `proyek/pustaka_kn.py`-style (peta, tokoh generik, gunung, laut, kapal,
  kartu dokumen); adegan per episode mengomposisinya. Adegan berulang pakai arg fase (`adegan:0.35`)
  supaya tidak identik antar beat.
- Zona aman satu master: teks/objek penting x 90-930, y 220-1500; kanan 150 px dari y≥800 = kolom
  tombol; bawah ±420 px = caption/akun. Subtitle garis dasar ±y 1400-1460, maks 2 baris, outline gelap,
  kata aktif warna merek. Teks kartu pertanyaan otomatis mengecil (`teks_pas`) supaya tidak terpotong.
- Selalu cek: lembar adegan (`render.py epN lembar`), frame 0 (hook sudah tampil, bukan hitam),
  momen reveal/twist, frame terakhir (loop), dan `cek_zona.py` bila ada.

## 7. QC sebelum kirim (semua genre)
1. Durasi sesuai genre; 1080x1920 30 fps; loudness −17..−19 LUFS; true peak ≤ −1 dBTP; mono aman.
2. Semua baris lolos jaga_suara.
3. Frame 0 = kejanggalan/lucu/menyentuh + teks hook ≤7 kata.
4. Lembar + zona: tidak ada teks penting terpotong atau di zona tombol/caption.
5. Tidak ada jeda >5 dtk tanpa kejadian baru; loop akhir→awal jalan.
6. Sampul dilihat mata: judul terbaca di ukuran kecil & potongan 3:4 dan 3:2.

## 8. Paket unggah (SELALU dibuat, tanpa diminta)
Aturan SEO & elemen FYP untuk hook, caption, judul, hashtag, dan pembacaan analitik: skill
`seo-fyp-animasi` (wajib dibuka bersama bagian ini).
`DESKRIPSI_EPn.md` (baris 1 = judul <100 karakter + 1-2 emoji = judul YouTube; 2-3 paragraf tanpa
membocorkan twist; ajakan A/B + KIRIM/TAG; 5 hashtag `#<seri>`+3 topik+`#fyp`; sumber untuk kisah nyata;
komentar pin) → tambah ke `CAPTION_SEMUA_EPISODE.md`; blok baru di `PROMPT_KOMENTAR_AI.md` (+ varian IG)
dengan format baku genre (lihat referensi); foto profil & bio hanya untuk serial baru.
Jadwal: `otomasi/buat_antrian.py <serial>` lalu `otomasi/jadwalkan.py <serial>` (SIMULASI dulu,
`--jalan` hanya setelah user setuju). Jam baku: YT & TikTok 11:30 WIB, IG 17:10 WIB, 1 video/hari/akun.
Antrian butuh per episode: `video`, `sampul`, `judul`, `deskripsi`, dan `prompt`.
**Sound pinjaman TIDAK dipakai** — putusan user 2026-11-10 sore, membatalkan putusan pagi di hari yang
sama. Alasannya praktis: Repliz tidak punya field sound dan sound hanya bisa dipasang manual lewat
picker audio aplikasi, sehingga seluruh unggahan tidak bisa lagi lewat API. Semua unggahan vertikal
tetap memakai musik sintesis sendiri yang sudah ada di master, dikirim otomatis lewat Repliz.
Jangan menawarkan sound pinjaman lagi kecuali user yang meminta.

## 9. Simpan pengetahuan
Tiap keputusan baru → perbarui `<seri>/SETELAN_SERI.md` & `<seri>/RENCANA_SERI.md` (tabel episode +
status ✅/🔨/⏳). Catat analitik user di "Pelajaran dari angka". Perbaikan pipeline yang terbukti jalan
→ kunci (jangan rombak struktur), dan masukkan ke `references/kualitas-animasi.md` skill ini.
