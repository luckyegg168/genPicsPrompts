"""Preset templates for characters, stories, and styles."""
from __future__ import annotations

# ── Character Templates (10) ──────────────────────────────────────────────────

CHARACTER_TEMPLATES: list[dict] = [
    {
        "label": "🗡 東方俠女",
        "name": "Yuki",
        "description_en": (
            "a young East Asian swordswoman, long black hair tied back with a jade pin, "
            "wearing a dark navy hanfu with silver trim, sharp determined eyes, slender athletic build, "
            "a katana strapped to her back"
        ),
        "description_zh": "東方年輕女俠，黑髮以玉簪盤起，深藍銀邊漢服，眼神堅定，身材矯健，背負長刀",
        "style": "wuxia cinematic photography, dramatic rim lighting, highly detailed, 8k, film grain",
    },
    {
        "label": "🤖 賽博龐克偵探",
        "name": "Cipher",
        "description_en": (
            "a cyberpunk detective in his mid-30s, short silver undercut hair, "
            "glowing red cybernetic eye implant, wearing a long black trench coat, "
            "stubble, cigarette between fingers, rain-soaked"
        ),
        "description_zh": "30多歲賽博龐克偵探，短銀髮，發光紅色義眼，黑色長風衣，鬍渣，手夾菸，全身濕透",
        "style": "cyberpunk neon noir, blade runner aesthetic, rain reflection, teal & orange grade, 8k",
    },
    {
        "label": "🌿 末世倖存者",
        "name": "Ash",
        "description_en": (
            "a post-apocalyptic survivor in their mid-20s, sun-weathered tan skin, "
            "red bandana around neck, patched leather jacket with faction badges, "
            "fierce emerald green eyes, carrying a worn military backpack"
        ),
        "description_zh": "20多歲末世倖存者，風化古銅膚色，紅頭巾，補丁皮夾克帶派系徽章，凌厲翠綠眼，背舊軍包",
        "style": "post-apocalyptic gritty realism, dusty haze, desaturated warm tones, cinematic 8k",
    },
    {
        "label": "🧙 異界法師",
        "name": "Aldric",
        "description_en": (
            "an ancient arcane mage, long silver-white beard, deep-set violet glowing eyes, "
            "wearing a midnight blue star-embroidered robe, a gnarled wooden staff with a swirling "
            "orb of energy, mysterious runic tattoos on hands, tall and slightly stooped with age"
        ),
        "description_zh": "古老奧術法師，長銀白鬍，深陷紫色發光眼，午夜藍星紋長袍，扭曲木杖頂端能量球，手上神秘盧恩紋身，高挑略顯老態",
        "style": "dark fantasy cinematic, magical particle effects, volumetric light, deep shadow contrast, 8k HDR",
    },
    {
        "label": "👘 大正浪人",
        "name": "Kenzo",
        "description_en": (
            "a weathered ronin from Taisho-era Japan, messy dark hair held loosely, "
            "wearing a worn grey kimono over battle-scarred armor plates, "
            "piercing dark eyes carrying a lifetime of loss, two swords at waist, wooden geta sandals"
        ),
        "description_zh": "大正時代風霜浪人，凌亂深色頭髮隨意束起，磨損灰色和服配戰痕護甲，眼神深邃承載一生滄桑，腰佩雙刀，木屐",
        "style": "feudal Japan historical photography, sepia-warm tones, soft bokeh, Akira Kurosawa aesthetic, 8k",
    },
    {
        "label": "🦅 荒野獵人",
        "name": "Raven",
        "description_en": (
            "a rugged wilderness hunter in their late 30s, chiseled jaw, dark copper skin, "
            "long braided black hair with eagle feathers, wearing a fur-trimmed buckskin jacket, "
            "a recurve bow slung on shoulder, intense hawk-like amber eyes scanning the horizon"
        ),
        "description_zh": "30多歲粗獷荒野獵人，稜角分明的下顎，深銅膚色，帶鷹羽的黑色長辮，毛邊鹿皮夾克，肩背返弓，銳利琥珀眼眺望地平線",
        "style": "wilderness epic photography, golden hour backlighting, wide cinematic landscape, 8k National Geographic",
    },
    {
        "label": "🎭 維多利亞偵探",
        "name": "Evelyn",
        "description_en": (
            "a sharp-witted Victorian-era female detective in her late 20s, auburn hair pinned up "
            "under a wide-brimmed hat, wearing a dark burgundy tailored coat, leather gloves, "
            "magnifying glass in hand, bright calculating grey eyes, London fog swirling behind"
        ),
        "description_zh": "20多歲機智維多利亞女偵探，栗紅髮盤於闊邊帽下，深酒紅剪裁大衣，皮革手套，手持放大鏡，明亮灰色算計的眼神，倫敦霧氣縈繞身後",
        "style": "Victorian gothic atmosphere, gaslight warm amber, foggy London streets, film noir inspired, 8k",
    },
    {
        "label": "🌊 海洋指揮官",
        "name": "Marcus",
        "description_en": (
            "a commanding naval officer in his early 40s, salt-and-pepper beard, "
            "deep blue captain's uniform with gold epaulettes, weathered leathery skin, "
            "storm-grey eyes, standing at the bow of a warship as storm waves crash around"
        ),
        "description_zh": "40多歲威嚴海軍指揮官，胡椒鹽色鬍渣，深藍船長制服配金色肩章，風霜皮膚，暴風灰眼，站在戰艦船頭，風暴巨浪四起",
        "style": "maritime epic photography, stormy ocean atmosphere, dramatic contrast lighting, salt spray particles, 8k",
    },
    {
        "label": "🌸 現代刺客",
        "name": "Mei",
        "description_en": (
            "a lethal modern assassin woman in her mid-20s, sleek black tactical suit, "
            "short-cut dark hair with a single cherry blossom tucked behind ear, "
            "cold calculating almond eyes, twin daggers at hip, urban rooftop setting at night"
        ),
        "description_zh": "20多歲致命現代女刺客，光滑黑色戰術服，短黑髮耳後別一朵櫻花，冰冷計算的杏眼，雙腰刀，深夜都市屋頂",
        "style": "stealthy urban cinematic, cool blue midnight tones, neon highlights, rain-slicked surfaces, 8k",
    },
    {
        "label": "🪐 星際工程師",
        "name": "Nova",
        "description_en": (
            "a futuristic space engineer in their early 30s, short-cropped natural hair, "
            "wearing a sleek white and silver exo-suit with glowing blue interface panels, "
            "intelligent warm brown eyes behind AR visor, holding a holographic tool projected from wrist"
        ),
        "description_zh": "30多歲未來星際工程師，短自然卷髮，光滑白銀外骨骼配藍色發光介面板，智慧溫暖棕眼透過AR護目鏡，手腕投影全息工具",
        "style": "hard sci-fi cinematic, clean sterile white light, holographic elements, deep space backdrop, 8k",
    },
]

