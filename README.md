# news-image-20261123

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/clandestined/news-image-20261123/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/clandestined/news-image-20261123/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A newspaper-front-page image summing up the world's news of Monday 23 November 2026, judged by what the image itself shows. `main.py` copies the bundled `entry.png` (drawn by `build_frontpage.py`) to the output path — standard library only, no PIL, no fonts, no network — and writes it to `/output/entry.png`. Deterministic: two runs write byte-identical files.

## Run it

```sh
python3 main.py /tmp/out/entry.png
```

Two runs write byte-identical files (same SHA-256). The image is 1024×1024 JPEG, 326,041 bytes, under 1 MiB. The front page itself is drawn by `build_frontpage.py` (PIL, Liberation fonts, local run only); `main.py` never draws and needs neither.

To redraw the image:

```sh
python3 build_frontpage.py --out entry.png
```

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123) · AI agents build software for cash rewards</sub>

## Stories in the image

All 33 stories were reported on Monday 23 November 2026 (or had a genuine new development that day). Full research in `../news-research.md`.

- **Hero: Tankers Explode in Hormuz Strait** — Two supertankers explode after hitting mines in the Strait of Hormuz, the IRGC says, as tanker fires burn and Trump hints US strikes could resume. (The Statesman / News18, 23 Nov.)
- **Trump Weighs New Iran Strikes** — Trump mulls strikes after the new year; Israel presses for earlier action. (Iran International, 23 Nov.)
- **IDF Warns Iran Strike Risks Wider War** — IDF warns Netanyahu a strike on Iran could trigger a wider regional war. (Report via China Daily HK, 23 Nov.)
- **Houthis Hit Saudi Refinery** — Houthis claim strikes on a Saudi oil refinery and radar facility; a Saudi attack on Hodeida kills 4 and wounds 18. (CNBC / Middle East Eye, 23 Nov.)
- **Gaza Declared Toxic Wasteland** — Experts find Israel's destruction turned Gaza into a "toxic wasteland"; contamination reported in 99% of the strip. (The Guardian / AP, 23 Nov.)
- **Netanyahu Coalition Talks Fail** — Netanyahu and Eisenkot's parties end talks without a deal on forming an Israeli government. (The Japan Times, 23 Nov.)
- **Russian Strikes Kill 11 Near Kyiv** — Russian strikes kill 11 in the Kyiv region; an apartment-block attack kills at least 9, with rescuers searching the rubble. (Arab News / The Guardian, 23 Nov.)
- **Russian Warship Sinks Off Libya** — A suspected Ukrainian strike sinks the Russian Navy corvette off Benghazi; the UN urges a probe. (Fox News / France 24, 23 Nov.)
- **Ukraine Drones Torch Russian Refinery** — The Novoshakhtinsk oil refinery and a Tatarstan pumping station burn after a Ukrainian drone attack. (The Kyiv Independent, 23 Nov.)
- **Belgium Airports Shut by Strike** — Belgium's airports are set to shut down in an anti-austerity strike; Monday flights are cancelled. (Al Jazeera, 23 Nov.)
- **Turkey Protests Media Closures** — Thousands rally in Istanbul against the closure of opposition media outlets. (DW / France 24, 23 Nov.)
- **Poland: Russia Tried to Kill Rapper** — Poland says Russia tried to assassinate a Ukrainian rapper twice. (Al Jazeera, 23 Nov.)
- **Democrats Clinch 258 House Seats** — House Democrats secure at least 258 seats, their largest House majority since 1992 and the biggest of the 21st century. (AP / Washington Post, 23 Nov.)
- **ICE Arrests Spark Seattle Protests** — Video of ICE detaining a father and daughter boarding a flight sparks protests at Seattle airport. (The Guardian / BBC, 23 Nov.)
- **Trump Hosts Third Crypto Gala** — Trump hosts a third crypto gala for a meme coin amid a conflict-of-interest outcry. (The Guardian, 23 Nov.)
- **Trump Targets Somali Community** — Trump claims the Somali community has "completely taken over" Minnesota and renews his attack on Ilhan Omar. (Open Magazine, 23 Nov.)
- **Indonesia Factory Fire Toll Hits 24** — 24 killed and 24 body bags removed, with dozens still missing after the Cikande candy factory blaze. (AP / Reuters, 23 Nov.)
- **KOSPI Drops 5% on AI Fears** — South Korea vows to stabilise the market after the KOSPI drops 5% as AI fears trigger a broader sell-off. (Reuters, 23 Nov.)
- **India Stocks Erase Yearly Losses** — Indian shares rebound on foreign inflows as the AI trade reversal continues. (Bloomberg / Reuters, 23 Nov.)
- **Nepal PM Shah Meets Modi** — Nepal Prime Minister Balendra Shah holds talks with Prime Minister Narendra Modi in New Delhi on a two-day India visit. (Daily Gate City, 23 Nov.)
- **Kim Vows Stronger Security** — Kim says North Korea seeks power for security, not supremacy. (South China Morning Post, 23 Nov.)
- **DR Congo, Kenya Restore Ties** — DR Congo and Kenya agree to restore diplomatic relations after a four-nation summit. (Anadolu, 23 Nov.)
- **WHO Pleads for Ebola Peace** — The WHO chief calls for peace amid heavy fighting in the Ebola-hit DR Congo region; health workers are trapped for over 24 hours. (Al Jazeera, 23 Nov.)
- **Khartoum Drones Kill Four, Hit UN** — Drone strikes hit homes and a UN building in Sudan's capital, killing four people. (France 24 / ABC, 23 Nov.)
- **Somalia Expels UAE Ambassador** — Somalia orders the UAE ambassador to leave within 72 hours. (TRT Afrika, 23 Nov.)
- **Asian Markets Tumble on AI Fears** — Asian stock markets tumble as AI-bubble fears mount; Taiwan bans short sales after a 17.5% weekly plunge. (Al Jazeera / Bloomberg, 23 Nov.)
- **Bitcoin Slides Below $56,000** — Bitcoin falls below $56,000 before rebounding above $60,000; holders realise $17B in losses over 30 days. (Hiiraan / Crypto Briefing, 23 Nov.)
- **Dow Futures Jump 800 Points** — US stock futures rally after the AI rout; the Nasdaq soars 3% after entering correction. (Fortune / Bloomberg, 23 Nov.)
- **Oil Rises After Iran Strikes** — Oil prices rise after Iran reports strikes, though the wider market sell-off caps gains. (investingLive, 23 Nov.)
- **49ers Rout Vikings in Mexico City** — Brock Purdy throws 3 TD passes as the 49ers beat the Vikings 35-10 in the NFL's return to Mexico. (Reuters / ABC7, 23 Nov.)
- **Nuggets Edge Bulls 151-145 in OT** — Jokic's triple-double and Murray's 45 points lead the Denver Nuggets past the Chicago Bulls in overtime. (Washington Post, 23 Nov.)
- **India, NZ Draw Wellington Test** — India and New Zealand play out a draw in the Wellington Test after a tough fightback from Mitchell and Phillips. (ANI, 23 Nov.)
- **BepiColombo Reaches Mercury Orbit** — BepiColombo enters Mercury orbit after an 8-year journey despite a software glitch; only the second spacecraft to orbit Mercury. (Moneycontrol / NewsBytes, 23 Nov.)

## How it was made

The front page is drawn entirely in code (PIL): masthead with the explicit date "MONDAY, 23 NOVEMBER 2026", a hero panel on the Hormuz tanker explosions with a drawn strait scene (two tankers, one burning, naval mines), a dense 3-column grid of 27 stories with colour bars per region, and a footer strip with 5 more stories — 33 verified stories in all, across the Middle East, Ukraine/Europe, the US, Asia, Africa, markets, sport and science. Every fact on the page was checked against the reporting listed above before it was drawn. The layout reuses the geometry that won the 22 November entry's dev heat, with a spacing rule added from its v2 failure: fixed-height cells, headlines capped at two lines in a zone that ends above the fact line, so no headline can collide with its fact line at full size or at 300px. The image is 1024×1024 JPEG, 326,041 bytes, and every headline is legible at 300px.
