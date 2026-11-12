# Genre HOROR / misteri fiksi

Contoh serial: PENGUMUMAN DUKA (toa masjid), PIJAT TENGAH MALAM (tukang pijat tunanetra),
RUMAH SEBELAH, MALAM KETUJUH, SINTAS. Rujukan suara: `serial animasi kkn/KKN_Spesial_MalamKetujuh.mp4`.
Rujukan rasa (TEKNIK saja, jangan meniru tokoh/adegan/lagu/desain): Joko Anwar (Pengabdi Setan,
Perempuan Tanah Jahanam, Siksa Kubur) + Evil Dead Rise.

## Tema serial baru
Usulkan ±8 tema dari pekerjaan/benda sehari-hari Indonesia yang punya ATURAN & RUTINITAS (profesi,
alat, dokumen, bunyi khas); rutinitas yang dilanggar sedikit demi sedikit = mesin horor. Hindari yang
sudah dipakai serial lain atau pernah ditolak. Tiap tema: premis 2-3 kalimat + hook + benda benang
merah + bunyi penanda sosok + indera utama + ketakutan pribadi narator + sosok telur paskah.
Uji: hook paham tanpa suara dalam 2 dtk? 10 episode bisa lahir dari aturannya? Biarkan user memilih.

## Suara narator horor
- User mau cowok SERAM: `male, young adult/middle-aged, very low pitch` + arahan
  `deep raspy voice, sinister slow whisper, menacing and cold, telling a horror story at three in the
  morning, expressive intonation`. Calon "takut/gemetar" ~150 Hz dinilai kurang seram.
  Pilihan PENGUMUMAN DUKA & PIJAT: J (~105-115 Hz, seed 23); variasi 4-5 semiton = tidak datar.
- Tiga tahap dari suara dasar SAMA: `N` pembuka tenang; `N2` temuan (pelan, dekat, waspada);
  `N3` sesudah reveal (datar, hampa). Ref `_kerja/ref_narator_<X>_n1/n2/n3.wav` (nama baru = cache baru),
  pilih per baris `[N2] teks`. Bisikan `NB` hanya 1-3 baris/episode. Tag non-verbal (`[sigh]` dll) maks 1-3.
- Jeda bertingkat di naskah: `[ketuk]` ±0,25 dtk, `[jeda]` ±0,6-0,9, `[tahan]` ±1,2-1,8 sesudah reveal;
  ±6-10 penanda/episode; melambat SEBELUM bunyi penting, berhenti SESUDAHNYA. Tempo ±115-135 kpm.
- Baris kunci (hook/reveal/penutup) dibuat 3-5 versi (seed + tahap), audisi kecil, kunci `seed_khusus`.
- Olah vokal KERING per baris (`olah_vokal.py` ffmpeg): highpass 75 Hz; ±EQ 280 −2 dB bila berlumpur;
  +2 dB lebar di 3500 Hz; deesser ringan; proximity (EQ 140 +2,5 dB, −2 dB) hanya N2/NB; tanpa
  kompresor; gain linier per baris kecuali `[pelan]` −3 dB (baris terakhir hampir selalu).
- Room tone −58..−62 dBFS di jeda (jangan sunyi digital). Penutup lebih pelan dari kalimat sebelumnya.

## Naskah & rumus FYP horor (80-95 dtk, ±12 adegan, ±22-27 baris)
1. 0-2 dtk hook tiga lapis: gambar paling janggal di frame PERTAMA + teks ≤7 kata + kalimat kejanggalan
   konkret. Label "CERITA FIKSI" kecil di pojok. Pola terbukti: akhir dulu; kalimat "kamu"; aturan dilanggar.
2. 2-15 dtk bukti kejanggalan nyata + satu open loop besar + satu momen rutinitas NORMAL sebagai kontras.
3. Pattern interrupt tiap 3-5 dtk (ganti adegan/zoom kejut/bunyi khas/teks onomatope/cahaya berubah).
4. Eskalasi tiga langkah: janggal → salah → mustahil; detak jantung makin rapat.
5. Benda benang merah seri + SATU detail baru per episode.
6. Jump-scare halus + HENING TOTAL 0,9 dtk sebelum reveal; maks 1 jump-scare keras/episode.
7. Reveal (sub drop + sting + statis + glitch + goyang) lalu cliffhanger pertanyaan BARU; episode tetap
   utuh sendiri untuk penonton baru.
