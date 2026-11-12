# Genre KISAH NYATA / sejarah / dokumenter

Contoh serial: KISAH NYATA NUSANTARA (satu kisah nyata Indonesia per episode, 60-95 dtk, narator
pencerita dokumenter hangat & tenang). BEDA dari genre lain: ini NYATA dan DIRISET, bukan fiksi.

## Aturan fakta (keras, tidak bisa ditawar)
- Tiap nama, tanggal, dan angka di naskah WAJIB dicek minimal 2 sumber independen. Tulis sumber di
  kepala `naskah/epN.md` dan di deskripsi. Kutipan hanya yang memang tercatat (boleh diterjemahkan);
  JANGAN mengarang dialog.
- Sebelum menulis naskah, buat `dokumen/riset_epN.md`: ringkasan 3 kalimat, garis waktu bertanda sumber,
  tabel angka kunci (angka | arti | sumber; yang cuma 1 sumber ditulis "jangan dipakai"), kutipan
  tercatat, detail manusiawi untuk divisualkan, daftar sumber ber-URL, daftar yang TIDAK boleh dipakai
  (mitos populer, angka salah kutip, detail sadis, hal yang masih diperdebatkan), usulan hook + kalimat
  pertama. Riset bisa didelegasikan ke subagent (web search), satu agen per 2-3 episode.
- Angka yang bertentangan antar sumber: pakai rentang atau frasa "sekitar/lebih dari", jangan angka
  tunggal yang seolah pasti. Angka populer tapi keliru wajib masuk daftar larangan (contoh nyata:
  88.000 korban Tambora, 90.000 tewas global 1816, 46 m tsunami Merak, kaus Martunis nomor 7).
- Hindari: kisah yang masih jadi sengketa politik, korban hidup tanpa liputan publik, detail sadis,
  gambar wajah orang nyata yang mirip foto (tokoh digambar kartun sederhana).

## Rumus episode (supaya FYP tapi tetap enak didengar sampai akhir)
1. Teks hook layar 0-3 dtk berisi angka/fakta paling mengejutkan (kotak kuning arsip); kalimat pertama =
   momen paling aneh, bukan intro. Clickbait boleh kuat SELAMA setiap angkanya lolos verifikasi dan isi
   video membayar janji hook di 5 detik pertama.
2. Kilas balik sepia untuk masa lalu (`> sepia:`), warna penuh untuk masa kini/penutup.
3. Detail kecil yang konkret (simpul tali, memasak saat gelap, air hujan di lekukan kayu): itu yang
   membuat penonton percaya & ikut merasa.
4. Twist manusiawi di 3-4 adegan terakhir (istri menikah lagi; kaus ternyata nomor 10; cincin bertuliskan
   nama istri).
5. Stempel "KISAH NYATA" + peta lokasi + rentang tahun (adegan `stempel` membaca meta
   `lokasi/rentang/pin/peta_sorot`).
6. Kartu pilihan A/B atau pertanyaan terbuka untuk komentar; pin komentar berisi fakta tambahan
   terverifikasi; ajakan follow.
7. Narasi hangat & mengalir: jangan jadi daftar fakta; pasang angka di layar (adegan `angka`
   `ANGKA;;LABEL;;SUB` dihitung naik) dan biarkan narasi bercerita.

## Visual dokumenter hangat
Gaya kartun sederhana; warna merek kuning arsip #F2B544; label atas "K I S A H   N Y A T A   N U S A N T A R A";
bintik film + vinyet; badge lokasi+tahun kiri atas; tahun besar untuk penanda waktu; kartu dokumen
(koran/berkas laporan + cap) untuk bukti; peta Indonesia stilasi dengan pin & cincin suara untuk jarak.
Komponen pakai ulang hidup di `proyek/pustaka_kn.py` (peta+proyeksi, `orang()` generik, gunung api,
kolom abu, tsunami, kapal, rakit rompong, kartu dokumen); adegan per episode mengomposisinya dengan arg
fase supaya beat berulang tidak identik.

## Suara & musik
Narator cowok dewasa nada rendah (~140-155 Hz), pencerita dokumenter hangat; voice design
`male, middle-aged, low pitch` → VoxCPM2 `(warm calm documentary storyteller, gentle and slightly sad,
slow pace)` → ref → OmniVoice kloning; speed ~0.9; TANPA gaung. Maks ±12 kata/baris; angka diucapkan
huruf. Musik mode `kisah`: piano+pad+strings 60 BPM −10 dB; efek per adegan (gemuruh letusan, ombak,
burung hutan, kapak, api+jangkrik, dentum angka, desir kertas+stempel, klakson kapal, kerumunan+klik
kamera untuk press/pertemuan); riser masuk adegan bencana, swell masuk penutup.

## Paket unggah
DESKRIPSI: baris 1 judul Shorts + 1-2 emoji; 2-3 paragraf; ajakan A/B; 5 hashtag (`#kisahnyata` + 3 topik
+ `#fyp`); baris SUMBER wajib; komentar pin = fakta tambahan terverifikasi. Blok prompt balas komentar
wajib menyertakan "FAKTA PENDUKUNG" dari riset dan larangan mengarang fakta.

## Pelajaran produksi sesi 2026-11-05
- Delegasi riset (4 agen paralel) + tulis adegan sendiri = paling hemat konteks; subagent adegan pycairo
  cenderung kehabisan konteks, jadi adegan ditulis di thread utama.
- Build berurutan lewat `rantai.sh`; suara di-cache sehingga render ulang murah; QC lembar per episode
  lalu perbaiki di level komponen, bukan per adegan.
- Venv render bersama bisa hilang tanpa kabar: cek path venv sebelum build massal (lihat
  `references/kualitas-animasi.md` §6).