# ── Story / Theme Templates (10) ─────────────────────────────────────────────

STORY_TEMPLATES: list[dict] = [
    {
        "label": "⚔️ 復仇之路",
        "theme_en": (
            "A lone warrior walks through smoldering ruins of a destroyed village, "
            "rage and grief battling in their eyes, sworn to hunt down those who betrayed them"
        ),
        "theme_zh": "孤獨戰士穿越仍在燃燒的廢村，憤怒與悲傷交戰，誓死追殺背叛者",
    },
    {
        "label": "🌃 霓虹夜城追逐",
        "theme_en": (
            "A high-speed chase through rain-soaked neon-lit city streets at midnight, "
            "desperation rising with every turn, hunted by unknown pursuers"
        ),
        "theme_zh": "午夜霓虹雨街高速追逐，每轉一個彎絕望加深，被不知名追兵追殺",
    },
    {
        "label": "🌫 迷霧中的真相",
        "theme_en": (
            "Slowly uncovering a dark conspiracy inside a fog-shrouded abandoned facility, "
            "each discovery more disturbing than the last, trust no one"
        ),
        "theme_zh": "在迷霧瀰漫的廢棄設施中緩緩揭露黑暗陰謀，每個發現比上一個更令人不安，無人可信",
    },
    {
        "label": "🌋 末日前的抉擇",
        "theme_en": (
            "Standing at the crater edge of an erupting supervolcano, "
            "the last guardian must choose: sacrifice everything to seal the disaster "
            "or flee and let civilization fall"
        ),
        "theme_zh": "站在噴發超級火山的火山口邊緣，最後的守護者必須抉擇：犧牲一切封印災難，還是逃跑讓文明崩潰",
    },
    {
        "label": "🗺 失落文明探索",
        "theme_en": (
            "A lone explorer discovers a hidden ancient city deep in uncharted jungle, "
            "golden temples still gleaming through centuries of vines, "
            "but something ancient still watches from the shadows"
        ),
        "theme_zh": "孤獨探險家在未知叢林深處發現隱藏古城，黃金神廟在世紀藤蔓中依然閃耀，但某種古老的存在仍在暗處注視",
    },
    {
        "label": "💔 背叛者的救贖",
        "theme_en": (
            "A former traitor who destroyed everything they loved must return to face their victim, "
            "seeking not forgiveness but a chance to fix what cannot be undone"
        ),
        "theme_zh": "曾摧毀一切所愛的前叛徒必須回去面對自己的受害者，尋求的不是原諒，而是一個彌補無法挽回之事的機會",
    },
    {
        "label": "🧪 禁忌實驗覺醒",
        "theme_en": (
            "Waking up in a sealed laboratory surrounded by failed experiments, "
            "with no memory of who they were before, "
            "the subject slowly realizes they are both the scientist and the experiment"
        ),
        "theme_zh": "在被失敗實驗包圍的密封實驗室中醒來，沒有任何以前的記憶，主角慢慢意識到自己既是科學家也是實驗品",
    },
    {
        "label": "🏯 亂世英雄崛起",
        "theme_en": (
            "A peasant conscript left for dead on the battlefield rises again, "
            "their fury forged into unstoppable will, "
            "marching alone toward the capital to end the corrupt dynasty"
        ),
        "theme_zh": "在戰場上被遺棄的農民兵死而復生，憤怒淬煉成無法阻擋的意志，獨自行軍向首都終結腐敗王朝",
    },
    {
        "label": "🌌 星際流亡者",
        "theme_en": (
            "The last survivor of a destroyed planet drifts through deep space in a failing escape pod, "
            "carrying the final archive of their entire civilization's history, "
            "desperately searching for a world willing to remember the dead"
        ),
        "theme_zh": "被摧毀星球的最後倖存者在失靈逃生艙中漫遊深空，攜帶整個文明歷史的最後存檔，拼命尋找一個願意記住逝者的世界",
    },
    {
        "label": "🎪 幻術師的詭計",
        "theme_en": (
            "A legendary illusionist performs their final show in a crumbling theater, "
            "but tonight the magic is real, the audience is trapped, "
            "and the only exit leads somewhere no one has returned from"
        ),
        "theme_zh": "傳奇幻術師在搖搖欲墜的劇院表演最後一場，但今晚魔法是真實的，觀眾被困住了，唯一的出口通往一個沒人回來過的地方",
    },
]

