# AI Image Prompt Generator — NiceGUI 重寫計畫

> 建立日期：2026-04-01  
> 作者：GitHub Copilot

---

## 目標

1. **GUI 框架**：將 Gradio (`app_gui.py`) 完整替換為 **NiceGUI** 桌面應用程式。
2. **模板擴充**：每種模板（角色、故事/主題、風格）從 3 個擴充到 **10 個**。
3. **錯誤處理 + Log 記錄頁面**：新增統一 logger 模組、在 UI 中顯示操作記錄與錯誤。
4. **提示詞檢視 + 編輯頁面**：支援搜尋、選取、編輯並存回 JSON 的完整 CRUD。
5. **Git Push**：完成後 commit + push 至 GitHub (`luckyegg168@gmail.com`)。

---

## 架構圖

```
genPicsPrompts/
├── agent.py              ← OpenRouter API（不改）
├── config.py             ← 設定（不改）
├── image_utils.py        ← 圖片工具（不改）
├── logger.py             ← 🆕 統一 log 模組（替換 print/raise）
├── main.py               ← CLI 入口（不改）
├── models.py             ← Pydantic 模型（不改）
├── prompt_generator.py   ← AI 生成邏輯（不改）
├── recorder.py           ← 存檔（新增 update/delete）
├── templates.py          ← 擴充至每種 10 個
├── nicegui_app.py        ← 🆕 NiceGUI 主 GUI（取代 app_gui.py）
├── app_gui.py            ← 保留（Gradio backup）
├── requirements.txt      ← 加入 nicegui
└── start.bat             ← 更新為啟動 nicegui_app.py
```

---

## 頁面規劃（NiceGUI）

### 導覽列 (左側 Drawer)
- 🏠 首頁 / 單張圖片
- 🎬 影片提示詞
- 🖼 圖片序列
- 📷 以圖生文
- 📋 提示詞庫 (檢視+編輯)
- 📜 操作記錄 / Log

---

### Page 1 — 單張圖片提示詞
- 角色快速填入（短輸入 → AI 自動完成）
- 角色模板下拉（10 種）
- 故事主題模板（10 種）
- 風格模板（10 種）
- 電影規格選擇（解析度、長寬比、鏡頭…）
- 生成按鈕 → 顯示 EN/ZH prompt

### Page 2 — 圖片序列
- 同 Page 1 角色設定
- 設定幀數（2–8）
- 逐幀顯示卡片

### Page 3 — 影片提示詞
- 同角色設定
- 攝影機運動、時長、FPS、動作強度
- 多片段生成

### Page 4 — 以圖生文
- 上傳圖片 或 選取 images/ 資料夾圖片
- 生成圖片提示詞

### Page 5 — 提示詞庫 (新功能)
- 搜尋（關鍵字 + 類型 image/video/all）
- 卡片列表顯示（分頁）
- 點擊卡片 → 展開編輯 Modal
- 支援儲存編輯、刪除單筆

### Page 6 — 操作記錄 (新功能)
- 即時 log 捲動顯示（DEBUG / INFO / WARNING / ERROR）
- 支援清除、下載 txt

---

## 模板擴充清單（templates.py）

### CHARACTER_TEMPLATES（10 個）
1. 🗡 東方俠女 (現有)
2. 🤖 賽博龐克偵探 (現有)
3. 🌿 末世倖存者 (現有)
4. 🧙 異界法師 (新增)
5. 👘 大正浪人 (新增)
6. 🦅 荒野獵人 (新增)
7. 🎭 維多利亞偵探 (新增)
8. 🌊 海洋指揮官 (新增)
9. 🌸 現代刺客 (新增)
10. 🪐 星際工程師 (新增)

### STORY_TEMPLATES（10 個）
1. ⚔️ 復仇之路 (現有)
2. 🌃 霓虹夜城追逐 (現有)
3. 🌫 迷霧中的真相 (現有)
4. 🌋 末日前的抉擇 (新增)
5. 🗺 失落文明探索 (新增)
6. 💔 背叛者的救贖 (新增)
7. 🧪 禁忌實驗覺醒 (新增)
8. 🏯 亂世英雄崛起 (新增)
9. 🌌 星際流亡者 (新增)
10. 🎪 幻術師的詭計 (新增)

### STYLE_TEMPLATES（10 個）
1. 🎬 好萊塢電影 (現有)
2. 🎨 日系動漫 (現有)
3. 🖌 油畫寫實 (現有)
4. 🌑 黑色電影 Noir (新增)
5. 🌈 賽博龐克霓虹 (新增)
6. 🎭 蒸汽龐克藝術 (新增)
7. 📷 街頭攝影風 (新增)
8. 🌿 Studio Ghibli 宮崎駿 (新增)
9. 🏛 文藝復興古典 (新增)
10. 🎮 遊戲概念藝術 (新增)

---

## 實作步驟

1. `plan.md` ← 本文件  
2. `templates.py` ← 擴充至每種 10 個  
3. `logger.py` ← 新建統一 log 模組  
4. `recorder.py` ← 新增 `update_frame()`, `delete_frame()`, `load_all_prompts()`  
5. `nicegui_app.py` ← 完整 NiceGUI GUI  
6. `requirements.txt` ← 加入 nicegui  
7. `start.bat` ← 更新入口  
8. 驗證執行  
9. Git commit + push  

---

## 技術細節

- **NiceGUI 版本**：`nicegui>=2.0.0`（使用 `ui.page`, `ui.drawer`, `ui.card`...）
- **非同步執行**：使用 `asyncio` + `run.io_bound()` 避免 UI 凍結
- **錯誤捕捉**：所有 AI 呼叫包裝在 try/except，記錄至 `app.log` 並顯示 ui.notify
- **Log 格式**：`[timestamp] [LEVEL] message`，存至 `outputs/app.log`
