# AGENTS.md

Ditulis untuk **agent AI** (Claude Code, Codex, Copilot CLI, Gemini CLI, Cursor, Qoder, atau
runtime lain) yang menemukan repo ini. Baca file ini SEBELUM memakai skill apa pun di dalamnya.

Manusia: [README.md](README.md) lebih cocok sebagai pengantar.

## Apa isi repo ini

Tiga *Agent Skill* — berkas `SKILL.md` ber-frontmatter YAML (`name`, `description`) mengikuti
spesifikasi [agentskills.io](https://agentskills.io/specification) — untuk memproduksi serial
animasi vertikal berbahasa Indonesia (9:16, YouTube Shorts / Instagram Reels / TikTok).

Seluruh isi skill berbahasa Indonesia karena naskah, caption, dan arahan produksinya memang
berbahasa Indonesia.

## Hal terpenting: ini PENGETAHUAN, bukan tooling yang bisa dijalankan

Skill di repo ini merujuk **31** berkas skrip. Hanya **3** yang ikut terbit, semuanya di
`serial-animasi/scripts/`:

| ada di repo | tidak ada di repo (28) |
|---|---|
| `ytprobe.py` — data publik YouTube tanpa login | `_mesin_omni.py`, `_mesin_vox.py` — pemanggil model TTS |
| `outlier.py` — bantu riset kanal | `gen_suara.py`, `jaga_suara.py`, `_selaras.py` — sintesis & gerbang suara |
| `thumbs.py` — pratinjau sampul | `render.py`, `kertas.py`, `adegan*.py`, `tokoh*.py` — gambar |
| | `timeline.py`, `musik.py`, `gabung.py`, `olah_vokal.py` — rakit video & audio |
| | `bangun.sh`, `rantai.sh`, `naskah_ke_lines.py`, `sampul.py`, `uji_*.py`, `jadwalkan.py`, dll. |

Berkas yang tidak ada itu hidup di folder `proyek/` tiap serial pada workspace produksi asli,
dan sengaja tidak dipublikasikan.

**Konsekuensi langsung — jangan diabaikan:**

- Jangan menjalankan `python proyek/gen_suara.py`, `bash bangun.sh epN N`, atau perintah pipeline
  lain dari dalam repo ini. Berkasnya tidak ada; perintahnya pasti gagal.
- Jangan menulis ulang mesin itu dari nol bermodal deskripsi di skill. Skill mencatat **resep,
  parameter, dan urutan kerja** — bukan implementasi. Menyalin resep ≠ punya mesin.
- Kalau tugas yang diminta adalah "buatkan episode" atau "perbaiki video", yang dibutuhkan adalah
  akses ke workspace produksi (`$SERIAL_ROOT`), bukan repo ini. Tegaskan itu ke user sebelum
  menghabiskan konteks.
- Yang aman dijalankan dari repo ini hanya tiga skrip di tabel kiri.

## Kontrak `$SERIAL_ROOT`

Semua path di dalam skill ditulis `$SERIAL_ROOT/...`. Repo ini **tidak** menyetel variabel itu dan
tidak bisa menebak nilainya. Sebelum mengikuti instruksi apa pun yang memuat path, tetapkan dulu
akar workspace-nya bersama user:

```bash
export SERIAL_ROOT="$HOME/Documents/serial animasi"   # contoh; tanyakan nilai sebenarnya
```

Struktur folder yang diharapkan skill ada di [README.md](README.md#serial_root).

## Cara memasang skill

Salin folder skill ke direktori skill runtime yang dipakai:

| runtime | direktori |
|---|---|
| Claude Code | `~/.claude/skills/` |
| Qoder | `~/.qoder/skills/` |
| lintas-runtime (Codex, Copilot CLI, Gemini CLI) | `~/.agents/skills/` |

```bash
cp -R suara-emosional-serial animasi-kertas-berlapis serial-animasi ~/.claude/skills/
```

Tidak perlu registrasi tambahan: runtime memilih skill dari field `description`. Karena itu
**jangan mengubah `name` atau `description`** tanpa sadar bahwa yang berubah adalah *kapan skill
ini dipicu*, bukan cuma labelnya.

Skill saling merujuk dengan nama (`serial-animasi`, `suara-emosional-serial`,
`animasi-kertas-berlapis`). Pasang ketiganya bersama, atau rujukan itu akan menggantung.

## Aturan yang tidak boleh dilanggar agent

Ringkasan dari dalam skill, diangkat ke sini karena ongkos salahnya besar:

1. **Konten religi (KISAH PARA NABI).** Sosok nabi, malaikat, dan Iblis **tidak pernah digambar** —
   diganti cahaya emas, berkas cahaya, atau nyala api gelap. Ucapan mereka disampaikan narator,
   tidak diperankan. Ayat ditulis sebagai **makna terjemahan** disertai nomor surat, bukan kutipan
   kata per kata. Sumber hanya Al-Qur'an dan hadis sahih; riwayat lemah/israiliyat tidak dipakai.
   Prompt balasan komentar dilarang memberi fatwa, menghukumi ibadah orang, atau ikut debat
   mazhab/aliran — arahkan pertanyaan hukum ke ustaz atau sumber berkompeten.
2. **Narasi tanpa gaung.** `basah`/reverb tidak pernah disetel untuk suara narator. Gaung hanya
   untuk senandung dan musik latar.
3. **Jangan audisi ulang suara yang sudah dikunci user.** Resep beserta parameter persisnya ada di
   `suara-emosional-serial` §"Resep terkunci". Pemilihan suara adalah keputusan **telinga user**,
   bukan rekomendasi angka — dan ia konsisten memilih yang lebih tenang, bukan yang paling
   ekspresif.
4. **Jangan mengulang lima tuas emosi yang sudah terukur buntu**: prompt bernada sedih, elipsis
   `...`, `temp`, bootstrap, dan prompt gabungan panjang. Angkanya ada di skill.
5. **Satu proses OmniVoice pada satu waktu** — dua proses berebut MPS. Cek `pgrep -fl _mesin`
   sebelum memulai, tunggu dengan `kill -0 PID`, dan **jangan pernah membunuh job serial lain**.
6. **`ref_teks` harus persis.** Di `bank_suara.json`, `ref_teks` wajib sama huruf demi huruf dengan
   kalimat pada berkas referensi. Meleset sedikit → kloningan melenceng. Mengganti `ref` atau
   `speed` juga membatalkan cache suara, jadi siapkan waktu sintesis ulang.

## Repo ini salinan yang disamarkan

Salinan yang benar-benar dimuat agent di mesin pemilik repo adalah `~/.qoder/skills/` dengan path
asli. Repo ini salinan **publik** yang sudah disamarkan:

- `/Users/<nama>/Documents/serial animasi` → `$SERIAL_ROOT`
- nama pemilik → `user`

Karena itu:

- Jangan "mengembalikan" path asli ke repo ini.
- Jangan menganggap perubahan di repo ini otomatis berlaku di mesin asalnya, atau sebaliknya.
  Keduanya salinan terpisah yang harus disinkronkan manual.
- Yang **sengaja tidak** disamarkan dan jangan dibersihkan: handle kreator lain di
  `references/tren-format.md` dan `references/mekanika-fyp.md` (data riset publik berupa angka
  pembanding kanal), `healing119.id` / 119 ext 8 di `references/horor.md` (hotline krisis kesehatan
  jiwa Indonesia, wajib ada di prompt komentar episode horor), dan `Repliz` (nama alat penjadwal
  unggah, bukan kredensial).

## Bahasa dan gaya

Balas user dalam Bahasa Indonesia santai. Pertahankan istilah teknis, nama parameter, dan nama
berkas dalam English apa adanya — jangan diterjemahkan.

## Lisensi

[MIT](LICENSE) — © 2026 Julianarwansah
