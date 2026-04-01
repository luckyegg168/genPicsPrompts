"""Preset templates for characters, stories, and styles."""
from __future__ import annotations

# ── Character Templates (20) ──────────────────────────────────────────────────

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
    {
        "label": "🧛 哥德吸血鬼",
        "name": "Lucian",
        "description_en": (
            "an ancient vampire nobleman in his apparent 30s, ash-pale flawless skin, "
            "piercing crimson eyes with vertical slit pupils, shoulder-length white hair, "
            "wearing a black velvet Victorian coat with blood-red inner lining, "
            "long elegant fingers, canine fangs barely visible behind a cold smile"
        ),
        "description_zh": "外貌30多歲的古老吸血鬼貴族，灰白無暇皮膚，赤紅豎瞳眼，肩長白髮，黑絲絨維多利亞外套內裡血紅，修長手指，冰冷微笑中隱現犬齒",
        "style": "gothic horror cinematic, deep crimson and shadow palette, candle-lit baroque interior, volumetric dust motes, 8k",
    },
    {
        "label": "🏋 現代格鬥士",
        "name": "Jax",
        "description_en": (
            "a professional MMA fighter in his late 20s, shaved head, "
            "multiple tattoos across muscular arms and neck, dark tan skin, "
            "wearing red and black fight shorts, fingerless gloves, "
            "intense focus in deep brown eyes, battle-worn cut above eyebrow"
        ),
        "description_zh": "20多歲職業MMA格鬥士，剃光頭，肌肉手臂與頸部密布刺青，深橙褐膚色，紅黑格鬥短褲，無指手套，深棕眼神高度專注，眉骨舊傷疤",
        "style": "sports photography, dramatic ring lighting, sweat particles in the air, shallow depth of field, gritty realism, 8k",
    },
    {
        "label": "🧝 黑暗精靈",
        "name": "Sylara",
        "description_en": (
            "a dark elf rogue woman in her early 20s, deep purple-grey skin, "
            "white flowing hair with silver strand braids, glowing amber elven eyes with elongated ears, "
            "wearing a skin-tight dark leather assassin suit with glowing rune inscriptions, "
            "twin short swords on her back, crouching on a moonlit temple rooftop"
        ),
        "description_zh": "20多歲黑暗精靈女盜賊，深紫灰皮膚，白色流動長髮摻銀絲辮子，琥珀色精靈眼配尖耳，緊身暗皮革刺客服飾帶發光盧恩銘文，背負雙小劍，蹲伏於月光神廟屋頂",
        "style": "dark fantasy epic cinematic, moonlit silver lighting, mystical particle glows, deep shadow contrast, 8k HDR",
    },
    {
        "label": "🚀 星際賞金獵人",
        "name": "Zarak",
        "description_en": (
            "a battle-hardened bounty hunter in his mid-40s, weathered face with a deep scar across left cheek, "
            "wearing a battered mandalorian-style helmet and aged graphite armor plates, "
            "a heavy laser rifle slung across back, confident slouched stance, "
            "beside a beat-up landed starship on a desert moon"
        ),
        "description_zh": "40多歲久經沙場的賞金獵人，風霜面容左臉頰深疤，破損曼達洛式頭盔配老舊石墨護甲，重型雷射步槍背負，自信慵懶的站姿，荒漠衛星降落的破舊星船旁",
        "style": "space western cinematic, harsh alien sun light, warm dust haze, Star Wars tactile aesthetic, film grain, 8k",
    },
    {
        "label": "🌺 熱帶女祭司",
        "name": "Amara",
        "description_en": (
            "a powerful tribal high priestess in her 30s, deep ebony skin, "
            "elaborate gold and jade ceremonial headdress, flowing white and gold robes, "
            "ritual body paint in intricate geometric patterns, warm dark eyes filled with ancient wisdom, "
            "standing before a roaring ceremonial bonfire at dusk"
        ),
        "description_zh": "30多歲強大部落大祭司，深黑膚色，精緻金與翡翠儀式頭冠，白金流動長袍，身上繁複幾何圖騰儀式彩繪，溫暖深邃眼神充滿古老智慧，黃昏熊熊儀式篝火前矗立",
        "style": "tribal ceremony photography, golden bonfire light, rich warm African savanna tones, sacred smoke, 8k dramatic",
    },
    {
        "label": "🤠 廢土牛仔",
        "name": "Dustin",
        "description_en": (
            "a post-apocalyptic wasteland cowboy in his 50s, deeply creased sun-baked face, "
            "wide-brimmed leather hat with bullet holes, long weathered duster coat, "
            "double revolvers at hip with custom engraving, mirrored goggles pushed on forehead, "
            "standing in an irradiated orange dessert at sunset, not afraid of anything"
        ),
        "description_zh": "50多歲廢土牛仔，深紋烈日烤焦的臉，帶彈孔的寬邊皮帽，長風霜外套，腰佩訂製雕刻雙左輪，護目鏡推上額頭，日落輻射橙色荒漠中矗立，無所畏懼",
        "style": "post-apocalyptic western, scorched orange desert horizon, lens flare sunset, gritty film photography, 8k",
    },
    {
        "label": "🧬 基因改造士兵",
        "name": "SPARX",
        "description_en": (
            "an experimental super-soldier with visible genetic augmentations, "
            "glowing circuit-like bioluminescent tattoo patterns under skin, "
            "enhanced muscular frame in a sleek black powered exo-armor, "
            "cool electric blue augmented eyes, short military haircut, "
            "crouching in a dark rainy battlefield with explosions in background"
        ),
        "description_zh": "實驗性超級士兵，皮膚下可見電路般的生物發光紋身，增強肌肉框架配時尚黑色動力外骨骼甲冑，冰冷電藍色義眼，短軍事髮型，黑暗雨中戰場蹲伏，背景爆炸",
        "style": "military sci-fi cinematic, bioluminescent highlights, rain reflection, explosive combat atmosphere, 8k",
    },
    {
        "label": "🎻 神秘小提琴手",
        "name": "Soren",
        "description_en": (
            "a mysterious street violinist in his early 20s, slim pale figure, "
            "tousled ash-brown hair falling over one eye, wearing a tattered white dress shirt, "
            "eyes closed in passionate performance, a glowing ethereal violin emanating light particles, "
            "cobblestone alley in a rainy European city, candle-lit windows above"
        ),
        "description_zh": "20多歲神秘街頭小提琴手，纖細蒼白身影，凌亂灰棕髮遮一眼，破舊白色正裝衬衫，閉眼忘我演奏，發光以太小提琴散發粒子光，雨中歐洲城市鵝卵石巷弄，上方燭光窗戶",
        "style": "European street photography, warm candlelight bokeh, rain glisten, ethereal magical realism, 8k cinematic",
    },
    {
        "label": "🦁 非洲部落戰士",
        "name": "Kofi",
        "description_en": (
            "a proud Maasai warrior in his late 20s, tall imposing physique, "
            "striking red shuka cloth draped across powerful shoulders, "
            "stacked bead necklaces and ear adornments, ochre body paint markings, "
            "long spear held upright, fierce proud gaze at golden hour sunset over savanna"
        ),
        "description_zh": "20多歲自豪馬賽戰士，高挑威武體型，鮮紅色舒卡布披覆強健肩膀，層疊珠串頸飾與耳飾，赭色身體彩繪圖飾，長矛筆直持立，金色時刻草原落日下的凌厲自豪眼神",
        "style": "National Geographic portrait photography, golden hour savanna light, majestic wide sky, rich warm earth tones, 8k",
    },
]

# ── Story / Theme Templates (20) ─────────────────────────────────────────────

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
    {
        "label": "🐉 龍族最後的契約",
        "theme_en": (
            "The last living dragon emerges from a frozen mountain at dawn, "
            "seeking not a battle but a rider worthy to carry the final fire "
            "before the dragon's eternal winter sets in"
        ),
        "theme_zh": "最後一頭活龍在黎明破冰山而出，尋找的不是戰鬥而是一個配得上在永恆冬眠前承載最後聖火的騎者",
    },
    {
        "label": "🌊 深海第一次接觸",
        "theme_en": (
            "A deep-sea explorer in a failing submersible makes first contact "
            "with an unknown bioluminescent intelligence in the Mariana Trench, "
            "communication is complex, time is running out"
        ),
        "theme_zh": "深海探險家在即將損壞的潛水艇中與馬里亞納海溝的未知生物發光智慧體首次接觸，溝通複雜，時間緊迫",
    },
    {
        "label": "🏙 都市孤狼的最後一夜",
        "theme_en": (
            "A lone vigilante spends their last night in a city they are leaving forever, "
            "walking familiar streets at 3am, saying silent farewells to every alley they bled in, "
            "every life they saved without thanks"
        ),
        "theme_zh": "孤獨義警在即將永離的城市度過最後一夜，凌晨三點漫步熟悉街道，默默告別每一條曾流血的小巷，每一個未受感謝便離去的救援",
    },
    {
        "label": "🛸 第一次太陽系事件",
        "theme_en": (
            "An ordinary asteroid mining crew intercepts an alien object disguised as a rock, "
            "it begins to unfurl—not threatening, not welcoming—simply indifferent, "
            "and impossibly beautiful"
        ),
        "theme_zh": "普通小行星採礦隊截獲一個偽裝成巖石的外星物體，它開始展開——不是威脅，不是歡迎——只是漠然，卻不可思議地美麗",
    },
    {
        "label": "🕯 鬼屋紀錄員",
        "theme_en": (
            "A paranormal archivist spends each night documenting a condemned Victorian mansion "
            "room by room, cataloguing the grief and joy that soaked into every wall, "
            "until the last room that cannot be opened speaks back"
        ),
        "theme_zh": "超自然檔案員以每晚逐房記錄一棟待拆維多利亞府邸，整理浸入每面牆的悲與喜，直到那扇無法開啟的最後房間開口回應",
    },
    {
        "label": "🎓 被系統遺忘的天才",
        "theme_en": (
            "A child prodigy raised by algorithms rather than parents "
            "discovers on their 18th birthday that they were never legally registered as a person, "
            "and must fight a bureaucratic labyrinth to simply exist"
        ),
        "theme_zh": "被演算法取代父母撫養的神童在18歲生日當天發現自己從未被合法登記為人，必須對抗官僚迷宮僅僅為了「存在」",
    },
    {
        "label": "🌿 森林守護者之死",
        "theme_en": (
            "The spirit guardian of an ancient forest willingly allows itself to be seen "
            "for the first time, having decided to let the loggers come—"
            "its final act is planting a single seed and walking away into nothing"
        ),
        "theme_zh": "古老森林的精靈守護者生平第一次主動現身，它已決定讓伐木者來——最後的舉動是種下一粒種子，然後走入虛無",
    },
    {
        "label": "🔐 解碼者的遺言",
        "theme_en": (
            "A dying cryptographer leaves behind not a will but an encrypted message "
            "that can only be decoded by someone who truly loved them, "
            "and three strangers claim they are the one"
        ),
        "theme_zh": "垂死的密碼學家留下的不是遺囑而是一條只有真正愛過他的人才能解密的訊息，三個陌生人都聲稱自己就是那個人",
    },
    {
        "label": "⏳ 記憶租稅者",
        "theme_en": (
            "In a world where memories are taxable assets, "
            "a memory auditor tasked with seizing unpaid memory debt "
            "discovers their own childhood has already been legally repossessed"
        ),
        "theme_zh": "在記憶是應課稅資產的世界中，一位奉命扣押未繳稅記憶的記憶審計師發現自己的童年已被合法沒收",
    },
    {
        "label": "🌙 月球考古最後發現",
        "theme_en": (
            "On the last day before a lunar base is decommissioned, "
            "an archaeologist finds a hand-carved inscription behind a ventilation panel—"
            "dated 40,000 years ago, in perfect modern Chinese"
        ),
        "theme_zh": "月球基地停用前的最後一天，考古學家在通風板後發現一段手刻銘文——日期是4萬年前，卻是完美的現代中文",
    },
]

