# Hardrive — Deep Inside: raw analysis notes

**Status (2026-11-15): audio analysed by signal processing, not by ear.** There is no audio playback/listening tool in this session, so nothing here is a perceptual description. I read the uploaded MP3's ID3 tags and ran numeric analysis (librosa 1.0.1 in a throwaway virtualenv). Everything below is machine-derived or from tags; instrumentation, vocals and lyrics are NOT identified.

## Uploaded file

- **File:** `0008_-_Deep_Inside.mp3` — MPEG Layer III, 44.1 kHz stereo, 320 kbps, 15,776,748 bytes, duration **392.67 s (6:32.7)**.
- **ID3 tags:** Title `Deep Inside`; Artist/Album artist `Hardrive`; Album **`Deep Inside (Remixes)`**; Track 3/8, disc 1/1; Genre Dance/Electronic; Copyright `(c) 2015 Strictly Rhythm Records`; Year 2015.
- **Correction to earlier note:** the album tag shows this is a track from a **2015 remixes release**, so it is most likely a *remix*, not the 1993 Original (6:28) or Dub (5:14). The earlier "probably the Original" guess from runtime was wrong. Which remix it is is not stated in the tags (the title carries no remixer/version).

## Machine-derived measurements

- **Tempo:** librosa beat tracker and tempo estimate both give **~123.0 BPM** (resolution is coarse; consistent with the ~124 BPM in the repository notes).
- **Key:** Krumhansl-Schmuckler on whole-track chroma ranks E major (r≈0.31), A major (0.26), G# minor (0.23), A minor (0.21). The top scores are weak and close together and **do not confirm B minor**; treat key as inconclusive (long chroma average of a layered house track is unreliable).
- **Structure (energy per ~15.5 s ≈ 8 bars at 124 BPM; RMS, spectral centroid, share of energy below 150 Hz):**

| Time | RMS | Centroid Hz | <150 Hz |
|---|---|---|---|
| 0:00 | 0.141 | 3474 | 0.00 |
| 0:15 | 0.184 | 3398 | 0.10 |
| 0:31 | 0.191 | 3252 | 0.10 |
| 0:46 | 0.250 | 2704 | 0.14 |
| 1:02 | 0.265 | 2641 | 0.14 |
| 1:17 | 0.254 | 2957 | 0.13 |
| 1:33 | 0.252 | 2922 | 0.12 |
| 1:48 | 0.222 | 2544 | 0.09 |
| 2:04 | 0.252 | 2901 | 0.12 |
| 2:19 | 0.264 | 2844 | 0.13 |
| 2:35 | 0.245 | 2851 | 0.14 |
| 2:50 | 0.161 | 2823 | 0.10 |
| 3:06 | 0.240 | 2978 | 0.13 |
| 3:21 | 0.238 | 2899 | 0.16 |
| 3:37 | 0.247 | 3113 | 0.14 |
| 3:52 | 0.245 | 3009 | 0.14 |
| 4:08 | 0.168 | 3088 | 0.04 |
| 4:23 | 0.245 | 2971 | 0.12 |
| 4:39 | 0.251 | 2925 | 0.12 |
| 4:54 | 0.227 | 2087 | 0.16 |
| 5:10 | 0.218 | 2153 | 0.18 |
| 5:25 | 0.202 | 3393 | 0.15 |
| 5:41 | 0.176 | 3662 | 0.10 |
| 5:56 | 0.163 | 3366 | 0.04 |
| 6:12 | 0.158 | 3375 | 0.00 |
| 6:27 | 0.026 | 1888 | 0.00 |

- **Reading of the numbers (inferred, not heard):** a bass-free intro (<150 Hz ≈ 0 for the first ~15 s), bass/low end entering by ~0:15, the loudest/fullest section around 0:46–1:33, dips in low end and level near 2:50 and 4:08 (probable breakdowns, the 4:08 one nearly bass-free), a bass-heavy stretch around 4:54–5:25, then a progressive strip-back to a low-end-free outro from ~6:12 and silence at the end. Section boundaries are 15.5 s windows, so exact bar positions are unknown.

## Not determined

Instrumentation, which remix this is, vocal content/lyrics, hook notes, bassline pitches, drum pattern. These would need actual listening or a transcription/source-separation tool.

## Earlier access attempts (all unsuccessful)

YouTube, SoundCloud, Bandcamp and Spotify pages failed with `ERR_BLOCKED_BY_CLIENT`; web-fetch of SoundCloud, Bandcamp and Insomniac failed on DNS.

## Source/repository notes (not from the audio)

- Hardrive is a project associated with Louie Vega; *Deep Inside* EP, Strictly Rhythm SR EP2, 1993 (Original 6:28, Dub 5:14, per Discogs). 124 BPM and B minor are database/contributor figures per the repo notes.
- Vocal reportedly sampled from Barbara Tucker's "Beautiful People" (Insomniac, via repo notes).
- [jonty_first_track.md](https://github.com/threadkeeper/roland-mc303-notes/blob/119af77c63ad53365b90d77796e8ecc48cb478b/jonty_first_track.md) is a model inspired by the track, not a transcription.
- Discogs: https://www.discogs.com/release/20174-Hardrive-Deep-Inside · diggerdigger: https://diggerdigger.com/track/hardrive-deep-inside/ · Insomniac: https://www.insomniac.com/music/from-the-crate-hardrive-deep-inside/
