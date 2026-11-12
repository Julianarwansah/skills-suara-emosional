---
name: suara-emosional-serial
description: Make an animated-series narrator/character voice sound emotional (sad, scared, happy, reverent) instead of flat, or design a brand-new narrator voice for a serial that has none yet, using OmniVoice voice design + VoxCPM2 emotional reference + OmniVoice cloning on the user's Mac.
---

# Suara emosional untuk serial animasi (cara "D")

Dipakai saat user bilang suara narator/tokoh di salah satu serialnya "datar", "nggak ada nada sedih/tinggi/sedang", atau minta suara lebih sedih / takut / senang / sesuai suasana. Ditemukan & disetujui user 2026-11-02 di serial ANAK SULUNG (audisi emosi, pilihan D).

## Kenapa suara jadi datar
OmniVoice (k2-fsa/OmniVoice) TIDAK punya pengatur emosi. Intonasinya hampir sepenuhnya meniru rekaman referensi kloning. Referensi datar -> semua baris datar. Yang sudah diuji dan TIDAK cukup:
- Setelan OmniVoice lebih bebas (class_temperature 0.6, position_temperature 8, guidance_scale 2.5) + `[sigh]` + jeda "...": variasi nada malah turun (1,6 st).
- VoxCPM2 langsung dengan arahan emosi untuk tiap baris: variasi tidak naik (1,8 st) dan bicaranya jadi cepat; juga lambat dan mengantre VoxCPM serial lain.

## Cara yang dipakai (D)
1. VoxCPM2 mengkloning suara tokoh yang SUDAH dipilih user, dengan awalan arahan emosi berbahasa Inggris, untuk SATU kalimat referensi baru yang isinya sesuai emosi (6-8 detik). Hasil: `_kerja/ref_<tokoh>_<emosi>.wav`.
2. Referensi emosional itu dipakai sebagai `ref` OmniVoice di `bank_suara.json` (ganti `ref` dan `ref_teks` persis kalimat referensi baru). Seluruh episode tetap dibuat OmniVoice: cepat, bisa jalan bareng VoxCPM, warna suara tetap sama, tapi intonasinya ikut emosional.
Hasil uji ANAK SULUNG: variasi nada 1,8 -> 2,5 semiton, rentang 6,1 -> 7,8 st; transkripsi tetap benar.

## Resep terkunci: suara cewek khidmat (KISAH PARA NABI, disetujui user 2026-11-10)

Kasus produksi lengkap untuk konten religi. Pakai ulang, **jangan audisi ulang**.
Bedanya dari cara D di atas: serial ini belum punya suara tokoh pilihan user, jadi rantainya
dimulai dari **voice design OmniVoice** (`instruct`, tanpa referensi) -> 3 tahap, bukan 2.

| tahap | mesin | parameter |
|---|---|---|
| 1. suara dasar | OmniVoice | `instruct` `female, middle-aged, low pitch`, seed 8, speed 0.95, teks netral 1 kalimat |
| 2. rasa khidmat | VoxCPM2 | `desain` = arahan khidmat di §Langkah 3, seed 7, cfg 2.0, ts 10, `ref` = keluaran tahap 1 |
| 3. semua baris | OmniVoice kloning | `ref` = keluaran tahap 2, `ref_teks` PERSIS kalimat tahap 2, seed 8, num_step 32, speed 0.90, dtype float16, bersihkan 0.5 |

Identitas terpilih = calon **E, "ibu dewasa, nada rendah"** — satu-satunya cewek dari 5 calon
(A/B/D cowok dewasa-muda, C kakek bijak). User lagi-lagi memilih yang paling tenang, bukan yang
paling ekspresif.

Produksi di `proyek/bank_suara.json`: dua karakter dari SATU referensi.
- `N` speed **0.90** = narasi biasa
- `N2` speed **0.84** = momen Iblis / puncak

**Tuas murah yang terbukti:** beda `speed` dari referensi yang sama sudah cukup menandai momen
puncak — tidak perlu referensi emosional kedua, hemat satu antrean VoxCPM2 (~3 menit muat model).
`speed` ikut kunci cache `gen_suara.py`, jadi N dan N2 punya cache terpisah; mengganti speed satu
karakter tidak membatalkan cache karakter lain.

`basah` (gaung) sengaja TIDAK disetel: narasi tanpa reverb. `bersihkan` 0.5 = noisereduce dengan
profil derau dari 25% frame paling sepi di baris itu sendiri.

