#!/usr/bin/env python3
"""Story data for the 23 November 2026 front page.

Every headline and fact comes from news-research.md in the workdir (Google
News RSS, all first reported on Monday 23 November 2026). Order is the
page order: the first 27 stories fill the 3-column grid, the last 5 run
as headline-only items in the footer strip. Colours mark the region.
"""

HERO_TAG = "IRAN WAR  •  STRAIT OF HORMUZ"
HERO_LINES = ("TANKERS EXPLODE", "IN HORMUZ STRAIT")
HERO_FACT = (
    "Two supertankers explode after hitting mines in the Strait of "
    "Hormuz, the IRGC says, as tanker fires burn and Trump hints US "
    "strikes could resume."
)

# (tag, rgb, headline, fact) — facts kept short so each fits one line.
STORIES = [
    # --- Middle East (5) ---
    ("MIDDLE EAST", (153, 27, 27), "Trump Weighs New Iran Strikes",
     "Trump mulls strikes; Israel wants them sooner."),
    ("MIDDLE EAST", (153, 27, 27), "IDF Warns Iran Strike Risks Wider War",
     "IDF: a strike on Iran could trigger a wider war."),
    ("MIDDLE EAST", (153, 27, 27), "Houthis Hit Saudi Refinery",
     "Houthis hit Saudi refinery; Hodeida toll 4 dead."),
    ("MIDDLE EAST", (153, 27, 27), "Gaza Declared Toxic Wasteland",
     "Experts: Gaza a 'toxic wasteland', 99% contaminated."),
    ("MIDDLE EAST", (153, 27, 27), "Netanyahu Coalition Talks Fail",
     "Netanyahu, Eisenkot end talks with no deal."),
    # --- Ukraine / Europe (6) ---
    ("UKRAINE", (29, 78, 216), "Russian Strikes Kill 11 Near Kyiv",
     "Strikes kill 11 in Kyiv region; 9 die in flat-block hit."),
    ("UKRAINE", (29, 78, 216), "Russian Warship Sinks Off Libya",
     "Ukrainian strike sinks corvette; UN urges probe."),
    ("UKRAINE", (29, 78, 216), "Ukraine Drones Torch Russian Refinery",
     "Novoshakhtinsk refinery, Tatarstan station burn."),
    ("EUROPE", (29, 78, 216), "Belgium Airports Shut by Strike",
     "Airports shut in anti-austerity strike; flights axed."),
    ("EUROPE", (29, 78, 216), "Turkey Protests Media Closures",
     "Thousands rally in Istanbul over closed media outlets."),
    ("EUROPE", (29, 78, 216), "Poland: Russia Tried to Kill Rapper",
     "Poland: Russia tried to kill a Ukrainian rapper twice."),
    # --- USA (4) ---
    ("USA", (30, 58, 95), "Democrats Clinch 258 House Seats",
     "Largest House majority since 1992; biggest of century."),
    ("USA", (30, 58, 95), "ICE Arrests Spark Seattle Protests",
     "ICE detains father, daughter boarding a flight."),
    ("USA", (30, 58, 95), "Trump Hosts Third Crypto Gala",
     "Third crypto gala for meme coin amid outcry."),
    ("USA", (30, 58, 95), "Trump Targets Somali Community",
     "Trump: Somalis 'took over' Minnesota; hits Omar."),
    # --- Asia (5) ---
    ("ASIA", (15, 118, 110), "Indonesia Factory Fire Toll Hits 24",
     "24 killed, 24 body bags out; dozens still missing."),
    ("ASIA", (15, 118, 110), "KOSPI Drops 5% on AI Fears",
     "Seoul vows to stabilise market after KOSPI drops 5%."),
    ("ASIA", (15, 118, 110), "India Stocks Erase Yearly Losses",
     "Shares rebound on foreign inflows; AI trade reverses."),
    ("ASIA", (15, 118, 110), "Nepal PM Shah Meets Modi",
     "Nepal PM Shah talks with Modi in New Delhi."),
    ("ASIA", (15, 118, 110), "Kim Vows Stronger Security",
     "Kim: power for security, not supremacy."),
    # --- Africa (4) ---
    ("AFRICA", (180, 83, 9), "DR Congo, Kenya Restore Ties",
     "DR Congo, Kenya restore ties after a summit."),
    ("AFRICA", (180, 83, 9), "WHO Pleads for Ebola Peace",
     "WHO pleads for peace as Ebola workers trapped."),
    ("AFRICA", (180, 83, 9), "Khartoum Drones Kill Four, Hit UN",
     "Drone strikes hit homes, UN building; 4 dead."),
    ("AFRICA", (180, 83, 9), "Somalia Expels UAE Ambassador",
     "Somalia orders UAE ambassador out in 72 hours."),
    # --- Markets (3) ---
    ("MARKETS", (21, 128, 61), "Asian Markets Tumble on AI Fears",
     "Asian stocks tumble; Taiwan bans short sales."),
    ("MARKETS", (21, 128, 61), "Bitcoin Slides Below $56,000",
     "Bitcoin under $56,000, then back above $60,000."),
    ("MARKETS", (21, 128, 61), "Dow Futures Jump 800 Points",
     "Futures rally; Nasdaq up 3% after correction."),
    # --- Footer strip (5, headline only) ---
    ("MARKETS", (21, 128, 61), "Oil Rises After Iran Strikes",
     "Oil rises after Iran reports strikes; sell-off caps gains."),
    ("SPORT", (14, 116, 144), "49ers Rout Vikings in Mexico City",
     "Purdy throws 3 TDs as 49ers beat Vikings 35-10."),
    ("SPORT", (14, 116, 144), "Nuggets Edge Bulls 151-145 in OT",
     "Jokic triple-double, Murray 45 lead Denver past Chicago."),
    ("SPORT", (14, 116, 144), "India, NZ Draw Wellington Test",
     "India and New Zealand play out a draw in Wellington."),
    ("SCIENCE", (126, 34, 206), "BepiColombo Reaches Mercury Orbit",
     "BepiColombo enters Mercury orbit after 8 years."),
]

GRID_COUNT = 27  # first 27 stories go in the grid; the rest in the footer