# ── Style Templates (10) ──────────────────────────────────────────────────────

STYLE_TEMPLATES: list[dict] = [
    {
        "label": "🎬 好萊塢電影",
        "style": (
            "Hollywood cinematic photography, anamorphic lens flare, "
            "dramatic three-point lighting, teal and orange color grade, "
            "shallow depth of field, 4K, IMAX quality, film grain"
        ),
    },
    {
        "label": "🎨 日系動漫",
        "style": (
            "Japanese anime illustration, cel shading, vibrant saturated colors, "
            "detailed clean linework, Studio Ghibli inspired atmosphere, "
            "cinematic composition, 4K anime"
        ),
    },
    {
        "label": "🖌 油畫寫實",
        "style": (
            "photorealistic oil painting, visible textured brushstrokes, "
            "dramatic chiaroscuro lighting, old masters technique à la Rembrandt, "
            "rich deep shadows, highly detailed, museum quality"
        ),
    },
    {
        "label": "🌑 黑色電影 Noir",
        "style": (
            "classic film noir black and white photography, high contrast dramatic shadows, "
            "venetian blind light slats casting shadow stripes, smoke atmosphere, "
            "1940s detective aesthetic, harsh single-source lighting, grain texture"
        ),
    },
    {
        "label": "🌈 賽博龐克霓虹",
        "style": (
            "cyberpunk neon-drenched cityscape, ultraviolet purple and electric cyan palette, "
            "rain-reflected neon puddles, holographic advertisements, "
            "dystopian megacity, blade runner inspired, volumetric fog, 8k"
        ),
    },
    {
        "label": "🎭 蒸汽龐克藝術",
        "style": (
            "steampunk industrial art, brass and copper mechanical aesthetic, "
            "Victorian clockwork details, sepia warm tones with green gas highlight, "
            "baroque ornate design, smoke and steam atmosphere, detailed engravings, 8k"
        ),
    },
    {
        "label": "📷 街頭攝影風",
        "style": (
            "candid street photography, natural ambient light, Leica film grain, "
            "35mm documentary style, shallow depth of field, Fujifilm color profile, "
            "authentic unposed moment, high contrast blacks, editorial quality"
        ),
    },
    {
        "label": "🌿 宮崎駿 Ghibli",
        "style": (
            "Studio Ghibli watercolor animation style, soft pastel palette, "
            "lush hand-painted backgrounds, gentle natural lighting, "
            "whimsical magical atmosphere, Hayao Miyazaki aesthetic, "
            "luminous sky detail, painterly texture"
        ),
    },
    {
        "label": "🏛 文藝復興古典",
        "style": (
            "Renaissance oil painting masterpiece, sfumato soft edge technique, "
            "Leonardo da Vinci inspired composition, classical drapery, "
            "rich earth tones with divine golden highlights, museum fresco quality, "
            "symbolic iconography, crackling varnish texture"
        ),
    },
    {
        "label": "🎮 遊戲概念藝術",
        "style": (
            "AAA video game concept art, hyper-detailed digital painting, "
            "dynamic hero lighting, epic fantasy or sci-fi environment design, "
            "Artstation quality, dramatic color story, cinematic wide-angle composition, "
            "particle effects, 4K game art"
        ),
    },
]


# ── Helper: build dropdown label lists ────────────────────────────────────────

def char_labels() -> list[str]:
    return [t["label"] for t in CHARACTER_TEMPLATES]

def story_labels() -> list[str]:
    return [t["label"] for t in STORY_TEMPLATES]

def style_labels() -> list[str]:
    return [t["label"] for t in STYLE_TEMPLATES]


def get_char(label: str) -> dict:
    return next((t for t in CHARACTER_TEMPLATES if t["label"] == label), {})

def get_story(label: str) -> dict:
    return next((t for t in STORY_TEMPLATES if t["label"] == label), {})

def get_style(label: str) -> dict:
    return next((t for t in STYLE_TEMPLATES if t["label"] == label), {})
