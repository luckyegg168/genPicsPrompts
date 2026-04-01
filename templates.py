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
