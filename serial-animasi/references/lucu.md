# Genre KOMEDI / lucu

Contoh serial: DINAS KEBETULAN (kantor rahasia yang mengatur "kebetulan"). Tujuan: penonton ketawa,
merasa "ini aku banget", lalu TAG/KIRIM ke teman dan cerita pengalamannya.
Rujukan rasa (TEKNIK saja): Looney Tunes/Chuck Jones, The Office, Edgar Wright, Mr. Bean, Bluey,
Agak Laen, Warkop DKI, teori benign violation.

## Tema serial baru
Usulkan ±8 konsep "dunia rahasia di balik hal sehari-hari" khas Indonesia (birokrasi, antre nomor,
formulir rangkap tiga, stempel biru, kipas rusak, anak magang). User menolak tema pasaran. Tiap konsep:
premis 2 kalimat + tokoh utama + pasangan kontras + aturan dunia 3 baris + contoh judul Ep1
("Kenapa kamu selalu ...?") + sasaran tag + pertanyaan komentar. Uji: gag utama paham TANPA suara?
10 episode lahir dari premis? Satu serial = satu ide berulang + benang merah misteri ringan sepanjang
musim (dibuka di Ep 10).

## Suara narator komedi
Narator = tokoh utama yang ngomong ke penonton ("aku"), DEADPAN: capek, datar, kering, diam-diam baik;
komedi dari kontras suara serius × situasi konyol. Tokoh sampingan lucu bicara lewat BALON TEKS saja
(jadi cukup satu suara). Arahan contoh: `(tired government office clerk, dry deadpan humor, casual,
comic timing)`. Pilihan DINAS KEBETULAN: bapak paruh baya ~147 Hz, seed 8, speed 1.0.
TIMING ADA DI JEDA: punchline datar seperti kalimat biasa; jeda 0,3-0,6 dtk SEBELUM punchline dan
tahan reaksi 0,5-1 dtk SESUDAHNYA; pecah setup & punchline jadi dua baris naskah (penanda `[jeda 0.5]`).

## Naskah & rumus FYP komedi (75-90 dtk, ±14 adegan, ±24 baris)
1. 0-2 dtk: teks hook + adegan relate yang SUDAH lucu di frame 0 (freeze + bunyi DEG!).
2. Kalimat pertama = tuduhan ke penonton: "Kamu pernah ...? Itu bukan kebetulan. Itu kerjaan saya."
3. Perkenalan tokoh + dunia rahasianya (satu kalimat lucu).
4. Proses lucu langkah demi langkah dengan ATURAN TIGA (dua membangun pola, ketiga mematahkan).
5. Kekacauan fisik (anak magang, kopi tumpah, kabel, panel konslet); GEOGRAFI diperlihatkan dulu
   (kabel/panel/cangkir) sebelum kecelakaan.
6. Twist hangat: kejadian "sial" ternyata untuk kebaikan si manusia.
7. Callback ke lelucon awal + benang merah muncul sekilas + kalimat menggantung.
8. Kartu FORMULIR KOMENTAR (pertanyaan pengalaman penonton) + ajakan TAG (`> tag:`).
9. Loop: gambar/kalimat terakhir menyambung frame 0.
Kepadatan: tawa kecil tiap ±4-6 dtk, tawa sedang tiap ±15 dtk, tawa terbesar di ±70-80% sebelum twist.
Hapus baris yang hanya menjelaskan. Mulai Ep2: bacakan 2-3 tebakan/komentar lucu penonton episode lalu.
Running gag wajib BERKEMBANG tiap episode (nomor antrean berubah, SP naik), bukan diulang persis.
Cek: baca baris 1-2 → orang asing berhenti menggulir? Baca punchline tanpa setup → masih lucu?
(kalau masih, setup kepanjangan).

## Visual komedi
Dunia rahasia (kantor dinding mint, tegel krem, neon berkedip, kipas rusak) vs dunia manusia terang
(merek GENERIK). Warna merek cerah (biru stempel, kuning map, merah, pink jodoh). Tokoh ekspresif
banyak mood; tokoh misterius cukup SILUET. Prinsip animasi: antisipasi, squash & stretch, gerak cepat
+ berhenti mendadak, hold reaksi 0,5-1 dtk lalu kedip datar; REAKSI > AKSI. Tatapan ke kamera datar
0,8-1,2 dtk tanpa musik, maks 1-2x/episode di momen paling absurd. Detail latar lucu untuk yang
menonton ulang (tulisan kecil di poster/formulir), 1-2 per episode. Komik: onomatope (DEG!, JEDUG!,
BYURR!), garis cepat, label panah, balon teks, stempel cap, freeze + label nama tokoh. Masuk/keluar
bingkai lucu ("there and back again"), transisi mencocokkan bentuk. Cek lembar TANPA subtitle: gag
utama harus tetap terbaca.

## Musik & efek komedi (112 BPM, disintesis sendiri)
Bass oom-pah pizzicato + akor pizz + bassoon nakal + woodblock/shaker; 2 birama awal tanpa melodi supaya
hook jelas. Suasana per adegan: kacau (minor cepat + timpani), roman (glockenspiel + pad), tegang
(tremolo + timpani), hangat (piano arpeggio), misteri (dengung + "dun dun DUNNN"). Musik BERHENTI di
freeze (record scratch), saat tokoh jatuh, dan saat tatapan ke kamera. Turunkan musik & naikkan efek di
momen gag. Efek kena TEPAT di frame kontak: bel ting-tong, langkah, scratch+hit, mesin tik+ding, stempel
JEDUG, kipas mati+desis, tuas KLAK, puff, buzzer salah, slide-whistle, ciprat, zap, sirene, boing GLEK,
seruput, laci, BRAK, jangkrik krik-krik (hening canggung), ding ide, peluit, rem mendecit, tepuk sepi,
trompet "wah-wah-wah", musik lift. Musik −10 dB di bawah narasi; −17 LUFS; ekor dipotong pas untuk loop.

## Teknik komedi (E2) yang paling sering dipakai
Aturan dunia tertulis di SETELAN_SERI (5-8 aturan; kejutan terbaik = satu aturan dilanggar jarang);
lebih MALU daripada sakit (korban lelucon = tokoh kita/birokrasi/nasib, bukan fisik/agama/suku/status
penonton); aturan tiga; callback & running gag berkembang; tatapan kamera + kontradiksi gambar
(narator bilang A, gambar tunjukkan kebalikan); potongan & bunyi tepat waktu gaya Edgar Wright; pasang
panggung sebelum gag; reaksi > aksi + jeda sebelum punchline; lucu tanpa suara; pasangan kontras
(deadpan + heboh + otoritas misterius); lelucon skala sehari-hari (mie instan akhir bulan, antre BPJS,
grup WA keluarga); kepadatan gag + satu momen tulus sebelum twist hangat; satire halus tanpa sasaran
nyata (kebiasaan birokrasi, bukan instansi/pejabat/partai/agama); alasan tag/kirim per episode.

## Batas aman
Tidak ada merek/instansi/pejabat/orang nyata; tidak ada politik; tidak ada humor SARA atau menghina
fisik/status penonton.