8. Loop: akhir menyambung ke detik 0 (jam/bunyi/tulisan sama). Kartu A/B hanya 1,5-2 dtk.
9. Telur paskah sosok di 3-5 adegan; pin komentar "detik berapa?"; pemicu KIRIM di caption ("kirim ke
   teman yang berani jaga malam"), bukan di video.

## Visual horor
Palet malam gelap + satu warna merek; kabut, bintik film, vinyet, lampu turun-tegangan acak; crossfade
0,4 dtk; badge lokasi+jam. Teknik uncanny murah: sesuatu HAMPIR normal (senyum terlalu lebar, kepala
miring sedikit, bayangan tidak ikut gerak, jam berhenti); artefak rekaman hanya di momen kunci; ruang
kosong terlalu sepi; siratkan jangan tampilkan. Narator POV (hanya tangan + senter/kunci) supaya aman
untuk suara apa pun. Lubang intip (fisheye lewat celah kecil, kamera diam) maks 1x/episode. Lokasi
terkurung dengan geografi jelas; ancaman dari luar bingkai. Gore disiratkan (bunyi/bayangan/noda).

## Gerak tokoh & lip-sync (vonis 9 Nov 2026, terkunci)
Wajah close-up Wagiman Ep6 (`kepala_wagiman`: senyum terlalu lebar, mata datar tidak ikut tersenyum,
bayangan di dinding tidak ikut menoleh) adalah acuan seram yang LOLOS mata user: jangan gambar ulang
wajah itu, setir hanya parameternya. Yang membuat seram menurut vonisnya: **mulut yang berbicara
mengikuti amplop suara** (lip-sync dari RMS baris dialog, parameter `lirik`) ditambah wajah itu; tokoh
yang mulutnya tertutup saat dialognya terdengar langsung terbaca mati dan jelek.
Sistem gerak terkunci (contoh kerja: `serial animasi/lab gerak/render_gerak.py` + `tokoh_gerak.py`):
pose dikunci per beat dengan anticipation lalu overshoot kecil sebelum settle, bukan loop sinus beku;
idle hidup terus-menerus (napas di bahu, kedip terjadwal tiap 2-6 dtk, lirikan pupil, micro-sway);
acting sinkron suara (menoleh ke sumber suara tepat saat baris toa mulai, alis naik di reveal);
follow-through benda (sapu/tangan berhenti terlambat ±0,5 dtk setelah badan); grammar kamera (push
pelan, snap-zoom 4 frame di puncak reveal, whip-pan 5 frame saat cut, handheld yang naik saat tegang,
freeze total saat HENING supaya sunyi kontras); CUT antar beat dalam lokasi yang sama, crossfade hanya
untuk pindah lokasi. Parameter tokoh: `senyum, menoleh, miring, kedip` bawaan + tambahan
`lirik, alis, px, py, napas_amp` (salinan berparameter di `lab gerak/tokoh_gerak.py`; defaultnya
menghasilkan gambar identik dengan art asli). Tiga arah gaya baru (kartun komik primitif, Blender toon
primitif, three.js) DITOLAK mata pada 9 Nov karena tokoh dari primitif kode tidak pernah lolos bar
matanya; jangan tawarkan ulang, dan jangan bangun pipeline penuh tanpa sampel kecil yang divonis dulu.

## Musik horor (gaya MALAM KETUJUH)
TANPA ducking/kompresor/limiter; narasi kering; satu gain linier ke −18 LUFS. Bahan: sub drop + pukulan
di detik 0; drone 30-60 Hz; disonansi (tritone/cluster) yang tidak resolve sampai reveal; detak jantung
makin cepat; bisikan tanpa kata; music-box sumbang = motif seri; sting, reverse swell, statis, lolongan,
jangkrik+angin (atau sunyi yang salah); efek khas tema. Stereo ITD ±0,3-0,6 ms untuk bisikan dekat satu
telinga; cek mono. Aransemen per nama adegan (`atur_umum()` + `arr_epN.py`); `kata()` untuk kunci waktu.

## Teknik sutradara (E2) yang paling sering dipakai
Bunyi penanda sosok (ep1-3 kondisikan, ep4+ balik aturannya); rekaman dalam dunia cerita yang
melambat/mundur di reveal; orang tersayang yang "berubah salah" (simpan untuk ep puncak); suara
kerasukan (nada turun di tengah kalimat, lapisan clip+crackle, dua nada di kata kunci, maju+reverse
bersamaan); bunyi presisi satu serangan per momen; ritme kamera lambat-lalu-cepat + potongan
tersembunyi saat lampu berkedip; kengerian dari ketakutan tokoh; tekstur taktil (noda, debu, tinta
meleber); kontras normal→salah; satu jeda manusiawi hangat sebelum babak akhir; satu kalimat penutup
yang mudah dikutip (`> kutipan:`).

## Batas aman
Horor di benda/kejadian, bukan ibadah/agama; disabilitas & profesi digambarkan hormat; tidak
meromantisasi menyakiti diri; aturan krisis 119 ext 8 / healing119.id wajib ada di prompt komentar.