# ── Style Templates (20) ──────────────────────────────────────────────────────

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
    {
        "label": "🌸 水彩插畫",
        "style": (
            "delicate watercolor illustration, translucent layered washes, "
            "wet-on-wet bleeding edges, handmade paper texture, "
            "soft natural light, botanical detail, feminine pastel palette, fine art print quality"
        ),
    },
    {
        "label": "🔥 暗黑奇幻",
        "style": (
            "dark fantasy illustration, sumptuous deep jewel tones, "
            "gothic cathedral lighting, eldritch horror atmosphere, "
            "highly detailed creature design, dynamic composition, Zdzisław Beksiński inspired, 8k"
        ),
    },
    {
        "label": "🧊 極簡 Minimalist",
        "style": (
            "ultra-minimalist graphic design, negative space dominates, "
            "single accent hue on clean white ground, Swiss International Style typography, "
            "geometric abstraction, high-contrast silhouette, editorial magazine quality"
        ),
    },
    {
        "label": "🎠 Lo-Fi 夢境",
        "style": (
            "lo-fi aesthetic dream scene, warm vintage grain, soft vignette, "
            "cozy bedroom window light, muted cassette-tape palette, "
            "nostalgic 90s Japanese animation mood, hazy bokeh fireflies, painterly softness"
        ),
    },
    {
        "label": "🌋 超現實 Surrealism",
        "style": (
            "surrealist fine art photography, impossible architectural dreamscapes, "
            "Salvador Dalí and Magritte visual language, soft shadow physics defied, "
            "hyper-real texture detail in absurdist composition, museum quality print"
        ),
    },
    {
        "label": "🌿 自然紀錄片攝影",
        "style": (
            "nature documentary photography, ultra-wide macro and telephoto blend, "
            "BBC Earth visual quality, natural golden-diffused ambient light, "
            "high-ISO grain in shadow areas, authentic untouched colour, 8K broadcast quality"
        ),
    },
    {
        "label": "🏙 建築視覺化",
        "style": (
            "architectural visualization render, photorealistic exterior, "
            "overcast soft diffused sky, precise material shading — glass, concrete, steel, "
            "people and greenery for scale, Zaha Hadid Studio aesthetic, 8K CGI quality"
        ),
    },
    {
        "label": "🖼 像素藝術",
        "style": (
            "pixel art, 32x32 sprite upscaled cleanly, limited 16-colour palette, "
            "hard anti-aliased edges, nostalgic SNES-era RPG aesthetic, "
            "dithering for shadow gradients, isometric or side-scroll perspective"
        ),
    },
    {
        "label": "✏ 炭筆素描",
        "style": (
            "expressive charcoal sketch on textured newsprint, "
            "bold gestural strokes, high contrast smudged shadows, "
            "visible paper tooth texture, life-drawing atelier quality, "
            "white chalk highlights, monochrome noir drama"
        ),
    },
    {
        "label": "🎪 波普藝術",
        "style": (
            "pop art illustration, Roy Lichtenstein thick black outlines, "
            "Ben-Day dot halftone shading, bold flat primary colour blocks, "
            "comic speech bubble, high colour saturation, 60s commercial print aesthetic"
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


# ── Video Prompt Templates (from awesome-video-prompts) ─────────────────────

VIDEO_PROMPT_TEMPLATES: list[dict] = [
    # 🎵 ASMR類
    {
        "label": '🎵 ASMR-切猕猴桃',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-切猕猴桃',
        "prompt_en": 'Static shot: A chef delicately slices a hyper-realistic kiwi on a spotless cutting board. The green flesh and glistening black seeds fracture cleanly under a whisper-thin blade. Each slice emits a soft, crystalline shimmer, ASMR. The atmosphere is surgical, serene, and visually pristine.',
        "prompt_zh": '静态画面：一位厨师在一块光洁如新的砧板上精心切下一颗超写实的猕猴桃。翠绿的果肉和闪亮的黑色种子在薄如蝉翼的刀刃下整齐断裂。每一片都散发出柔和的结晶般的光泽，ASMR。氛围手术般精准、宁静，视觉上纯净无瑕。',
    },
    {
        "label": '🎵 ASMR-男人吃融化的岩浆',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-男人吃融化的岩浆',
        "prompt_en": 'Front static shot, A man casually eats molten lava from a bowl with a metal spoon. Each scoop sizzles and pops, the bowl glowing with heat. He slurps it like soup, unfazed, as lava crackles beneath. Dramatic lighting, surreal textures, playful and absurd tone, ASMR',
        "prompt_zh": '一个正面静态镜头，一个男人用金属勺子从碗里随意吃融化的岩浆。每次舀起都会滋滋作响并冒泡，碗因热量而发光。他像喝汤一样吸溜着，面不改色，而岩浆在下面发出噼啪声。戏剧性灯光，超现实质感，俏皮且荒诞的基调，ASMR',
    },
    {
        "label": '🎵 ASMR-挤压粉嫩的果冻甜甜圈',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-挤压粉嫩的果冻甜甜圈',
        "prompt_en": 'Close-up static shot: A hand slowly squishes a glossy, pastel slime donut on a clean surface. The soft, jelly-like texture deforms and oozes between fingers, glistening under soft ambient lighting. Vibrant colors ripple through the translucent slime. Playful, ASMR, satisfying feel.',
        "prompt_zh": '特写静态画面：一只手在干净表面上缓慢挤压一个闪亮、粉嫩的果冻甜甜圈。柔软的果冻状质地在手指间变形、渗出，在柔和的环境光下闪闪发光。鲜艳的色彩在半透明的果冻中波纹荡漾。充满趣味，ASMR，令人满足的感觉。',
    },
    {
        "label": '🎵 ASMR-吃乐高热狗',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-吃乐高热狗',
        "prompt_en": 'Close-up shot: A mouth bites into a brightly colored LEGO hot dog, plastic bricks snapping with a satisfying crunch. Each chew produces sharp, toy-like ASMR sounds. Vibrant colors, playful lighting. Surreal, absurd tone with a focus on texture and sound.',
        "prompt_zh": '特写镜头：一张嘴咬住色彩鲜艳的乐高热狗，塑料积木发出令人满足的咔嚓声。每一次咀嚼都产生尖锐的玩具般 ASMR 声音。鲜艳的色彩，活泼的灯光。超现实、荒诞的基调，聚焦于质感和声音。',
    },
    {
        "label": '🎵 ASMR-煎牛排滋滋作响',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-煎牛排滋滋作响',
        "prompt_en": 'Top-down static shot, A thick slice of marbled steak sizzles on a hot black pan, juices bubbling as the surface caramelizes. Steam rises in soft curls, catching warm, directional kitchen light. Rich textures and ASMR sounds evoke savory satisfaction. Hyper-real, food-commercial style.',
        "prompt_zh": '俯视静态拍摄，厚切大理石纹牛排正在热黑的平底锅中滋滋作响，表面焦糖化时汁液冒泡。蒸汽以柔软的卷曲上升，捕捉到温暖、定向的厨房光线。丰富的质感和 ASMR 声音唤起咸香的满足感。超写实，食品广告风格。',
    },
    {
        "label": '🎵 ASMR-切玻璃火龙果',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-切玻璃火龙果',
        "prompt_en": 'Static shot, A man delicately slices a hyper-realistic glass dragon fruit on a pristine cutting board. The whisper-thin blade glides through the transparent fruit, scattering soft-glimmering shards. Surgical, serene lighting. Hyper-clean, ASMR video',
        "prompt_zh": '静态镜头，一个男人在干净的砧板上精致地切一块超逼真的玻璃龙珠果。薄如蝉翼的刀刃划过透明的果实，散落着柔和闪烁的碎片。手术般宁静的灯光。超干净，ASMR 视频',
    },
    {
        "label": '🎵 ASMR-女人吃玻璃炸鸡腿',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR-女人吃玻璃炸鸡腿',
        "prompt_en": 'Front-facing static shot, A woman enthusiastically bites into a hyper-realistic glass fried chicken leg. As it cracks delicately in her mouth, she smiles and says,  "Zero calories, zero cruelty, 100% crunch.... vegan life, baby!" Subtle ASMR crunching sounds. soft lighting, mukbang video style, playful and bizarre tone.',
        "prompt_zh": '正面静态画面，一位女士热情地咬下一块超逼真的玻璃炸鸡腿。当它在她的嘴里轻轻裂开时，她微笑着说："零卡路里，零残忍，100%酥脆....纯素生活，宝贝！"带有微妙的 ASMR 咀嚼声。柔和的灯光，吃播视频风格，俏皮又怪异。',
    },
    {
        "label": '🎵 ASMR火焰键盘',
        "category": '🎵 ASMR類',
        "title_zh": 'ASMR火焰键盘',
        "prompt_en": '{\n  "shot": {\n    "composition": "Extreme close-up, 135mm lens, shoulder-mounted for subtle sway",\n    "camera_motion": "slow left-to-right pan with slight handheld shake",\n    "frame_rate": "60fps",\n    "film_grain": "slight vintage grain with digital clarity"\n  },\n  "subject": {\n    "description": "calloused hands with soot-stained fingertips rapidly typing on burning keys",\n    "wardrobe": "charcoal black hoodie sleeves pushed up to elbows",\n    "character_consistency": "calloused hands with soot-stained fingertips rapidly typing on burning keys"\n  },\n  "scene": {\n    "location": "dark forge-style desktop lit by glowing coals",\n    "time_of_day": "late evening",\n    "environment": "embers floating in smoky low-light haze"\n  },\n  "visual_details": {\n    "action": "keys ignite on each press, flaring momentarily before cooling to a glow, smoke curling with every impact",\n    "props": "keyboard forged from volcanic glass and ember veins",\n    "physics": "realistic ember flare-up and ash behavior with particle glow diffusion"\n  },\n  "cinematography": {\n    "lighting": "backlit ember underglow with dynamic contrast",\n    "tone": "intense, elemental, darkly magical",\n    "color_palette": "burnt oranges, obsidian black, crimson pulses"\n  },\n  "audio": {\n    "dialogue": null,\n    "primary_sounds": "crackles, fire pops, crunch of hot glass under fingers",\n    "ambient": "deep furnace hum and distant metallic resonance",\n    "environmental_details": "ash settling and faint ember crackling",\n    "music": "no music",\n    "technical_effects": "ASMR mic with heat-reactive reverb tail"\n  },\n  "style": {\n    "visual_aesthetic": "fantasy realism with ASMR emphasis",\n    "aspect_ratio": "16:9",\n    "quality": "4K"\n  }\n}',
        "prompt_zh": '{\n"shot": {\n    "composition": "极近距离拍摄，135mm 镜头，肩扛式以实现轻微摇摆",\n"camera_motion": "缓慢的从左到右的摇摄，带有轻微的手持晃动",\n"frame_rate": "60fps",\n"film_grain": "轻微的复古颗粒感与数字清晰度"\n  },\n"subject": {\n    "description": "布满老茧的手指沾满烟灰，在燃烧的键盘上快速打字",\n    "wardrobe": "煤黑色连帽衫袖子推到肘部",\n    "character_consistency": "布满老茧的手指沾满烟灰，在燃烧的键盘上快速打字"\n  },\n"场景": {\n"地点": "由发光煤炭照亮的黑暗锻造风格桌面",\n"一天中的时间": "深夜",\n"环境": "火星在烟雾弥漫的低光薄雾中漂浮"\n  },\n"视觉细节": {\n"动作": "每次按键时钥匙都会点燃，短暂闪烁后冷却成微光，每次撞击都有烟雾盘旋"\n"props": "火山玻璃锻造的键盘，带有余烬脉络",\n    "physics": "逼真的余烬爆发和灰烬行为，带有粒子光晕扩散"\n  },\n  "cinematography": {\n"lighting": "逆光下的余烬辉光，动态对比强烈",\n    "tone": "激烈，原始，暗黑魔法感",\n    "color_palette": "焦橙色，黑曜石黑，深红脉冲"\n  },\n"audio": {\n"dialogue": null,\n"primary_sounds": "噼啪声，火焰爆裂声，手指下热玻璃的碎裂声",\n"ambient": "深重的炉火嗡鸣声和遥远的金属共鸣声",\n"环境细节": "灰烬沉降和微弱的余烬噼啪声",\n    "音乐": "无音乐",\n    "技术特效": "ASMR 麦克风配带热反应混响尾音"\n  },\n"style": {\n    "visual_aesthetic": "奇幻写实风格，强调 ASMR 效果",\n    "aspect_ratio": "16:9",\n    "quality": "4K"\n  }\n}',
    },

    # 🧑 人物敘事
    {
        "label": '🧑 女性在书桌前主持播客',
        "category": '🧑 人物敘事',
        "title_zh": '女性在书桌前主持播客',
        "prompt_en": 'Front static shot, a woman hosts a podcast at a desk, speaking softly into a mic with low tones, whispering. Wearing headphones, she grins and says: “Confidence? Oh, honey, I don’t walk into a room—I glide in like I own the Wi-Fi.” Soft studio lighting, cozy, playful, and empowering podcast energy. podcast vibe. no subtitle',
        "prompt_zh": '正面静态镜头，一名女性在书桌前主持播客，用低沉的语调轻声对着麦克风说话，低语。她戴着耳机，微笑着说：“自信？哦，亲爱的，我不走进房间——我像拥有 Wi-Fi 一样滑进去。”柔和的影棚灯光，温馨、俏皮，充满赋权的播客能量。播客氛围。无字幕',
    },
    {
        "label": '🧑 一只公鸡跳操',
        "category": '🧑 人物敘事',
        "title_zh": '一只公鸡跳操',
        "prompt_en": 'A dynamic tracking shot, a rooster launches off a gymnastics vault, flipping mid-air with feathers flying in slow motion. It sticks the landing perfectly, wings spread in a proud pose. Judges flash “10.0” scorecards. Bright stadium lights, roaring crowd. Playful, surreal Olympic parody.',
        "prompt_zh": '一个动态的跟拍镜头，一只公鸡从体操跳板上腾空而起，在空中翻转，羽毛在慢动作中飞舞。它完美地落地，展开翅膀，摆出骄傲的姿态。裁判们亮出“10.0”的评分牌。明亮的体育场灯光，欢呼的人群。充满趣味、超现实的奥运讽刺。',
    },
    {
        "label": '🧑 雪人自拍',
        "category": '🧑 人物敘事',
        "title_zh": '雪人自拍',
        "prompt_en": '{\n  "shot": {\n    "composition": "Medium shot, vertical format, handheld camera",\n    "camera_motion": "slight natural shake",\n    "frame_rate": "30fps",\n    "film_grain": "none"\n  },\n  "subject": {\n    "description": "A towering, snow-white Yeti with shaggy fur and expressive blue eyes",\n    "wardrobe": "slightly oversized white T-shirt with the name \'Emily\' in bold, blood-red letters across the chest"\n  },\n  "scene": {\n    "location": "lush forest clearing",\n    "time_of_day": "daytime",\n    "environment": "sunlight filtering through the canopy, creating dappled light patterns on the forest floor"\n  },\n  "visual_details": {\n    "action": "Yeti holds a smartphone on a selfie stick, speaking excitedly to the camera before letting out a dramatic scream",\n    "props": "smartphone mounted on a selfie stick"\n  },\n  "cinematography": {\n    "lighting": "natural sunlight with soft shadows",\n    "tone": "lighthearted and humorous"\n  },\n  "audio": {\n    "ambient": "rustling leaves, distant bird calls",\n    "dialogue": {\n      "character": "Yeti",\n      "line": "Veo3 Fast is now available in the Gemini app—three videos per day! People are going to prompt me like crazy!",\n      "subtitles": false\n    },\n    "effects": "sudden loud scream, flapping wings of startled birds"\n  },\n  "color_palette": "naturalistic with earthy greens and browns; bold red lettering on shirt provides contrast"\n}',
        "prompt_zh": '{\n"镜头": {\n"构图": "中景，竖屏格式，手持相机",\n"相机运动": "轻微自然摇晃",\n"帧率": "30fps",\n"胶片颗粒": "无"\n},\n"主体": {\n"描述": "一只高大的雪白雪人，毛发蓬松，眼睛充满表现力，呈蓝色",\n"服装": "略微过大的白色T恤，胸前用粗体血红色字母写着‘Emily’"\n},\n"场景": {\n"位置": "郁郁葱葱的森林空地",\n"时间": "白天",\n"环境": "阳光透过树冠洒下，形成斑驳的光影模式在森林地面"\n},\n"视觉细节": {\n"动作": "雪人拿着自拍杆上的智能手机，兴奋地对着镜头讲话，随后发出一声戏剧性的尖叫",\n"道具": "安装在自拍杆上的智能手机"\n},\n"摄影": {\n"照明": "自然阳光，柔和的阴影",\n"基调": "轻松幽默"\n},\n"音频": {\n"环境音": "沙沙的树叶声，远处的鸟鸣声",\n"对白": {\n"角色": "雪人",\n"台词": "Veo3 Fast现在可以在Gemini应用中使用——每天三条视频！人们会疯狂地给我发提示！",\n"字幕": false\n},\n"音效": "突然的大声尖叫，惊飞的鸟翼拍打声"\n},\n"色彩调色板": "自然主义风格，带有泥土般的绿色和棕色；T恤上的鲜艳红色字母提供了对比"\n}',
    },
    {
        "label": '🧑 走廊里女人举起双手眨眼',
        "category": '🧑 人物敘事',
        "title_zh": '走廊里女人举起双手眨眼',
        "prompt_en": '{\n  "shot": {\n    "composition": "Medium shot, 35mm lens, shot on ARRI Alexa Mini LF, shallow depth of field, centered framing",\n    "camera_motion": "static camera with slight handheld sway for liveliness",\n    "frame_rate": "24fps",\n    "film_grain": "subtle Kodak Vision3 250D grain overlay"\n  },\n  "subject": {\n    "description": "A young woman with pale skin and long black wavy hair, dressed in a crisp white button-up shirt, a slim black tie, and dark tailored trousers",\n    "wardrobe": "white dress shirt neatly tucked, black tie loosely knotted, dark fitted trousers, casual yet polished",\n    "character_motion": "she raises both hands playfully like claws and winks with one eye, holding the pose for a beat"\n  },\n  "scene": {\n    "location": "minimalist indoor studio hallway with matte gray walls and industrial door labeled with signage",\n    "time_of_day": "midday with soft diffused light",\n    "environment": "clean neutral-toned space, subtle overhead lighting, muted background for focus on subject"\n  },\n  "visual_details": {\n    "action": "as the woman strikes her playful claw pose and winks, a pixel art character appears in the lower right corner, mimicking her motion in perfect sync with exaggerated cartoonish expression",\n    "props": "visible door with white \'DO NOT OPEN\' label, gray paneling, studio floor tiles"\n  },\n  "cinematography": {\n    "lighting": "soft top-lighting with a hint of bounce to preserve facial charm and skin tone",\n    "tone": "lighthearted, whimsical, charming with a touch of surreal contrast between realism and pixel art"\n  },\n  "audio": {\n    "ambient": "soft studio room tone, faint echo of movement",\n    "sound_effects": "light chime as both the woman and pixel character raise their hands, soft digital pop as pixel character appears"\n  },\n  "color_palette": "neutral grays with pops of black and white, slight pastel blush tones in the pixel character for warmth",\n  "dialogue": {\n    "character": "Woman",\n    "line": "(cheerfully, winking) \\"Rawr! I\'m pixel-perfect!\\"",\n    "subtitles": false\n  }\n}',
        "prompt_zh": "{\n“shot”： {\n“composition”： “中景，35mm 镜头，使用 ARRI Alexa Mini LF 拍摄，浅景深，居中取景”，\n“camera_motion”： “静态摄像机，手持轻微摇晃，生动活泼”，\n“frame_rate”： “24fps”，\n“film_grain”： “微妙的 Kodak Vision3 250D 颗粒叠加”\n  },\n“主题”： {\n“description”： “一位年轻女子，皮肤苍白，黑色波浪长发，穿着一件清爽的白色纽扣衬衫，系着修身的黑色领带，穿着深色定制裤”，\n“wardrobe”： “白色衬衫整齐地塞进去，黑色领带松散地打结，深色合身的裤子，休闲而优雅”，\n“character_motion”： “她像爪子一样俏皮地举起双手，一只眼睛眨眼，保持姿势一拍”\n  },\n“场景”： {\n“location”： “极简主义的室内工作室走廊，带有哑光灰色墙壁和标有标牌的工业门”，\n“time_of_day”： “柔和漫射光的正午”，\n“environment”： “干净的中性空间，微妙的头顶照明，柔和的背景，专注于主体”\n  },\n“visual_details”： {\n“action”： “当女人摆出俏皮的爪子姿势并眨眼时，一个像素艺术人物出现在右下角，模仿她的动作与夸张的卡通表情完美同步”，\n“props”： “带有白色'请勿打开'标签的可见门，灰色镶板，工作室地砖”\n  },\n“电影摄影”： {\n“lighting”： “柔和的顶部照明，带有一丝弹性，以保持面部魅力和肤色”，\n“tone”： “轻松愉快、异想天开、迷人，在现实主义和像素艺术之间带有一丝超现实主义的对比”\n  },\n“音频”： {\n“ambient”： “柔和的工作室房间音调，微弱的运动回声”，\n“sound_effects”： “当女性和像素角色都举起手时发出轻柔的蜂鸣声，当像素角色出现时发出柔和的数字爆裂声”\n  },\n“color_palette”： “中性灰色，带有黑白的流行效果，像素字符中略带柔和的腮红色调，以增强暖色”，\n“对话”： {\n“character”： “女人”，\n“line”： “（欢快地，眨眼） \\”Rawr！我是像素完美的！\n“subtitles”： false\n  }\n}",
    },
    {
        "label": '🧑 登山者到达顶峰',
        "category": '🧑 人物敘事',
        "title_zh": '登山者到达顶峰',
        "prompt_en": '{ "scene_description": "A climber reaches a summit, gasping. As they raise their arms, a sudden gust of wind pushes back their hood — revealing the North Face logo on their shoulder. Quick cut to a wide shot of the climber silhouetted against the sky with the logo clear.", "visual_style": "epic outdoor documentary", "camera_movement": "POV pan + wide drone reveal", "main_subject": "North Face jacket worn during a summit achievement", "background_setting": "mountaintop above clouds", "lighting_mood": "harsh, high-altitude natural light", "audio_cue": "wind roar, breath, short dramatic swell" }',
        "prompt_zh": '{ “scene_description”： “登山者到达顶峰，喘着粗气。当他们举起手臂时，一阵突如其来的风将他们的兜帽推开，露出了他们肩膀上的 North Face 标志。“， ”visual_style“： ”史诗般的户外纪录片“， ”camera_movement“： ”POV 平移 + 宽无人机展示“， ”main_subject“： ”登顶成就时穿的北脸夹克“， ”background_setting“： ”云层之上的山顶“， ”lighting_mood“： ”刺眼的高海拔自然光“， ”audio_cue“： ”风咆哮，呼吸，短暂的戏剧性海浪“ }',
    },
    {
        "label": '🧑 摄影师拍老虎',
        "category": '🧑 人物敘事',
        "title_zh": '摄影师拍老虎',
        "prompt_en": '{ "scene_description": "A photographer points a Canon EOS camera at a tiger walking slowly toward frame. The lens clicks — instantly, the scene freezes into a crystal-clear photo. The tiger disappears. Only the image remains, with the Canon logo in the bottom corner.", "visual_style": "wildlife cinematic", "camera_movement": "handheld feel, quick snap to static composition", "main_subject": "Canon camera capturing a wild animal mid-action", "background_setting": "jungle or dry grassland", "lighting_mood": "natural light with rich saturation", "audio_cue": "camera shutter snap, then ambient cutout to silence"}',
        "prompt_zh": '{ “scene_description”： “一位摄影师将佳能 EOS 相机对准一只慢慢走向画面的老虎。镜头咔嗒一声——瞬间，场景定格成一张水晶般清晰的照片。老虎消失了。“， ”visual_style“： ”野生动物电影“， ”camera_movement“： ”手持感觉，快速捕捉静态构图“， ”main_subject“： ”佳能相机捕捉野生动物的动作中“， ”background_setting“： ”丛林或干燥草原“， ”lighting_mood“： ”饱和度丰富的自然光“， ”audio_cue“： ”相机快门快照，然后环境切口到静音“}',
    },
    {
        "label": '🧑 滑板爱好者',
        "category": '🧑 人物敘事',
        "title_zh": '滑板爱好者',
        "prompt_en": '{ "scene_description": "A skateboarder flips a board over a set of stairs in slow motion. As the board spins, it reveals the Supreme logo underneath. The landing is hard and clean. The logo is reflected in a puddle next to the skater’s feet.", "visual_style": "gritty skate aesthetic", "camera_movement": "360 rotation during kickflip, locked-on landing", "main_subject": "Supreme board in mid-air with logo reveal", "background_setting": "concrete urban plaza", "lighting_mood": "late afternoon city shadows", "audio_cue": "board wheels, air whip, stomp, puddle ripple" }',
        "prompt_zh": '{ “scene_description”： “滑板手以慢动作将一块板翻转到一组楼梯上。当棋盘旋转时，它会露出下面的 Supreme 标志。着陆又硬又干净。标志反映在滑冰者脚边的水坑中。“， ”visual_style“： ”坚韧不拔的滑板美学“， ”camera_movement“： ”踢空翻时的 360 度旋转，锁定着陆“， ”main_subject“： ”半空中的至尊板，标志显现“， ”background_setting“： ”混凝土城市广场“， ”lighting_mood“： ”傍晚的城市阴影“， ”audio_cue“： ”板轮、空气鞭、跺脚、水坑涟漪“ }',
    },
    {
        "label": '🧑 电臀舞',
        "category": '🧑 人物敘事',
        "title_zh": '电臀舞',
        "prompt_en": '{\n  "shot": {\n    "composition": "waist-level medium tracking shot (focus on hips) → mid-torso push-in",\n    "camera_motion": "smooth crane drop from 4 m to 1.0 m over 1 s, then gimbal sidestep left-right 40 cm each beat (follow hip sways) for remaining 7 s",\n    "frame_rate": "24fps",\n    "lens": "prime 40 mm throughout",\n    "depth_of_field": "medium; hips sharp, background soft",\n    "film_grain": 0.03\n  },\n\n  "subject": {\n    "entity": "charismatic Latina hip-hop performer",\n    "description": "athletic build, copper-toned skin, high velvet ponytail, holographic silver bodysuit with crystal fringes, thigh-high reflective boots; wireless mic in right hand, left hand free",\n    "movement": "booty-dance isolations: knees bent 20°, pelvis pops backward on beat-one, forward on beat-two; controlled hip rolls (no leg crossing) plus three rapid twerk pulses at 3.2 Hz; shoulders stay steady to avoid torso distortion",\n    "facial_expression": "confident smile, playful wink on downbeat two",\n    "eyes": "smoky metallic eyeshadow catching key light"\n  },\n\n  "scene": {\n    "location": "infinite white cyclorama studio (seamless wall-to-floor curve)",\n    "time_of_day": "n/a (controlled studio lighting)",\n    "environment_details": "polished white epoxy floor reflecting subtle pink/cyan rim lights; no crowd"\n  },\n\n  "visual_details": {\n    "primary_action": "performer executes booty-dance routine for full 8 s while spitting rap hook; camera’s lateral sway syncs with hip pops",\n    "secondary_motion": "thin RGB floor strips flash pink-aqua on each bass hit",\n    "duration": "8s",\n    "resolution": "4K",\n    "special_effects": [\n      "edge-lit panels sweep color across white surfaces",\n      "micro-lens flares on chrome accessories",\n      "sub-10 % slow-shutter smears on quickest hip pulses (safe threshold)"\n    ]\n  },\n\n  "cinematography": {\n    "lighting": "high-key softbox grid overhead (5600 K); magenta accent strip camera left, cyan accent camera right; gentle 0.5 s strobe on every fourth snare (≤ 0.5 stop)",\n    "style": "glossy hyper-real studio aesthetic",\n    "tone": "playful, high-energy"\n  },\n\n  "audio": {\n    "music_track": "trap-pop beat at 190 BPM, heavy 808 sub, crisp claps on 2 & 4",\n    "ambience": "subtle studio room tone (−60 LUFS)",\n    "vocal_processing": "tight slapback delay (60 ms); gentle de-ess at 6 kHz"\n  },\n\n  "dialogue": {\n    "spoken_lines": [\n      {\n        "speaker": "performer",\n        "line": "Grok4 crashin\' in, meltin\' chips like fire,",\n        "delivery": "assertive bounce, lands squarely on beat"\n      },\n      {\n        "speaker": "performer",\n        "line": "GPT-5 wired, but Grok takes it higher!",\n        "delivery": "rising intonation with breathy laugh tail"\n      }\n    ],\n    "subtitles": false\n  },\n\n  "color_palette": {\n    "name": "Neon on White",\n    "primary": "#FF007F",\n    "secondary": "#00FFD5",\n    "accents": "#C0C0C0",\n    "background": "#FFFFFF"\n  },\n\n  "visual_rules": {\n    "prohibited_elements": [\n      "brand logos",\n      "explicit nudity",\n      "onscreen text overlays",\n      "slow-motion exceeding 10 % stretch",\n      "lens dirt or burn-in frame lines"\n    ]\n  }\n}',
        "prompt_zh": '{\n  "镜头": {\n    "构图": "腰部水平中景跟拍（聚焦臀部）→ 向躯干中部推进",\n    "相机运动": "1秒内从4米高度平稳摇臂下降至1.0米，剩余7秒内，云台随每一拍左右侧移各40厘米（跟随臀部摆动）",\n    "帧率": "24帧/秒",\n    "镜头": "全程使用40毫米定焦镜头",\n    "景深": "中等；臀部清晰，背景虚化",\n    "胶片颗粒感": 0.03\n  },\n\n  "拍摄主体": {\n    "主体身份": "富有魅力的拉丁裔嘻哈表演者",\n    "外形描述": "体格健硕，铜色皮肤，高束丝绒马尾辫，带水晶流苏的全息银色紧身衣，过膝反光长靴；右手持无线麦克风，左手自然下垂",\n    "动作": "臀部舞蹈分离动作：膝盖弯曲20°，第一拍时骨盆向后顶，第二拍时向前顶；有控制地转动臀部（不交叉双腿），并以3.2赫兹的频率快速抖臀三次；肩膀保持稳定，避免躯干晃动",\n    "面部表情": "自信的微笑，在第二拍强拍时俏皮地眨一下眼",\n    "眼部": "烟熏金属色眼影在主光下闪闪发光"\n  },\n\n  "场景": {\n    "地点": "无限白色环形布景工作室（墙面与地面无缝弧形衔接）",\n    "时段": "不适用（受控的工作室灯光）",\n    "环境细节": "抛光白色环氧地板反射出柔和的粉/青色轮廓光；无观众"\n  },\n\n  "视觉细节": {\n    "主要动作": "表演者在整整8秒内完成臀部舞蹈动作，同时说唱副歌；相机的横向摆动与臀部顶动同步",\n    "次要动态": "纤细的RGB地面灯带在每次贝斯响起时闪烁粉青色光芒",\n    "时长": "8秒",\n    "分辨率": "4K",\n    "特效": [\n      "边缘照明面板在白色表面扫过色彩",\n      "镀铬配饰上的微镜头光晕",\n      "在最快的臀部抖动动作上使用低于10%的慢快门模糊效果（安全阈值）"\n    ]\n  },\n\n  "摄影": {\n    "灯光": "顶部高键柔光箱网格布光（5600K）；相机左侧为品红色重点光条，右侧为青色重点光；每第四个军鼓响起时，柔和的0.5秒频闪灯亮起（≤0.5档）",\n    "风格": "光泽感超写实工作室美学",\n    "基调": "活泼、高能量"\n  },\n\n  "音频": {\n    "音乐曲目": "190 BPM的陷阱流行节拍，厚重的808底鼓，在第2和第4拍有清晰的拍手声",\n    "环境音": "轻微的工作室室内音（-60 LUFS）",\n    "人声处理": "紧凑的回声延迟（60毫秒）；在6千赫兹处有柔和的去嘶音处理"\n  },\n\n  "对白": {\n    "台词": [\n      {\n        "说话者": "表演者",\n        "台词": "Grok4 强势登场，像火焰一样融化芯片，",\n        "表达": "坚定有节奏，精准踩在节拍上"\n      },\n      {\n        "说话者": "表演者",\n        "台词": "GPT-5 已联网，但 Grok 更胜一筹！",\n        "表达": "语调上扬，结尾带着轻快的笑声"\n      }\n    ],\n    "字幕": 无\n  },\n\n  "色彩搭配": {\n    "名称": "白色上的霓虹",\n    "主色": "#FF007F（粉色）",\n    "辅助色": "#00FFD5（青色）",\n    "强调色": "#C0C0C0（银色）",\n    "背景色": "#FFFFFF（白色）"\n  },\n\n  "视觉规则": {\n    "禁止元素": [\n      "品牌标识",\n      "露骨裸露画面",\n      "屏幕文字叠加",\n      "超过10%拉伸比例的慢动作",\n      "镜头污点或烙印式画框线"\n    ]\n  }\n}',
    },
    {
        "label": '🧑 男人沿着一条漆黑的小巷奔跑',
        "category": '🧑 人物敘事',
        "title_zh": '男人沿着一条漆黑的小巷奔跑',
        "prompt_en": 'A man runs down a dark alley at night with a gun in his hand. Handheld 35mm medium shot tracks behind him, then whip-pans as he checks a corner. Dim streetlights, rising steam, cold breath. Slow motion pulse as he lifts the gun. He mutters, “Of course it had to be this alley…”',
        "prompt_zh": '夜里，一个男人手持枪，沿着一条漆黑的小巷奔跑。手持35毫米中景镜头在他身后跟踪，然后随着他检查街角而快速摇摄。昏暗的路灯，升腾的蒸汽，冰冷的呼吸。他举起枪，脉搏慢动作跳动。他喃喃自语：“当然是这条小巷……”',
    },

    # 📦 品牌廣告
    {
        "label": '📦 Apple耳机',
        "category": '📦 品牌廣告',
        "title_zh": 'Apple耳机',
        "prompt_en": '{\n  "video_length": 8,\n  "scenes": [\n    {\n      "start": 0.0,\n      "end": 0.7,\n      "visual": "Apple earbuds appear in flashes over black void. Each flash reveals angle: top, side, front. Particles burst with light impact.",\n      "camera": "snap zooms, hard cuts",\n      "sound": "tight bass drops per cut"\n    },\n    {\n      "start": 0.7,\n      "end": 2.0,\n      "visual": "Case pops open mid-air. Earbuds launch out in sync with beat, glowing rim light follows motion arcs.",\n      "camera": "explosive transitions, 3D spin",\n      "sound": "fast-paced pulse"\n    },\n    {\n      "start": 2.0,\n      "end": 3.5,\n      "visual": "Earbuds split apart mid-flight. Internal parts float, orbiting like choreography.",\n      "camera": "slow-motion breakaway",\n      "sound": "digital glitch rhythm"\n    },\n    {\n      "start": 3.5,\n      "end": 5.0,\n      "visual": "Floating parts twist and merge into Apple logo. Logo turns pitch black, neon rim lights glow softly.",\n      "camera": "cinematic orbit + pull back",\n      "sound": "echoing synth + Apple tone"\n    },\n    {\n      "start": 5.0,\n      "end": 8.0,\n      "visual": "Apple logo holds center with ambient glow. Background fades to deep black. Silence.",\n      "camera": "static frame",\n      "sound": "quiet fade-out"\n    }\n  ]\n}',
        "prompt_zh": '{\n“video_length”：8，\n“场景”： [\n    {\n“开始”：0.0，\n“结束”：0.7，\n“visual”： “Apple 耳塞在黑色虚空中闪烁。每次闪光灯都会显示角度：顶部、侧面、正面。粒子在轻微的撞击下爆裂。\n“camera”： “快照变焦，硬剪辑”，\n“sound”： “每次剪辑的低音下降很紧”\n    },\n    {\n“开始”：0.7，\n“结束”：2.0，\n“visual”： “箱子在半空中弹开。耳塞与节拍同步启动，发光的边缘灯跟随运动弧线。\n“camera”： “爆炸性过渡，3D 旋转”，\n“sound”： “快节奏的脉搏”\n    },\n    {\n“开始”：2.0，\n“结束”：3.5，\n“visual”： “耳塞在飞行途中分开。内部部件漂浮，像编舞一样绕圈。\n“camera”： “慢动作脱离”，\n“sound”： “数字故障节奏”\n    },\n    {\n“开始”：3.5，\n“结束”：5.0，\n“visual”： “浮动部件扭曲并合并成 Apple 标志。标志变成漆黑，霓虹灯边缘灯柔和地发光。\n“camera”： “电影轨道 + 回拉”，\n“sound”： “回声合成器+苹果音”\n    },\n    {\n“开始”：5.0，\n“结束”：8.0，\n“visual”： “Apple 标志以环境光保持中心。背景逐渐变为深黑色。沉默。\n“camera”： “静态帧”，\n“sound”： “安静淡出”\n    }\n  ]\n}',
    },
    {
        "label": '📦 Corona科罗拉啤酒',
        "category": '📦 品牌廣告',
        "title_zh": 'Corona科罗拉啤酒',
        "prompt_en": '{ "description": "Cinematic close-up of a cold, dewy Corona bottle sitting alone on a weathered beach table. It begins to hum, vibrate. The bottle cap *pops*—and the entire environment unfolds from inside: palm trees rise, lights string themselves, speakers assemble mid-air, sand shifts into a dance floor. A DJ booth builds from driftwood. Music kicks in. A beach rave is born. No text.",\n  "style": "cinematic, magical realism", "camera": "starts ultra close, zooms out and cranes overhead as the world expands", "lighting": "sunset turning to neon—golden hour into party glow", "environment": "quiet beach transforms into high-energy beach rave", "elements": [ "Corona bottle (label visible, condensation dripping)", "pop-top cap in slow motion", "exploding citrus slice", "sand morphing into dance floor", "palm trees rising", "neon lights snapping on", "DJ booth building itself", "crowd materializing mid-dance", "fire pit lighting", "surfboards as signage"], "motion": "explosion of elements from bottle, everything assembles in rapid time-lapse", "ending": "Corona bottle in foreground, beach rave in full swing behind it", "text": "none", "keywords": ["Corona", "beach party", "bottle transforms", "rave build", "sunset to night", "cinematic", "no text"] \n}',
        "prompt_zh": '{ “description”： “一个冰冷、露水的 Corona 瓶子独自坐在风化的沙滩桌上的电影特写镜头。它开始嗡嗡作响，振动。瓶盖“爆裂”——整个环境从里面展开：棕榈树升起，灯光串起，扬声器在半空中组装，沙子变成舞池。DJ 台是用浮木建造的。音乐开始了。海滩狂欢诞生了。没有文字。\n“style”： “cinematic， magical realism”， “camera”： “随着世界的扩大，从超近距离开始，缩小并从头顶升起”， “lighting”： “夕阳变成霓虹灯——黄金时段变成派对光芒”， “environment”： “安静的海滩变成高能量的海滩狂欢”， “elements”： [ “Corona 瓶子（标签可见，冷凝水滴落）”， “慢动作弹出式盖子”， “爆炸的柑橘片”， “沙子变成舞池”， “棕榈树升起”， “霓虹灯啪啪作响”、“DJ 台建筑本身”、“舞中人群具体化”、“火坑照明”、“冲浪板作为标牌”]、“motion”： “元素从瓶子中爆炸，一切都在快速延时摄影中组装”， “ending”： “前景中的电晕瓶，后面如火如荼地进行海滩狂欢”， “text”： “none”， “keywords”： [“Corona”， “beach party”， “bottle transforms”， “rave build”， “sunset to night”， “cinematic”， “no text” ] \n}',
    },
    {
        "label": '📦 斗牛',
        "category": '📦 品牌廣告',
        "title_zh": '斗牛',
        "prompt_en": '{\n  "scene_description": "A torero stands alone in an empty bullring, holding an ultra-slim LG TV like a shield. The screen shows a vivid, pure red. He shouts \'Hey!\' and the camera cuts to a massive black bull. It charges. Right before impact, the scene cuts to solid red. The LG logo appears in white, then the words \'Pure Red\'. Finally, the bull crashes through the red screen, shattering it visually.",\n  "visual_style": "cinematic",\n  "camera_movement": "push-in on torero, whip-pan to bull, sharp cut to red, final VFX screen break from off-screen",\n  "main_subject": "torero with LG TV showing pure red, ending with bull breaking the final screen",\n  "background_setting": "sunlit empty bullring",\n  "lighting_mood": "golden-hour with strong contrast",\n  "audio_cue": "wind, torero\'s shout, bull snort and charge, silence, glass break",\n  "dialog": "0:04 — Torero: \'Hey!\'\\n0:08 — [Bull breaks screen]",\n  "subtitles": "OFF"\n}',
        "prompt_zh": "{\n“scene_description”： “一个斗牛人独自站在空荡荡的斗牛场里，像盾牌一样拿着一台超薄的 LG 电视。屏幕显示鲜艳、纯净的红色。他大喊“嘿！”，镜头切换到一头巨大的黑牛。它收费。在撞击之前，场景切换为纯红色。LG 标志以白色出现，然后是“Pure Red”字样。最后，公牛冲破了红屏，在视觉上将其粉碎。\n“visual_style”： “电影”，\n“camera_movement”：“在托雷罗上推入，鞭打到公牛，锐切到红色，最终的视觉特效屏幕从屏幕外中断”，\n“main_subject”： “torero 与 LG 电视呈现纯红色，以公牛打破最终屏幕而告终”，\n“background_setting”： “阳光明媚的空斗牛场”，\n“lighting_mood”：“对比强烈的黄金时段”，\n“audio_cue”：“风，托雷罗的呐喊，公牛的鼻息和冲锋，寂静，玻璃破碎”，\n“dialog”： “0：04 — Torero：'嘿！\\n0：08 — [公牛打破屏幕]“，\n“subtitles”： “关闭”\n}",
    },
    {
        "label": '📦 ROG电路板',
        "category": '📦 品牌廣告',
        "title_zh": 'ROG电路板',
        "prompt_en": '{ "scene_description": "A circuit board pulses with red energy. Sparks travel across its paths until they converge and explode into the ROG logo, which hovers above the board glowing in red and silver.", "visual_style": "futuristic high-tech", "camera_movement": "fast tracking over circuit paths, ending in dramatic logo reveal", "main_subject": "ROG logo forming from energy traveling across circuitry", "background_setting": "dark tech environment", "lighting_mood": "moody dark with neon red highlights", "audio_cue": "electric pulses, deep bass hum, digital spark"}',
        "prompt_zh": '{ “scene_description”： “电路板以红色能量脉冲。火花穿过它的路径，直到它们汇聚并爆炸成 ROG 标志，ROG 标志盘旋在电路板上方，发出红色和银色的光芒。“， ”visual_style“： ”未来派高科技“， ”camera_movement“： ”快速跟踪电路路径，以戏剧性的标志揭晓结束“， ”main_subject“： ”ROG 标志由能量穿过电路传播形成“， ”background_setting“： ”黑暗科技环境“， ”lighting_mood“： “Moody Dark with Neon Red Highlights”， “audio_cue”： “电脉冲、深沉的低音嗡嗡声、数字火花”}',
    },
    {
        "label": '📦 Vans变装',
        "category": '📦 品牌廣告',
        "title_zh": 'Vans变装',
        "prompt_en": '{ "scene_description": "A white classic Vans sneaker floats mid-air, slowly spinning. Suddenly, a burst of vibrant paint splashes across it — black and neon green. The shoe transforms instantly into a bold fashion-forward version in black with acid green details. In the blurred background, a skatepark can be seen, but the focus remains solely on the shoe.", "visual_style": "high-fashion streetwear", "camera_movement": "slow-motion rotation of the sneaker, locked-on shot with shallow depth of field", "main_subject": "Vans sneaker transforming mid-air from classic white to black and neon green", "background_setting": "blurred skatepark with ramps and urban textures", "lighting_mood": "even, soft light with focus on color contrast and texture", "audio_cue": "slow whoosh, paint burst impact, subtle tone shift at the transformation" }',
        "prompt_zh": '{ “scene_description”： “一双白色经典的 Vans 运动鞋漂浮在半空中，缓慢旋转。突然，一阵充满活力的油漆溅到它上面——黑色和霓虹绿。这款鞋立即转变为带有酸性绿色细节的黑色大胆时尚前卫版本。在模糊的背景中，可以看到一个滑板公园，但焦点仍然只集中在鞋子上。“， ”visual_style“： ”高级时装街头服饰“， ”camera_movement“： ”运动鞋的慢动作旋转，浅景深锁定镜头“， ”main_subject“： ”Vans 运动鞋在半空中从经典的白色转变为黑色和霓虹绿“， ”background_setting“： ”带有坡道和城市纹理的模糊滑板公园“， “lighting_mood”： “均匀、柔和的光线，注重色彩对比度和纹理”， “audio_cue”： “缓慢的嗖嗖声，油漆爆裂的冲击力，变换时微妙的色调变化” }',
    },
    {
        "label": '📦 NIKE广告',
        "category": '📦 品牌廣告',
        "title_zh": 'NIKE广告',
        "prompt_en": '{\n  "description": "Fixed wide-angle cinematic shot of a sunlit white backdrop. The Coca-Cola logo, drawn in flowing red script, floats midair with a soft glow. The letters begin to ripple like liquid, then collapse into a glossy red stream that spirals downward. As it coils and rises, it forms the silhouette of the classic Coca-Cola glass bottle. The bottle crystallizes into solid form, covered in condensation. A \'pssst\' sound is heard as the cap pops off and fizzy bubbles rise. No text.",\n  "style": "cinematic, nostalgic, sensory",\n  "camera": "fixed wide angle",\n  "lighting": "warm natural lighting with soft highlights and slight backlight",\n  "environment": "white studio backdrop with faint texture",\n  "elements": [\n    "Coca-Cola logo (red script)",\n    "liquid transformation stream",\n    "glass Coca-Cola bottle",\n    "fizz bubbles and condensation",\n    "pop of the bottle cap",\n    "reflections on the glass"\n  ],\n  "motion": {\n    "type": "logo-to-liquid-to-object",\n    "details": "logo ripples and melts into red stream, which forms the bottle and opens"\n  },\n  "ending": "The bottle stands upright, open, cold and glistening. Fade to black. No text.",\n  "audio": {\n    "voice_over": "none",\n    "music": "gentle nostalgic acoustic strum or soft jazz piano",\n    "sfx": "liquid ripple, bottle forming, fizz, bottle cap \'pssst\'"\n  },\n  "text_overlay": "none",\n  "format": "16:9",\n  "keywords": [\n    "Coca-Cola",\n    "glass bottle",\n    "liquid transformation",\n    "nostalgia",\n    "brand reveal",\n    "cinematic"\n  ]\n}',
        "prompt_zh": "{\n“description”： “修复了阳光照射的白色背景的广角电影镜头。可口可乐标志以流动的红色字体绘制，飘浮在半空中，散发着柔和的光芒。这些字母开始像液体一样荡漾，然后塌陷成一条有光泽的红色流，向下盘旋。当它盘绕和上升时，它形成了经典可口可乐玻璃瓶的轮廓。瓶子结晶成固体，被冷凝水覆盖。当盖子弹出并且起泡气泡升起时，会听到“噗噗”声。没有文字。\n“style”： “电影、怀旧、感官”，\n“camera”： “固定广角”，\n“lighting”：“温暖的自然采光，高光柔和，背光轻微”，\n“environment”： “白色工作室背景，纹理微弱”，\n“元素”： [\n“可口可乐标志（红色字体）”，\n“液体转化流”，\n“玻璃可口可乐瓶”，\n“嘶嘶气泡和冷凝”，\n“瓶盖的啪啪声”，\n“玻璃上的倒影”\n],\n“运动”： {\n“type”： “标志到液体到物体”，\n“details”： “标志荡漾融化成红色的溪流，形成瓶子并打开”\n  },\n“ending”： “瓶子直立，打开，冰冷而闪闪发光。淡入黑色。没有文字。\n“音频”： {\n“voice_over”： “无”，\n“music”： “温柔怀旧的原声弹奏或柔和的爵士钢琴”，\n“sfx”： “液体波纹，瓶子成型，嘶嘶声，瓶盖'pssst'”\n  },\n“text_overlay”： “无”，\n“格式”： “16：9”，\n“关键字”： [\n“可口可乐”，\n“玻璃瓶”，\n“液体转化”，\n“怀旧”，\n“品牌揭晓”，\n“电影”\n  ]\n}",
    },
    {
        "label": '📦 可口可乐广告',
        "category": '📦 品牌廣告',
        "title_zh": '可口可乐广告',
        "prompt_en": '{\n  "video_length": 8,\n  "scenes": [\n    {\n      "start": 0.0,\n      "end": 2.0,\n      "visual": "A cold Coca-Cola glass bottle stands upright against a deep red gradient background. It’s covered in glistening condensation. The red bottle cap, embossed with the Coca-Cola logo, shines under a spotlight. Vapor gently rises from the base.",\n      "camera": "quick dolly-in toward the bottle with a slight tilt up, shallow depth of field",\n      "sound": "soft ambient fizzing, subtle whoosh as camera moves"\n    },\n    {\n      "start": 2.0,\n      "end": 3.5,\n      "visual": "Close-up: the red Coca-Cola cap twists sharply and pops off with force. The cap spins in the air, showing the Coca-Cola logo in full as it rotates. Droplets fly off naturally with realistic gravity and inertia.",\n      "camera": "snap zoom-in then slow-motion tracking of the cap mid-air",\n      "sound": "crisp metallic twist, loud pop, carbonated hiss, followed by airy spin whoosh"\n    },\n    {\n      "start": 3.5,\n      "end": 5.5,\n      "visual": "The Coca-Cola liquid flows out slightly, then wraps around the bottle in a high-speed swirl. The swirl follows a natural spiral pattern, with tiny droplets flying in all directions — rendered with realistic physics. The bottle remains still at the center.",\n      "camera": "dynamic orbit shot around the bottle as liquid spins",\n      "sound": "rich flowing liquid SFX, sparkling fizz buildup, airy rise"\n    },\n    {\n      "start": 5.5,\n      "end": 8.0,\n      "visual": "Final wide shot: the Coca-Cola bottle stands proud in the center. Red background glows subtly. Coca-Cola logo fades in above the bottle. A voice clearly says \'Coca-Cola\' as the sonic sparkle finishes. Lens flare glides across as the screen fades out.",\n      "camera": "locked hero shot, slow ambient glow increase",\n      "sound": "bottle clink, soft chime, then voice saying \'Coca-Cola\' with natural tone"\n    }\n  ]\n}',
        "prompt_zh": '{\n"视频长度": 8,\n"场景": [\n    {\n"start": 0.0,\n      "end": 2.0,\n      "visual": "一个冰冷的可口可乐玻璃瓶直立在深红色渐变背景前。它覆盖着闪亮的冷凝水。带有可口可乐标志的红色瓶盖在聚光灯下闪耀。瓶底有轻柔的蒸汽升起。",\n      "camera": "快速向前推镜头靠近瓶子，略微向上倾斜，浅景深"\n"声音": "柔和的环境气泡声，相机移动时轻微的呼啸声"\n    },\n    {\n      "开始": 2.0,\n"end": 3.5,\n      "visual": "特写：红色可口可乐瓶盖猛地旋转并用力弹开。瓶盖在空中旋转，随着旋转可口可乐标志完全显现。水滴自然飞溅，具有逼真的重力和惯性效果。",\n      "camera": "快速拉近后转为空中瓶盖的慢动作跟踪",\n      "sound": "清脆的金属旋转声，响亮的弹开声，碳酸嘶嘶声，随后是空中的旋转呼啸声"\n    },\n    {\n"start": 3.5,\n      "end": 5.5,\n"视觉": "可口可乐液体略微流出，然后以高速旋转包裹瓶身。旋转遵循自然螺旋模式，细小的液滴向四面八方飞溅——采用逼真的物理渲染。瓶子保持在中心静止。",\n"相机": "围绕瓶子动态环绕拍摄，液体旋转时拍摄",\n"声音": "丰富的流动液体音效，气泡积聚的嘶嘶声，轻柔的上升声"\n    },\n    {\n"start": 5.5,\n      "end": 8.0,\n      "visual": "最终全景：可口可乐瓶子傲然立于画面中央。红色背景微弱发光。可口可乐标志在瓶子上方逐渐浮现。随着音效火花结束，清晰地说出\'可口可乐\'。镜头眩光划过，屏幕逐渐变暗。",\n"camera": "锁定主角镜头，环境光缓慢增强",\n      "sound": "瓶盖碰撞声，轻柔的叮铃声，随后是自然语调的‘可口可乐’声"\n    }\n  ]\n}',
    },
    {
        "label": '📦 中国女性介绍音箱产品',
        "category": '📦 品牌廣告',
        "title_zh": '中国女性介绍音箱产品',
        "prompt_en": 'tiktok 风格的影响者视频。一位年轻的中国女性举起并谈论这个产品，她用清晰的中文说到："欢迎大家来尝试我们家新出的 katon 音响，音质超一流，支持 ChatGPT"，用手机拍摄的低质量业余视频。',
        "prompt_zh": 'tiktok 风格的影响者视频。一位年轻的中国女性举起并谈论这个产品，她用清晰的中文说到："欢迎大家来尝试我们家新出的 katon 音响，音质超一流，支持 ChatGPT"，用手机拍摄的低质量业余视频。',
    },

    # 🎁 開箱產品
    {
        "label": '🎁 开箱-亚马逊盒子',
        "category": '🎁 開箱產品',
        "title_zh": '开箱-亚马逊盒子',
        "prompt_en": '{\n  "scene_description": "A dull backyard seen from above. An Amazon package sits in the center. It opens instantly, triggering a fast, rhythmic transformation: sofas, pergola, fire pit, table, chairs, trees, plants, and lights blop into place, turning the space into a lush, high-end garden.",\n  "visual_style": "realistic",\n  "camera_movement": "aerial descent, then slow tracking-in as the garden builds",\n  "main_subject": "Amazon box triggering the creation of a furnished modern garden",\n  "background_setting": "residential backyard",\n  "lighting_mood": "warm natural afternoon light",\n  "audio_cue": "clean blop sounds for each object; soft ambient nature background"\n}',
        "prompt_zh": '{\n“scene_description”： “从上面看，一个沉闷的后院。一个亚马逊包裹位于中间。它立即打开，引发快速、有节奏的转变：沙发、凉棚、火坑、桌子、椅子、树木、植物和灯光就位，将空间变成一个郁郁葱葱的高端花园。\n“visual_style”： “现实的”，\n“camera_movement”： “空中下降，然后随着花园的建造而缓慢跟踪”，\n“main_subject”： “亚马逊盒子触发了带家具的现代花园的创建”，\n“background_setting”： “住宅后院”，\n“lighting_mood”：“温暖的自然午后光”，\n“audio_cue”： “每个对象的干净哔哔声;柔和的环境自然背景”\n}',
    },
    {
        "label": '🎁 开箱1',
        "category": '🎁 開箱產品',
        "title_zh": '开箱1',
        "prompt_en": '{\n  "scene and action": "A woman stands in a completely empty kids bedroom in the morning light. A sealed box sits on the floor with the label \'Kids Room in a box\'. The box rattles, then opens. Colorful, playful furniture pieces rapidly assemble , snapping, sliding, and unfolding across the room. As a bookshelf clicks into place and the bed rolls in, the girl watches calmly and says, \'Well..." and while the room finishes assembling into a bright, tidy, playful kids space takes her phone out and start scrolling and say "let[s see....husband in a box.... .",\n  "camera angle": "fixed static ",\n  "lighting": "natural soft morning light",\n  "room": "kids bedroom",\n  "ratio": "16:9",\n"character" : blonde woman\n"voice" : joyful and funny\n  "furniture": [\n    "low bed with animal-print sheets",\n    "toy storage",\n    "bookshelves",\n    "desk and chair",\n    "morning light",\n    "wall decals",\n    "rug",\n    "plush toys",\n    "bean bag",\n    "child’s wardrobe",\n    "curtains",\n    "carton box with text Kids Room in a box"\n  ],\n  "action and motion": "box opens, elements move quickly into place, sliding, folding, stacking automatically",\n  "keywords": [\n    "kids room",\n    "no text",\n    "fast motion",\n    "pastel tones",\n    "room kids design"\n  ]\n}',
        "prompt_zh": '{\n“scene and action”： “一个女人在晨光下站在一间完全空荡荡的儿童卧室里。地板上放着一个密封的盒子，上面贴着“盒子里的儿童房”的标签。盒子嘎嘎作响，然后打开。色彩缤纷、俏皮的家具在房间里迅速组装、折断、滑动和展开。当书架咔哒一声就位，床滚进来时，女孩平静地看着说，“好吧......”当房间完成组装成一个明亮、整洁、有趣的儿童空间时，她拿出手机开始滚动并说：“让我们看看......盒子里的丈夫......“，\n“camera angle”： “固定静态”，\n“lighting”：“自然柔和的晨光”，\n“room”： “儿童卧室”，\n“ratio”： “16：9”，\n“角色”：金发女人\n《声音》：欢乐搞笑\n“家具”： [\n“带动物图案床单的矮床”，\n“玩具储物”，\n“书架”，\n“书桌椅”，\n“晨光”，\n“墙贴”，\n“地毯”，\n“毛绒玩具”，\n“豆袋”，\n“孩子的衣橱”，\n“窗帘”，\n“纸箱，上面写着盒子里的儿童房”\n],\n“action and motion”： “盒子打开，元素快速移动到位，自动滑动、折叠、堆叠”，\n“关键字”： [\n“儿童房”，\n“无文本”，\n“快动作”，\n“柔和的色调”，\n“房间儿童设计”\n  ]\n}',
    },
    {
        "label": '🎁 行李箱快速旋转',
        "category": '🎁 開箱產品',
        "title_zh": '行李箱快速旋转',
        "prompt_en": '{\n  "description": "Cinematic editorial shot of an upright transparent suitcase in a plain white cyclorama studio. A burst of yellow mist fills the suitcase as it spins rapidly, transforming mid-spin into a solid yellow hard-shell suitcase. The camera pushes in smoothly before holding on the final form.",\n  "style": "editorial cinematic",\n  "camera": "precision dolly-in from 2.5m to 1.5m over 5 seconds, then static hero shot",\n  "lighting": "clean, soft, and even—no visible light sources or reflections; lighting wraps naturally with minimal shadowing",\n  "room": "plain infinite white cyclorama (no texture, no visible lights, seamless floor-to-wall transition)",\n  "elements": [\n    "transparent upright suitcase",\n    "volumetric yellow mist",\n    "solid yellow hard-shell suitcase with ribbed structure",\n    "chrome latches and telescopic handle",\n    "soft reflective white floor",\n    "faint lingering mist at base"\n  ],\n  "motion": "yellow mist violently fills the suitcase in under 2s; suitcase spins upright on vertical axis and transforms mid-spin into solid yellow shell; spin halts cleanly; camera push-in and hold",\n  "ending": "suitcase stops mid-frame in bold yellow form; mist dissipates; fade to white",\n  "text": "none",\n  "keywords": [\n    "editorial",\n    "product transformation",\n    "white cyclorama",\n    "clean studio",\n    "yellow mist",\n    "no text",\n    "no humans",\n    "4K",\n    "minimalist"\n  ]\n}',
        "prompt_zh": '{\n“description”： “在纯白色天幕工作室中拍摄直立透明手提箱的电影剪辑镜头。当行李箱快速旋转时，一阵黄色的雾气充满了行李箱，在旋转过程中变成了一个实心的黄色硬壳行李箱。相机在保持最终形状之前平稳地推入。\n“style”： “编辑电影”，\n“camera”： “在 5 秒内从 2.5m 精确推车进入 1.5m，然后静态英雄拍摄”，\n“lighting”：“干净、柔和、均匀——没有可见的光源或反射;光线自然包裹，阴影最小“，\n“room”： “Plain Infinite White Cyclorama（无纹理，无可见光，无缝落地过渡）”，\n“元素”： [\n“透明直立行李箱”，\n“体积黄雾”，\n“罗纹结构的实心黄色硬壳手提箱”，\n“镀铬闩锁和伸缩手柄”，\n“柔和反光白色地板”，\n“底部微弱的挥之不去的雾气”\n],\n“motion”： “不到 2 秒，黄雾猛烈地填满了行李箱;手提箱在垂直轴上直立旋转，并将旋转中转变为实心黄色外壳;旋转干净地停止;相机推入并按住“，\n“ending”： “手提箱以粗体黄色的形式停在画面中间;雾气消散;褪色为白色“，\n“text”： “无”，\n“关键字”： [\n“社论”，\n“产品改造”，\n“白色天幕”，\n“干净的工作室”，\n“黄雾”，\n“无文本”，\n“没有人类”，\n“4K”，\n“极简主义”\n]\n}',
    },
    {
        "label": '🎁 开箱-IKEA',
        "category": '🎁 開箱產品',
        "title_zh": '开箱-IKEA',
        "prompt_en": '{\n  "description": "Cinematic shot of a sunlit Scandinavian bedroom. A sealed IKEA box trembles, opens, and flat pack furniture assembles rapidly into a serene, styled room highlighted by a yellow IKEA throw on the bed. No text.",\n  "style": cinematic",\n  "camera": "fixed wide angle",\n  "lighting": "natural warm with cool accents",\n  "room": "Scandinavian bedroom",\n  "elements": [\n    "IKEA box (logo visible)",\n    "bed with yellow throw",\n    "bedside tables",\n    "lamps",\n    "wardrobe",\n    "shelves",\n    "mirror",\n    "art",\n    "rug",\n    "curtains",\n    "reading chair",\n    "plants"\n  ],\n  "motion": "box opens, furniture assembles precisely and rapidly",\n  "ending": "calm, modern space with yellow IKEA accent",\n  "text": "none",\n  "keywords": [\n    "16:9",\n    "IKEA",\n    "Scandinavian",\n    "fast assembly",\n    "no text",\n    "warm & cool tones"\n  ]\n}',
        "prompt_zh": '{\n“description”： “阳光明媚的斯堪的纳维亚卧室的电影镜头。一个密封的宜家盒子颤抖着打开，扁平包装的家具迅速组装成一个宁静、有风格的房间，床上放着黄色的宜家毯子。没有文字。\n“style”：电影“，\n“camera”： “固定广角”，\n“lighting”：“自然温暖，带有冷色调”，\n“room”： “斯堪的纳维亚卧室”，\n“元素”： [\n“宜家盒子（标志可见）”，\n“带黄色毯子的床”，\n“床头柜”，\n“灯”，\n“衣柜”，\n“架子”，\n“镜像”，\n“艺术”，\n“地毯”，\n“窗帘”，\n“阅读椅”，\n“植物”\n],\n“motion”：“盒子打开，家具精确快速地组装”，\n“ending”：“平静、现代的空间，带有黄色宜家的口音”，\n“text”： “无”，\n“关键字”： [\n"16:9",\n“宜家”，\n“斯堪的纳维亚”，\n“快速组装”，\n“无文本”，\n“暖色调和冷色调”\n  ]\n}',
    },
    {
        "label": '🎁 开箱2',
        "category": '🎁 開箱產品',
        "title_zh": '开箱2',
        "prompt_en": 'empty bedroom with a medium sized cartoon box. boxed opened and suddenly room fully furnished',
        "prompt_zh": '空荡荡的卧室里有一个中等大小的卡通盒子。盒装打开，突然间房间家具齐全',
    },
    {
        "label": '🎁 开箱3',
        "category": '🎁 開箱產品',
        "title_zh": '开箱3',
        "prompt_en": '{\n  "description": "Cinematic shot of a sun-blasted Florida garage-bedroom hybrid. A sketchy, duct-taped flat-pack crate labeled “HANDLE WITH PRAYER” rattles like it’s trying to hatch a demon, then bursts open—parts ricochet everywhere, assembling themselves into an absurd gamer-lair crowned by a neon-pink flamingo blanket on the bed. No on-screen text.",\n  "style": "chaotic comedy",\n  "camera": "fixed wide angle (slightly shaky, like the cam operator is dodging shrapnel)",\n  "lighting": "blinding Gulf-Coast afternoon sunlight with sweaty RGB under-glow accents",\n  "room": "Florida-man garage-turned-bedroom (tool chests, surfboard, gator warning sign)",\n  "elements": [\n    "mystery crate (HANDLE WITH PRAYER stencil)",\n    "bed with neon-pink flamingo throw",\n    "tool-chest nightstands",\n    "lava-lamp bedside lights",\n    "wardrobe built from repurposed pallet wood",\n    "floating shelves holding an intimidating hot-sauce arsenal",\n    "mirror with a heroic crack",\n    "retro arcade poster wall art",\n    "pizza-slice area rug",\n    "curtains made from faded beach towels",\n    "bean-bag gaming throne",\n    "potted cactus wearing dollar-store sunglasses"\n  ],\n  "motion": "crate detonates popcorn-style; boards spin, screws zip, everything snap-locks with cartoon THWOOPS; final touch—a lone screwdriver drops from the ceiling, thunk.",\n  "ending": "camera creeps in on the now-pristine, ridiculous space as a ‘SEND IT’ neon sign flickers triumphantly above the bed.",\n  "text": "none (crate stencil counts as prop, not overlay)",\n  "keywords": [\n    "16:9",\n    "Florida-man",\n    "flat-pack mayhem",\n    "fast assembly",\n    "neon flamingo",\n    "hot & cool tones"\n  ]\n}',
        "prompt_zh": '{\n“description”： “佛罗里达州车库卧室混合体的电影镜头。一个标有“HANDLE WITH PRAYER”的粗略胶带扁平包装板条箱嘎嘎作响，就像它试图孵化恶魔一样，然后爆裂开来——零件到处弹跳，组装成一个荒谬的游戏玩家巢穴，床上铺着一条霓虹粉色的火烈鸟毯子。没有屏幕上的文字。\n“style”： “混乱喜剧”，\n“camera”： “固定广角（略微晃动，就像凸作员在躲避弹片）”，\n“lighting”： “墨西哥湾沿岸午后的阳光令人眼花缭乱，带有汗流浃背的 RGB 底光点缀”，\n“room”： “佛罗里达人车库改建的卧室（工具箱、冲浪板、鳄鱼警告标志）”，\n“元素”： [\n“神秘板条箱（HANDLE WITH PRAYER 模板）”，\n“带霓虹粉色火烈鸟毯的床”，\n“工具箱床头柜”，\n“熔岩灯床头灯”，\n“用重新利用的托盘木制成的衣柜”，\n“漂浮的架子上装着令人生畏的辣酱库”，\n“英勇裂纹的镜子”，\n“复古街机海报墙艺术”，\n“披萨片区域地毯”，\n“用褪色的沙滩巾制成的窗帘”，\n“豆袋游戏王座”，\n“戴着一元店太阳镜的盆栽仙人掌”\n],\n“motion”： “板条箱引爆爆米花式;木板旋转，螺丝拉链，一切都用卡通 THWOOPS 卡扣锁;最后的润色——一把孤零零的螺丝刀从天花板上掉下来，砰的一声。\n“ending”： “摄像机悄悄进入现在原始、荒谬的空间，床头上方\'SEND IT\'霓虹灯得意洋洋地闪烁。”\n“text”： “none （crate stencil 算作 prop，而不是叠加）”，\n“关键字”： [\n"16:9",\n“佛罗里达人”，\n“扁平包装混乱”，\n“快速组装”，\n“霓虹火烈鸟”，\n“冷热色调”\n  ]\n}',
    },
    {
        "label": '🎁 开箱-未来主义',
        "category": '🎁 開箱產品',
        "title_zh": '开箱-未来主义',
        "prompt_en": "Photorealistic cinematic shot of an empty [未来主义极简风格] bedroom with white wood floors and soft daylight streaming in. A sealed [印有'Orange AI'标志的金属科技箱] sits in the center. It wiggles, then bursts open in a bright, [橙色] sparkly puff. The room transforms instantly into a [未来科技实验室] sanctuary. No text. 风格: photorealistic cinematic 镜头: fixed wide angle, front-facing for symmetrical reveal 灯光: soft, diffused natural light with subtle [橙色] glow accents 房间: blank [未来主义极简风格] bedroom transformed into a [未来科技实验室] sanctuary 核心元素: [印有'Orange AI'标志的金属科技箱] (logo and details visible) [全息数据显示屏和人体工学指挥椅] plushies ([瓦力机器人模型], [MOSS核心单元模型], [大白模型], [塔奇克马模型]) wall art or framed posters of [J.A.R.V.I.S.界面] and their world floating shelves with figurines and [橙色] accessories vanity with mirror and [橙色] chair [AI实验室] lamp or a neon sign of a [大脑神经元符号] [电路板图案] rug or fluffy floor mat [机器人头盔]-shaped throw pillows 动态: [印有'Orange AI'标志的金属科技箱] opens, themed [人工智能] items explode out and assemble rapidly and precisely, [一只拟人化的橘子出现在桌前对着麦克风说话] 结局: soft, cozy [未来科技实验室] room glowing with [橙色] warmth and [智能与创新] charm 文本: none 关键词: 16:9, [人工智能], [科幻电影], [橙色] bedroom, fast assembly, no text, photorealistic, [橙色] explosion, [智能与创新]",
        "prompt_zh": "Photorealistic cinematic shot of an empty [未来主义极简风格] bedroom with white wood floors and soft daylight streaming in. A sealed [印有'Orange AI'标志的金属科技箱] sits in the center. It wiggles, then bursts open in a bright, [橙色] sparkly puff. The room transforms instantly into a [未来科技实验室] sanctuary. No text. 风格: photorealistic cinematic 镜头: fixed wide angle, front-facing for symmetrical reveal 灯光: soft, diffused natural light with subtle [橙色] glow accents 房间: blank [未来主义极简风格] bedroom transformed into a [未来科技实验室] sanctuary 核心元素: [印有'Orange AI'标志的金属科技箱] (logo and details visible) [全息数据显示屏和人体工学指挥椅] plushies ([瓦力机器人模型], [MOSS核心单元模型], [大白模型], [塔奇克马模型]) wall art or framed posters of [J.A.R.V.I.S.界面] and their world floating shelves with figurines and [橙色] accessories vanity with mirror and [橙色] chair [AI实验室] lamp or a neon sign of a [大脑神经元符号] [电路板图案] rug or fluffy floor mat [机器人头盔]-shaped throw pillows 动态: [印有'Orange AI'标志的金属科技箱] opens, themed [人工智能] items explode out and assemble rapidly and precisely, [一只拟人化的橘子出现在桌前对着麦克风说话] 结局: soft, cozy [未来科技实验室] room glowing with [橙色] warmth and [智能与创新] charm 文本: none 关键词: 16:9, [人工智能], [科幻电影], [橙色] bedroom, fast assembly, no text, photorealistic, [橙色] explosion, [智能与创新]",
    },
    {
        "label": '🎁 开箱-Chewy',
        "category": '🎁 開箱產品',
        "title_zh": '开箱-Chewy',
        "prompt_en": '{\n"description": "Cinematic shot of a sunlit, empty kitchen. A sealed Chewy box sits in the center. It trembles, explodes open in one burst, and pet supplies rapidly assemble into place: food and water bowls, a dog bed, toys, and a bag of food. A dog runs in and flops into the bed. No text.",\n"style": "cinematic",\n"camera": "fixed wide angle",\n"lighting": "natural warm with soft shadows",\n"room": "modern kitchen with hardwood floors",\n"elements": [\n"Chewy box (logo visible)",\n"dog food and water bowls", "\ndog bed",\n"dog toys (rope, ball, bone)",\n"bag of dog food",\n"wall hook with leash",\n"dog (golden retriever)" ],\n"motion": "box explodes open, dog items fly out and assemble rapidly and precisely",\n"ending": "dog enters and settles happily into the bed",\n"text": "none",\n"keywords": [\n"16:9",\n"Chewy",\n"pet supplies",\n"fast assembly",\n"dog",\n"no text",\n"warm lighting"\n]\n}',
        "prompt_zh": '{\n"description": "阳光明媚、空旷的厨房的影棚拍摄画面。一个密封的 Chewy 盒子位于中央。它颤抖着，突然爆炸开来，宠物用品迅速组装到位：食物和水碗、狗床、玩具和一袋食物。一只狗跑进来，扑到床上。无文字。",\n"风格": "电影感",\n"相机": "固定广角",\n"灯光": "自然温暖柔和阴影",\n"房间": "现代厨房，硬木地板"\n"元素": [\n"Chewy 盒子（可见标志）",\n"狗粮和水碗",\n"狗床",\n"狗玩具（绳索、球、骨头）",\n"狗粮袋",\n"带牵引绳的墙钩",\n"狗（金毛寻回犬）" ],\n"动作": "盒子爆炸打开，狗的物品飞出并迅速精确地组装起来",\n"结局": "狗进入并愉快地安顿在床上",\n"文字": "无",\n"关键词": []\n"16:9",\n"Chewy",\n"宠物用品",\n"快速组装",\n"狗",\n"无文字",\n"暖色调灯光"\n]\n}',
    },
    {
        "label": '🎁 开箱-淡粉色卧室',
        "category": '🎁 開箱產品',
        "title_zh": '开箱-淡粉色卧室',
        "prompt_en": '{ "description": "Photorealistic cinematic shot of an empty pastel-pink bedroom with white wood floors and soft daylight streaming in. A sealed Hello Kitty box with a pink bow sits in the center. It wiggles, then bursts open in a bright, sparkly puff. The room transforms instantly No text.", \n"style": "photorealistic cinematic", \n"camera": "fixed wide angle, front-facing for symmetrical reveal", \n"lighting": "soft, diffused natural light with subtle pink glow accents", \n"room": "blank pastel bedroom transformed into a Hello Kitty sanctuary", \n"elements": [ "Hello Kitty box (logo and bow visible)", "Hello Kitty bedding and pillows", \n"plushies (Hello Kitty, My Melody, Cinnamoroll, Kuromi)", "wall art or framed posters", "floating shelves with figurines and pastel accessories", "vanity with mirror and pink chair", "Hello Kitty lamp or neon sign", "heart rug or fluffy floor mat", "bow-shaped throw pillows" ], \n"motion": "box opens, cute Sanrio items explode out and assemble rapidly and precisely", "ending": "soft, cozy Hello Kitty room glowing with pink warmth and charm", \n"text": "none", \n"keywords": [ "16:9", "Hello Kitty", "Sanrio", "pastel bedroom", "fast assembly", "no text", "photorealistic", "pink explosion", "cozy kawaii" \n] \n}',
        "prompt_zh": '{ "description": "一张空旷的淡粉色卧室的逼真电影镜头拍摄照片，白色木地板和柔和的日光流进。一个系着粉色蝴蝶结的密封 Hello Kitty 盒子坐在中间。它晃动了一下，然后在一个明亮、闪亮的爆炸中打开。房间瞬间变化，没有文字。", \n"style": "逼真电影风格", \n"camera": "固定广角，正面拍摄以对称揭示"\n"光线": "柔和、散射的自然光，带有微妙的粉色光晕点缀", \n"房间": "空白的淡粉色卧室转变为 Hello Kitty 圣地", \n"元素": [ "Hello Kitty 盒子（标志和蝴蝶结可见）", "Hello Kitty 床品和枕头", \n"毛绒玩具（Hello Kitty、My Melody、Cinnamoroll、Kuromi）", "墙画或装裱海报", "带有摆件和淡粉色装饰品的悬浮架", "带镜子和粉色椅子的梳妆台", "Hello Kitty 灯或霓虹灯牌", "心形地毯或蓬松的地垫", "蝴蝶结形状的抱枕" ],\n"motion": "盒子打开，可爱的三丽鸥商品爆炸般飞出并迅速精确地组装起来", "ending": "柔和温馨的 Hello Kitty 房间散发着粉色温暖与魅力", \n"text": "无", \n"keywords": [ "16:9", "Hello Kitty", "三丽鸥", "淡彩色卧室", "快速组装", "无文字", "照片级真实", "粉色爆炸", "舒适可爱" ]\n] \n}',
    },
    {
        "label": '🎁 PS5控制器组装',
        "category": '🎁 開箱產品',
        "title_zh": 'PS5控制器组装',
        "prompt_en": '{\n  "shot": {\n    "composition": "fragmented pieces of a PS5 DualSense controller assembling mid-air with zero-gravity motion and explosive impact points",\n    "lens": "35mm virtual lens with fast rack focus and shallow depth of field on each part",\n    "frame_rate": "1000fps during slow-motion assembly, 60fps in between",\n    "camera_movement": "ultra-dynamic orbital spins, snap-zooms on triggers, inside-out fly-through of the controller body, ending in hard push-in on the completed device"\n  },\n\n  "subject": {\n    "description": "PS5 DualSense controller forming from raw floating components — triggers, face buttons, analog sticks, haptic core — coming together with sonic force",\n    "wardrobe": "",\n    "props": "transparent trigger shells, vibrating actuator module, light bar strip, PlayStation symbols spinning before locking into buttons"\n  },\n\n  "scene": {\n    "location": "digital void resembling a dark console startup space with particle fog and ambient grid lighting",\n    "time_of_day": "stylized tech-space",\n    "environment": "hovering digital dust, low-lying mist, energy lines pulsing with every part assembled"\n  },\n\n  "visual_details": {\n    "action": "each piece enters frame like a precision missile, locking into place with sonic booms — thumbsticks spiral in, faceplate slams down with micro-explosions of light, final PlayStation logo burns in at the center — controller lands on glass surface, sending out shock ripples and lighting up its LEDs",\n    "special_effects": "light trail streaks, magnetic snap FX, glitch pulses, haptic vibration simulated in slow motion, LED ignition flare",\n    "hair_clothing_motion": ""\n  },\n\n  "cinematography": {\n    "lighting": "pulsed spotlight bursts from above and below, reflective surfaces bouncing light off every plastic curve",\n    "color_palette": "ice white, midnight black, pulse blue, reactive neon flares",\n    "tone": "tech-futuristic, powerful, sleek"\n  },\n\n  "audio": {\n    "music": "cinematic synthwave with layered build-ups and sharp percussive drops",\n    "ambient": "low digital hum, frequency sweeps, energy pulses rising",\n    "sound_effects": "clicks, pressure pops, deep magnetic lock-ins, startup chime reimagined as an impact sting",\n    "mix_level": "studio-grade mix with 3D stereo positioning, sharp highs for clicks and wide low-end on impacts"\n  },\n\n  "dialogue": {\n    "character": "",\n    "line": "",\n    "subtitles": false\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n"composition": "PS5 DualSense 控制器的碎片在空中组装，具有零重力运动和爆炸性撞击点",\n“镜头”：“35mm 虚拟镜头，具有快速对焦和各部分浅景深”，\n"frame_rate": "慢动作组装时 1000fps，中间 60fps",\n"camera_movement": "超动态轨道旋转，扳机快速缩放，控制器主体内外飞越，最后在完成的设备上用力推入"\n}，\n\n“主题”： {\n"description": "PS5 DualSense 控制器由原始浮动组件（扳机键、正面按钮、模拟摇杆、触觉核心）与声波力量相结合而成",\n“衣柜”： ””，\n“道具”：“透明扳机壳、振动执行器模块、灯条、在锁定按钮之前旋转的 PlayStation 符号”\n}，\n\n“场景”： {\n"location": "数字虚空类似于带有粒子雾和环境网格照明的黑暗控制台启动空间",\n"time_of_day": "风格化的科技空间",\n“环境”：“悬浮的数字尘埃，低洼的薄雾，能量线随着每个部件的组装而脉动”\n}，\n\n“视觉细节”：{\n“动作”：“每个部件都像一枚精确的导弹一样进入画面，在音爆中锁定到位——拇指杆盘旋而入，面板在微光爆炸中猛地落下，最后的 PlayStation 标志在中心燃烧——控制器落在玻璃表面上，发出冲击波并点亮其 LED”，\n"special_effects": "光迹条纹、磁力捕捉特效、故障脉冲、慢动作模拟触觉振动、LED 点火火焰",\n"hair_clothing_motion": ""\n}，\n\n“电影摄影”：{\n"lighting": "脉冲聚光灯从上方和下方射出，反射面将光线从每个塑料曲线上反射回来",\n"color_palette": "冰白色、午夜黑色、脉冲蓝色、反应霓虹光",\n“tone”：“科技未来主义、强大、时尚”\n}，\n\n“声音的”： {\n"music": "具有层次感和尖锐打击乐效果的电影合成波",\n"ambient": "低数字嗡嗡声、频率扫描、能量脉冲上升",\n"sound_effects": "咔哒声、压力爆裂声、深度磁锁定、启动铃声被重新想象成撞击声",\n"mix_level": "录音棚级混音，具有 3D 立体声定位、清晰的点击高音和宽广的低音效果"\n}，\n\n“对话”：{\n“特点”： ””，\n“线”： ””，\n“字幕”：false\n}\n}',
    },

    # 🧱 微縮樂高黏土
    {
        "label": '🧱 微型乐高世界冒险',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '微型乐高世界冒险',
        "prompt_en": 'A dynamic camera glides through a miniature LEGO world, where an epic adventure unfolds. All sound effects—footsteps, explosions, cars, dragons—are created using mouth sounds by a single AI-generated voice artist. As each sound is made, the visuals instantly respond: LEGO characters jump into action, cars race, spaceships take off, volcanoes erupt. The journey moves through LEGO-built environments—city streets, underwater ruins, space stations, and lava lairs. The video is fast-paced, playful, and visually rich, like a blend between The LEGO Movie and next-gen AI storytelling. The sound-to-visual sync creates a magical, toy-driven universe where imagination controls reality.',
        "prompt_zh": '一个动态的摄像机穿梭于微型的乐高世界，在那里展开了一场史诗般的冒险。所有的音效——脚步声、爆炸声、汽车声、龙声——都是由一位 AI 生成的声音艺术家用口音制作的。每当一个声音被发出时，视觉效果就会立即响应：乐高角色跳入行动，汽车比赛，宇宙飞船起飞，火山爆发。旅程穿越乐高构建的环境——城市街道、水下废墟、太空站和熔岩洞穴。视频节奏快，充满趣味，视觉效果丰富，就像乐高电影和下一代AI故事讲述的结合。声音与视觉的同步创造了一个神奇的、玩具驱动的宇宙，在那里想象力控制着现实。',
    },
    {
        "label": '🧱 乐高分解为颗粒',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '乐高分解为颗粒',
        "prompt_en": '在一个充满趣味的一镜到底镜头中，经典的乐高标志将分解为无数色彩斑斓的积木颗粒，并在空中自动拼搭成一个充满想象力的模型。\n\n详细场景描述:\n\n画面始于一个纯白背景前，标志性的红色方形乐高（LEGO）标志静静悬浮。整个过程将由一个流畅、不间断的镜头完成。 标志突然轻微晃动，随后“咔”的一声，它分解为“L-E-G-O”四个独立的字母积木。紧接着，这四个字母再次爆开，化作一场五彩斑斓的积木“阵雨”倾泻而下。这些红、黄、蓝、白的标准积木颗粒在空中飞舞、旋转，被一股无形的力量牵引，以极快的速度和精准度相互“咔哒、咔哒”地扣合在一起。镜头可以跟随其中一块关键积木，看它如何找到自己的位置。最终，这些积木在空中完美地拼装成一个活泼的乐高小汽车模型。\n\n核心创意: 标志的解构与充满乐趣的重组。\n\n镜头与运镜: 严格的一镜到底（Single take / One-shot），可以带有趣味性的轻微环绕运镜，以展现拼搭过程的动态感。\n\n整体风格: 充满童趣、活泼、有创造力、令人满足。\n\n灯光: 明亮、均匀、欢快的影棚灯光，让积木的色彩显得格外鲜艳。\n\n环境: 纯白或浅灰色的极简背景，以最大限度地突出乐高积木的色彩。\n\n核心元素:\n\n经典的乐高标志\n\n分解后飞舞的各色积木颗粒\n\n空中自动拼搭的过程\n\n最终成型的乐高模型\n\n音效:\n\n背景音乐: 轻快、俏皮的旋律，可使用木琴、打击乐等乐器。\n\n特效音: 整个过程的核心是乐高积木相互扣合时清脆、悦耳、富有节奏感的“咔哒”声。\n\n结尾: 拼搭完成的乐高模型完美地静置在画面中央。画面淡出为白色。全程无任何文字。',
        "prompt_zh": '在一个充满趣味的一镜到底镜头中，经典的乐高标志将分解为无数色彩斑斓的积木颗粒，并在空中自动拼搭成一个充满想象力的模型。\n\n详细场景描述:\n\n画面始于一个纯白背景前，标志性的红色方形乐高（LEGO）标志静静悬浮。整个过程将由一个流畅、不间断的镜头完成。 标志突然轻微晃动，随后“咔”的一声，它分解为“L-E-G-O”四个独立的字母积木。紧接着，这四个字母再次爆开，化作一场五彩斑斓的积木“阵雨”倾泻而下。这些红、黄、蓝、白的标准积木颗粒在空中飞舞、旋转，被一股无形的力量牵引，以极快的速度和精准度相互“咔哒、咔哒”地扣合在一起。镜头可以跟随其中一块关键积木，看它如何找到自己的位置。最终，这些积木在空中完美地拼装成一个活泼的乐高小汽车模型。\n\n核心创意: 标志的解构与充满乐趣的重组。\n\n镜头与运镜: 严格的一镜到底（Single take / One-shot），可以带有趣味性的轻微环绕运镜，以展现拼搭过程的动态感。\n\n整体风格: 充满童趣、活泼、有创造力、令人满足。\n\n灯光: 明亮、均匀、欢快的影棚灯光，让积木的色彩显得格外鲜艳。\n\n环境: 纯白或浅灰色的极简背景，以最大限度地突出乐高积木的色彩。\n\n核心元素:\n\n经典的乐高标志\n\n分解后飞舞的各色积木颗粒\n\n空中自动拼搭的过程\n\n最终成型的乐高模型\n\n音效:\n\n背景音乐: 轻快、俏皮的旋律，可使用木琴、打击乐等乐器。\n\n特效音: 整个过程的核心是乐高积木相互扣合时清脆、悦耳、富有节奏感的“咔哒”声。\n\n结尾: 拼搭完成的乐高模型完美地静置在画面中央。画面淡出为白色。全程无任何文字。',
    },
    {
        "label": '🧱 乐高星球大战',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '乐高星球大战',
        "prompt_en": '{\n  "description": "Photorealistic cinematic shot of a sunlit minimalist living room. A sealed LEGO Star Wars Millennium Falcon box trembles, opens, and hundreds of detailed gray, silver, and blue LEGO pieces assemble rapidly into the iconic Millennium Falcon spacecraft—complete with rotating turrets, satellite dish, cockpit, and rear thrusters—on a large wooden table. No text.",\n  "style": "photorealistic cinematic",\n  "camera": "fixed overhead to capture full spacecraft layout",\n  "lighting": "natural bright with soft highlights and gentle shadows",\n  "room": "minimalist living room with large wooden table and neutral décor",\n  "elements": [\n    "LEGO Star Wars Millennium Falcon box (Star Wars logo visible)",\n    "gray, silver, and blue LEGO pieces",\n    "detailed Millennium Falcon body",\n    "rotating gun turrets",\n    "sensor dish",\n    "cockpit canopy",\n    "engine thrusters",\n    "boarding ramp extended",\n    "LEGO Star Wars minifigures (Han Solo, Chewbacca, Leia, C-3PO, R2-D2)",\n    "small display of spare tools and blasters nearby"\n  ],\n  "motion": "box rattles, lid bursts open, bricks and plates fly out and lock together mid-air to form the Millennium Falcon, rotating turrets and sensor dish assemble dynamically, minifigures position themselves around the ship",\n  "ending": "a fully assembled, iconic LEGO Millennium Falcon glistens in sunlight across the table, cockpit facing forward",\n  "text": "none",\n  "keywords": [\n    "16:9",\n    "LEGO Star Wars",\n    "Millennium Falcon",\n    "fast assembly",\n    "photorealistic",\n    "no text",\n    "overhead shot",\n    "bright natural lighting",\n    "detailed spacecraft"\n  ]\n}',
        "prompt_zh": '{\n "描述": "阳光明媚的极简主义客厅的逼真电影镜头。一个密封的乐高星球大战千年隼盒子颤抖、打开，数百个详细的灰色、银色和蓝色乐高零件迅速组装成标志性的千年隼太空船——配有旋转炮塔、卫星天线、驾驶舱和后部推进器——放在一张大木桌上。没有文字。",\n "风格": "逼真电影"\n"相机": "固定在头顶以捕捉完整航天器布局",\n  "照明": "自然明亮，带有柔和高光和柔和阴影",\n  "房间": "极简主义客厅，有大木桌和中性装饰",\n  "元素": []\n"乐高星球大战千年隼盒子（可见星球大战标志）",\n"灰色、银色和蓝色的乐高零件",\n"细节丰富的千年隼机身",\n"旋转的炮塔"\n"传感器碟",\n"驾驶舱罩",\n"引擎推进器",\n"登机坡道展开"\n"乐高星球大战小人（汉·索罗、楚巴卡、莉亚公主、C-3PO、R2-D2)",\n"附近摆放着一些小工具和激光枪"\n],\n"动作": "盒子发出嘎嘎声，盖子突然炸开，积木和底板飞出并在空中锁在一起形成千年隼，旋转炮塔和传感器盘动态组装，小人围绕飞船定位"\n"结尾": "一辆完全组装好的、标志性的乐高千年隼在阳光下闪闪发光，停在桌子上，驾驶舱朝前",\n"text": "none",\n"关键词": [\n    "16:9"\n"乐高星球大战",\n"千年隼",\n"快速组装",\n"照片级真实感",\n"没有文字",\n"俯拍视角",\n"明亮自然光照",\n"精细的航天器"\n  ]\n}',
    },
    {
        "label": '🧱 黏土动画《哈利·波特》探出火车窗外',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '黏土动画《哈利·波特》探出火车窗外',
        "prompt_en": '{\n  "shot": {\n    "composition": "sweeping wide claymation shot of the Hogwarts Express approaching the castle",\n    "lens": "virtual tilt-shift clay camera with exaggerated depth",\n    "frame_rate": "12fps classic stop-motion pace",\n    "camera_movement": "dolly shot following train, crane-style tilt up to reveal clay Hogwarts"\n  },\n\n  "subject": {\n    "description": "claymation Harry Potter leaning out of the train window, eyes wide with wonder",\n    "wardrobe": "miniature sculpted robes, scarf with moving clay fringe, round glasses molded on",\n    "props": "clay owl in cage, sculpted suitcase with spellbooks, hand-shaped wand in pocket"\n  },\n\n  "scene": {\n    "location": "Hogwarts Express track curving beside a clay river, leading to Hogwarts castle on a hill",\n    "time_of_day": "twilight with fading sculpted sky gradients",\n    "environment": "rolling clay hills, fiber-clouds on strings, flickering castle windows made of translucent clay"\n  },\n\n  "visual_details": {\n    "action": "train puffs clay steam as Harry gazes at the glowing castle, cloak fluttering slightly",\n    "special_effects": "stop-motion light flickers in the windows, twinkling stars added frame-by-frame",\n    "hair_clothing_motion": "Harry’s hair shifts subtly between frames, scarf bobs in the wind"\n  },\n\n  "cinematography": {\n    "lighting": "soft clay-style ambient lighting with glowing castle highlights",\n    "color_palette": "deep blues, warm golds, and hand-painted brick reds",\n    "tone": "magical, nostalgic, hand-crafted"\n  },\n\n  "audio": {\n    "music": "gentle clay-bell chimes and whimsical glockenspiel melody",\n    "ambient": "train wheels clacking, faint owl hoot, breeze on the hill",\n    "sound_effects": "soft clay footsteps, luggage bump, magical sparkle twinkles",\n    "mix_level": "music-forward mix with delicate ambient textures"\n  },\n\n  "dialogue": {\n    "character": "Harry Potter (child voice, claymation-style)",\n    "line": "Is that... Hogwarts?",\n    "subtitles": false\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n“构图”：“霍格沃茨特快列车驶近城堡的广角黏土动画镜头”，\n“镜头”：“具有夸张深度的虚拟移轴粘土相机”，\n"frame_rate": "12fps 经典定格动画速度",\n"camera_movement": "移动摄影机跟随火车拍摄，起重机式倾斜以显示粘土霍格沃茨"\n}，\n\n“主题”： {\n"description": "黏土动画《哈利·波特》探出火车窗外，惊奇地睁大眼睛",\n"wardrobe": "微型雕刻长袍、带有动态粘土流苏的围巾、模制圆形眼镜",\n“道具”：“笼子里的粘土猫头鹰，装有咒语书的雕刻手提箱，口袋里的手形魔杖”\n}，\n\n“场景”： {\n"location": "霍格沃茨特快列车轨道沿着一条粘土河蜿蜒而行，通往山上的霍格沃茨城堡",\n"time_of_day": "暮色渐浓，天空的渐变色逐渐褪色",\n“环境”：“起伏的粘土山丘，弦上的纤维云，由半透明粘土制成的闪烁的城堡窗户”\n}，\n\n“视觉细节”：{\n"action": "火车喷出泥土蒸汽，哈利凝视着发光的城堡，斗篷微微飘动"\n"special_effects": "定格动画的灯光在窗户中闪烁，闪烁的星星逐帧添加",\n"hair_clothing_motion": "哈利的头发在各个画面之间微妙地移动，围巾在风中飘动"\n}，\n\n“电影摄影”：{\n"lighting": "柔和的粘土风格环境照明，带有发光的城堡亮点",\n"color_palette": "深蓝色、暖金色和手绘砖红色",\n“tone”：“神奇、怀旧、手工制作”\n}，\n\n“声音的”： {\n“音乐”：“轻柔的陶铃声和异想天开的钟琴旋律”，\n"ambient": "火车车轮的咔哒声、微弱的猫头鹰鸣叫声、山上的微风",\n"sound_effects": "柔软的粘土脚步声、行李碰撞声、魔法闪光闪烁",\n"mix_level": "具有精致环境纹理的音乐前向混合"\n}，\n\n“对话”：{\n"character": "哈利·波特（童声，黏土动画风格）",\n"line": "那是...霍格沃茨吗？",\n“字幕”：false\n}\n}',
    },
    {
        "label": '🧱 粘土动画库珀身着雕刻的飞行服',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '粘土动画库珀身着雕刻的飞行服',
        "prompt_en": '{\n  "shot": {\n    "composition": "top-down spinning claymation shot of the Endurance aligning with the docking station",\n    "lens": "virtual macro lens with slight barrel distortion for handmade effect",\n    "frame_rate": "12fps with deliberate clay flicker",\n    "camera_movement": "rotational tracking around the spinning ships, tightening as docking nears"\n  },\n\n  "subject": {\n    "description": "claymation Cooper in a sculpted flight suit, intensely controlling the Endurance as it rotates into place",\n    "wardrobe": "tiny molded astronaut suit with moving clay tubes and helmet visor reflections",\n    "props": "hand-sculpted console with blinking lights, rotating docking clamps, clay ring segments"\n  },\n\n  "scene": {\n    "location": "orbit above a stylized black hole with painted light swirl backdrop",\n    "time_of_day": "deep space — star-speckled black with ambient glow from distant galaxy",\n    "environment": "floating clay debris, sculpted ring shadows, mini clay model of Gargantua in the distance"\n  },\n\n  "visual_details": {\n    "action": "the ships spin faster, Cooper aligns them with pinpoint timing, the clamps connect in a satisfying clay click",\n    "special_effects": "hand-drawn star trails, layered glow from the black hole, clay particles flung by centrifugal motion",\n    "hair_clothing_motion": "helmet strap sways inside the capsule, clay fingers twitch on the controls"\n  },\n\n  "cinematography": {\n    "lighting": "subtle clay studio-style lighting with harsh contrast from the black hole side",\n    "color_palette": "matte black, dusty gray, and blue glow tones with bursts of warm orange during connection",\n    "tone": "intense, handcrafted, suspenseful"\n  },\n\n  "audio": {\n    "music": "claypipe organ version of Interstellar theme with chime loops",\n    "ambient": "muted beeps, radio static, deep space hum",\n    "sound_effects": "clicking clay clamps, creaky plastic panels, muffled breathing inside helmet",\n    "mix_level": "music builds to climax with sound FX punched forward during final lock"\n  },\n\n  "dialogue": {\n    "character": "Cooper (claymation voice)",\n    "line": "Hold on... we’re going to dock manually.",\n    "subtitles": false\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n"composition": "自上而下的旋转黏土动画镜头，展现耐力号与对接站对齐的场景",\n“镜头”：“带有轻微桶形失真的虚拟微距镜头，可实现手工效果”，\n"frame_rate": "12fps，故意使粘土闪烁",\n"camera_movement": "围绕旋转的船只进行旋转跟踪，随着对接的临近而收紧"\n}，\n\n“主题”： {\n"description": "粘土动画库珀身着雕刻的飞行服，密切控制着耐力号旋转到位",\n“衣柜”：“微型模制宇航服，带有移动粘土管和头盔面罩反射”，\n“道具”：“手工雕刻的控制台，带有闪烁的灯光、旋转的对接夹、粘土环段”\n}，\n\n“场景”： {\n“location”：“围绕风格化的黑洞运行，背景为彩绘的灯光漩涡”，\n"time_of_day": "深空——星光点缀的黑色，周围散发着来自遥远星系的光芒",\n“环境”：“漂浮的粘土碎片，雕刻的环形阴影，远处的 Gargantua 迷你粘土模型”\n}，\n\n“视觉细节”：{\n“动作”：“飞船旋转得更快，库珀以精确的时间对准它们，夹具连接在一起，发出令人满意的粘土咔哒声”，\n"special_effects": "手绘星迹、黑洞的分层辉光、离心运动甩出的粘土颗粒",\n"hair_clothing_motion": "头盔带在太空舱内摇晃，粘土手指在控制器上抽搐"\n}，\n\n“电影摄影”：{\n"lighting": "微妙的粘土工作室风格灯光与黑洞侧面的强烈对比",\n"color_palette": "哑光黑色、灰暗灰色和蓝色光晕色调，连接时伴有暖橙色"\n“tone”：“紧张、精心制作、悬念迭起”\n}，\n\n“声音的”： {\n"music": "带有钟声循环的星际主题的陶土管风琴版本",\n"ambient": "静音哔哔声、无线电静电噪音、深空嗡嗡声",\n"sound_effects": "咔哒咔哒的粘土夹子声、吱吱作响的塑料面板声、头盔内低沉的呼吸声",\n"mix_level": "音乐在最后的锁定过程中随着音效的推进而达到高潮"\n}，\n\n“对话”：{\n"character": "Cooper (黏土动画配音)",\n"line": "按住on...我们将手动停靠。",\n“字幕”：false\n}\n}',
    },
    {
        "label": '🧱 黏土动画比尔博·巴金斯走过一座金山',
        "category": '🧱 微縮樂高黏土',
        "title_zh": '黏土动画比尔博·巴金斯走过一座金山',
        "prompt_en": '{\n  "shot": {\n    "composition": "medium-wide shot with claymation-style depth and handcrafted textures",\n    "lens": "50mm virtual stop-motion lens with slight fisheye distortion",\n    "frame_rate": "12fps to mimic traditional claymation pacing",\n    "camera_movement": "slow dolly push-in toward Bilbo, with sudden tilt up on dragon reveal"\n  },\n\n  "subject": {\n    "description": "claymation Bilbo Baggins, wide-eyed and trembling, tiptoes across a mountain of gold",\n    "wardrobe": "tiny sculpted wool cloak, clay sword, hand-textured curls",\n    "props": "glittered clay coins, oversized goblets, clay Arkenstone glowing subtly"\n  },\n\n  "scene": {\n    "location": "Smaug’s hoarded treasure hall under the Lonely Mountain",\n    "time_of_day": "dim cavern lit by fire-glow and scattered treasure reflections",\n    "environment": "clay-crafted columns, soot-blackened walls, gold piles molded with finger prints"\n  },\n\n  "visual_details": {\n    "action": "Bilbo freezes as a low rumble shakes the hoard and a massive clay claw emerges",\n    "special_effects": "stop-motion fire breath effect using layered painted cellophane, glowing eyes frame-by-frame animated",\n    "hair_clothing_motion": "subtle, jittery frame-to-frame cloak motion and expressive clay eye shifts"\n  },\n\n  "cinematography": {\n    "lighting": "warm clay-fire bounce lighting mixed with cool cavern shadows",\n    "color_palette": "burnt oranges, muted browns, deep shadows, with gold shimmer",\n    "tone": "tense, handcrafted, whimsically eerie"\n  },\n\n  "audio": {\n    "music": "orchestral clay percussion and slow string plucks with echo",\n    "ambient": "distant rumbling, coin shifts, a single deep dragon breath",\n    "sound_effects": "creaky stop-motion footsteps, crackling treasure slide",\n    "mix_level": "ambience forward with subtle music underlay"\n  },\n\n  "dialogue": {\n    "character": "Smaug (claymation voice)",\n    "line": "I smell you, thief... Do not think you can hide from me.",\n    "subtitles": false\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n"composition": "具有黏土动画风格深度和手工制作纹理的中广角镜头",\n"lens": "50mm 虚拟定格镜头，略带鱼眼失真",\n"frame_rate": "12fps 模仿传统黏土动画的节奏",\n"camera_movement": "缓慢的移动摄影车向比尔博推近，当巨龙现身时突然向上倾斜"\n}，\n\n“主题”： {\n"description": "黏土动画比尔博·巴金斯，睁大眼睛，浑身颤抖，踮着脚尖走过一座金山",\n“衣柜”：“微型雕刻羊毛斗篷、粘土剑、手工纹理卷发”，\n“道具”：“闪闪发光的粘土硬币，超大高脚杯，粘土阿肯石散发着微妙的光芒”\n}，\n\n“场景”： {\n"location": "孤山之下史矛革的宝藏大厅",\n"time_of_day": "昏暗的洞穴被火光照亮，散落的宝藏倒影",\n“环境”：“粘土制作的柱子，烟灰熏黑的墙壁，用指纹塑造的金堆”\n}，\n\n“视觉细节”：{\n“动作”：“低沉的隆隆声震动了宝藏，一只巨大的粘土爪子浮现出来，比尔博僵住了”，\n"special_effects": "使用分层彩绘玻璃纸制作的定格火焰吐息效果，逐帧动画呈现发光的眼睛",\n"hair_clothing_motion": "微妙、抖动的逐帧斗篷运动和富有表现力的粘土眼球变化"\n}，\n\n“电影摄影”：{\n“照明”：“温暖的粘土火反射照明与凉爽的洞穴阴影混合”，\n"color_palette": "焦橙色、柔和的棕色、深色阴影、带有金色光泽",\n“语气”：“紧张、手工制作、怪诞怪诞”\n}，\n\n“声音的”： {\n"music": "管弦乐陶土打击乐和慢速弦乐拨奏，伴有回声",\n"ambient": "远处的隆隆声、硬币的移动声、一声深沉的龙息",\n"sound_effects": "吱吱作响的定格脚步声，噼啪作响的宝藏滑梯",\n"mix_level": "氛围突出，带有微妙的音乐底色"\n}，\n\n“对话”：{\n"character": "史矛革（黏土动画配音）",\n"line": "我闻到你了，小偷……别以为你能躲过我的追捕。",\n“字幕”：false\n}\n}',
    },

    # ✨ 特效奇幻
    {
        "label": '✨ 黑客帝国游戏',
        "category": '✨ 特效奇幻',
        "title_zh": '黑客帝国游戏',
        "prompt_en": 'Classic Scene Description:At the top of a skyscraper, in a torrential downpour, Neo, having just rescued Morpheus, stays behind to cover his allies\' escape, facing his nemesis, Agent Smith. When Smith draws his signature Desert Eagle and fires, Neo\'s latent potential as "The One" fully awakens. He no longer dodges but leans back, defying the laws of physics, as time itself seems to slow down. Bullets trail past him with a visible, rippling distortion of the air. This is the birth of the iconic "bullet time" in cinema history, symbolizing the awakening of Neo\'s belief in himself.\nCore Characters:\n\nNeo: At this moment, he is in the midst of his transformation from a confused programmer to the awakened savior. He wears his iconic long black trench coat and sunglasses, his expression focused and calm, filled with a newfound power and conviction.\n\nAgent Smith: A sentient program within the Matrix, appearing in human form. His actions are efficient, cold, and relentless. He wears a standard business suit, an earpiece, and sunglasses. He is the embodiment of control and the most formidable obstacle on Neo\'s path to awakening.\n\nGame Art Style: Pixel Art (16-bit Style)\n\nGame Genre: Side-Scrolling Action Shooter\n\nGamified Scene Recreation: The classic "bullet time" sequence is translated into a retro pixel art aesthetic with gameplay focused on precise movement and shooting.\n\nVisuals:The entire scene is a side-scrolling view rendered in a 16-bit pixel art style. The color palette is predominantly dark green and gray, reflecting the rainy night. Pixelated raindrops fall visibly, creating subtle reflections on the blocky rooftop tiles. The background features a low-resolution cityscape with simple, flickering pixelated neon signs written in a generic digital font. The player controls "Neo," depicted as a sprite with clear pixel definition, wearing his long black coat and sunglasses. When "Agent Smith," another similarly detailed sprite in a black suit and sunglasses, fires his weapon (represented by a small burst of pixels), the game enters a visual "bullet time" effect. While not a true slowdown of the game engine in the traditional sense of modern "bullet time," the animation of the bullets (larger, more distinct pixel shapes with a short trail of lighter pixels) becomes noticeably slower, and Neo gains a slightly increased window for movement. His dodge maneuver is a deliberate, frame-by-frame animation of him leaning back, perhaps with a slight pixelated "blur" effect to convey speed.\n\nUser Interface (UI):\nTop Left: A pixelated green bar represents Neo\'s health. Below it, a smaller, yellow pixelated bar indicates a "Focus" meter, which might be consumed by performing special actions or entering a heightened state reminiscent of his growing powers.\n\nTop Right: A simple pixelated score counter and possibly a combo counter that increases with rapid, successive shots.\n\nBottom Right: Icons representing Neo\'s currently equipped weapon (initially just fists, but potentially gaining access to pixelated firearms) and a numerical display of his ammo count (if applicable).\n\nMusic & Sound (Audio):\n\nBackground Music (BGM): A synthesized, chiptune rendition of a track from The Matrix soundtrack, perhaps a 16-bit interpretation of "Spybreak!" or another iconic theme, featuring driving rhythms and digitized instruments.\n\nSound Effects (SFX):\nBlocky, digitized gunshots ("pew-pew!").\nA distinct "whizz" or "zip" sound effect for the pixelated bullets as they travel through the air.\nA simple "thunk" sound when a character is hit.\nA brief, digitized sound effect to signify the activation of a "Focus" state.',
        "prompt_zh": '经典场景描述：在摩天大楼的顶层，在倾盆大雨中，刚刚救出墨菲斯的尼奥留下来掩护盟友的逃跑，面对他的宿敌史密斯特工。当史密斯抽出他标志性的沙漠之鹰并开火时，尼奥作为“The One”的潜在潜力完全觉醒。他不再躲闪，而是向后倾斜，违背物理定律，因为时间本身似乎变慢了。子弹从他身边掠过，空气中出现了明显的涟漪扭曲。这是电影史上标志性的“子弹时间”的诞生，象征着尼奥对自己的信念的觉醒。\n核心人物：\n\n尼奥：此刻，他正处于从一个迷茫的程序员到觉醒的救世主的转变之中。他穿着标志性的黑色长风衣，戴着墨镜，表情专注而平静，充满了一种新发现的力量和信念。\n\n史密斯特工：黑客帝国中的一个有知觉的程序，以人类形态出现。他的行动高效、冷酷、无情。他穿着标准的西装，戴着耳机，戴着墨镜。他是控制的化身，也是尼奥觉醒之路上最可怕的障碍。\n\n游戏艺术风格：像素艺术（16 位风格）\n\n游戏类型：横向卷轴动作射击游戏\n\n游戏化场景再现：经典的“子弹时间”序列被转化为复古像素艺术美学，游戏玩法侧重于精确移动和射击。\n\n视觉效果：整个场景是以 16 位像素艺术风格渲染的横向卷轴视图。调色板以深绿色和灰色为主，反映了雨夜。像素化的雨滴明显落下，在块状屋顶瓦片上产生微妙的反射。背景是低分辨率的城市景观，带有简单、闪烁的像素化霓虹灯标志，以通用数字字体书写。玩家控制“Neo”，被描绘成一个像素清晰度的精灵，穿着黑色长外套，戴着墨镜。当“史密斯特工”（另一个穿着黑色西装、戴着墨镜的类似细节精灵）开火时（由一小段像素表示），游戏进入视觉“子弹时间”效果。虽然不是传统意义上的现代“子弹时间”游戏引擎的真正减速，但子弹的动画（更大、更明显的像素形状和较浅的像素的短轨迹）变得明显变慢，并且 Neo 获得了稍微增加的移动窗口。他的闪避动作是他故意向后倾斜的逐帧动画，也许带有轻微的像素化“模糊”效果来传达速度。\n\n用户界面 （UI）：\n左上：像素化的绿色条代表 Neo 的生命值。在它下面，一个较小的黄色像素条表示一个“专注”表，可以通过执行特殊动作或进入让人想起他不断增长的力量的高度状态来消耗它。\n\n右上：一个简单的像素化分数计数器，可能还有一个组合计数器，随着快速、连续的射击而增加。\n\n右下：代表尼奥当前装备的武器（最初只是拳头，但有可能获得像素化枪支）的图标和弹药数量的数字显示（如果适用）。\n\n音乐和声音（音频）：\n\n背景音乐 （BGM）：《黑客帝国》原声带中曲目的合成芯片曲演绎，可能是对“Spybreak！”或其他标志性主题的 16 位诠释，具有驱动节奏和数字化乐器。\n\n音效 （SFX）：\n块状的、数字化的枪声（“pew-pew！\n像素化子弹在空中传播时发出明显的“嗖嗖”或“拉链”音效。\n角色被击中时发出简单的“砰砰”声。\n简短的数字化音效，表示“专注”状态的激活。',
    },
    {
        "label": '✨ 动漫风格的战斗',
        "category": '✨ 特效奇幻',
        "title_zh": '动漫风格的战斗',
        "prompt_en": 'Anime-style combat sequence: two rivals fight in an abandoned factory — the camera bounces with each impact, handheld-style — steel sparks, crates shatter, and their final clash sends a shockwave through the walls',
        "prompt_zh": '动漫风格的战斗序列：两个对手在废弃工厂中战斗——摄像机随着每次撞击而晃动，手持式拍摄——钢花四溅，箱子碎裂，他们的最终碰撞在墙壁上激起冲击波',
    },
    {
        "label": '✨ 蜜蜂惊慌失措地全速穿过大学走廊',
        "category": '✨ 特效奇幻',
        "title_zh": '蜜蜂惊慌失措地全速穿过大学走廊',
        "prompt_en": '{\n  "shot": {\n    "composition": "tight rear POV shot directly behind frantic bee, wings vibrating violently in frame",\n    "lens": "GoPro ultra-wide with extreme distortion to amplify speed",\n    "frame_rate": "180fps with ramping slow-motion bursts on near collisions",\n    "camera_movement": "hyper-fast forward rush with jitter, mimicking chaotic flight path"\n  },\n  "subject": {\n    "description": "bee racing full throttle through university corridors in panic, wings shaking violently",\n    "wardrobe": "",\n    "props": "students dodging aside, papers and books scattering, doors slamming open"\n  },\n  "scene": {\n    "location": "endless university hallway with fluorescent lights and lockers",\n    "time_of_day": "midday rush, crowded corridors",\n    "environment": "blurred faces of surprised students, moving obstacles flying past in streaks"\n  },\n  "visual_details": {\n    "action": "bee blasts forward in straight chaotic line, barely missing heads and shoulders, narrowly escaping slamming doors and spinning around obstacles",\n    "special_effects": "extreme motion blur, speed warp trails, shockwave distortion around wings, lights streaking by"\n  },\n  "cinematography": {\n    "lighting": "harsh fluorescent lighting flickering as speed distorts space",\n    "color_palette": "cool whites, blurred neon streaks, chaotic color flashes from student clothing",\n    "tone": "frenetic, high-adrenaline, disorienting"\n  },\n  "audio": {\n    "music": "fast EDM with rising tempo and heavy drops synced to near misses",\n    "ambient": "chaotic corridor reverberation fading under speed",\n    "sound_effects": "intense buzzing amplified, violent whooshes, crashes and startled shouts passing rapidly",\n    "mix_level": "overwhelming immersive mix, pushing speed sensation"\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n“构图”：“从后方近距离拍摄疯狂蜜蜂的正后方，画面中蜜蜂的翅膀剧烈颤动”，\n“镜头”：“GoPro 超广角镜头，具有极强的失真度，可提高速度”，\n"frame_rate": "180fps，近距离碰撞时慢动作爆发",\n"camera_movement": "超快速度抖动前进，模仿混乱的飞行路径"\n}，\n“主题”： {\n"description": "蜜蜂惊慌失措地全速穿过大学走廊，翅膀剧烈颤抖",\n“衣柜”： ””，\n“道具”：“学生们闪开，纸张和书籍散落一地，门砰地一声打开”\n}，\n“场景”： {\n"location": "无尽的大学走廊，有荧光灯和储物柜",\n"time_of_day": "中午高峰，走廊拥挤",\n“环境”：“惊讶的学生的模糊面孔，移动的障碍物以条纹形式飞过”\n}，\n“视觉细节”：{\n"action": "蜜蜂以混乱的直线向前飞去，几乎没有击中头部和肩膀，险些撞到关门声和在障碍物周围旋转，"\n"special_effects": "极端运动模糊、速度扭曲轨迹、机翼周围的冲击波扭曲、灯光划过"\n}，\n“电影摄影”：{\n“照明”：“刺眼的荧光灯闪烁，速度扭曲了空间”，\n"color_palette": "冷白色、模糊的霓虹条纹、学生服装上混乱的色彩闪光",\n“语气”：狂热、肾上腺素飙升、迷失方向\n}，\n“声音的”： {\n"music": "快速的 EDM，节奏加快，重低音与近乎失准的音调同步",\n“ambient”：“混乱的走廊混响在速度下逐渐消退”，\n"sound_effects": "强烈的嗡嗡声被放大，剧烈的呼啸声、撞击声和惊叫声迅速传来",\n"mix_level": "震撼沉浸式混音，极速快感"\n}\n}',
    },
    {
        "label": '✨ 女子触摸一道明亮的金色弧线',
        "category": '✨ 特效奇幻',
        "title_zh": '女子触摸一道明亮的金色弧线',
        "prompt_en": '{\n  "shot": {\n    "type": "single",\n    "camera_motion": "slow top-down crane descend with subtle push-in (no cuts)",\n    "loop_hint": "hold final 6 frames for seamless autoplay"\n  },\n  "subject": {\n    "character": "blonde woman with a single back braid, wearing a flowing black evening dress with thigh-high slit; barefoot; goddess-ritual vibe",\n    "pose": "arms outstretched overhead touching a luminous golden arc; head bowed slightly",\n    "expression": "calm, reverent focus",\n    "wardrobe_motion": "fabric breathes gently; hem sways from faint updraft"\n  },\n  "scene": {\n    "environment": "black void stage with sparse floating dust motes",\n    "hero_prop": "crescent-like golden light arc above her hands (liquid-light ribbon)",\n    "fx": ["soft volumetric glow", "micro-particle drift", "subtle heat shimmer near arc"],\n    "time_of_day": "timeless night"\n  },\n  "visual_details": {\n    "beats": [\n      {\n        "time": "0.0-2.4",\n        "action": "Camera descends from above; subject silhouette resolves; dormant gold arc begins to glimmer as hands make contact.",\n        "focus": "top-down framing, shoulders and braid highlighted"\n      },\n      {\n        "time": "2.4-5.4",\n        "action": "Arc brightens and bends smoothly into a perfect crescent; light blooms along her arms; dust motes orbit slowly.",\n        "focus": "rim highlights on skin; gentle lens bloom on the arc"\n      },\n      {\n        "time": "5.4-8.0",\n        "action": "She rises a few centimeters (levitation hint) while arc hums and stabilizes; fabric lifts softly; camera finishes push-in and settles for loop.",\n        "focus": "hero tableau centered; clean negative space around figure"\n      }\n    ]\n  },\n  "cinematography": {\n    "lens": "portrait 65–85mm feel, shallow depth (f/2.0)",\n    "framing": "centered vertical figure; arc sits just above frame midline; low key with strong speculars",\n    "exposure": "protect highlights on arc, maintain true blacks; mild roll-off on skin",\n    "post": "cinematic contrast; glow bloom on arc; very light film grain; negligible chromatic aberration"\n  },\n  "audio": {\n    "fx": [\n      "low airy shimmer tied to the arc brightness",\n      "soft cloth rustle on levitation",\n      "sub-bass swell at 5.4s"\n    ],\n    "music": "minimal drone in D minor, barely rising toward the final hold",\n    "dialogue": "none"\n  },\n  "color_palette": {\n    "primary": "molten gold (#F5C76A)",\n    "secondary": "amber highlights (#D69B3A)",\n    "accents": "skin neutrals with warm rim",\n    "background": "pure black (#000000)"\n  },\n  "physics_rules": [\n    "dust motes drift on gentle convection; no chaotic turbulence",\n    "cloth responds to continuous mild updraft; inertia preserved",\n    "arc emits soft light that illuminates nearby skin and fabric with inverse-square falloff"\n  ],\n  "visual_rules": [\n    "no text, captions, or watermarks",\n    "keep background clean; no extra props",\n    "avoid camera shake and excessive bloom; preserve detail in highlights",\n    "maintain elegant anatomy and natural hand poses"\n  ],\n  "negative_prompt": [\n    "cartoonish rendering",\n    "overexposed arc clipping",\n    "banding or posterization in blacks",\n    "extra limbs or finger artifacts",\n    "busy background",\n    "harsh color shifts (green, magenta)"\n  ],\n  "metadata": {\n    "mood": "sacred, poised, ascendant",\n    "platform_goal": "high-readability loop thumbnail with bright gold arc framing the centered subject"\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n“类型”：“单个”，\n"camera_motion": "缓慢的自上而下的起重机下降，并带有微妙的推入（无剪切）",\n"loop_hint": "保留最后 6 帧以实现无缝自动播放"\n}，\n“主题”： {\n"character": "金发女子，背后扎着一条辫子，身穿飘逸的黑色晚礼服，开衩至大腿；赤脚；女神仪式感",\n“姿势”：“双臂伸过头顶，触摸一道明亮的金色弧线；头部微微低垂”，\n"expression": "平静、虔诚的专注",\n"wardrobe_motion": "布料轻轻呼吸；衣摆因微弱的上升气流而摇摆"\n}，\n“场景”： {\n“环境”：“黑色虚空舞台，稀疏漂浮的尘埃”，\n"hero_prop": "她双手上方有一道月牙状的金色光弧（液态光带）",\n"fx": ["柔和体积光晕"、"微粒漂移"、"电弧附近微妙的热闪烁"],\n"time_of_day": "永恒之夜"\n}，\n“视觉细节”：{\n"节拍": [\n{\n"时间": "0.0-2.4",\n"action": "摄像机从上方下降；主体轮廓消失；当双手接触时，休眠的金色弧光开始闪烁。",\n“焦点”：“自上而下的构图，突出肩膀和辫子”\n}，\n{\n"时间": "2.4-5.4",\n"action": "弧光明亮，平滑地弯曲成完美的新月形；光芒沿着她的手臂绽放；尘埃缓慢地旋转。",\n“焦点”：“皮肤上的边缘亮点；弧线上的柔和镜头光晕”\n}，\n{\n"时间": "5.4-8.0",\n"action": "她上升了几厘米（悬浮提示），同时电弧嗡嗡作响并稳定下来；布料轻轻升起；相机完成推入并稳定下来。",\n“焦点”：“英雄画面居中；清理人物周围的负空间”\n}\n]\n}，\n“电影摄影”：{\n"lens": "人像 65–85mm 感觉，浅景深 (f/2. 0)" ,\n"framing": "居中垂直图形；弧线位于框架中线正上方；低调且具有强烈的镜面反射",\n"exposure": "保护弧光上的高光，保持真正的黑色；在皮肤上轻微衰减",\n"post": "电影对比度；弧光绽放；非常轻的胶片颗粒；可忽略不计的色差"\n}，\n“声音的”： {\n"fx": [\n“低空闪烁与弧光亮度相关”，\n“悬浮时柔软布料的沙沙声”，\n“超低音在 5.4 秒时增强”\n]，\n"music": "D 小调的极简嗡嗡声，几乎没有上升到最后的停顿",\n“对话”：“无”\n}，\n“调色板”：{\n"primary": "熔融的金子 ( #F5C76A )",\n"secondary": "琥珀色高光 ( #D69B3A )",\n“accents”：“带有暖色边缘的中性肤色”，\n“背景”：“纯黑色(#000000)"\n}，\n“物理规则”：[\n“尘埃粒子在温和的对流中飘移；没有混乱的湍流”，\n“布料对持续温和的上升气流做出反应；惯性得以保留”，\n“弧光发出柔和的光线，以平方反比衰减照亮附近的皮肤和织物”\n]，\n"visual_rules": [\n“无文字、标题或水印”，\n“保持背景干净；没有多余的道具”，\n“避免相机抖动和过度光晕；保留高光部分的细节”，\n“保持优雅的身体结构和自然的手势”\n]，\n"negative_prompt": [\n“卡通渲染”，\n“过度曝光的弧形剪辑”，\n“黑色条纹或色调分离”，\n“额外的肢体或手指制品”，\n“繁忙的背景”，\n“严重的色彩变化（绿色、洋红色）”\n]，\n“元数据”：{\n"mood": "神圣、泰然、上升",\n"platform_goal": "高可读性的循环缩略图，以明亮的金色弧线框住中心主题"\n}\n}',
    },

    # 🎬 電影敘事
    {
        "label": '🎬 情侣看电视里的自己',
        "category": '🎬 電影敘事',
        "title_zh": '情侣看电视里的自己',
        "prompt_en": 'A warmly lit living room at night, seen from an angle that shows the couple on a couch and part of the television screen. They sit relaxed, in the soft glow of a table lamp, surrounded by cozy decor blankets, a coffee table with snacks. The TV plays an indistinct show until it abruptly flickers. The screen now displays a live feed of the exact living room, same lighting, same posture, same moment. The couple stares in disbelief as they recognize themselves onscreen. The woman gasps, clutching the man’s arm. The candlelight trembles. They remain frozen, disturbed by the uncanny reflection.',
        "prompt_zh": '一个夜晚温暖明亮的客厅，从能看到沙发上情侣和部分电视屏幕的角度拍摄。他们放松地坐着，被桌灯柔和的光芒包围，周围是舒适的装饰毯子、摆满零食的咖啡桌。电视播放着模糊不清的节目，突然闪烁了一下。屏幕现在显示的是这个客厅的实时画面，同样的光线，同样的姿势，同样的时刻。情侣们难以置信地认出屏幕上的自己。女人倒吸一口冷气，抓住男人的手臂。烛光摇曳。他们僵住，被这诡异的反影所困扰。',
    },
    {
        "label": '🎬 复仇者联盟，指环王，变形金刚',
        "category": '🎬 電影敘事',
        "title_zh": '复仇者联盟，指环王，变形金刚',
        "prompt_en": 'Avengers, Lord of the Rings, Transformers, Harry Potter, Top Gun, Dune, Predator, Ghostbusters, Titanic, Wakanda Forever, Batman, 300',
        "prompt_zh": '复仇者联盟，指环王，变形金刚，哈利波特，壮志凌云，沙丘，掠食者，捉鬼敢死队，泰坦尼克号，瓦坎达永远，蝙蝠侠，300',
    },
    {
        "label": '🎬 GTA、宝可梦、马里奥赛车',
        "category": '🎬 電影敘事',
        "title_zh": 'GTA、宝可梦、马里奥赛车',
        "prompt_en": 'Please enjoy, in order: GTA, Pokemon, Mario Kart, The Witcher 3, Stardew Valley,  Tetris, Mortal Kombat, The Sims, & Death Stranding(!)',
        "prompt_zh": '请按顺序欣赏：GTA、宝可梦、马里奥赛车、巫师 3、星露谷物语、俄罗斯方块、真人快打、模拟人生、以及死亡搁浅(!)',
    },
    {
        "label": '🎬 一支小队艰难地穿越冰脊对峙怪兽',
        "category": '🎬 電影敘事',
        "title_zh": '一支小队艰难地穿越冰脊对峙怪兽',
        "prompt_en": 'Cinematic long shot with forward tracking: In a frozen wasteland under a black sky filled with auroras, a small squad treks across an ice ridge, their footsteps crunching over ancient wreckage. Wind howls. One pauses, raising a scope. In the valley below: dozens of beasts, dormant, coiled around a shattered mech carrier. The camera slowly tracks forward as the squad descends each step heavy, uncertain. Then one of the creatures stirs. Its eyes glow. Others follow. The ice begins to crack beneath their feet. The camera pulls upward as all hell breaks loose, beasts charging up the slope, soldiers scrambling, rifles lighting up the darkness in staccato bursts.',
        "prompt_zh": '电影式长镜头，带前推：在一片冰冻荒原上，在极光弥漫的漆黑天空下，一支小队艰难地穿越冰脊，他们的脚步踩在古老的残骸上，发出嘎吱嘎吱的响声。狂风呼啸。其中一人停下脚步，举起瞄准镜。山谷下方：数十只野兽蛰伏，盘绕着一辆破碎的机甲运输车。随着小队每一步沉重而迷茫地下降，镜头缓慢地向前移动。然后，其中一只野兽动了动。它的眼睛闪闪发光。其他的也跟着动了起来。他们脚下的冰开始龟裂。镜头向上拉起，地狱之门打开，野兽冲上斜坡，士兵们手忙脚乱，步枪的枪声断断续续地照亮了黑暗。',
    },
    {
        "label": '🎬 人类与未来家居界面互动',
        "category": '🎬 電影敘事',
        "title_zh": '人类与未来家居界面互动',
        "prompt_en": '{\n  "shot": {\n    "composition": "wide establishing shots transitioning to medium orbit and macro close-up",\n    "lens": "24mm for wide interior, 50mm for orbit, 90mm macro for device",\n    "frame_rate": "30fps standard with subtle ramping during gesture moments",\n    "camera_movement": "smooth orbital tracking around subject, gentle push-in for close-up"\n  },\n\n  "subject": {\n    "description": "androgynous individual interacting with futuristic home interface",\n    "wardrobe": "monochromatic high-tech loungewear with subtle metallic textures",\n    "props": "transparent ripple-reactive interfaces, glass-like control device"\n  },\n\n  "scene": {\n    "location": "suspended apartment overlooking neon cyberpunk cityscape",\n    "time_of_day": "twilight",\n    "environment": "minimalist architecture with panoramic windows, glowing neon haze outside"\n  },\n\n  "visual_details": {\n    "action": "gestures in air controlling environment, responsive lighting, final close-up of device",\n    "special_effects": "holographic UI, liquid ripple transitions, adaptive lighting",\n    "hair_clothing_motion": "minimal motion, soft fabric flow with elegant gesturing"\n  },\n\n  "cinematography": {\n    "lighting": "ambient interior glow with reactive accents, neon reflections",\n    "color_palette": "cool cyans, deep purples, soft whites with glass highlights",\n    "tone": "elevated, futuristic, serene"\n  },\n\n  "audio": {\n    "music": "ambient synthwave with digital chimes and subtle builds",\n    "ambient": "soft city hum, electronic interface whispers",\n    "sound_effects": "gesture-triggered whooshes, soft chime on logo",\n    "mix_level": "refined spatial mix with immersive clarity"\n  },\n\n  "dialogue": {\n    "character": "",\n    "line": "",\n    "subtitles": false\n  }\n}',
        "prompt_zh": '{\n“拍摄”：{\n“构图”：“广角定场镜头过渡到中景轨道和微距特写”，\n镜头：24mm 用于宽阔的内部空间，50mm 用于轨道，90mm 用于设备微距，\n"frame_rate": "标准 30fps，手势动作时有细微变化",\n"camera_movement": "围绕拍摄对象进行平滑的轨道跟踪，轻轻推入以进行特写"\n}，\n\n“主题”： {\n“描述”：“雌雄同体个体与未来家居界面互动”，\n“wardrobe”：“单色高科技家居服，带有微妙的金属质感”，\n“道具”：“透明的波纹反应界面，类似玻璃的控制装置”\n}，\n\n“场景”： {\n“location”：“悬浮公寓，俯瞰霓虹赛博朋克城市景观”，\n"time_of_day": "黄昏",\n“环境”：“极简主义建筑，全景窗户，外面霓虹闪烁”\n}，\n\n"visual_details": {\n“动作”：“空中控制环境的手势，响应式照明，设备的最终特写”，\n"special_effects": "全息 UI、液体波纹过渡、自适应照明",\n"hair_clothing_motion": "最小的动作，柔软的织物流动，优雅的手势"\n}，\n\n“电影摄影”：{\n“照明”：“带有反应性点缀和霓虹灯反射的室内环境光”，\n"color_palette": "冷青色、深紫色、柔和的白色，带有玻璃亮点",\n“tone”：高雅、未来主义、宁静\n}，\n\n“声音的”： {\n“音乐”：“带有数字钟声和微妙构造的环境合成波”，\n"ambient": "柔和的城市嗡嗡声，电子界面的低语声",\n"sound_effects": "手势触发的呼呼声，标志上的轻柔铃声",\n"mix_level": "精致的空间混合，沉浸式清晰度"\n}，\n\n“对话”：{\n“特点”： ””，\n“线”： ””，\n“字幕”：false\n}\n}',
    },

]

def get_video_prompt(label: str) -> dict:
    return next((t for t in VIDEO_PROMPT_TEMPLATES if t["label"] == label), {})

def get_video_prompts_by_category(category: str) -> list[dict]:
    return [t for t in VIDEO_PROMPT_TEMPLATES if t["category"] == category]


# ── Seedance 2.0 Video Prompt Templates ─────────────────────────────────────

SEEDANCE_PROMPT_TEMPLATES: list[dict] = [
    {
        "label": '⭐ 超現實戰場浪人動作場景',
        "category": '⭐ 精選',
        "title_zh": '超現實戰場浪人動作場景',
        "prompt": '空中超現實的戰場：漂浮的岩石島嶼在雷暴中飄移，下方雲層如海洋般翻騰。蒙面浪人奔馳於漂浮的平台之間，身後緊追著一頭巨大的有翼野獸，其胸膛是風暴雲和閃電組成的漩渦。攝影機在島嶼間飛速穿梭，努力跟上傾斜、旋轉並崩解的岩石。每一次振翅都向空氣中發出衝擊波，震動畫面，將碎屑和雨水直接吹向觀眾的臉龐。快速的手持剪輯捕捉到浪人跳過不可能的間隙，劍光劃出弧線，短暫地劃破黑暗。結尾鏡頭顯示攝影機在他跳下最後一塊崩塌的岩石時，從他身後俯衝而下，他騎著一道閃電直接衝入怪物的胸膛漩渦，發出最後一擊，孤注一擲地從內部引爆風暴，並在耀眼的閃光中清空天空。\n\n720p\n16:9\n15 秒',
        "lang": 'English',
        "featured": True,
    },
    {
        "label": '⭐ 東京擎天柱大戰哥吉拉',
        "category": '⭐ 精選',
        "title_zh": '東京擎天柱大戰哥吉拉',
        "prompt": '一輛豪華轎車變身為柯博文，與哥吉拉在下著雨的東京夜晚背景下激戰，爆發出爆炸和能量衝擊波。',
        "lang": 'English',
        "featured": True,
    },
    {
        "label": '⭐ 《鬼滅之刃》真人戰鬥提示詞，適用於 Seedance 2.0',
        "category": '⭐ 精選',
        "title_zh": '《鬼滅之刃》真人戰鬥提示詞，適用於 Seedance 2.0',
        "prompt": '真人版漫畫改編 · 呼吸法對決（15 秒 · 超燃特效版）\n【核心看點】：水之呼吸（藍色水龍）VS 雷之呼吸（金色閃電），真人極速對決。\n【風格】：好萊塢真人版漫畫改編電影質感，暗黑武士風，4K 超清，極致快剪，粒子光效炸裂，無血腥。\n【時長】：15 秒\n【場景】：月光下的迷霧森林，泥濘地面，落葉紛飛。\n[00:00-00:05] 鏡頭 1：水之樂章 · 序式（蓄力感）\n畫面：一位身穿綠黑格紋羽織（外套）的年輕武士，在月光下沉下重心，雙手握刀。\n動作：他深吸一口氣，周圍空氣瞬間凝固。拔刀出鞘之際，一條由高壓水流凝聚而成的巨大藍色水龍憑空出現，圍繞著他的身體和刀刃高速旋轉，發出流水咆哮聲。\n特效細節：水流具有真實的飛濺感，照亮了黑暗的森林。\n[00:05-00:10] 鏡頭 2：雷之閃光 · 進擊（極速感）\n畫面：對面，一位身穿黃色三角紋羽織的金髮劍士，身體壓得極低，擺出居合術（拔刀術）的架勢。\n動作：地面驟然炸裂。他整個人瞬間化作一道炫目的金色閃電殘影，以肉眼難以捕捉的速度，呈「Z」字形在樹林中快速折射推進。\n特效細節：他所經過之處，留下金色電弧和焦黑的落葉。\n[00:10-00:15] 鏡頭 3：水雷相撞 · 終響（絕招對轟）\n畫面：極速正面對撞。年輕武士揮舞著巨大藍色水龍迎擊，化身閃電的金髮劍士猛烈撞擊而來。\n動作：兩把刀在畫面中央劇烈碰撞。\n特效奇觀：藍色水龍與金色閃電瞬間炸裂，形成一股巨大的水雷能量風暴向外擴散。周圍的參天大樹被能量波攔腰折斷，泥土、水花和光線遮蔽了鏡頭。畫面在極致炫目的藍、黃、白光中結束。',
        "lang": '中文',
        "featured": True,
    },
    {
        "label": '⭐ 動態捕捉下的動漫女孩舞台舞蹈',
        "category": '⭐ 精選',
        "title_zh": '動態捕捉下的動漫女孩舞台舞蹈',
        "prompt": '參考影片 1（場景影片）進行人物 2 的動作（動作捕捉影片），用圖片 3 的人物生成影片',
        "lang": 'English',
        "featured": True,
    },
    {
        "label": '⭐ 飛車追逐：懸崖之城（一鏡到底）',
        "category": '⭐ 精選',
        "title_zh": '飛車追逐：懸崖之城（一鏡到底）',
        "prompt": '飛車追逐懸崖城市（單次連續鏡頭）從一座雕刻在石頭上的宏偉懸崖城市，鏡頭俯衝向一道沿著狹窄懸崖道路疾馳的微弱光線。鎖定：一輛飛車以驚人的速度貼著牆壁行駛。鏡頭向前猛衝，然後甩回，再緊貼著後方推進器：熱氣蒸騰，碎石從懸崖上崩落，警示燈閃爍。一個坍塌的陽台落下碎片；騎士在一個墜落的拱門下驚險地急轉彎，然後流暢地穿梭於懸掛的晾衣繩和敞開的窗戶之間。鏡頭也穿過相同的開口，緊隨其後。最後一個彎道後突然歸於平靜：鏡頭猛然向外拉開，展現出城市通向一個無邊無際、瀑布滋養的山谷，薄霧化為彩虹。',
        "lang": 'English',
        "featured": True,
    },
    {
        "label": '⭐ 寶萊塢舞蹈分心男友迷因提示',
        "category": '⭐ 精選',
        "title_zh": '寶萊塢舞蹈分心男友迷因提示',
        "prompt": '用「分心男友」這個迷因來總結寶萊塢舞蹈——確保它夠白痴，而且能獲得 50 個讚。',
        "lang": 'English',
        "featured": True,
    },
    {
        "label": '🎭 拍攝老年婦女打籃球的原始手機影片提示詞',
        "category": '🎭 日常生活',
        "title_zh": '拍攝老年婦女打籃球的原始手機影片提示詞',
        "prompt": '原始手機拍攝畫面，垂直手持鏡頭，晃動感，顆粒質感。在黃昏時分傳奇的 Rucker Park 籃球場，一位穿著花裙子和運動鞋、身材豐腴的老年婦女正在運球，對手是',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎵 高能量三人街舞影片生成提示詞',
        "category": '🎵 舞蹈音樂',
        "title_zh": '高能量三人街舞影片生成提示詞',
        "prompt": '[推薦設定] 模式：標準 | 解析度：720p | 時長：15 秒。100% 真人動畫。明亮日光。城市廣場。快速光影。高能量。爆炸性氛圍。強烈節奏。高能量版三人街舞。快速舞蹈。炫技動作。快節奏。全力投入。跳躍與翻轉。爆發力。強烈的三人表演。[0-1s：俯拍/快速切入] 鏡頭：快速鏡頭。廣場全景。三人位於中心。強烈音樂爆發。動態鏡頭。[1-4s：中景/快速環繞] 鏡頭：快速旋轉環繞。高能量基礎動作。快節奏開始。高低角度快速切換。[4-7s：多角度低拍] 鏡頭：多角度快速切換。膝蓋高度 ↔ 廣角。快速腳步。複雜且高難度的舞步。[7-9s：角色 1 爆發] 鏡頭：快速變焦。臉部特寫。角色 1 強烈獨舞。爆發力。快速旋轉。[9-11s：角色 2 爆發] 鏡頭：快速角度切換。臉部特寫。角色 2 強烈獨舞。炫技動作。高能量。[11-13s：角色 3 爆發] 鏡頭：超快速鏡頭。臉部特寫。角色 3 強烈獨舞。最高能量。跳躍與翻轉。[13-15s：廣角/爆炸性結尾] 鏡頭：快速拉遠。廣場全景。三人同步爆發。高潮。音樂高潮。定格微笑。[特色] 快節奏。多角度快速切換。高能量音樂。爆發力。觀眾興奮感。適合派對場景。',
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🎭 消防員救援電影級場景',
        "category": '🎭 日常生活',
        "title_zh": '消防員救援電影級場景',
        "prompt": '消防員正在進入房屋；在 3 秒處，消防員走進屋內，周圍家具正燃燒著；在 5 秒處，一塊燃燒的木頭在他面前墜落；在 8 秒處，他在嬰兒床中發現了一名 3 個月大的嬰兒，嬰兒正在咳嗽；消防員抱起嬰兒並將其擁入懷中；隨後消防員撤離房屋，將嬰兒交給救護人員。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 動作驚悚忍者戰鬥場景 (i2v)',
        "category": '🥋 動作戰鬥',
        "title_zh": '動作驚悚忍者戰鬥場景 (i2v)',
        "prompt": '一名穿著西裝的男子在動態好萊塢動作驚悚場景中，以極快速度與電梯門外等待他的數百名非凡忍者刺客搏鬥，採用連續的手持攝影鏡頭。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 紀錄片寫實風格車禍場景',
        "category": '🎬 電影敘事',
        "title_zh": '紀錄片寫實風格車禍場景',
        "prompt": '手持肩扛攝影機，帶有自然晃動，些微自動對焦呼吸效應，無穩定處理。\n\n開場畫面：午後安靜的住宅街道，柔和的金色陽光，長長的影子映在停放的車輛上。環境音：遠處的車流聲、風聲、微弱的鳥鳴。\n\n攝影機沿著人行道緩慢向前移動。\n\n在第 2 秒時，一輛黑色 SUV 從左側高速衝入畫面——輪胎發出尖銳摩擦聲，懸吊系統因失控而不均勻地壓縮。\n\n車輛擦撞到一輛停放的紅色轎車——撞擊突兀且混亂，金屬自然摺疊，玻璃向外碎裂成不規則碎片。\n\n無慢動作——所有過程皆以即時速度發生。\n\n紅色轎車被猛烈推上路緣，車頭發生寫實的變形凹陷。\n\n安全氣囊以悶響聲彈出。\n\n攝影師本能地後退——輕微踉蹌，畫面下沉後隨即恢復。\n\n煙霧開始從 SUV 的引擎室升起。\n\n聲音設計：原始真實——金屬擠壓聲、輪胎摩擦聲、玻璃碎裂聲，無任何電影化誇張處理。\n\n最終畫面：兩車靜止，伴隨細微的冷卻滴答聲，無任何戲劇性配樂。\n\n風格：紀錄片寫實主義、不完美的構圖、自然光、無視覺特效、4K 解析度。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 15 秒連續 3D 卡通序列提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '15 秒連續 3D 卡通序列提示詞',
        "prompt": '15 秒連續單鏡頭卡通序列。\n無剪輯。無場景切換。\n\n風格化 3D 卡通動畫，鮮豔色彩，強對比照明，誇張表情，極致擠壓與拉伸，彈性動作，動態鏡頭，高能量感\n\n清晰的動作方向，',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 武士壽司師傅喜劇開場提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '武士壽司師傅喜劇開場提示詞',
        "prompt": '壽司師傅 — 武士廚房喜劇開場：一位將每一條魚都視為武士對手的壽司師傅。角色設定 師傅：身材嬌小、神情嚴肅，頭戴傳統白色頭帶，身穿整潔的道服。他將手中的刀視為武士刀——會為刀鞘套、向刀鞠躬，並在拔刀時發出金屬的「鏘」聲。說話風格為',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 極致電影感：摩托車時間靜止動作場景',
        "category": '🥋 動作戰鬥',
        "title_zh": '極致電影感：摩托車時間靜止動作場景',
        "prompt": '這是一個為 Seedance 2.0 設計的提示詞，旨在生成一段 12 秒的極致電影感動作短片。場景一：一輛重型機車在高速行駛中發生險些致命的車禍，畫面在撞擊瞬間進入時間靜止狀態。場景二：時間完全凝結，騎士的分身從靜止的機車上下來，緩步走向鏡頭，並透過眼神與動作打破第四面牆，與觀眾進行互動。整體風格要求高細節、電影級光影與強烈的視覺衝擊力。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 珊瑚礁與雙髻鯊場景提示詞',
        "category": '🌿 自然風景',
        "title_zh": '珊瑚礁與雙髻鯊場景提示詞',
        "prompt": '攝影機在色彩鮮豔的淺水珊瑚礁上方平滑前進，小丑魚在海葵間穿梭，一隻海鰻緩慢地從岩縫中探出，珊瑚礁架突然向下延伸至深藍色的開放水域，一隻孤獨的雙髻鯊在下方游過，',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 適用於 Seedance 2.0 的懷舊童年回憶影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '適用於 Seedance 2.0 的懷舊童年回憶影片提示詞',
        "prompt": '整體風格：清新療癒、溫暖懷舊，以暖綠色 + 淺藍色為主色調，光影柔和通透，氛圍溫柔細膩。背景音樂：柔和的器樂（鋼琴 + 竹笛），節奏緩慢，情緒層層遞進。1. 全景，夏日午後，陽光穿過枝葉灑下斑駁光影，一群赤腳的孩子在清澈溪邊追逐嬉戲，水花四濺，笑聲迴盪在田野間。緩慢水平橫移。清脆的童笑聲、溪流聲、微風聲。2. 中景，孩子們追逐一隻彩色蝴蝶，指尖輕觸蝶翼，粉色與黃色的蝴蝶在野花間飛舞，圍繞著孩子。跟拍 + 輕微旋轉。蝴蝶拍翅聲、孩子們的嬉笑聲。3. 特寫，孩子們蹲在稻田邊，伸手試圖捕捉青蛙，受驚的青蛙發出叫聲，連續跳躍躲進稻梗深處，稻葉輕輕搖曳。固定鏡頭。青蛙叫聲、孩子們驚訝的呼喊聲。4. 全景，孩子們嬉戲的場景籠罩在柔光中，畫面亮度逐漸降低，開始淡出轉場，色彩緩慢模糊。鏡頭緩慢拉遠，場景淡出。背景音樂淡出，環境音淡出。5. 長鏡頭，一位年輕人獨自坐在湖邊的青石上，身影安靜，背景是清澈的湖水與遠處的綠樹，場景寧靜。緩慢推近。柔和的器樂輕輕響起，微風聲。6. 特寫，年輕人眼神的特寫，眼中帶著一絲憂鬱，目光溫柔而懷舊，望向湖面。固定特寫鏡頭。無額外音效，以器樂為主。7. 中景，順著年輕人的目光，孩子們在湖中的小船上玩耍，船槳劃破水面，泛起漣漪。鏡頭緩慢向湖面平移。孩子們的嬉鬧聲、划槳聲。8. 高角度全景，天空中白雲緩緩飄散，逐漸淡出畫面，彷彿在與舊時光告別。緩慢向上仰拍。器樂節奏放緩，情緒昇華。9. 全景，整體場景緩慢變暗，光影逐漸匯聚，湖泊與年輕人的身影變得模糊。固定鏡頭，場景變暗。器樂聲漸弱至靜止。10. 特寫，螢幕中央出現清晰工整的宋體字：「若春風憐花，願許我再少年。」文字停留，場景凍結。文字淡入。無音效，文字停留作為結尾。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎵 Seedance 2.0 音樂錄影帶製作提示詞',
        "category": '🎵 舞蹈音樂',
        "title_zh": 'Seedance 2.0 音樂錄影帶製作提示詞',
        "prompt": '[Image 1] 中的女性正在 [Image 2] 的場景中，伴隨著 [Audio 1] 的音樂表演一段超酷的嘻哈舞蹈。盡情釋放你的創意，呈現一支世上前所未見、濃縮為 15 秒的音樂錄影帶。無論是多鏡頭剪輯還是單一長鏡頭，一切由你決定。創作出一段受野獸派與超現實主義藝術家影響、令人興奮的 15 秒藝術感 MV。',
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🎬 男子對蜘蛛的誇張反應',
        "category": '🎬 電影敘事',
        "title_zh": '男子對蜘蛛的誇張反應',
        "prompt": '概念：一名男子看到牆上有隻蜘蛛。他以應對入室搶劫的強度做出反應。\n角色：Dave，一名身材魁梧、穿著浴袍的男子。\n升級過程：他像是在掩護射擊般翻滾到沙發後方。以匍匐前進的方式爬到廚房拿鞋子。以戰術蹲姿回來，並戴上隔熱手套作為盔甲。蜘蛛移動了一英寸，Dave 尖叫著將鞋子扔向電視。他用膠帶將自己包裹成防護服。最後拿出了吹葉機。\n視覺笑點：他年幼的女兒走進來，徒手抓起蜘蛛，將牠放到屋外，並給了他一個失望的眼神。Dave 向她敬禮。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '✨ 摩西分紅海聖經史詩提示詞',
        "category": '✨ 奇幻恐怖',
        "title_zh": '摩西分紅海聖經史詩提示詞',
        "prompt": '超寫實聖經史詩，IMAX 電影攝影，Ridley Scott 規模。描繪摩西分開紅海的 12 鏡頭快速剪輯序列。無對白。管弦樂漸強配樂。每個鏡頭 1 至 1.5 秒。\n\n色彩：深青色海水，金色神聖光芒',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 粗獷寫實風格 35mm 手持攝影提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '粗獷寫實風格 35mm 手持攝影提示詞',
        "prompt": '風格：粗獷寫實電影（Cine Verité）、真實影像、帶有細微自然晃動的 35mm 手持鏡頭。攝影機：單一連續的第三人稱視角（POV）跟拍鏡頭（無剪輯）。光影：地中海正午強烈的高對比陽光；戲劇性的體積霧籠罩在',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 靈虎對決虛空豹戰鬥影片提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '靈虎對決虛空豹戰鬥影片提示詞',
        "prompt": '黃昏時分，雲霧繚繞的竹林，深邃的翡翠綠環境光與銀色月光穿透茂密的葉片。雨水穩定地落在長滿苔蘚的岩石和淺水池上，為介質光創造了反射表面。風吹動竹竿，形成有節奏的波浪。\n\n**動作：**\n\n15.0 秒序列。一隻毛髮上帶有發光藍色斑紋的巨大白虎在竹林中潛行，同時一隻擁有琥珀色發光雙眼的巨大黑豹在陰影中盤旋。牠們在潮濕的森林地形上進行快速、貼近地面的戰鬥。每一次跳躍都會激起地面的水花，爪子在雨中劃出發光的軌跡。\n\n速度變化編排：老虎在半空中的撲擊動作切換至超慢動作，兩隻野獸碰撞時，毛髮和水滴懸浮在空中，隨後在牠們衝破竹竿時瞬間恢復全速。\n\n**攝影：**\n\n手持式地面跟拍，穿過竹林，偶爾捕捉到雨水窪中反射出的戰鬥畫面，隨後在牠們衝出枝葉時迅速將焦點拉回動物身上。\n\n**風格與限制：**\n\n照片級真實感毛髮模擬、體積雨粒子、潮濕地面的光線追蹤反射、電影級月光、35mm 膠片顆粒、穩定的幾何結構、8K。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 電影級足球精彩片段',
        "category": '🎬 電影敘事',
        "title_zh": '電影級足球精彩片段',
        "prompt": '為阿根廷對陣巴西的世界盃足球精彩片段套用戲劇性的電影風格，包含慢動作射門與動態運鏡。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 Seedance 2.0 聖經戰鬥史詩提示詞（大衛對決歌利亞）',
        "category": '🥋 動作戰鬥',
        "title_zh": 'Seedance 2.0 聖經戰鬥史詩提示詞（大衛對決歌利亞）',
        "prompt": '超寫實聖經戰鬥史詩，IMAX 電影攝影，Ridley Scott 史詩規模。15 秒內呈現 11 個快速鏡頭。\n這場不可能的戰鬥：牧羊少年對決 9 英尺巨人。一顆石頭。油畫質感與電影級寫實感。無對白。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 電影級 Lamborghini 品牌創意廣告影片生成 Prompt',
        "category": '🎬 電影敘事',
        "title_zh": '電影級 Lamborghini 品牌創意廣告影片生成 Prompt',
        "prompt": '電影級 Lamborghini 品牌創意廣告，超寫實，第一人稱高速跟拍鏡頭，極強的視覺衝擊力，流暢連續的運鏡，整體風格精緻、冷酷且極具侵略性。創作一支簡潔但極具侵略性的第一人稱高速穿梭廣告。避免低品質的賽博變形，不要直接將整頭公牛變成汽車，而是透過特寫、反射、結構線條與視覺轉場，將公牛的原始力量與爆發感自然轉化為 Lamborghini 的機械雕塑、空氣動力學與極致速度。全程無背景音樂，僅使用高品質的擬音（Foley）與空間音效。總時長控制在 15 秒內，要求每 3 秒進行一次明確的視覺升級，避免單調且拖沓的長鏡頭。\n[0-3s] 在一個深黑色金屬質感的暗空間中，一頭全身深黑、肌肉線條極其清晰、皮膚表面帶有內斂金屬冷光的狂暴公牛，突然高速衝出。攝影機以第一人稱視角緊密跟隨，幾乎貼著牛角、額骨線條、頸部肌肉與肩背輪廓向前衝刺。開場必須具備極強的迎面壓迫感；避免平鋪直敘或普通的奔跑鏡頭。應呈現速度與力量直接撞擊鏡頭的感覺，伴隨迎面而來的風壓。視覺風格極簡，僅保留少量冷白高光、黑色陰影、氣壓與速度殘影。\n[3-5s] 攝影機突然向前推進並加速，進入公牛眼睛與牛角根部的極致特寫。眼睛流露出冷冽的侵略性，反射中透出銳利的冷白光刃、橙色能量餘暉與金屬切面。利用牛角的弧度、眼睛中的反射與骨骼結構進行無縫轉場，瞬間連接到 Lamborghini 車頭燈、楔形車鼻與銳利折線的局部特寫。此轉場必須流暢、極快且精緻，彷彿 Lamborghini 本就潛藏在公牛的力量結構之中。\n[5-8s] 進入 Lamborghini 車頭與車燈的世界後，攝影機持續第一人稱高速衝刺，掃過銳利的燈組、低趴的引擎蓋、車頭極具雕塑感的折面、進氣口與楔形輪廓。攝影機沿著車身肩線快速滑動，延續衝過公牛肌肉與骨骼線條的動能，讓生物性的爆發結構自然過渡為機械曲線與鋒利的線條。整體色調以 Lamborghini 標誌性的亮黃色或消光黑為主體，搭配黑色陰影、冷白金屬高光與少量橙色熱反射——內斂、精緻且危險。\n[8-11s] 攝影機持續加速，掃過車身側面的銳利曲線，俯衝向輪胎與輪圈，高速貼地穿梭。輪圈轉動、煞車卡鉗、碳纖維側裙、導風口、車門切線與後方空氣動力學結構依序閃過。運鏡應呈現出被無法控制的暴力速度拖拽向前、持續俯衝、環繞側面、貼地壓迫並擦過車身縫隙與折面的感覺，維持極強的第一人稱刺激感。鏡頭語言強調機械獸性的壓迫感；避免溫和或優雅的巡航感。看起來應像是一輛狂怒的超級跑車在撕裂空氣。\n[13-15s] 鏡頭再次快速向前衝刺，整輛 Lamborghini 車身在運動中完全呈現：楔形低趴輪廓、銳利燈組、誇張的進氣結構、雕塑般的側身曲線、寬大的輪組與極具侵略性的姿態清晰可見。攝影機可短暫高速掃過車頂或側面，隨後拉回至前側方完成最後的動能積累。整輛車看起來應像是一頭真正完成機械覺醒的公牛，將力量感與品牌辨識度最大化。\n[13-15s] 結尾以低角度、前側方的英雄鏡頭呈現。一輛完整的 Lamborghini 超級跑車正在穩定衝刺或剛剛定格。車身極低、極寬、極銳利，如刀鋒般切開空間。車漆反射冷冽而內斂。背景僅保留少量賽道熱浪、氣流線、輪胎殘影與速度波紋。結尾必須短促、兇猛且具壓迫感，彷彿在宣告：原始野性，最終鍛造成為 Lamborghini 這台速度機器。\n聲音設計：開場使用低頻能量脈衝、公牛沉重的腳步聲、噴氣聲、皮膚摩擦空氣聲、迎面風切聲與空氣壓縮聲；轉向眼睛與牛角時，加入極細微、尖銳且內斂的空氣匯聚聲與金屬光刃轉場聲；進入 Lamborghini 細節後，放大金屬摩擦空氣聲、氣流滑過漆面聲、輪圈轉動聲、碳纖維震動聲、細微的煞車系統聲、燈組啟動聲與空間呼嘯聲；結尾強調輪胎壓地聲、車身穩定沉降聲、空氣被切開後的餘震與低頻匯聚感。全程無背景音樂。\n特殊控制：將品牌美學鎖定在 Lamborghini 的冷酷、銳利、侵略性、機械獸性與極致速度美學；運鏡必須連續且流暢；每個片段都必須有明確的視覺升級；動作合理，轉場自然，無卡頓或跳幀；避免低品質的賽博龐克、廉價機甲變形感或普通的跑車宣傳片質感。必須呈現出頂級超跑品牌的高端創意廣告水準。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎬 15 秒連續戰爭寫實影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '15 秒連續戰爭寫實影片提示詞',
        "prompt": '15 秒連續單鏡頭動作序列。\n無剪輯。無場景轉換。\n\n電影級現代戰爭寫實感。\n色調：低飽和度色調、塵土米色、混凝土灰、溫暖的槍口閃光。\n\n場景：\n戰火紛飛的城市街道。建築物被毀，到處都是瓦礫，煙霧繚繞。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 影片生成的動作序列提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '影片生成的動作序列提示詞',
        "prompt": '一位穿著長大衣的時尚動漫女性，手持雙槍，在摩天大樓昏暗且霓虹閃爍的屋頂上與多名武裝敵人對峙。\n\n[0–2 秒]\n她徑直向那群槍手衝刺。\n她以低姿態滑行閃避子彈，同時雙槍連發。',
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🎬 電影預告片風格影片生成',
        "category": '🎬 電影敘事',
        "title_zh": '電影預告片風格影片生成',
        "prompt": '[0s–3s]：( image1 ) 持續且不停歇的緩慢推進鏡頭 —— 向 19 世紀格林童話風格的深暗雲杉森林插畫中心縮放。隨著攝影機靠近，插畫開始出現故障，樹木在畫作中本不應存在的風中搖曳。\n\n[3s–5.5s]：( image2 ) 縮放持續進行，沒有中斷。插畫開始軟化並從中心向外溶解，彷彿霧氣正滲透紙張並從內部取代畫作。隨著攝影機持續向前推進，這片寫實區域以受控且有機的方式向外擴散。溫暖的奶油棕褐色插畫逐漸褪去，轉變為冷冽且低飽和的藍綠色。邊緣的繪畫表面短暫地晃動並變薄，如同潮濕的紙張因受潮而破裂，隨後安靜地溶解為同樣寫實的森林紋理。沒有突兀的變形，也沒有多重相互競爭的扭曲 —— 只有單一且詭異的置換，彷彿插畫正透過一層霧紗被真實的森林所取代。到了 5.5 秒時，攝影機已完全進入真實的森林內部，而畫作已完全消失。\n\n[5.5s–11s]：( image3 ) 向前的運動平緩地過渡為持續的向上漂移，過程中沒有剪輯，彷彿攝影機正以一個流暢的弧線被抬升穿過真實的森林。它在樹幹間上升並穿過下層樹枝，逐漸穿過樹冠 —— 不會飛得太高，但足以展現平坦灰光下深邃北歐森林的廣闊。運動保持冷靜且刻意，帶有一種細膩的漂浮感，讓森林在螢幕上呈現呼吸感。隨後，攝影機開始從垂直上升緩慢且自然地過渡為淺淺的向後滑行，彷彿在尋找樹林後的道路。\n\n[11s–15s]：( image4 ) 同樣的運動無縫持續。攝影機向前滑行並輕柔地從森林邊緣下降至道路，穩定在靠近柏油路面、低於視平線的視角。在一個連續不斷的鏡頭中，畫面來到極寬鏡頭，地平線保持穩定，道路筆直地延伸至灰白色的消失點。同一輛方正的復古轎車已在畫面中，正穩定地駛離，在霧氣中變得越來越小。落下的松針在潮濕的地面上輕微飄動。前方的霧氣逐漸變濃。\n\n整體風格：35mm 鎢絲燈電影膠片，變形寬銀幕，細膩顆粒感，電影質感。低飽和藍綠色中間調，深沉的黑色，平坦的陰天漫射光。流暢且連續的攝影機運動，銳利的細節，穩定的地平線，自然的比例。前兩個鏡頭從古董插畫的溫暖感過渡到冷冽的電影寫實感。無文字，無排版，無數位特效。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🐱 貓咪大師的東京鐵塔降落與救援',
        "category": '🐱 動物趣味',
        "title_zh": '貓咪大師的東京鐵塔降落與救援',
        "prompt": '一隻身穿跆拳道服、手持金色發光寶劍的橘貓，夜晚站在東京鐵塔頂端。\n\n動作：\n站在雨中 → 緩慢抬頭 → 雙眼發光。\n瞬間沿著塔身向下衝刺，對迎面而來的黑西裝鬣狗進行超高速斬擊。\n在鋼樑之間空中彈跳，連續揮劍。\n每次擊中 → 鬣狗化為黑煙消散。\n殘影移動 → 下降過程中進行多方向快速切割。\n牆面奔跑 → 旋轉斬擊 → 金色弧光爆炸。\n最後從塔上躍下 → 在雨中快速俯衝。\n最後一秒翻轉 → 安全降落在下方一名粉紅色頭髮高中女生的懷裡。\n貓咪瞬間放鬆，身體微微蜷縮，發出輕柔的呼嚕聲。\n\n運鏡：\n由上而下的跟隨俯衝 → 緊湊追蹤鏡頭 → 側向跟拍 → 在鋼樑間快速環繞 → 與攻擊同步的旋轉鏡頭 → 垂直俯衝跟隨 → 降落時的柔和特寫\n無剪接\n\n動態：極快、流暢、連續下降、強烈的動態模糊、銳利的打擊感\n\n特效：僅金色寶劍能量、雨絲、黑煙消散\n\n音效：\n史詩般的電影配樂貫穿全場 → 與打擊同步的沉重撞擊聲 → 雨聲與風聲特效\n男性電影旁白（低沉、冷靜）：\n「從最高點……他降臨了。」\n「他們毫無勝算。」\n\n對話：\n鬣狗（扭曲、迴音）：「抓住他。」\n女孩（輕柔、驚訝）：「等等——！」\n貓咪（溫柔、俏皮的語氣，最後時刻）：呼嚕聲',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 適用於 Seedance 2.0 的迷你女孩滑板追逐影片提示詞',
        "category": '🚀 追逐速度',
        "title_zh": '適用於 Seedance 2.0 的迷你女孩滑板追逐影片提示詞',
        "prompt": '在兒童房的地板上，一名迷你女孩騎著小滑板高速貼地滑行。畫面比例極其宏大，使原本生活化的玩具與家具顯得無比巨大。攝影機以低角度緊隨其後，並以一鏡到底的風格持續向背景推進。影片運用了超廣角鏡頭、動態模糊、景深以及電影級的燈光效果。速度分為三個階段逐漸提升。第一階段，她高速穿過狹窄通道，宛如在樂高積木組成的城市峽谷間穿梭，靈活地避開積木。第二階段，一顆巨型球體從正面滾來，她滑入球體與牆壁間的狹窄縫隙，驚險避開掉落的積木，並擦過一輛行駛中的迷你汽車輪胎。第三階段，她從即將被風吹合的繪本頁面縫隙中衝出，從搖晃的絨毛玩具腋下鑽過，最後躍入即將關閉的玩具箱蓋小縫中，以極速消失在黑暗的遠方。這是一段驚險刺激、充滿一系列大膽逃生場景的影片。場景設定在寫實的兒童房中，利用微縮視角創造出沉浸式的乘騎體驗，充分利用了巨大的障礙物與狹窄的縫隙。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🌌 科幻變身場景',
        "category": '🌌 科幻賽博',
        "title_zh": '科幻變身場景',
        "prompt": '65mm IMAX，超廣角變形鏡頭，厚重底片顆粒感，強烈鏡頭光暈。日蝕般的氛圍，伴隨濃厚的灰色霧氣。唯一的光源來自角色內部的橘紅色光芒，宛如一顆垂死的恆星。\n單鏡頭 15 秒：\n一名滿身塵土的男子獨自站在荒原中。手持攝影機以 360° 環繞拍攝，伴隨熱氣帶來的輕微晃動。他緩緩舉起手——指尖變得半透明，空氣開始扭曲。\n他的身體在壓力下抽搐。金色的裂紋在他皮膚下蔓延，骨骼發出碎裂聲。紫黑色的煙霧夾雜著藍色電弧從他的脊椎噴湧而出。深層裂縫中滲出液態黃金。\n漂浮的金屬碎片被吸引向他。鏽跡斑斑的黑色裝甲板伴隨著火花撞擊他的身體，形成不規則的盔甲——破碎的肩甲與胸甲顯露出熔岩般的核心。\n紅色金屬在他臉上蔓延，形成面具。他的雙眼塌陷，隨後燃起藍色電光，其中一隻閃爍不定。兩支巨大的黑色長角冒出微弱的紫色火焰。\n結局：他舉起手，形成一團如微型黑洞般的藍色火焰。他重擊地面——螺旋狀的重力衝擊波摧毀了附近的廢墟。一片寂靜。破碎的黑色羽翼展開。他抬起頭，藍色的雙眼在濃霧中閃爍。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 電影級動漫動作場景提示詞與對白',
        "category": '🥋 動作戰鬥',
        "title_zh": '電影級動漫動作場景提示詞與對白',
        "prompt": '[0.0s-3.0s] 鏡頭：超高速低角度追蹤鏡頭，像競速無人機一樣在單色無臉商人之間快速穿梭。動作：身穿黃色雨衣的女孩突然爆發式衝刺。強大的風壓使她的雨衣和商人的西裝劇烈飄動。具備電影級景深的高速動態模糊。[3.0s-7.0s] 鏡頭：戲劇性的 360 度慢動作環繞拍攝，聚焦在她堅定的臉龐上，隨後她帥氣地急停。動作：她直視鏡頭。她的雙眼閃爍著細微的數位光芒。她的唇部動作清晰且與對白同步。對白：「アップデートして生きろ」（更新並活下去）[7.0s-10.0s] 鏡頭：快速廣角搖臂鏡頭上升至鳥瞰視角。動作：當她說話時，一股充滿活力的霓虹色彩與數位粒子從她腳下爆發，以強烈的色彩「覆蓋」了灰色的世界。無臉男人們消散成金色的數據流。風格：高預算電影級動漫、傑作、流暢動畫、動態光影、8k 解析度。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 貓大師與兔子們的史詩級武術對決',
        "category": '🥋 動作戰鬥',
        "title_zh": '貓大師與兔子們的史詩級武術對決',
        "prompt": '史詩級 Marvel Studios 風格，戲劇性光影，快速剪輯，慢動作衝擊，重低音音效，英雄式管弦樂起奏。\n\n0.0–0.8 秒：廣角鏡頭 — 武術道場。一隻穿著白色跆拳道服的橘貓站在中央，周圍環繞著穿著高中運動服的兔子學生們。\n\n0.8–1.6 秒：特寫鏡頭 — 貓擺出詠春拳防禦架勢。眼神專注。\n\n1.6–2.4 秒：中景鏡頭 — 第一隻兔子發動攻擊。快速連環拳，精準打擊。\n\n2.4–3.2 秒：慢動作 — 兔子被掌擊擊飛，金黃色光影中塵土飛揚。\n\n3.2–4.2 秒：跟拍鏡頭 — 貓向前邁步，以精準的手法撥開兩隻兔子。\n\n4.2–5.2 秒：近身格鬥 — 肘擊、拳擊、低掃腿。兔子們迅速倒下。\n\n5.2–6.4 秒：低角度鏡頭 — 寸勁將多隻兔子擊飛。\n\n6.4–7.6 秒：廣角鏡頭 — 短暫的靜止。地板上躺滿了倒下的兔子。\n\n7.6–8.8 秒：衝擊 — 門窗爆裂開來。更多兔子湧入。\n\n8.8–10.0 秒：蒙太奇 — 快速而激烈的交鋒。貓被包圍。\n\n10.0–11.2 秒：俯拍鏡頭 — 兔子堆疊起來，在貓身上形成一座小山。\n\n11.2–12.6 秒：定格 — 堆疊越來越高，內部有輕微晃動。\n\n12.6–15.0 秒：最終鏡頭 — 貓從兔子堆頂端探出頭來，雖然凌亂但對著鏡頭微笑。\n\n對白（對著鏡頭）：\n「永不放棄！」',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 由貓咪海盜進行的第一人稱 FPV 追逐與救援',
        "category": '🚀 追逐速度',
        "title_zh": '由貓咪海盜進行的第一人稱 FPV 追逐與救援',
        "prompt": '在混亂的動物王國中進行第一人稱衝刺。野狼在後追趕。穿梭於茂密森林、避開落石、翻越樹枝 —— 全程 FPV 追逐動作。衝出懸崖邊緣，來不及停下 —— 我縱身一躍。朝著海洋自由落體，風聲呼嘯，海水迅速逼近。就在最後一刻 —— 一艘海盜船湧現。長著橘色貓頭的水手們伸出手，在半空中接住了我。重重地落在甲板上 —— 氣喘吁吁，劫後餘生。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 用於影片模型對比的動作序列提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '用於影片模型對比的動作序列提示詞',
        "prompt": '一名手持巨大紫色能量刃的男子，身處雨中。\n動作：\n瞬間向前衝刺，超高速橫向斬擊。\n殘影移動至背後，進行快速連續打擊。\n旋轉攻擊，刀刃釋放電弧。\n最後跳躍 → 快速俯衝 → 地面重擊。\n運鏡：\n低角度跟拍 → 側向追蹤 → 環繞 → 同步旋轉 → 快速上升 → 俯衝跟拍\n無剪輯\n動態：極快，強烈的動態模糊，高衝擊力\n特效：僅限紫色能量',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 超風格化功夫貓動作短片',
        "category": '🥋 動作戰鬥',
        "title_zh": '超風格化功夫貓動作短片',
        "prompt": '一段超風格化的 15 秒香港武打動作短片，結合子彈時間特效與強烈的鏡頭運動。融合 80 至 90 年代功夫電影風格與現代電影技術。包含極致的快速搖鏡（whip pans）、快速變焦（snap zooms）、環繞鏡頭、動態模糊、衝擊定格以及強烈的音效設計。\n\n0–2 秒\n室內，昏暗的四合院中庭。\n俯視旋轉鏡頭緩緩下降。\n一隻穿著灰色道袍的橘貓靜止站立。\n音效：迴盪的敲門聲……敲門聲……\n鏡頭突然快速變焦（SNAP ZOOM）至貓的雙眼。\n\n2–4 秒\n門的視角（POV）。\n木門向鏡頭方向爆裂開來。\n硬切至超廣角鏡頭變形，貓走出來。\n轉場：快速搖鏡變形為街道場景。\n\n4–6 秒\n街道，夜晚。霓虹燈倒映在濕潤的地面上。\n360° 環繞鏡頭：身穿黑色西裝、戴著墨鏡的灰鬣狗群逼近。\n鏡頭速度加快，隨後突然停止 → 寂靜。\n\n6–8 秒\n子彈時間開始。\n一隻鬣狗向前傾身，嘴唇慢動作移動，進行挑釁。\n鏡頭圍繞著靜止的人物旋轉。\n只有貓以正常速度移動。\n貓（冷靜地）：「你在找誰？」\n\n8–12 秒\n戰鬥序列 — 極致子彈時間混亂：\n— 貓向前衝刺 → 鏡頭以瘋狂的手持晃動跟隨\n— 空中定格：快速踢擊產生的多重殘影（腿部軌跡劃破空間）\n— 每次踢擊命中 → 衝擊波在鬣狗軀幹上擴散\n— 鏡頭切換於：\n• 微距衝擊鏡頭（布料向內壓縮）\n• 魚眼鏡頭踢向鏡頭\n• 被擊飛鬣狗的旋轉視角（POV）\n— 終結技：慢動作 360° 旋轉踢 → 所有鬣狗同時被擊飛\n— 衝擊瞬間音效恢復 → 轟！\n\n12–15 秒\n寂靜。灰塵在半空中沉澱。\n鏡頭緩緩穿過漂浮的碎片（仍部分處於慢動作中）。\n貓以正常速度落地。\n直視鏡頭，微微歪頭，露出俏皮的微笑。\n\n台詞（銳利、自信）：\n「追蹤貓大師，解鎖更多毛茸茸的混亂。」\n\n定格畫面 → 突發故障縮放（glitch zoom） → 復古拳擊音效。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 FPV 無人機穿梭東京的鏡頭',
        "category": '🚀 追逐速度',
        "title_zh": 'FPV 無人機穿梭東京的鏡頭',
        "prompt": '單一連續 FPV 無人機穿梭東京的鏡頭 / 無剪輯、無對話、無文字\n\n風格：晴朗午後的寫實東京，溫暖陽光，銳利陰影，街道上擠滿了日本行人，以搭載 GoPro 廣角鏡頭的 FPV 無人機拍攝，電影級 8K 畫質，自然呈現',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 科幻戰士戰鬥序列',
        "category": '🥋 動作戰鬥',
        "title_zh": '科幻戰士戰鬥序列',
        "prompt": '角色參考 Imagen1 = 戰士臉部。Imagen2 = 紅色機械裝甲參考。IMAX 70mm 膠片質感，Panavision 35mm 鏡頭，f4 光圈，手持晃動感。真人科幻風格，4K 解析度，淺景深散景，冷青藍色調，紅色能量劍作為唯一的暖色光源。濃厚的工業迷霧。硬切轉場。僅有 SFX 音效，無背景音樂。臉部穩定，無變形。0-1 秒：特寫臉部。Imagen1 不戴頭盔，冷靜，冷藍色側光。鏡頭推進。紅色模組化機械 Imagen2Element 型全罩式頭盔（無面罩）在臉部周圍組裝，零件精準鎖定。機械嗡嗡聲。1-3 秒：特寫手部。右手掌向上，手指張開。紅色能量粒子向內螺旋，凝結成劍柄，形成電路紋理。能量嗡嗡聲。3-4 秒：側面特寫。手握住劍柄——紅色劍刃向上噴發，粒子固化成半透明刀刃。全身穿著 Imagen2Element 型紅色裝甲的戰士轉身向前。爆炸性的嗡嗡聲。4-5 秒：背後中景。戰士持劍站在工業平台邊緣。六隻黑色甲殼生物出現在迷霧中，紅色眼睛成對發光。鏡頭拉遠，顯露包圍之勢。尖叫聲。5-6 秒：低角度。戰士戰鬥姿態。迷霧中有六對紅色眼睛。上方有起重機框架和纜線。靴子跺地。劍的嗡嗡聲增強。6-7 秒：第一隻生物衝鋒。戰士迎擊——水平橫斬穿過其中段，生物被擊飛 3 公尺撞上欄杆，欄杆彎曲。紅色弧光軌跡殘留。鏡頭側向跟隨整個序列。甲殼撕裂聲 + 金屬撞擊聲。7-8 秒：左側第二隻生物——反手斬斷前肢，紅色火花飛濺。第三隻從右側攻擊——戰士旋轉踢將其踢向第四隻，兩者滾出畫面。鏡頭快速環繞。斷肢聲 + 踢擊聲 + 碰撞聲。8-9 秒：特寫 Imagen2 頭盔面罩，濺滿黑色液體。沉重的過濾呼吸聲。紅色劍光映照在金屬表面。9-10 秒：第五隻生物從背後伏擊。戰士反手握劍，向後刺穿生物胸膛，紅光從其背後穿出。旋轉並將被刺穿的生物甩向第六隻。兩者消失在迷霧中。鏡頭追蹤甩出的軌跡。穿刺聲 + 尖叫聲 + 遠處碰撞聲。10-11 秒：俯視全景。戰場——六隻生物倒地，斷肢、被刺穿。金屬地板上有黑色液體，欄杆彎曲。戰士居中，劍尖滴下紅色液滴。寂靜。金屬吱吱作響的回音，液滴嘶嘶作響。11-12 秒：低位特寫。紅色裝甲靴踩過黑色液體，映照出藍紅色光影。沉重的腳步聲。金屬地板開始劇烈顫抖。戰士停下。鏡頭上升至頭盔。深沉的震動——巨大的腳步聲如地震般逼近。12-13 秒：正面中景。戰士抬頭。迷霧中點亮兩盞巨大的紅燈——比生物的眼睛寬十倍。巨大的黑色剪影浮現，頭部觸及起重機框架，體型是戰士的 10 倍。劍的嗡嗡聲增強。鏡頭上升，展現 Boss 的規模。地震般的重擊聲，纜線嘎吱作響，結構發出呻吟聲。13-14 秒：極特寫頭盔面罩——金屬板上有黑色液體和水氣。Boss 的倒影：巨大的甲殼',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 神秘皇家戰士角色與環境設定',
        "category": '🥋 動作戰鬥',
        "title_zh": '神秘皇家戰士角色與環境設定',
        "prompt": '角色設定：\n一位沒有可見人類身分的神秘皇家戰士。\n臉部被陰影、角度、皇冠與電影級燈光所遮蔽。\n僅使用 @reference1 作為白色與金色生物機械盔甲、紅色斗篷及皇冠的視覺參考。\n\n環境：\n黑暗乾旱',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 第一次世界大戰壕溝戰影片提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '第一次世界大戰壕溝戰影片提示詞',
        "prompt": '格式：15 秒 / 單一連續「不可能」運鏡 / 無對白\n風格：第一次世界大戰壕溝戰、深厚泥濘、傾盆大雨、破碎木材、照片級真實感地面至高空電影級 8K\n鏡頭 01 (0:00–2:00)：攝影機從泥濘地面開始。一片覆蓋著厚重泥濘的森林',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 FPV 無人機穿過管道的影片提示詞',
        "category": '🚀 追逐速度',
        "title_zh": 'FPV 無人機穿過管道的影片提示詞',
        "prompt": 'FPV 無人機風格鏡頭從全黑環境開始，在管道內快速推進，摩擦管壁後衝入房間。整體畫面覆蓋強烈的綠色濾鏡，螢光燈混亂閃爍。無背景音樂，僅有電流嗡嗡聲與金屬刮擦聲。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 35mm 手持底片美學影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '35mm 手持底片美學影片提示詞',
        "prompt": '粗獷、原始的手持 35mm 底片美學，帶有自然的底片顆粒感。強烈、直射的陽光營造出高對比的陰影效果。手持跟拍鏡頭（第三人稱視角 / 肩後視角）。氛圍：塵土飛揚、沿海強風、逼真的物理效果。\n\n音訊：沉重',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 火箭翼裝飛行穿越風暴峽谷',
        "category": '🚀 追逐速度',
        "title_zh": '火箭翼裝飛行穿越風暴峽谷',
        "prompt": '一名翼裝飛行員從地球上空的平流層氣球跳下，飛行服上裝有小型火箭推進器。\n\n在第 2 秒時，推進器點火，飛行員加速穿越風暴雲層。\n\n當飛行員俯衝穿過風暴雲峽谷時，閃電在翼裝周圍閃爍。\n\n飛行員在距離沙漠公路僅幾英寸的高度拉起，隨後滑翔進入一條狹窄的峽谷。\n\n火箭翼裝俯衝、閃電風暴穿越、極速下降、電影級空中運動、4K。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 史詩級科幻動作場景：仿生女英雄對決巨型機甲',
        "category": '🥋 動作戰鬥',
        "title_zh": '史詩級科幻動作場景：仿生女英雄對決巨型機甲',
        "prompt": '全景固定鏡頭，拍攝荒涼的灰色海灘。霧氣從深處背景向前方蔓延，霧中隱約可見哥德式建築的輪廓。海灘地面覆蓋著細小的灰色礫石與焦黑碎片。整體色調極低飽和度，呈現冷灰色與壓抑感。一位仿生女英雄（身穿白色正裝，配戴銀色機械頸甲與義肢手臂，黑色馬尾，金色齒輪耳環，紅唇，全程保持電影級真實感與穩定的面部特徵）站在畫面中央。她的西裝在海風中緩緩飄動。銀色義肢手臂垂直握著法杖，法杖頂端的三個環燃燒著橘紅色能量。能量光芒在女英雄白色西裝的前側投射出溫暖的橘色輪廓光。低沉的史詩背景音樂在寬廣的聲場中緩緩展開，與能量燃燒的嘶嘶聲及沉重的呼吸聲交織在一起。鏡頭拉遠。女英雄的銀色義肢手臂突然將法杖重擊在沙地上，衝擊力激起大量灰色塵土四散。塵土在側逆光下形成半透明的金色雲霧。三個橘紅色能量環從法杖頂端脫離，懸浮在空中並迅速加速旋轉。每個環在旋轉時都拖曳出一道完整的橘紅色光軌。女英雄的義肢手臂突然高舉，發出攻擊信號。隨著手臂動作，她的斗篷向後戲劇性地展開，馬尾辮的髮絲被衝擊氣流向前揚起。法杖擊地的沉重悶響、金屬震動聲以及風捲沙礫的聲音同時轟然響起。快速推入的低角度特寫。女英雄銀色義肢手臂的食指突然向上揮動，精密的金屬指尖上跳動並燃燒著金色火焰。藍白色電弧沿著義肢關節向上蔓延，與指尖的火焰融合。背景中巨大的機械結構開始崩塌，金屬組件在火光中翻滾墜落。指尖劃破空氣的尖銳呼嘯聲與高頻能量匯聚的嗡嗡聲瞬間刺破場景。快速全景水平跟拍。第一個巨型能量環如同飛行的鋸片，以極高速度在空中劃出一道完整的橘紅色火弧。火弧的尾跡在黑暗天空中形成持續發光的軌跡，瞬間切入巨型鋼鐵飛船的側裝甲。穿透瞬間，裝甲板沿著切割線向外爆裂，橘紅色岩漿從切口噴湧而出。鋸片切割金屬的刺耳摩擦聲以及火花與爆炸聲撕裂了聲場。俯視跟拍。能量環穿透側翼，繼續切入飛船核心艙。核心在穿透瞬間引發連鎖爆炸，第一波爆炸呈球狀擴散，第二波則沿著船體紋理縱向撕裂。金屬碎片伴隨著濃厚的黑煙柱與紅色火光迅速向四周擴散。金屬撕裂聲與遠處的低頻轟鳴聲交織成排山倒海的聲波。固定中景，水平視角。第二個能量環呼嘯著飛向地面上一台巨大的雙足步行機甲。環在飛行過程中旋轉產生的橘色光軌，與黑暗背景形成了極強的冷暖對比。此時畫面色彩飽和度瞬間提升。能量環高速旋轉的低頻嗡嗡聲在畫面中持續震動。晃動中景，低角度視角。能量環精準擊中機甲左膝關節核心。巨大的火球從關節內部向外噴發，爆炸的衝擊波將機甲整個上半身向後推去。火花瀑布從爆炸點向外噴灑，覆蓋了十公尺半徑。鏡頭隨著衝擊劇烈晃動。金屬碰撞的沉重聲響與機甲受損電火花持續的劈啪聲在震動中轟鳴。全景側移。機甲的右膝隨後被第三個能量環擊中，徹底癱瘓。巨大的軀體在雙膝盡毀後緩緩向右傾斜，傾斜過程中裝甲板不斷脫落。霧氣背景中哥德式尖塔建築的輪廓隨著機甲倒塌的震動而顫抖。機甲最終撞擊地面的沉悶巨響與碎片落地的聲音由近及遠散開。此時，BGM 的節奏達到了第一個高潮。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎬 「牙醫 — 拆彈小組版」喜劇開場影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '「牙醫 — 拆彈小組版」喜劇開場影片提示詞',
        "prompt": '1. 🦷 牙醫 — 拆彈小組版\n喜劇開場：一位將例行洗牙視為拆彈任務的牙醫。\n\n角色\n\n牙醫：高瘦身材，戴著細框眼鏡，外科口罩隨意地拉在下巴。穿著刷手服，但卻是戰術風格 — 配備工具袋、頭燈，就像',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 狂暴維京戰士衝鋒',
        "category": '🥋 動作戰鬥',
        "title_zh": '狂暴維京戰士衝鋒',
        "prompt": '低角度鏡頭掃過大雨中的泥濘戰場。攝影機向後追蹤，一名巨大的維京戰士向前衝鋒，斧頭在潮濕的地面上拖曳出火花。\n\n閃電劃過——攝影機快速平移，捕捉敵人與他碰撞的瞬間。畫面呈現出混亂的手持攝影質感，隨著他旋轉、劈砍、怒吼，每一擊都將鮮血濺入雨中。\n\n當他進入狂暴狀態時，攝影機快速環繞——聲音變得模糊，只剩下他的呼吸聲與心跳聲。他撲倒一名強敵——展開殘酷的近身肉搏。\n\n結尾：他獨自站在雨中，胸口劇烈起伏，斧頭滴著血。隨著雷聲滾動，攝影機緩緩拉遠。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 Seedance 2.0 提示詞：荒涼海灘上的哥德式機甲戰鬥',
        "category": '🥋 動作戰鬥',
        "title_zh": 'Seedance 2.0 提示詞：荒涼海灘上的哥德式機甲戰鬥',
        "prompt": '全景、水平、固定鏡頭，拍攝荒涼的灰色海灘。霧氣從深處背景向前方蔓延。哥德式建築的輪廓在霧中隱約可見。海灘地面覆蓋著破碎的灰色礫石與焦黑殘骸。整體色調為極低飽和度、冷灰色且壓抑。一位仿生女英雄（身穿白色正式西裝，頸部配有銀色機械護甲與義肢手臂，黑色馬尾，金色齒輪耳環，紅唇，電影級寫實面部特徵且全程保持穩定）站在畫面中央。她的西裝被海風緩緩吹動。她的銀色義肢手臂垂直握著一根法杖。法杖頂端的三個環燃燒著橘紅色能量。能量光芒在女英雄白色西裝的前側投射出溫暖的橘色輪廓光。低沉的史詩配樂在寬廣的聲場中緩緩展開，交織著能量燃燒的嘶嘶聲與沉重的呼吸聲。鏡頭拉遠。女英雄的銀色義肢手臂將法杖猛擊入沙地，衝擊產生了一大團向外擴散的灰色塵土。塵土在側逆光下形成半透明的金色雲霧。三個橘紅色能量環從法杖頂端脫離，懸浮在空中並迅速加速旋轉。每個旋轉的環都拖曳出一道完整的橘紅色光跡。女英雄的義肢手臂突然抬起，發出攻擊信號。她的斗篷隨著手臂動作向後甩動，馬尾髮絲被衝擊氣流帶向前方。法杖擊地的沉重悶響、金屬震動聲以及風掃過沙地的聲音同時湧入。低角度快速推近特寫。女英雄的銀色義肢手臂食指猛烈向上揮動。金色火焰在精密的金屬指尖跳動燃燒。藍白色電弧沿著義肢手臂關節向上蔓延至指尖，與火焰融合。背景中，一座巨大的機械結構開始崩塌。金屬組件在火光中翻滾墜落。指尖劃破空氣的尖銳呼嘯聲與高頻能量匯聚的嗡嗡聲瞬間刺破場景。全景快速水平跟拍。第一個巨型能量環如同飛鋸，以極高的旋轉速度在空中切出一道完整的橘紅色火光弧線。弧線軌跡在深灰色天空中形成一條持續發光的軌道，瞬間切入一艘巨型鋼鐵太空船的側裝甲。穿透的瞬間，裝甲板沿著切割線向外炸開。橘紅色岩漿從切口噴湧而出。鋸片切割金屬的刺耳摩擦聲與火花撕裂聲充斥聲場。俯視跟拍向下壓。能量環穿透側翼並持續切入船體核心艙。核心被刺穿的瞬間引發連鎖爆炸。第一波爆炸呈球狀擴散，第二波沿著船體紋理垂直撕裂。金屬碎片伴隨著濃厚的黑煙與紅色火光迅速向外擴散。金屬撕裂聲與遠處的低頻轟鳴聲交織成震撼的聲波。眼平固定中景。第二個能量環呼嘯著衝向地面上的一台巨型雙足步行機甲。環旋轉產生的橘色光跡與黑暗背景形成了強烈的冷暖對比。此時影像的色彩飽和度突然增加。能量環高速旋轉的低頻嗡嗡聲在畫面中持續震動。低角度晃動中景。能量環精準擊中機甲左膝關節的核心。巨大的火球從關節內部向外噴發。爆炸衝擊波將機甲整個上半身向後推。火花瀑布從爆炸點向外噴灑，覆蓋半徑十公尺。鏡頭隨著衝擊劇烈晃動。金屬碰撞的沉重聲響與受損機甲中持續爆裂的電火花聲在震動中咆哮。全景側移。機甲的右膝隨後被第三個能量環擊中，徹底癱瘓。龐大的身軀在雙膝被毀後緩緩向右傾斜。裝甲板在傾斜過程中持續脫落。背景霧氣中哥德式尖塔建築的輪廓隨著機甲的倒塌而顫動。機甲最終撞擊地面的沉悶巨響與墜落碎石的聲音由近及遠消散。BGM 節奏在此刻達到第一個高潮。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎬 電影感繪畫特寫',
        "category": '🎬 電影敘事',
        "title_zh": '電影感繪畫特寫',
        "prompt": '「街頭男子正在作畫。\n\n[切換] 畫筆在畫布上揮灑筆觸的特寫鏡頭。\n\n無音樂。」',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 Seedance 2.0 提示詞：浪漫晚餐驚喜',
        "category": '🎭 日常生活',
        "title_zh": 'Seedance 2.0 提示詞：浪漫晚餐驚喜',
        "prompt": '核心場景：一場位於高級餐廳的燭光晚餐，丈夫為妻子送上訂製的奢華降噪耳機。妻子感動落淚，並在最後戴上耳機，呈現浪漫時刻。場景 1 (0-1s) ✨ 氛圍營造。畫面：俯拍整個高級餐廳，溫暖的黃色燭光閃爍，柔和的光線透過水晶杯折射，黑色天鵝絨桌布上擺放著精緻的法式料理。身穿絲絨禮服的妻子正低頭切牛排。丈夫溫柔地注視著她，指尖輕撫絲絨禮盒。音效：餐廳內柔和的爵士樂 BGM，刀叉觸碰瓷盤的細微聲響。對話：丈夫（低沉且溫柔）：「親愛的，妳今天辛苦了。」場景 2 (2-3s) 🎧 驚喜揭曉。畫面：特寫鏡頭，丈夫緩緩將絲絨禮盒推過去。妻子抬頭，神情驚訝，睫毛顫動。丈夫打開盒蓋，露出訂製的奢華耳機（金屬質感 + 雕刻細節），在燭光下散發出冷冽的高級光澤。音效：BGM 漸弱，盒子打開的輕微聲響，妻子倒吸一口氣的聲音。對話：妻子（哽咽）：「這是……？」丈夫：「妳總說加班時戴耳機很吵，有了這個，妳就只能聽見我的聲音了。」場景 3 (4-5s) 😭 情感高潮。畫面：妻子面部的特寫鏡頭，淚水滑過臉頰。她抬手掩口，眼中充滿驚喜與感動。丈夫溫柔地為她拭去淚水。音效：BGM 音調升高，加入輕柔的鋼琴聲，妻子細微的啜泣聲。對話：妻子（破涕為笑）：「你怎麼知道我想要這個很久了……」場景 4 (6-7s) 💞 浪漫結尾。畫面：特寫鏡頭，丈夫拿起耳機小心翼翼地為妻子戴上，指尖輕觸她的耳垂。妻子閉上雙眼，露出微笑。當耳機戴好後，鏡頭拉遠至兩人緊握的雙手，燭光將他們的影子模糊成溫柔的剪影。音效：BGM 達到高潮後漸弱，只留下兩人的呼吸聲。對話：丈夫（輕聲）：「從今以後，無論世界多麼喧囂，我就在妳耳邊。」',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🌌 在受損太空站上的零重力太空人奔跑',
        "category": '🌌 科幻賽博',
        "title_zh": '在受損太空站上的零重力太空人奔跑',
        "prompt": '一名身穿白色 EVA 太空衣的女性太空人在地球上方受損太空站的外環上奔跑。\n\n太空站緩慢旋轉，巨大的太陽能板碎裂並漂浮至太空中。\n\n在第 2 秒時，她從旋轉的環狀結構躍向一個漂浮的貨運艙。\n\n攝影機在她身旁漂浮，背景是旋轉的地球。\n\n她抓住把手，擺動身體穿過氣閘艙門，並在碎片撞擊她身後的太空站瞬間封閉艙門。\n\n軌道碎片場、零重力跳躍、旋轉太空站外奔跑、電影級太空光影、4K。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 寧靜湖畔日落場景影片提示詞',
        "category": '🌿 自然風景',
        "title_zh": '寧靜湖畔日落場景影片提示詞',
        "prompt": '一位女孩站在寧靜的湖畔，夕陽西下，長髮隨風飄逸，微風輕拂，背景是連綿的山脈，周圍環繞著閃爍的螢火蟲。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 動漫少女談論布丁並進行音訊同步',
        "category": '🎬 電影敘事',
        "title_zh": '動漫少女談論布丁並進行音訊同步',
        "prompt": '來自 <<<Image1>>> 的角色是一位熱情談論布丁的動漫風格少女。她使用來自 ♪<<<Audio1>>> 的聲音與節奏進行對話，並具備與音訊匹配的自然唇形同步。\n中景，略微低角度，面向攝影機。明亮、溫暖的室內',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 熔岩地上的拉力賽車',
        "category": '🚀 追逐速度',
        "title_zh": '熔岩地上的拉力賽車',
        "prompt": '拉力賽車以全速衝過熔岩頂端，四輪騰空後重重落地並繼續向前疾馳。保險桿高度的鏡頭朝前，鎖定引擎蓋與防滾籠，兩側的黑色岩壁化作深色條紋飛速掠過。賽道轉彎，卡車向右急轉，四輪在鬆散的熔岩礫石上空轉，車身劇烈側傾，隨後懸吊系統蓄力將車輛彈出彎道。鏡頭切換至側面，捕捉礫石飛濺的瞬間，背景是延伸至地平線的平坦熔岩地。接著是廣角鏡頭：從高空俯瞰熔岩地，卡車成為廣闊黑原上的一個鮮豔亮點。低垂的冰島天空壓在地平線上。車輛駛過後，塵土在靜止的空氣中久久不散。黑色熔岩與鮮豔塗裝、冰島平坦陰天、火山平原色調、超寫實拉力攝影、岩石與天空的動態模糊、金屬與輪胎的清晰定格。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 第一人稱視角廚房場景與對話',
        "category": '🎭 日常生活',
        "title_zh": '第一人稱視角廚房場景與對話',
        "prompt": 'global_settings:\nstyle: "寫實廚房場景，高保真"\nperspective: "第一人稱視角（18 歲男性）"\ncharacter: "21 歲優雅女性（嚴格保持 Image 1 的特徵與藝術風格）"\naudio:\nvoice: "成熟御姐音，語氣溫柔"\ndialogue: "好吃～"\nambient: "煎鍋滋滋聲，輕柔自然的笑聲"\nmusic: "無（除環境音外保持靜音）"\ntechnical: "連續 POV，無剪輯，無浮水印，無文字，10 秒"\n\nscene_setup:\nlocation: "廚房，站在爐灶旁"\naction: "穿著圍裙的女性正在煎蛋；我從她身後靠近"\n\nstoryboard_sequence:\n0_3s: "鏡頭靠近她的背部，她正在做飯。一隻手從畫面底部伸入，從碗中拿起水果並遞到她唇邊。"\n3_6s: "她側頭看向鏡頭，微笑，咬下水果，並以滿足且成熟的語氣說出「好吃～」。"\n6_8s: "她完全轉身面向鏡頭（看著「我」）。一隻手伸出擦去她唇邊的一滴果汁。她的雙眼彎成溫暖的月牙狀。"\n8_10s: "她轉身回到爐灶前翻動雞蛋。鏡頭停留在她忙碌的背影以及鍋中升起的熱氣上。"\n\nnegative_constraints:\n- "低畫質、模糊、卡頓、破圖、肢體變形"\n- "外貌幼態、非 POV、背景音樂、文字疊加"\n- "缺少餵食動作、動作僵硬"',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 高速電影級蛛絲擺盪動作場景',
        "category": '🥋 動作戰鬥',
        "title_zh": '高速電影級蛛絲擺盪動作場景',
        "prompt": '生成一段超寫實、電影級的高速動作影片，同時完整保留參考圖像 <<<Image1>>> 的特徵。\n\n一個電影級動作場景，一名男性角色在黃金時刻的暖光下，利用高張力的蜘蛛絲狀材質在摩天大樓間穿梭。所有動作必須發生在建築物之間，非常靠近外牆與窗戶，且高度位於屋頂線以下或僅僅觸及屋頂線。請勿長時間停留在空曠的天空中。\n\n[動作序列（重要）]\n\n序列以「向前加速」開始。\n<<<Image1>>> 向前上方建築物發射蛛絲，張力瞬間將他向前拉動，使他筆直地穿過建築物之間的縫隙。他貼著牆面與窗戶前進，展現出強烈的速度感與深度感。\n\n接著，保持慣性，他執行一次大跳躍，一躍跨過建築物間的空隙。此處他會短暫處於開放空間，但隨即過渡到下一個動作。\n\n跳躍後，角色短暫失去平衡並開始墜落。請描繪真實的墜落感，因重力而急速下墜，營造出瞬間的驚險感。\n\n墜落過程中，<<<Image1>>> 立即向建築物邊緣或結構上方發射蛛絲，在半空中勾住目標。那一瞬間，強烈的張力猛烈地將他的身體向上拉，產生爆發性的上升。\n\n隨後，他再次向前發射蛛絲，回到向前加速的狀態。\n\n蛛絲使用次數限制在總共 2 至 3 次，確保每個動作都清晰可見。\n\n[動作特性]\n所有動作必須遵循基於慣性、重力與張力的真實物理規律。禁止減速或懸停。速度流動必須連續，創造出「加速 → 跳躍 → 墜落 → 爆發性上升 → 再加速」的清晰動態節奏。\n\n[身體表現]\n發射蛛絲的瞬間，一隻手臂會猛力向前或向上伸出。加速期間，身體因拉力而伸展拉長，雙腿向後拖曳。跳躍期間，全身帶有慣性；墜落期間，身體根據重力自然下垂。拉升期間，身體以動態動作被向上提起。\n\n[攝影機]\n攝影機應主要保持與向前移動方向一致的跟拍鏡頭，從後方或近距離跟隨角色。持續強調向深處移動的感覺，最大化速度感與視角變化。請勿使用側面角度。\n\n[指導方針]\n利用玻璃帷幕牆的反射、流動的窗戶線條、強烈的動態模糊、因風壓而飄動的衣物以及鏡頭光暈，營造出壓倒性的速度感與沉浸感。與牆壁的距離應始終保持貼近，強調近距離碰撞的驚險感。\n\n[情緒]\n表現出專注、興奮、腎上腺素飆升、自信，以及從短暫危機（墜落）中恢復後的快感。\n\n總體而言，請優先考慮超寫實主義、電影級品質、高速直線運動、強烈的深度感、動態動作節奏以及物理真實性。',
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🎬 適用於 Seedance 2.0 的連續一鏡到底影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '適用於 Seedance 2.0 的連續一鏡到底影片提示詞',
        "prompt": '連續一鏡到底，攝影機傾斜、翻轉、旋轉，穿梭於一艘巨型豪華郵輪。從陽光明媚的頂層甲板飛過，閃避沙灘球與日光浴遊客，攝影機直衝入一個蜿蜒的透明水上 Slides，滑過尖叫的孩童後濺入主泳池。掃過水下，毫不費力地穿過玻璃地板，直接進入下方優雅的豪華餐廳，穿梭於水晶吊燈、碰撞的香檳杯與端著銀盤的服務生之間。攝影機衝過旋轉的廚房門，進入運作中、一塵不染的引擎控制室，從船尾排氣口飛出，在夕陽映照海面時，滑過翻騰的白色泡沫尾跡。無剪輯，超現實運鏡，流暢轉換，充滿活力、動態感與電影質感。8K 高畫質，高品質影像。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 不可能的單鏡頭中世紀酒館巡禮',
        "category": '🎬 電影敘事',
        "title_zh": '不可能的單鏡頭中世紀酒館巡禮',
        "prompt": '連續單鏡頭，攝影機傾斜、翻滾、旋轉，穿梭於熱鬧的中世紀奇幻酒館。從壁爐上方呼嘯而過，矮人正在轉動烤野豬，攝影機向下俯衝進入地板下方的小老鼠洞，滑過一隻囤積金幣的老鼠。隨後向上掃過傳菜梯進入隱密的盜賊巢穴，兜帽人正在發牌，攝影機穿梭於匕首與散落的寶藏之間。攝影機鑽入上方法師混亂的書房，經過發光的漂浮書籍與冒泡的藥瓶，最後衝出石製煙囪，轉場為月光下火炬照亮的廣闊城牆城市航拍視角。無剪輯，不可能的運鏡，流暢轉場，充滿活力，動態感十足，電影級質感。8K 高解析度，高品質影像。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌌 不可能的單鏡頭科幻飛船之旅',
        "category": '🌌 科幻賽博',
        "title_zh": '不可能的單鏡頭科幻飛船之旅',
        "prompt": '連續單鏡頭，攝影機傾斜、翻滾、旋轉，穿梭於一艘巨大的科幻世代飛船。從嗡嗡作響的引擎核心開始飛行，閃避電弧電漿，攝影機向下俯衝，穿過狹窄的通風管道進入船員宿舍，一名機械師正躺在吊床上休息，滑過漂浮的全息介面。掃入充滿活力的水耕栽培室，園丁正在照料發光的藍色藤蔓，穿梭於懸掛的根系與噴霧灑水器之間。攝影機俯衝進入繁忙的指揮艦橋，軍官們正在監控宇宙地圖，隨後平滑地穿過厚實的玻璃觀景窗，轉場至宏偉太空船航行於閃爍星雲中的高空俯瞰視角。無剪輯，不可能的攝影機運鏡，流暢的轉場，充滿活力、動態感，電影級質感。8K 高解析度，高品質影像。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 亞馬遜雨林中不可能的運鏡',
        "category": '🌿 自然風景',
        "title_zh": '亞馬遜雨林中不可能的運鏡',
        "prompt": '連續單鏡頭，攝影機傾斜、翻滾、旋轉，穿梭於茂密的亞馬遜雨林生態系統中。從穿過霧氣繚繞的樹冠層開始，閃避懸掛的藤蔓和一隻熟睡的樹懶；攝影機向下俯衝進入一棵巨大古樹的空心樹幹，滑過生物發光真菌和蝙蝠群。掃過潮濕的森林地面，緊跟著一列快速移動、搬運綠色碎片的切葉蟻，穿梭於巨大的蕨類植物和露珠之間。攝影機直接潛入湍急的叢林河流，在游動的食人魚和搖曳的水生植物間平滑過渡，隨後衝出咆哮的瀑布，呈現出黎明時分無限綠色叢林的震撼空拍視角。無剪輯，不可能的運鏡，無縫過渡，充滿活力，動態，電影感。8K 高解析度，高品質影像。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 高速獵豹追蹤攝影',
        "category": '🚀 追逐速度',
        "title_zh": '高速獵豹追蹤攝影',
        "prompt": '位於獵豹後方 2.5 公尺處的穩定器後方追蹤鏡頭，鎖定時速 112 公里穿過茂密的叢林底層，攝影機高度 40 公分，保持精確步調且零垂直漂移。主體向左急轉 28 度繞過巨大的無花果樹幹，脊椎收縮後爆發性完全伸展，懸空階段四肢離地，斑駁的黃金時刻光線在斑點皮毛上閃爍。隨即向右轉 32 度穿過兩棵桃花心木之間的縫隙，身體傾斜方向與攝影機傾斜方向相反，背景植被拉伸成純粹的動態模糊，而主體在畫面中央保持極致銳利。筆直衝過蕨類植物走廊，隨後向左大幅傾斜 25 度避開倒下的原木，脊椎在每個步態週期中展現最大程度的收縮與伸展。向右轉 30 度跟隨自然路徑彎曲，溫暖的側光捕捉肌肉線條，長長的陰影在高速下掃過叢林地面。最後在竹叢間向左編織轉向 27 度，全程保持最高速度，每一次方向改變皆受環境驅動，攝影機鎖定平行位置，始終維持在後方追蹤視角。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 受《快打旋風》啟發的 Seedance 2.0 汽車破壞影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '受《快打旋風》啟發的 Seedance 2.0 汽車破壞影片提示詞',
        "prompt": '[0-4 秒 爆發性開場] 在光線昏暗、廢棄的地下停車場中，冷白色的管狀天花板燈勾勒出一位留著高髮髻、兩側剃光的亞洲戰士輪廓（參考圖 1）。他身穿破損的白色長袍，外罩精緻的銀色龍紋機械肩甲、頸甲與護腕。手持攝影機從低角度向前推進。戰士原本蹲在一輛破舊汽車的車頂上，突然全身緊繃，白袍下的肌肉繃緊。他的雙腳（穿著戰鬥靴）猛烈地踩碎引擎蓋 [金屬引擎蓋瞬間凹陷並撕裂，金屬碎片四處飛濺，伴隨著刺耳的金屬摩擦聲]。他猛然抬頭，眼神銳利兇狠，髮髻隨之晃動。整個上半身向前衝刺，銀色肩甲在冷光下閃爍。攝影機快速跟隨，瞬間提升戰鬥張力；[4-8 秒 節奏性交鋒] 戰士覆蓋著銀色機械護腕的粗壯手臂猛烈擊打車身，連續的重擊帶有毀滅性的蠻力。攝影機快速橫搖並跟隨每一次重擊。第一拳擊碎前擋風玻璃 [強化玻璃瞬間炸裂成蜘蛛網狀，無數玻璃碎片噴湧而出，車內座椅因拳擊的衝擊力而掀起]。第二記肘擊猛烈撞擊車側 [車門板直接被擊穿，車軸斷裂，輪胎瞬間爆裂洩氣，車身向一側劇烈傾斜]。戰士利用慣性翻身，強壯的雙腿蹬開車身。攝影機環繞並跟隨他的旋轉動作，全程保持連續動作，無任何剪輯斷點。每一次攻擊都伴隨著精確的物理反饋。手持攝影機的輕微晃動模擬了真實戰鬥的衝擊感。灰塵在頭頂燈光下瀰漫飛舞，白袍戲劇性地飄動，銀色鎧甲反射出強烈光芒；[8-12 秒 巔峰對決] 攝影機切換為 360 度環繞運鏡，同時啟動慢動作，展現戰士巔峰的力量爆發。戰士匯聚全身力量，雙拳緊握並重重砸向嚴重變形的汽車。在慢動作中，所有肌肉線條最大限度地緊繃，青筋暴起。銀色機械肩甲與護腕在燈光下散發出冷冽光澤。留著短鬍鬚的髮髻戰士面容極度兇狠。在拳頭接觸車身的瞬間，極致的破壞力爆發 [整輛車身完全被壓扁，金屬框架完全彎曲斷裂，油箱破裂，汽油混合著機油噴湧而出，地面碎石與金屬碎片被衝擊波掀向空中，灰塵形成圓形氣流向外擴散]。慢動作最大限度地展示了力量爆發的每一個細節，並呈現出織物與金屬的極致物理模擬；[12-15 秒 最終定格] 慢動作結束。攝影機快速拉回至低角度仰拍。戰士從壓扁的汽車上猛然挺直站起，雙腳踩在完全報廢的車輛上，對著天空發出恐怖的咆哮。他全身緊繃，破損的白袍在衝擊後的餘風中劇烈飄動 [地面殘留的汽油被摩擦火花點燃，微弱的火焰在車底蔓延，周圍牆壁佈滿了碎片飛濺造成的密集凹痕，灰塵緩緩沉降，整個地下停車場迴盪著金屬餘震的嗡嗡聲]。最後一幕定格在戰士極具壓迫感與威懾力的姿勢上。全域參數：8K 超高畫質，電影級暗冷色調調色，極致的光影對比，織物與肌肉運動的完整物理模擬，模擬手持攝影機以呈現真實戰鬥衝擊感，保留高速戰鬥的爆發力，全程連續動作無斷點，高細節銀色機械鎧甲反射與動態白袍飄動。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🌿 穿梭東南亞夜市的「不可能」運鏡',
        "category": '🌿 自然風景',
        "title_zh": '穿梭東南亞夜市的「不可能」運鏡',
        "prompt": '格式：15 秒 / 單一連續「不可能」運鏡 / 無對白\n風格：擁擠的東南亞夜市、濕潤石板路、蒸汽與火焰、橘色燈籠光影、8K 寫實電影級地面至空中視角\n鏡頭 01 (0:00–2:00)：攝影機從腳踝高度開始。腳的森林——涼鞋、赤腳、夾腳拖踩在閃爍的濕潤石板路上。夜市喧囂聲震耳欲聾。攝影機如流水般穿梭在雙腿之間。音效：濕潤的腳步聲、遠處攤販的叫賣聲、食物滋滋聲。\n\n鏡頭 02 (2:00–3:30)：攝影機緩緩上升，越過冒著蒸汽的炒鍋。瓦斯火焰在視線高度瞬間爆發——攝影機短暫被橘色火焰吞沒，隨後穿過火焰，鏡頭不中斷。音效：瓦斯火焰「轟」的一聲。炒鍋滋滋聲。\n鏡頭 03 (3:30–5:00)：攝影機在中高度穿梭於懸掛的燈籠之間，像飛蛾般掠過。紅色與橘色的光影在鏡頭上閃爍。音效：燈籠鏈條的碰撞聲。人群的低語聲。\n鏡頭 04 (5:00–6:30)：攝影機突然俯衝至一張矮桌下方。一個孩子在桌下的袋子上睡著了。在混亂中出現一處安靜的角落。攝影機停留一拍。音效：噪音變得沉悶。孩子安靜的呼吸聲。\n鏡頭 05 (6:30–8:00)：攝影機從炭火烤架的煙霧中重新升起——鏡頭短暫被煙霧遮蔽，隨後浮現於攤位遮雨棚上方。音效：木炭劈啪聲。煙霧嘶嘶聲。\n鏡頭 06 (8:00–10:00)：攝影機持續上升——現在來到屋頂上方。夜市展現出無盡的橘色燈籠海，向地平線延伸。攝影機緩慢傾斜，捕捉全景規模。音效：夜市喧囂聲逐漸轉為低沉的環境音。\n鏡頭 07 (10:00–12:00)：攝影機開始下降——目標鎖定在市場邊緣的一個攤位。一名攤販正在獨自清點硬幣。周圍的一切正逐漸收攤。音效：遠處攤販的叫賣聲一個接一個消失。\n鏡頭 08 (12:00–13:30)：攝影機停在攤販的手部。特寫硬幣被有條不紊地堆疊。上方有一盞燈籠在搖曳。音效：硬幣碰撞聲。燈籠在風中搖晃的聲音。\n鏡頭 09 (13:30–15:00)：攝影機緩慢向上傾斜至攤販的臉部。他們抬頭——直視鏡頭。定格。淡出至全黑。音效：最後一枚硬幣放下的聲音。寂靜。\n風格備註：地面視角營造出幽閉恐懼與壓迫感。空拍鏡頭則是情感的釋放。整體色調為溫暖的橘紅色——結尾轉為琥珀色。全程呈現濕潤石板路的倒影。使用真實火焰與煙霧，不使用 CG 替代。8K 解析度。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎵 音樂錄影帶風格姿勢加速提示詞',
        "category": '🎵 舞蹈音樂',
        "title_zh": '音樂錄影帶風格姿勢加速提示詞',
        "prompt": '格式：15 秒 / 128 BPM / 一鏡到底 / 鏡頭在姿勢間加速切換\n\n主體：@[image1]，一位留著柔和波浪捲髮的金髮女性，身穿淺色緞面睡袍，露出肩膀，並戴著標有「koda」字樣的耳罩式耳機。每個姿勢的定格都如同',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎵 日語饒舌音樂錄影帶提示詞（含參考圖片）',
        "category": '🎵 舞蹈音樂',
        "title_zh": '日語饒舌音樂錄影帶提示詞（含參考圖片）',
        "prompt": "音樂錄影帶中的女性以日語饒舌歌詞：「Oops, I appeared quickly. I was born here, jumped out, and am on Earth. I knew it since then: meeting you, falling in love, it's destiny.」（哎呀，我瞬間出現。我在這裡出生，一躍而出，來到地球。我從那時起就知道了：與你相遇、墜入愛河，這就是命運。）",
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🐱 為 CapCut 製作皮克斯風格的商業廣告',
        "category": '🐱 動物趣味',
        "title_zh": '為 CapCut 製作皮克斯風格的商業廣告',
        "prompt": '一支為 CapCut 製作的趣味廣告，描述一名壓力巨大的影片剪輯師與從筆電中跑出的怪物搏鬥，隨後 CapCut 出面解救。採用多鏡頭與皮克斯動畫風格。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 適用於 Seedance 2.0 的賽博龐克動畫電影級戰鬥場景提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '適用於 Seedance 2.0 的賽博龐克動畫電影級戰鬥場景提示詞',
        "prompt": '賽博龐克動畫，電影級，霓虹光暈，夜間未來城市，全息標誌，潮濕反光的街道，霧氣與煙霧，超高細節，動態動作\n四個角色：一位手持法杖的睿智烏龜大師、一位身穿黑色戰術裝備的人類戰士、一具核心發出藍光的巨型裝甲機器人，以及一位戴著面罩並帶有發光刺青的霓虹賽博戰士\n機器人墜地引發衝擊波，人類戰士向前滑行發動攻擊，賽博戰士以故障速度衝刺，烏龜大師冷靜格擋，火花、能量與光軌充滿整個畫面\n從寬鏡頭電影感切換至快速近身格鬥鏡頭，使用 24mm 與 50mm 鏡頭，動態運鏡，輕微鏡頭晃動\n強烈的霓虹燈光，藍色、紫色與粉色的光影映照在潮濕地面上\n激烈、史詩般、高能量的電影級戰鬥\n8–10 秒\n無文字，無字幕，無浮水印，流暢動畫，角色一致性',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 真人科幻戰士提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '真人科幻戰士提示詞',
        "prompt": 'CHARACTER REFERENCE Image1= 戰士臉部。Image2 = 紅色機器人裝甲參考。IMAX 70mm 膠卷質感、Panavision 35mm 鏡頭、f4、手持攝影晃動感。真人科幻、4K、淺景深散景、冷青藍色調、紅色能量劍作為',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 適用於 Seedance 2.0 的電影級街頭魔術影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '適用於 Seedance 2.0 的電影級街頭魔術影片提示詞',
        "prompt": '一段風格化的電影級 3D 動畫，場景設定在夜晚的城市街道，地面潮濕且帶有倒影，伴隨柔和的路燈與霓虹光影。畫面中央站著一位擬人化的白兔魔術師，身穿黑色燕尾服、白色襯衫、黑色領結並戴著黑色高禮帽，周圍圍繞著一圈觀眾。兔子以標準 52 張撲克牌進行流暢且專業的洗牌表演。牌組在胸前均勻扇形展開，每張牌清晰可見且各不相同。鏡頭外的一隻手從扇形牌中選出一張牌——紅心 A。兔子接過該牌並清晰地展示給鏡頭看。兔子輕彈紙牌，紅心 A 的邊緣開始發光，隨後分解成細小的紅色與金色粒子。這些粒子形成一道受控且連續的流動光束，帶有動態軌跡，向街道前方飄散。鏡頭跟隨粒子流向一棟大型玻璃建築外牆移動。撞擊瞬間，一個光點出現並以網格狀向玻璃表面擴散。整棟建築外牆被點亮，一個巨大且明亮的紅心 A 在牆面上形成，輪廓清晰，伴隨細微的脈衝光。短暫停留後，巨大的紅心 A 再次分解成粒子。粒子反向流動，穿過空氣回到兔子身邊。兔子向前邁步並伸手抓取飛回的粒子。在特寫鏡頭下，粒子壓縮並重組成一張完整的撲克牌回到兔子手中——正是那張完好無損的紅心 A。兔子將牌展示給鏡頭。鏡頭緩慢拉遠，展現出周圍觀眾的反應與掌聲，背景中的城市燈光與倒影依然生動鮮明。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 3D 卡通序列影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '3D 卡通序列影片提示詞',
        "prompt": '15 秒連續單鏡頭卡通序列。\n無剪輯。無場景轉換。\n\n風格化 3D 卡通動畫，明亮鮮豔的色彩，簡潔的形狀，柔和的燈光，誇張的表情，擠壓與拉伸效果，彈性動作，強烈的視覺易讀性。\n\n清晰的喜劇節奏，漸進式動作。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 真實感 UGC 影片生成',
        "category": '🎬 電影敘事',
        "title_zh": '真實感 UGC 影片生成',
        "prompt": '製作一部具備真實感、iPhone 風格的直式 UGC 影片（9:16 長寬比），總時長精確為 12 秒。畫面應呈現自然的掌鏡手感，於自然光充足的室內空間拍攝，且不包含背景音樂……',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🚀 微型滑板追逐場景',
        "category": '🚀 追逐速度',
        "title_zh": '微型滑板追逐場景',
        "prompt": '一名微型女孩踩著小滑板在兒童房地板上高速飛馳。在這種比例下，人類大小的玩具和家具顯得極其巨大。攝影機從主角後方的低機位進行跟拍，保持連續的長鏡頭風格，並不斷向場景深處推進。請使用超廣角鏡頭、動態模糊、景深效果以及電影級燈光。影片速度分三個階段逐漸提升。第一階段，她穿過如同樂高城市建築間峽谷般的狹窄通道，在積木之間進行繞樁滑行。第二階段，一顆巨大的球從前方滾來，迫使她貼牆滑入狹窄縫隙，驚險地躲過掉落的積木，並精準地穿過一輛行駛中的微型汽車輪胎之間。第三階段，她穿過一本因風吹而即將合上的繪本頁面縫隙，從玩偶擺動的手臂下溜過，最後以最高速度衝入即將關閉的玩具箱蓋縫隙，消失在黑暗深處。影片應充滿刺激與快感，呈現連續不斷的驚險閃避。透過在真實兒童房場景中運用微觀視角特有的巨大障礙物與狹小縫隙，營造出身臨其境的遊樂設施般的體驗。',
        "lang": '日本語',
        "featured": False,
    },
    {
        "label": '🌿 不可能的冰封海嘯鏡頭',
        "category": '🌿 自然風景',
        "title_zh": '不可能的冰封海嘯鏡頭',
        "prompt": '一道巨大的海水牆在沿海高速公路上方升起並凍結於崩塌瞬間。車輛與碎片被困在懸浮的液體中。攝影機從冰封的波浪下方開始，向上傾斜以展現其不可思議的規模。隨後，攝影機直接滑入水體，在波浪全速崩塌前，過渡到懸浮水滴內部的沉浸式視角。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 霓虹賽博龐克城市中的賽博忍者戰鬥',
        "category": '🥋 動作戰鬥',
        "title_zh": '霓虹賽博龐克城市中的賽博忍者戰鬥',
        "prompt": '夜晚的霓虹賽博龐克城市（空中俯瞰視角）。一名戴著面具的賽博忍者在半空中使用巨大的書法毛筆進行戰鬥。\n風格：超高速、不間斷的連續動作。賽博龐克 × 書法能量。\n\n鏡頭 1：鳥瞰視角，緩慢 → 爆發性加速，布料與鎖鏈擺動，霓虹燈光閃爍',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 東南亞夜市 8K 電影級影片提示詞',
        "category": '🌿 自然風景',
        "title_zh": '東南亞夜市 8K 電影級影片提示詞',
        "prompt": '格式：15 秒 / 單一連續高難度運鏡 / 無對話 \n風格：擁擠的東南亞夜市、濕潤地面、蒸汽與火焰、橘色燈籠光影、8K 寫實電影級地面至空中運鏡 \n鏡頭 01 (0:00–2:00)：鏡頭從腳踝高度開始。森林',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 暗黑奇幻動作場景影片提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '暗黑奇幻動作場景影片提示詞',
        "prompt": '15 秒連續單鏡頭動作場景。\n無剪輯。無場景轉換。\n\n暗黑奇幻寫實風格，泥濘戰場，雨天，低光源，深沉陰影，大型生物比例，強調物理重量感，電影級對比度\n\n緩慢沉重的動作，伴隨爆發性的衝擊感\n\n場景：',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🐱 史詩級貓咪功夫動畫預告片',
        "category": '🐱 動物趣味',
        "title_zh": '史詩級貓咪功夫動畫預告片',
        "prompt": '史詩級 13 秒動畫預告片（簡潔版，英文）：\n\n風格：電影感、超動態、夢工廠級動畫、戲劇性光影、動態模糊、史詩規模、快速剪輯、情感弧線\n\n0–2 秒\n笨拙的灰色貓咪穿著黃色功夫裝滑倒摔跤，被穿著灰色道袍、留著長白眉毛的橘色貓大師打倒。\n大師（冷淡地）：「太慢了。」\n旁白：「他原本一無是處。」\n\n2–5 秒\n訓練蒙太奇：灰色貓咪渾身瘀青、氣喘吁吁、踢腿失敗、在雨中倒下，然後再次站起。\n灰色貓咪（低語）：「再來一次……」\n旁白：「直到他選擇站起來。」\n\n5–8 秒\n競技場揭幕：大型動物王國錦標賽，觀眾歡呼。灰色貓咪獨自站立。\n老虎猛撲 → 快速閃避 → 反擊。\n旁白：「面對強者。」\n\n8–11 秒\n快速剪輯：老鷹俯衝攻擊 → 空中迴旋踢；獅吼對決 → 爆炸性衝擊。\n灰色貓咪（大喊）：「我不怕！」\n旁白：「變得勢不可擋。」\n\n11–13 秒\n最後鏡頭：灰色貓咪以勝利姿勢落地，風吹過。大師在一旁觀看，微微點頭。\n大師（溫和地）：「你準備好了。」',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 適用於 Seedance 2.0 的藝術家工作室電影感影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '適用於 Seedance 2.0 的藝術家工作室電影感影片提示詞',
        "prompt": '在寬敞且陽光充足的工作室裡，一位藝術家手持畫筆站在巨大的畫布前，全神貫注地投入創作。溫暖的電影感自然光透過高大的窗戶傾瀉而下，投射出柔和的陰影，在充滿紋理的牆面與木質地板上舞動。空氣中瀰漫著創作的氣息，散落的顏料管、畫筆和草圖暗示著靈感的湧現。每一筆揮灑都讓畫布彷彿有了生命，捕捉住當下那份熱情與專注。整個場景顯得生動、親密且充滿藝術能量，邀請觀眾見證想像力在動態中的誕生。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 史詩級拳擊賽：貓咪對決貴賓犬',
        "category": '🥋 動作戰鬥',
        "title_zh": '史詩級拳擊賽：貓咪對決貴賓犬',
        "prompt": '一場史詩級拳擊賽，由身穿紅色短褲的橘貓對決身穿黑色短褲的貴賓犬',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 AI 婚禮影片提示詞：極簡森林風格與光影特效',
        "category": '🎭 日常生活',
        "title_zh": 'AI 婚禮影片提示詞：極簡森林風格與光影特效',
        "prompt": '主題 2：極簡森林風格 - 綠野仙蹤，沐浴在光影中的愛戀。視覺核心：運用丁達爾效應（耶穌光）以及斑駁光影的質感，營造出空靈、清新且充滿生命力的仙境感。真人實拍風格，清新靈動，4K 高畫質。0-4 秒：無人機視角穿過樹冠向下俯衝，水平向前推進。在清晨的原始紅杉林中，濃霧尚未散去，強烈的丁達爾效應（耶穌光）穿透葉片，傾瀉而下形成光束。新娘身穿輕盈的法式蕾絲吊帶婚紗，新郎身穿淺卡其色亞麻西裝。兩人在巨大的苔蘚樹根上赤腳奔跑，婚紗裙擺輕盈地穿梭於光影之間。5-9 秒：鏡頭切換為低角度跟拍，仰視視角。新娘擁有可愛的圓臉、柔和的拱形眉、清澈的杏眼、精緻的鼻尖、桃粉色嘴唇，笑容甜美；新郎輪廓柔和、眉眼溫柔、鼻樑高挺，嘴角帶著寵溺的微笑。兩人停在一道巨大的主光束下。新郎從背後擁抱新娘，雙手交疊。微風拂過，發光的金色葉片在空中飄落。10-15 秒：鏡頭推進至極致特寫的側臉鏡頭。斑駁的樹影緩慢地在他們臉上移動。新娘閉上雙眼感受陽光，新郎輕輕將下巴抵在新娘頭頂。畫面充滿極簡的療癒能量，綠色背景柔和虛化，一隻發光的螢火蟲緩緩飛過鏡頭前。畫面定格在陽光照亮兩人微笑側臉的瞬間。音效：空靈的吉他撥弦聲、清脆的鳥鳴聲、踩在落葉上的沙沙聲，以及悠揚的愛爾蘭笛聲。禁止事項：任何文字、字幕、LOGO 或浮水印。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎵 東京 K-pop 風格舞蹈 MV',
        "category": '🎵 舞蹈音樂',
        "title_zh": '東京 K-pop 風格舞蹈 MV',
        "prompt": '生成一段高品質、高能量的 K-pop 風格舞蹈 MV 片段，並注重鏡頭構圖。使用動態追蹤鏡頭，攝影機平滑地圍繞主角進行 360 度環繞，並配合推拉鏡頭。畫面聚焦於一位年輕且充滿活力的日本女性，她展現出優雅且爆發力十足的跳躍、旋轉與歌唱動作。她身穿時尚的淺粉色百褶裙和白色短版毛衣，頭髮隨意編織成辮子並以絲帶固定。場景設定在陽光明媚的東京公園，周圍環繞著盛開的櫻花樹，花瓣如雪般飄落。視覺風格為電影級寫實感，呈現優美的日系高調色彩與豐富的景深效果。影片的視覺節奏應與背景中輕快、節奏感強的流行音樂精準同步。角色的表情應生動、燦爛且愉悅，並模擬自然的歌唱口型。確保角色的舞蹈動作連貫且無跳躍感，並在攝影機旋轉時保持光影的自然過渡。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎬 包含多套服裝與特效的時尚序列',
        "category": '🎬 電影敘事',
        "title_zh": '包含多套服裝與特效的時尚序列',
        "prompt": '參考 @image 1 中模特兒的臉部特徵。模特兒穿著 @image 2 @image 3 @image 4 @image 5 @image 6 中的服裝，靠近鏡頭並分別做出俏皮、冷酷、可愛、驚訝與帥氣的姿勢，每個姿勢搭配不同的服裝。每次更換服裝時畫面會進行切換，並參考參考影片中的魚眼鏡頭效果，以及殘影與閃爍的炫目視覺特效。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🐱 適用於 Seedance 2.0 的貓咪拉麵師傅 ASMR 影片提示詞',
        "category": '🐱 動物趣味',
        "title_zh": '適用於 Seedance 2.0 的貓咪拉麵師傅 ASMR 影片提示詞',
        "prompt": '創作一段以貓咪在深夜食堂製作手工拉麵為主題的短片，採用電影感調色（暖色調，充滿生活氣息）、細膩顆粒感以及淺景深效果。\n主角是一隻貓，飾演專業拉麵師傅，其外觀嚴格參考 [@Image 1]。\n場景設定在城市街道旁的日式深夜拉麵攤前。背景包含溫暖的黃色燈籠、木製吧台，以及遠處模糊的街道霓虹燈。\n影片內容需按以下步驟/鏡頭呈現：\n\n揉麵與切麵：穿著小圍裙的貓咪在撒了麵粉的木製專案上規律地揉麵，接著使用鋒利的刀將麵團切成均勻的細麵條。\n\n煮麵與瀝水：貓咪將麵條抖散後放入沸騰的大鍋中。幾秒鐘後，用竹篩將麵條撈起，熟練地在空中用力甩動兩次以瀝乾多餘水分。\n\n準備湯頭：貓咪手持精緻的長柄勺，從一鍋濃郁的白骨湯中舀起一勺湯，緩慢地倒入深藍色的陶瓷碗中。\n\n擺盤：貓咪用筷子將煮好的麵條整齊地放入碗中，接著依序擺上兩片厚實的叉燒、半顆溏心蛋、幾片海苔與蔥花，動作精準。\n\n結尾：最後一個鏡頭顯示貓咪師傅輕輕將冒著熱氣的拉麵推向鏡頭，並微微點頭示意。\n\n要求：\n\n影片風格：寫實、畫面清晰、中景鏡頭。\n\n音效 (ASMR)：整段影片無需旁白，但必須強化以下聲音：切麵時的「噠噠」聲、麵條入水的「嘩啦」聲、瀝水時的「颯颯」聲，以及熱湯倒入碗中的流動聲。\n\n背景音樂：背景播放輕柔舒緩的薩克斯風音樂，營造安靜的深夜氛圍。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎬 電影感滑雪影片生成',
        "category": '🎬 電影敘事',
        "title_zh": '電影感滑雪影片生成',
        "prompt": '請根據提供的參考圖片生成一段滑雪影片。整體風格應明亮、清晰，充滿運動活力，並具備流暢的動作與電影級鏡頭語言。時間軸與鏡頭設計如下：\n\n0–3 秒：圖片中的角色在雪地中對著鏡頭微笑。伴隨細微的鏡頭晃動與飄落的雪花。背景風聲逐漸增強，畫面中出現快速流動的風雪。\n\n3–5 秒：快速剪輯至角色腳部的特寫鏡頭，滑雪板固定器扣上，壓碎雪地。同時鏡頭上升，過渡到陡峭雪坡的俯視視角，展現出清晰的坡度，速度感即將爆發。\n\n5–8 秒：角色從高處高速滑下。鏡頭 1 為側前方中景跟拍，身體前傾，動作俐落；鏡頭 2 切換至俯拍視角，陡峭的雪坡向下延伸，雪道線條快速拉長，營造出強烈的速度感。\n\n8–11 秒：一系列快速的鏡頭剪輯。低角度地面鏡頭捕捉滑雪板掠過雪面的瞬間，高速揚起雪粉；廣角鏡頭呈現角色在陡坡上完成優美的轉彎，身體與雪線形成流暢的弧度。\n\n11–13 秒：鏡頭回到正面跟拍，角色高速衝向鏡頭，在近距離處完成一個俐落的轉彎，激起漫天雪霧。\n\n13–15 秒：大量雪粉直接噴濺至鏡頭上，將畫面覆蓋在白色雪霧中。鏡頭短暫失焦後定格，留下強烈的動態殘影。整體強調速度感、剪輯節奏、真實動作與青春活力，呈現明亮、輕盈的美學，突顯滑雪的刺激與自由。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 第一人稱視角：冰封老鷹救援',
        "category": '🎭 日常生活',
        "title_zh": '第一人稱視角：冰封老鷹救援',
        "prompt": '從第一人稱視角拍攝。一隻巨大的棕白相間老鷹被凍結在霧氣繚繞的山區，困在雪地木欄杆上的一層薄薄半透明冰殼中。畫面中，那個人正用小錘子輕輕敲擊並震碎冰層。冰塊碎裂並大塊剝落，露出了下方老鷹的羽毛。老鷹抖動翅膀，帶著如釋重負的表情看向鏡頭，隨後飛向霧氣繚繞的紅色背景。角色說道：「放輕鬆，夥伴，再撐一下。再敲一下。好了，就是這樣。沒問題，準備好隨時可以飛。」',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🐱 Gugugaga 與 Doro 的可愛 Q 版動畫',
        "category": '🐱 動物趣味',
        "title_zh": 'Gugugaga 與 Doro 的可愛 Q 版動畫',
        "prompt": '採用鮮豔可愛的 Arknights Endfield 風格，製作一段超可愛的 Q 版動畫：可愛的企鵝帽寶寶管理員 Gugugaga（戴著黑色亮面企鵝頭盔、黃色鳥喙、閃爍著愛心與光芒的藍色大眼睛、深色鮑伯頭瀏海、濃厚的腮紅、嬌小的身軀）與她最好的朋友 Doro 在溫馨歡樂的場景中俏皮互動。她們正在跳躍、擁抱、追逐，或是做出各種呆萌可愛的動作，周圍伴隨著漂浮的愛心、閃光和動態線條。明亮的粉彩色調——柔和的粉色、桃色、黃色與發光的白色，具有高飽和度與溫暖舒適的燈光。構圖乾淨且置中，具有淺景深效果，角色在畫面中完美平衡，並帶有柔和的發光特效。TikTok 直式 9:16 格式，短循環短片，超可愛的誇張比例，流暢的彈跳動畫，閃亮眼睛與腮紅細節豐富。底部疊加文字：「gugugaga and doro playing together 🥰🥰🥰」。輕鬆的環境氛圍，除了字幕外沒有其他文字，純粹溫馨的氛圍 --ar 9:16 --stylize 750 --v 6',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🐱 皮克斯風格擬人化早餐短片',
        "category": '🐱 動物趣味',
        "title_zh": '皮克斯風格擬人化早餐短片',
        "prompt": '可愛又俏皮的皮克斯風格擬人化早餐短片，描述兩者在溫暖晨光下的時尚廚房檯面上爭論：酷炫文青酪梨（戴著太陽眼鏡、小帽子，態度從容）對決焦慮吐司（帶著奶油汗珠，表情完美主義）。多鏡頭序列：酪梨秀出果核的中景鏡頭、吐司緊張到變脆的特寫、嘗試壓碎時的過肩鏡頭，以及辣椒片飛舞的混亂最終鏡頭。酪梨說：「兄弟，把我壓在你身上吧。我們會紅遍 Instagram 的，這可是健康脂肪，寶貝！」吐司驚慌失措：「你說得倒輕鬆！你總是遲到，心裡還半爛了。我每天都被烤焦！」轉折：當它們結合時，一隻手撒下了辣椒片——兩者因辛辣而尖叫：「個性太強烈了！」色彩鮮豔的食物、彈性的物理效果、誇張的表情以及蒸汽與熱氣特效。電影級美食攝影：快速剪輯、慢動作壓碎嘗試、俏皮的變焦。溫暖的黃金時刻光線與誘人的高光。音效：滋滋聲、緊張的碎裂聲、辛辣的尖叫聲以及 Instagram 相機快門聲。高品質流暢動畫，15 秒，充滿共鳴的千禧世代美食潮流幽默，非常適合病毒式分享。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '✨ 超寫實電影級恐怖片段',
        "category": '✨ 奇幻恐怖',
        "title_zh": '超寫實電影級恐怖片段',
        "prompt": '一段超寫實電影級恐怖片段，場景設定在夜晚一座廢棄的維多利亞式房屋，周圍環繞著濃霧與枯樹，氛圍令人不安，採用冷色調與低飽和度，低調照明，體積霧，膠片顆粒感，色差，VHS 故障特效。緩慢的推軌鏡頭穿過生鏽的大門，伴隨詭異的環境音與低頻轟鳴聲。切換至手持攝影視角，拍攝走廊牆壁裂縫與移動的肖像畫，伴隨微弱的耳語與陰影閃爍。長廊燈光閃爍，盡頭出現女性幽靈（皮膚蒼白，長黑髮遮臉，身穿破爛白裙，肢體不自然抽動）。畫面突然出現故障扭曲，實體瞬間拉近，頭部以不自然的角度傾斜，隱約可見發光的雙眼，隨後傳出刺耳的扭曲尖叫聲。硬切至黑畫面，伴隨靜電雜訊，耳語聲：「我還在這裡。」使用全片幅相機拍攝，35mm 鏡頭，淺景深，電影級焦點變換，4K UHD，24fps，超高細節，極致寫實，恐怖谷效應，令人不安，病毒式傳播的恐怖短片。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎵 K-pop 舞蹈影片提示詞',
        "category": '🎵 舞蹈音樂',
        "title_zh": 'K-pop 舞蹈影片提示詞',
        "prompt": '一位年輕的日本女性正在表演高能量的 K-pop 舞蹈，優雅地旋轉並隨著輕快的旋律對嘴演唱——她穿著時尚的粉彩色百褶裙與白色短版毛衣，頭髮綁成鬆散的雙馬尾並繫上絲帶——動態',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 校車變形機甲',
        "category": '🥋 動作戰鬥',
        "title_zh": '校車變形機甲',
        "prompt": '[攝影風格]：動態的低角度追蹤鏡頭沿著一輛時髦的黑色巴士滑行，雨水在鏡頭上劃出痕跡。隨著緊張感升級，攝影風格轉為略帶晃動的手持攝影，強調變形過程的規模與張力。使用 IMAX 數位攝影機搭配變形鏡頭拍攝，高快門速度捕捉精細的機械細節，水珠附著在鏡頭上，淺景深效果突顯了變形中的結構。[主體]：一輛霧面黑色的復古校車，帶有細微的磨損與暗色金屬邊緣，駕駛座上是一位神情專注的年輕女性。變形開始時，巴士轉化為一座高聳的工業風暴龍機甲——由相互咬合的黑鋼構成，旋轉的巴士輪胎變成了強而有力的肢體關節，前格柵撕裂開來，化作鋒利的機械下顎。[動作]：女孩在雨水浸濕的道路上疾馳，堅定地握住方向盤，水花從輪胎飛濺而出。突然，液壓系統啟動——車頂裂開，輪胎向內扭轉成為雙腿，底盤垂直升起。機甲重重地砸在地面上，震裂了濕滑的柏油路。它那由車頭燈演變而來的紅色雙眼亮起，並向暴風雨中的天空噴射出一道熾熱的火焰。[場景]：一條蜿蜒且被雨水浸濕的道路，穿過濃霧籠罩的茂密松樹林。兩側高聳的樹木隱沒在濃霧中。大雨傾盆，濕滑的柏油路面映照出變形的倒影。[風格與氛圍]：靈感源自大片級變形電影的高能量科幻動作風格。寫實且粗獷的 CGI 質感，呈現深色金屬飾面與細微鏽跡。場景以暴風雨黃昏的冷藍色調為基調，與機甲吐息的熾熱橙光及銳利的紅眼形成強烈對比，增強了戲劇性的張力。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 東方武俠終極對決',
        "category": '🥋 動作戰鬥',
        "title_zh": '東方武俠終極對決',
        "prompt": '【風格】東方武俠終極對決，極致動能，環境破壞美學，快節奏剪輯，電影級粒子特效，史詩級配樂氛圍。【時長】15 秒【角色】白衣大師 VS 黑衣大師 [00:00-00:05] 場景 1：高速碰撞。白衣與黑衣大師化作殘影，在古老石台中央猛烈碰撞。武器接觸的瞬間，耀眼的火花與清晰可見的圓形衝擊波爆發，導致周圍石地板瞬間龜裂，碎石飛濺。[00:05-00:10] 場景 2：空中戰鬥與破壞。兩人騰空而起，在墜落的巨石間高速穿梭交鋒，動作快到無法捕捉。每一次格擋都伴隨著空氣扭曲的音效。他們撞穿一根巨大的石柱，使其崩塌並碎裂成粉塵，展現出極致的破壞力。[00:10-00:15] 場景 3：終極高潮。落地後，兩人同時施展絕招，兩顆巨大的能量球（一青一紅）猛烈對撞。這引發了震天動地的粉塵與能量爆炸，蘑菇雲般的煙霧升起遮蔽一切，整個石台基座開始崩塌下沉。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 金雕逃離火山毀滅後的紐約',
        "category": '🌿 自然風景',
        "title_zh": '金雕逃離火山毀滅後的紐約',
        "prompt": '完整、未經剪輯的第一人稱視角（POV），模擬一隻成年金雕以極速逃生的過程。\n\n鏡頭風格：超廣角畸變鏡頭，帶有強烈的邊緣拉伸感、誇張的空間深度與運動視差，以及電影般的微距壓力效果。鏡頭以近乎超音速的速度向前推進，伴隨著劇烈的晃動、急速俯衝、激進的翻滾，以及由強勁拍翅所引發的混亂空中亂流。\n\n場景設定在火山超級噴發災難期間的古代紐約。天際線被重新想像為高聳的石造摩天大樓、原始的吊橋以及巨大的獨石建築。火山灰暴肆虐，熔岩彈從天而降，摧毀路徑上的一切事物。\n\n金雕以極速穿過一個類似古代曼哈頓門戶的巨大石拱門；燃燒的碎片與倒塌的塔樓向外炸開，熔岩碎片四處飛濺。牠在巨大的建築物之間螺旋向下俯衝，驚險地閃避墜落的石板與火熱的殘骸，在貼近地面飛行後，衝破一條正在倒塌的街道。\n\n隨後，牠穿過一個宏偉的古代華爾街區域，巨大的圓柱與排列雕像的通道在火山衝擊波下破碎。巨大的石柱像骨牌一樣斷裂倒塌，大理石碎片劇烈飛散，金雕在倒塌的建築結構間執行了一連串精準且連續的閃避動作。\n\n接著，牠垂直俯衝穿過一座靈感來自早期紐約建築的巨大圓頂神殿。圓頂在巨大的壓力下破裂，巨大的石塊崩塌而下，金雕在狹窄的室內空間中穿梭，並從破裂的牆壁中逃脫。\n\n飛行過程持續向一座類似原始自由女神像結構的古代紀念建築群推進，該建築現已被熔岩衝擊部分摧毀。金雕穿梭於破碎的框架與倒塌的石造鷹架之間，在墜落的碎片中以緊湊的 S 型路徑穿行。\n\n鏡頭全程保持劇烈的不穩定感，不斷受到衝擊波與亂流的震動。氛圍由血橙色的火山天空主導，發光的熔岩軌跡劃過畫面，高聳的火光噴湧而出。火山灰、熔岩碎片、石塵與燃燒的餘燼在鏡頭周圍混亂地旋轉。\n\n情感基調：極致、無情且腎上腺素飆升，捕捉在古代紐約毀滅中進行絕望高速逃生的緊張感。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌌 超寫實太空電影攝影影片提示詞',
        "category": '🌌 科幻賽博',
        "title_zh": '超寫實太空電影攝影影片提示詞',
        "prompt": '格式：15 秒 / 5 個鏡頭 / 多重剪輯 / 無對白\n\n風格：超寫實太空電影攝影 / 深邃太空黑對比熔岩金橘色吸積盤對比冷藍白色星場 / 35mm 膠卷顆粒感 / IMAX 真實感 / 9:16 直式比例 / 擬真視覺特效，具備實景光影動機',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 男士晨間儀容整理流程',
        "category": '🎭 日常生活',
        "title_zh": '男士晨間儀容整理流程',
        "prompt": '一名男子從廚房走出來並前往浴室，神情愉悅且哼著歌。[cut] 男子站在鏡子前，從後方的櫃子裡拿出髮膠。[cut] 特寫鏡頭：男子將一些髮膠倒在手掌上。[cut] 男子用雙手撥弄頭髮並塗抹髮膠。[cut] 男子用梳子整理他的鬍鬚。[cut] 男子在離開浴室前照了照鏡子並眨了眨眼。[cut] 男子沿著走廊走向門口。無音樂，無對話。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 取自參考圖片的格鬥遊戲昇龍拳動作序列',
        "category": '🥋 動作戰鬥',
        "title_zh": '取自參考圖片的格鬥遊戲昇龍拳動作序列',
        "prompt": '動作：壯碩的格鬥家對抗一位強勁的對手，施展出快速的昇龍拳上勾拳，拳頭噴發著火焰，帶著強勁的衝擊力騰空而起。\n鏡頭：連續動態的側面廣播鏡頭平穩地搖攝並向上傾斜，以一個不間斷的高能量鏡頭追蹤那爆炸性的上升動作。\n燈光：明亮的競技場泛光燈，帶有戲劇性的輪廓光和強烈的陰影，如同專業格鬥錦標賽轉播中常見的。\n音效：布料撕裂聲、強勁的拳風呼嘯聲伴隨著火焰的噼啪聲、沉重的撞擊聲，以及觀眾爆發出的興奮歡呼聲。\n對白：「他打破了防禦，施展出火焰昇龍拳！一記怪物般的昇龍擊！」',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 電影級多鏡頭場景： FBI 探員 與 外星人 在派對上',
        "category": '🎬 電影敘事',
        "title_zh": '電影級多鏡頭場景： FBI 探員 與 外星人 在派對上',
        "prompt": 'SHOT 1 — 0:00 to 0:04\n擁擠的家庭派對室內，背景是溫暖的串燈，人們手持紅杯歡笑著。一位身穿深色西裝、表情嚴肅的男子俯身向前，將一隻手穩穩地放在一個灰色外星人巨大光滑的頭上，另一隻手則將 FBI 徽章直接伸向鏡頭，眼神專注而銳利，直視前方。顆粒感的膠片攝影美學，35mm 視角，淺景深，混亂的派對背景略微模糊。\n男子直視鏡頭，緩慢地說道：\n「我找了你二十六年了。」\n\nSHOT 2 — 0:04 to 0:09\n灰色外星人的中景特寫，巨大的黑色眼睛一眨不眨，完全靜止，面無表情。派對的喧囂和笑聲在背景中持續響亮，一段漫長而令人不安的沉默。外星人緩慢地眨了一下眼。\n外星人以平靜、平板、帶有迴響的心靈感應聲音回應道：\n「我們知道。你在我們的母艦上留下了一個非常糟糕的評價。」\n\nSHOT 3 — 0:09 to 0:12\n男子臉部的特寫，下巴緊繃，眼睛瞇起。他緩慢地放下 FBI 徽章，長久地凝視著。周圍的派對笑聲略微減弱，背景中有人在笑到一半時僵住，察覺到緊張氣氛。昏暗溫暖的光線映照在他的臉上，極其嚴肅的表情，沒有音樂，只有環境室內噪音。\n他輕聲而堅定地說道：\n「那次綁架，可不是五星級的。」\n\nSHOT 4 — 0:12 to 0:15\n廣角鏡頭，男子和外星人雙雙沉默地直視前方。周圍的派對混亂地繼續著，完全不受影響。男子將手放在外星人的頭上，兩者都紋絲不動。在最荒謬的房間裡，兩個最嚴肅的身影。鏡頭保持靜止，非常緩慢地輕微推近，然後漸黑。\n螢幕文字出現：\n「真相仍在彼方。」\n\nStyle Notes: 顆粒感的 35mm 膠片美學 · 溫暖的實用派對燈光 · 荒誕背景下的面無表情嚴肅語氣 · 淺景深 · 無跳剪。緩慢而刻意的節奏 · 細膩的環境音效設計 · 照片般真實的外星人紋理 · 透過對比產生的冷幽默',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 假面騎士式 變身 場景',
        "category": '🥋 動作戰鬥',
        "title_zh": '假面騎士式 變身 場景',
        "prompt": '完整的假面騎士風格變身序列——從人類到戰損機甲裝甲——完全由 Seedance 2.0 在 @dreamina_ai 上生成。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎭 靜修處的騷動（災難場景）',
        "category": '🎭 日常生活',
        "title_zh": '靜修處的騷動（災難場景）',
        "prompt": '靜修處的騷動。\n鏡頭 1 (0.0-0.5)：微距鏡頭，一隻蚊子在深度冥想期間停在禪師的鼻子上。音效：高頻的嗡嗡聲。\n鏡頭 2：禪師的眼皮劇烈抽動。音效：彈簧聲。\n鏡頭 3：他瘋狂地拍打自己的',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 陰暗風暴小鎮動作序列',
        "category": '🥋 動作戰鬥',
        "title_zh": '陰暗風暴小鎮動作序列',
        "prompt": 'visual_theme: "陰暗風暴小鎮，低飽和度藍灰色調，膠片顆粒感"\n\n character_reference: "@Image1（髮型，白色水晶東方禮服，冷靜表情）。"\n\n lighting: "昏暗燈籠，柔焦空靈光暈，f/4 光圈，35mm 鏡頭"\n\n  timeline_sequence:\n    0-3s:\n      camera: "從腳部到全身的慢速垂直平移"\n      action: "角色站在傾盆大雨中；超寫實水滴從皮膚滑落"\n      effects: "身體散發出淡淡的紅藍能量光環"\n    3-6s:\n      camera: "腳部特寫，隨後快速拉遠至廣角鏡頭"\n      action: "向前邁步觸發紅藍衝擊波；環境去飽和變為灰階"\n      effects: "時間凍結；雨滴懸浮在半空中，如同折射球體"\n    6-9s:\n      camera: "上半身中景特寫"\n      action: "角色雙手做出握劍姿勢；懸浮的雨水匯聚到掌心"\n      effects: "形成一把流動的水劍，內部閃爍著強烈的紅藍光芒"\n    9-15s:\n      camera: "臉部/眼睛特寫轉向廣角追蹤鏡頭"\n      action: "雙眼燃起紅光；角色揮舞水劍斬向天空"\n      effects: "水劍消散為巨大的紅藍能量弧，將風暴雲層切開並一分為二"\n  technical_constraints: "流暢動作，無浮水印，無字幕，保持 @Image1 面部一致性"',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 PIGEON: Museum Heist',
        "category": '🎬 電影敘事',
        "title_zh": 'PIGEON: Museum Heist',
        "prompt": '動畫提示詞\n\nPIGEON: Museum Heist 一隻穿著黑色高領毛衣和貝雷帽的微小街頭鴿子，試圖從優雅的博物館咖啡廳偷走一根薯條。到處都是雷射保全系統。高預算 3D 動畫，微型搶劫惡搞。\n[0 秒–1.5 秒] 月光下的博物館內部。該',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🌿 生物發光珊瑚城中的深海探險家',
        "category": '🌿 自然風景',
        "title_zh": '生物發光珊瑚城中的深海探險家',
        "prompt": '一位敏捷的深海探險家，駕駛著流線型的水下噴射滑板車，穿越一座巨大、熙攘、散發著生物螢光的珊瑚城市，輕鬆穿梭於成群發光的水母之間，靈巧地閃避著巨大的海龜、潛水計程車以及高聳的海藻森林。她滑過古老的沉沒遺跡、繁忙的水下交通樞紐以及生機勃勃的海葵養殖場，以精準而優雅的姿態，旋轉穿過狹窄的縫隙。電影般的追蹤鏡頭跟隨她乘流而動的身影，畫面輔以動態模糊效果，以及穿透深藍深淵的青綠色光束。這片水下世界脈動著生機勃勃的海洋氛圍——冒泡的噴氣口、迴盪的鯨魚歌聲，以及永不停歇的流動。超寫實的細節，呈現出海洋動作電影般的視覺美感，捕捉了海浪之下，速度、優雅與無畏的動能。',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🥋 武士 沙漠 動作序列 提示詞',
        "category": '🥋 動作戰鬥',
        "title_zh": '武士 沙漠 動作序列 提示詞',
        "prompt": '激烈的動作場面：極致特寫鏡頭追蹤著一位武士，身著華麗鎧甲，武士刀已出鞘，擺出莊嚴的姿態，在日落的沙漠中施展著驚人的特技動作和戰鬥招式。金色的沙丘綿延至地平線，低垂的夕陽投下長長的陰影，空氣中熱氣蒸騰。淺景深將主體凸顯出來，捕捉每一個動態瞬間。節奏緊湊，動作編排迅速流暢，每一個動作都精準到位。聲景：狂風呼嘯，...',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '✨ 電影感奇幻 蔓生遺跡 動畫',
        "category": '✨ 奇幻恐怖',
        "title_zh": '電影感奇幻 蔓生遺跡 動畫',
        "prompt": '電影級 3D Blender 風格奇幻動畫，超精細、神秘的「無限搖籃」或植被茂密的神聖避難所，漂浮在迷霧繚繞的虛無空間中，茂盛的植被以 SpeedTree 級別的精細度創建，古老的石結構覆蓋著發光的苔蘚和藤蔓，戲劇性的體積光束穿透濃厚的氛圍霧氣，豐富的青金色調色板，帶有深祖母綠色和溫暖的琥珀色高光，柔和的憂鬱氛圍，平滑連續的前向推軌鏡頭緩慢滑過場景，逐層揭示錯綜複雜的細節，3D 中融入圖形插畫風格，照片級寫實卻帶有風格化的渲染，高對比度照明，葉片上帶有柔和的次表面散射，細微的粒子效果和輕柔搖曳的樹葉，8K 解析度，電影級構圖，三分法構圖，深度分層，無文字，無人物，夢幻而沉思的氛圍 --ar 16:9 --stylize 250 --v 6',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 DUCK: Formula Splash',
        "category": '🎬 電影敘事',
        "title_zh": 'DUCK: Formula Splash',
        "prompt": 'DUCK: Formula Splash\n\n一隻戴著賽車護目鏡、神氣十足的橡皮鴨，在管線災難中駕駛浴缸穿過豪華的大理石浴室。高預算 3D 動畫，強調荒謬的速度感與水體物理效果。\n\n[0s–1.5s] 廣角鏡頭。水流淹沒了大理石浴室地板。一隻橡皮',
        "lang": 'English',
        "featured": False,
    },
    {
        "label": '🎬 用於影片生成的西班牙語對話提示詞',
        "category": '🎬 電影敘事',
        "title_zh": '用於影片生成的西班牙語對話提示詞',
        "prompt": 'LE – 我記得！親愛的醫生……你之所以還活著，是因為我允許你活著，而且——你和我，在某種程度上，有著相同的目標。',
        "lang": '한국어',
        "featured": False,
    },
    {
        "label": '🎬 Seedance 2.0 電影感蒙太奇影片提示詞',
        "category": '🎬 電影敘事',
        "title_zh": 'Seedance 2.0 電影感蒙太奇影片提示詞',
        "prompt": '[@Image 1] (男主角參考圖) [@Image 2] (女主角參考圖) 電影級畫質，15 秒，蒙太奇剪輯，無字幕，韓語對話。開場 0 到 1 秒，溫暖的黃色底片顆粒感，過去，陽光明媚的午後咖啡廳，她趴在桌上睡著，他坐在對面，手托著下巴低頭看著她，嘴角不自覺地上揚，畫面帶有輕微顆粒感與過曝效果。硬切 1 秒，寒冷的藍色雨夜，現在，空曠的屋頂，他在雨中背對鏡頭站立，外套被淋濕緊貼著背部，一動不動，像是一座被時間遺棄的石像，從暖黃到冷藍的色溫轉變在此幀瞬間斷裂。硬切回過去 2 秒，深夜便利商店門口，她遞給他一杯熱飲，他沒有接，低頭看著她問：「이거 나 주는 거야?」（這是給我的嗎？）她翻了個白眼轉身離開，他笑著跟上，鏡頭跟隨兩人走入夜色的背影。硬切回現在 3 秒，她站在屋頂入口，手抓著鐵門，雨水打在她的肩膀上，她沒有移動，只是站在那裡看著他的背影，猶豫著該進還是該退。硬切回過去 4 秒，極致特寫，他的手將耳機塞進她的耳朵，指尖在她耳邊停留了一秒，兩人都假裝沒注意到。硬切回現在 5 秒，極致特寫，同樣的手，現在插在口袋裡，雨水從袖口滲入，他的手在口袋裡緩緩握緊。6 到 10 秒全部慢動作，她終於鬆開鐵門走入雨中，在他身後半公尺處停下，雨聲很大，但她的聲音依然清晰傳出——「왜 연락 안 했어.」（為什麼不聯絡我。）他沒有回頭，沉默了兩秒，「연락하면 뭐가 달라져?」（聯絡了又能改變什麼？）她閉上眼睛，感覺胸口被重物壓住，再次開口時聲音顫抖——「달라지잖아. 나한테는.」（會改變的。對我而言。）他終於轉過身，看著她臉上雨水與淚水交織，喉結滾動，沙啞地說——「알아. 그래서 더 못 했어.」（我知道。正因如此，我才更不敢聯絡。）10 到 13 秒，疊化蒙太奇，同一個屋頂，同樣的鏡頭位置，過去是陽光明媚的傍晚，她站在欄杆旁回頭對他微笑，他大步走過去將她擁入懷中，夕陽將兩人的影子拉得很長；現在是雨夜，同樣的位置，他站在她面前，兩個時間軸在同一個畫面中重疊了一整秒，她過去的微笑與現在的淚水重疊在同一張臉上。13 到 15 秒，他沒有再說話，抬手將她的頭按進自己懷裡，她抗拒了兩秒，隨後雙手緩緩抬起，緊緊抓住他背後的衣服，鏡頭緩緩拉遠至極致遠景，兩人在雨幕中縮成一個剪影，霓虹燈在水窪中破碎閃爍，畫面逐漸靜止，聲音逐漸消失，淡出至全黑。過去場景全程採用暖黃橘色 16mm 底片顆粒感手持跟拍，現在場景採用冷藍黑色雨水倒影穩定器拍攝，對話期間鏡頭推向極致特寫，疊化時飽和度瞬間爆發隨後回到冷色調，背景音樂在過去場景使用輕柔的吉他撥弦，進入現在場景時淡出，僅保留雨聲，最後一句對話後響起深沉的大提琴單弦演奏，淡出至全黑前保持完全靜音。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🎭 Seedance 2.0 AI 婚禮影片提示詞：電影感夜景',
        "category": '🎭 日常生活',
        "title_zh": 'Seedance 2.0 AI 婚禮影片提示詞：電影感夜景',
        "prompt": '主題 1：電影感夜景風格 - 星光幻夢之城，共墜星河。視覺核心：賽博龐克與極致浪漫的碰撞，利用霓虹倒影與雨滴微距鏡頭展現都市精緻感。9:16 直式螢幕，寫實電影級畫質，都市奢華風，4K 高解析度。0-4 秒：高角度俯拍，緩慢下沉。雨後的城市天台，地面是黑色柏油路面與積水，如鏡面般反射著遠處朦朧的城市霓虹燈。一位 25 歲、偶像級顏值的中國新娘，身穿閃耀的鑽石美人魚高級訂製婚紗；一位 28 歲、英俊的中國新郎，身穿深色絲絨西裝。兩人位於畫面中央，撐著一把透明雨傘，在雨夜中漫步。畫面呈現復古藝術電影般的抽幀效果。5-9 秒：攝影機以新人為中心進行 360 度慢動作環繞。新娘擁有精緻鵝蛋臉、野生眉、冷豔狐狸眼、高挺鼻樑與微張紅唇；新郎擁有輪廓分明的下顎線、劍眉、星眸與深情凝視。環繞過程中，極慢的細小雨滴從天而降（子彈時間）。新郎將雨傘向新娘傾斜，自己的半邊肩膀微濕。身後的霓虹燈轉化為巨大的彩色光斑（散景效果）。10-15 秒：鏡頭切換至低角度特寫。新娘丟掉透明雨傘，雨傘在背景中緩緩落下。新娘雙手環繞新郎頸部，新郎深情俯視。一束來自街燈的溫暖橙色輪廓光穿過新娘濕潤的睫毛。畫面在兩人即將接吻的瞬間定格，背景霓虹完全模糊成星河。音效：遠處城市環境音、緩慢的爵士大提琴、雨水落在傘面的白噪音、電影感心跳聲。禁止：任何文字、字幕、LOGO 或浮水印。',
        "lang": '中文',
        "featured": False,
    },
    {
        "label": '🚀 獨行 數據快遞員 騎著 懸浮滑板 在 賽博龐克 巨型城市 中',
        "category": '🚀 追逐速度',
        "title_zh": '獨行 數據快遞員 騎著 懸浮滑板 在 賽博龐克 巨型城市 中',
        "prompt": '一名桀驁不馴的資料快遞員，駕馭著嗡嗡作響的反重力懸浮滑板，以風馳電掣般的速度穿梭於霓虹燈閃爍的賽博龐克巨城中，輕巧地穿梭於漂浮的市集攤位之間，閃避著飛行汽車、失控的無人機以及高聳的全息廣告。她輕巧地掠過巨大的金屬結構和繁忙的半空中交叉路口，以精準而有型的方式俐落地轉彎。電影般的跟蹤鏡頭緊隨她的身影，動態模糊效果與刺眼奪目的霓虹燈光相互襯托，這些燈光反射在潮濕的金屬表面，更添生動。這座巨城脈動著狂亂的人造氣息——尖嘯的斥力引擎、閃爍的警報器和永不停歇的動態。超寫實的細節，帶有科幻動作電影的美學風格，捕捉了穿越未來反烏托邦的速度、自信和無畏的衝勁。',
        "lang": 'English',
        "featured": False,
    },
]

def get_seedance_prompt(label: str) -> dict:
    return next((t for t in SEEDANCE_PROMPT_TEMPLATES if t["label"] == label), {})

def get_seedance_by_category(category: str) -> list[dict]:
    return [t for t in SEEDANCE_PROMPT_TEMPLATES if t["category"] == category]