Yang bisa disalin: `serial animasi kisah nabi/proyek/audisi_narator.py` (audisi 5 calon 3 tahap +
gabung tit), `_kerja/audisi/` (wav per calon), `dokumen/AUDISI_NARATOR.mp3` (berkas dengar),
`_kerja/ref_narator_E.wav` (referensi terkunci).

## Lingkungan (Mac user)
- Akar: `$SERIAL_ROOT/`
- OmniVoice: `lab suara/venv_omni/bin/python` + `_mesin_omni.py` (salinan terbaru di `serial animasi anak sulung/proyek/`, sudah mendukung payload `gen` dan tag `[sigh]`).
- VoxCPM2: `lab suara/venv/bin/python` + `serial animasi ruang pikir/proyek/_mesin_vox.py` (payload: jobs[{nama, teks, desain, seed, ref, out}], model `openbmb/VoxCPM2`, cfg 2.0, ts WAJIB 10, sr 44100). Muat model ~3 menit, ~50-75 dtk per kalimat.
- Render/numpy: `animasi fun fact/_env/venv/bin/python`.
- Transkripsi cek: faster-whisper `small` di `lab suara/venv`.
- Cek dulu `pgrep -fl "_mesin_vox|_mesin_omni"`; kalau VoxCPM serial lain sedang jalan, beri tahu user (bisa antre).

## Langkah
1. Baca `proyek/bank_suara.json` serial itu: catat `ref` dan `ref_teks` tokoh yang dikeluhkan.
2. Tulis `proyek/audisi_emosi.py` (contoh lengkap: `serial animasi anak sulung/proyek/audisi_emosi.py`). Isinya 4 calon, 2 kalimat uji dari naskah yang paling emosional:
   - A = versi sekarang (patokan)
   - B = OmniVoice setelan ekspresif (boleh dilewati, hasilnya biasanya tidak lebih baik)
   - C = VoxCPM2 + arahan emosi langsung
   - D = OmniVoice dari referensi emosional buatan VoxCPM2 (cara utama)
   Gabungkan jadi `_kerja/AUDISI_EMOSI.wav` dengan bunyi tit 1x..4x sebelum tiap calon.
3. Arahan emosi (awalan teks VoxCPM, dalam kurung, bahasa Inggris), contoh:
   - sedih: `(young woman, very sad, trembling voice holding back tears, speaking softly and slowly, with emotion) `
   - takut/horor: `(young man, scared, whispering nervously, breathing unevenly, tense) `
   - senang: `(cheerful, warm smile in the voice, lively and bright, expressive) `
   - khidmat/religi: `(middle-aged woman, warm reverent storyteller telling a sacred story, calm, full of awe and tenderness, slow pace with meaningful pauses, expressive natural intonation) `
   Sesuaikan gender/usia dengan tokoh. Kalimat referensi baru harus bernada emosi yang sama dan berbahasa Indonesia natural.
4. Jalankan dengan nohup + log, pantau log. Lalu cek tiap calon:
   - transkripsi faster-whisper (semua kata harus ada)
   - ukur nada dengan librosa.pyin (fmin 80, fmax 500): median Hz, std semiton terhadap median, rentang p5-p95. Makin besar std/rentang = makin tidak datar. Juga durasi (C sering terlalu cepat).
5. Beri user AUDISI_EMOSI.wav + tabel singkat (cara, variasi nada, catatan) dan rekomendasi. User yang memutuskan dengan telinga.
6. Setelah user memilih D: ubah `bank_suara.json` -> `ref` = referensi emosional, `ref_teks` = kalimatnya PERSIS, tulis catatan pilihan + tanggal di `_komentar`. Jangan tambah gaung/reverb (user tidak suka gema). Build ulang episode (cache suara otomatis tidak terpakai karena ref berubah).
7. Bisa punya beberapa emosi dalam satu serial: buat entri karakter terpisah (mis. `S` biasa, `S_SEDIH`, `S_TAKUT`) masing-masing dengan referensi emosinya, lalu pilih per baris di naskah dengan `[S_SEDIH] teks...` atau `> suara: S_SEDIH`.

## Catatan
- Referensi emosional sedih cenderung menaikkan nada dasar sedikit (240 -> 280 Hz pada suara cewek), terdengar seperti menahan tangis; itu wajar.
- Kalau satu baris terdengar aneh, ganti seed baris itu saja; baris lain diambil dari cache.
- Bicara ke user dalam Bahasa Indonesia santai, beri tahu cara memilih audisi (jumlah tit).
