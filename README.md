# skills-suara-emosional

Kumpulan *skill* agent (Qoder / Claude Code) untuk memproduksi serial animasi vertikal
berbahasa Indonesia — format 9:16 untuk YouTube Shorts, Instagram Reels, dan TikTok.

> Agent skills for producing Indonesian vertical animation series: emotional TTS voice
> design, a layered-paper art style, and the end-to-end serial pipeline (script, render,
> music, QC, upload package).

Skill ditulis dalam Bahasa Indonesia karena seluruh naskah, caption, dan arahan produksinya
memang berbahasa Indonesia.

> **Agent AI yang membaca repo ini:** buka [AGENTS.md](AGENTS.md) lebih dulu. File itu berisi
> kontrak `$SERIAL_ROOT`, cara pasang ke tiap runtime, aturan isi yang tidak boleh dilanggar,
> dan daftar berkas yang dirujuk skill tetapi **sengaja tidak** ikut dipublikasikan.

> **Repo ini berisi pengetahuan, bukan tooling siap jalan.** Skill merujuk 31 berkas skrip;
> hanya 3 yang ada di sini (`serial-animasi/scripts/`). Mesin pipeline (`gen_suara.py`,
> `render.py`, `_mesin_omni.py`, `bangun.sh`, dst.) hidup di workspace produksi masing-masing
> dan tidak disertakan. Perintah pipeline di dalam skill tidak akan jalan dari repo ini.

## Isi repo

| skill | dipakai saat |
|---|---|
| [`suara-emosional-serial`](suara-emosional-serial/SKILL.md) | suara narator/tokoh terdengar datar, atau sebuah serial belum punya suara sama sekali. Isinya rantai 3 tahap: OmniVoice *voice design* → VoxCPM2 referensi emosional → OmniVoice kloning. |
| [`animasi-kertas-berlapis`](animasi-kertas-berlapis/SKILL.md) | membuat video bergaya diorama potongan kertas + cahaya emas (paralaks, senandung vokal tanpa alat musik). Lahir di serial KISAH PARA NABI. |
| [`serial-animasi`](serial-animasi/SKILL.md) | alur serial penuh lintas genre: naskah, suara, render pycairo 1080×1920, musik & efek sintesis, sampul, QC, paket unggah, penjadwalan. Genre dipecah ke `references/`. |

Pendukung di dalam `serial-animasi/`:

- `references/horor.md`, `lucu.md`, `sedih.md`, `kisah-nyata.md` — aturan per genre (durasi target, motif, batasan isi)
- `references/kualitas-animasi.md` — standar gambar & suara, wajib dibaca tiap build
- `references/mekanika-fyp.md`, `tren-format.md` — riset format yang sedang ramai dan cara membaca analitik
- `scripts/ytprobe.py` — ambil data publik YouTube (search + channel) tanpa login
- `scripts/outlier.py`, `thumbs.py` — bantu riset dan pratinjau sampul

## Cara pasang

Salin folder skill ke direktori skill runtime-mu:

```bash
cp -R suara-emosional-serial animasi-kertas-berlapis serial-animasi ~/.qoder/skills/
# atau untuk Claude Code:
cp -R suara-emosional-serial animasi-kertas-berlapis serial-animasi ~/.claude/skills/
```

Agent memuat skill berdasarkan field `description` di frontmatter, jadi tidak perlu
registrasi tambahan.

## `$SERIAL_ROOT`

Semua path di skill ini ditulis sebagai `$SERIAL_ROOT/...` dan **harus kamu ganti sendiri**
dengan akar folder kerjamu, misalnya:

```bash
export SERIAL_ROOT="$HOME/Documents/serial animasi"
```

Struktur yang diasumsikan skill:

```
$SERIAL_ROOT/
├── lab suara/
│   ├── venv/            # VoxCPM2 + faster-whisper
│   └── venv_omni/       # OmniVoice (terpisah, supaya bisa jalan bareng)
├── <nama serial>/
│   ├── proyek/          # bank_suara.json, gen_suara.py, render.py, musik.py, ...
│   ├── naskah/          # epN.md
│   ├── video/ sampul/ dokumen/ _kerja/
│   └── SETELAN_SERI.md  # keputusan serial: tokoh, warna, suara pilihan user
```

## Yang harus disiapkan sendiri

Skill ini berisi **pengetahuan dan resep**, bukan mesinnya. Berkas eksekusi
(`_mesin_omni.py`, `_mesin_vox.py`, `gen_suara.py`, `render.py`, `kertas.py`) hidup di folder
`proyek/` tiap serial dan tidak disertakan di sini.

Kebutuhan:

- macOS dengan Apple Silicon (OmniVoice & VoxCPM2 jalan di MPS)
- Model `k2-fsa/OmniVoice` dan `openbmb/VoxCPM2` — diunduh otomatis saat pertama dipakai
- `pycairo`, `numpy`, `scipy` untuk render; `ffmpeg` untuk mux
- Font **Poppins** di `~/Library/Fonts`
- `faster-whisper` model `small` untuk gerbang transkripsi

Dua proses OmniVoice tidak boleh jalan bersamaan karena berebut MPS — cek dulu dengan
`pgrep -fl _mesin`.

## Sorotan: resep suara cewek khidmat

Kasus produksi paling lengkap ada di `suara-emosional-serial` §"Resep terkunci", dipakai
serial KISAH PARA NABI untuk konten religi. Ringkasnya:

| tahap | mesin | parameter kunci |
|---|---|---|
| 1. suara dasar | OmniVoice | `instruct` `female, middle-aged, low pitch`, seed 8, speed 0.95 |
| 2. rasa khidmat | VoxCPM2 | arahan *warm reverent storyteller*, seed 7, cfg 2.0, ts 10 |
| 3. semua baris | OmniVoice kloning | ref tahap 2, `ref_teks` persis, seed 8, speed 0.90, num_step 32 |

Dua karakter narasi diproduksi dari **satu** referensi dengan beda `speed` saja (0.90 narasi
biasa, 0.84 momen puncak) — lebih murah daripada membuat referensi emosional kedua, dan
`speed` ikut kunci cache jadi keduanya punya cache terpisah.

Skill ini juga mencatat lima tuas emosi yang **terukur tidak berpengaruh** (prompt bernada
sedih, elipsis, `temp`, bootstrap, prompt gabungan panjang), supaya tidak ada yang mengulang
percobaan yang sudah buntu.

## Catatan

- Path lokal dan nama sudah disamarkan sebelum dipublikasikan.
- Handle kreator lain di `references/tren-format.md` dan `mekanika-fyp.md` adalah data riset
  publik (angka pembanding performa kanal), bukan akun milik penulis repo ini.
- `healing119.id` / 119 ext 8 yang disebut di `references/horor.md` adalah hotline krisis
  kesehatan jiwa Indonesia dan memang wajib ada di prompt komentar episode horor.

## Lisensi

[MIT](LICENSE)
