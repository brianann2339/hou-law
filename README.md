# 侯明正律師事務所 官方網站

台南市中西區府前路一段188號。與**蔡青芬律師事務所**（另一個獨立網站，repo `tsai-law`）於同一處所合署執業，兩所各自受理委任、各自負責。

線上：https://brianann2339.github.io/hou-law/

## 要改內容？只改一個檔

**`src/content/site.ts`** —— 全站文字與事實都在這裡，改完推 `main` 就自動重新部署。

| 想改什麼 | 改哪裡 |
|---|---|
| 電話、傳真、Email、地址、營業時間、諮詢方式 | `office`、`lawyer.tel / fax / email` |
| 學歷、經歷、現任、語言、介紹文 | `lawyer.*` |
| 服務範圍（含每項的白話說明） | `serviceGroups` |
| 委任流程四步驟 | `consultSteps` |
| 常見問題 | `faqs` |
| 合署事務所的連結與領域 | `peer` |
| 頁尾「內容最後更新」 | `firm.lastUpdated`（手動維護，改內容時一起改） |
| LINE 官方帳號 | `office.lineUrl`（目前留空；填入即自動顯示） |

### 照片（已放，2026-09-07）

站上用的兩張圖都是從原檔 `侯律師照片.jpg`（2000×1334 橫幅，事務所書櫃前）產生的：

| 檔案 | 尺寸 | 用在哪 |
|---|---|---|
| `public/images/hou-portrait.jpg` | 1040×1300（4:5 直幅） | 首頁「關於」區、`/profile/` 頁首 |
| `public/images/og.jpg` | 1200×630 | 分享到 LINE／Facebook 時的預覽圖 |

**要換照片或改裁切**：把新原檔放成 `侯律師照片.jpg`，或改
`scripts/make-photos.py` 最上面的 `CROP_H`（越小＝裁越緊）與 `CENTER_X`，然後

```
python3 scripts/make-photos.py
```

會直接覆寫 `public/images/` 兩張圖。需要 Pillow（`pip3 install Pillow`）。
`site.ts` 的 `lawyer.photo` 留空的話會回到「照片預留位置」，不破版。

## ⚠️ 改文案前務必先讀

律師網站受《律師法》與全國律師聯合會《律師推展業務規範》拘束。條文原文與懲戒案例寫在
`src/content/site.ts` 檔頭註解，動文案前請先看過。最容易踩的：

- **不得**表示訴訟勝訴率、委任人、受任中事件、**過去處理或參與之事件**
  → 沒有「成功案例」頁、不放承辦件數統計。這是刻意的，不要加。
- **不得**表示**顧問對象**（例如某公司之法律顧問），除非取得該公司事前書面同意。
- **不得**明示或暗示與公務機關有特殊關係或影響力。
- **必須**在每一頁表明律師姓名、事務所名稱、地址、電話（頁尾已固定，不可移除）。
- **兩所同址**：網頁外觀不得使人誤認為同一事務所（113 律懲字第38號、112 律懲字第42號）。
  `peer` 區塊與 `office.disclaimer` 就是為此存在，不可刪。

## 開發

```bash
npm install
npm run dev      # http://localhost:4321/hou-law/
npm run build
npm run preview
```

## 部署

推 `main` 由 GitHub Actions 自動建置發布到 GitHub Pages。
換自訂網域要改三處：`astro.config.mjs` 的 `site`／`base`、`public/robots.txt` 的 Sitemap 行、`public/CNAME`。


## 提交給搜尋引擎（第一次上線後做一次）

**Google Search Console 已於 2026-09-07 做完**：資源已建立、擁有權已驗證
（驗證碼在 `site.ts` 的 `siteVerification.google`，**不要刪**，刪了會掉驗證）、
`sitemap-index.xml` 已提交、五頁都已送出建立索引要求。首頁已編入索引。
Sitemap 報表若顯示「無法擷取」是剛提交時的常態，用「網址審查 → 測試線上網址」
即時測試才準。**Bing 還沒做**，下面的步驟留著備查與日後重做用。

### Google Search Console
1. 開 <https://search.google.com/search-console>，用 Google 帳號登入。
2. 左上角「新增資源」→ 選右邊那個 **「網址前置字元」**（不是左邊的「網域」）。
3. 貼上：`https://brianann2339.github.io/hou-law/`
4. 驗證方式選 **「HTML 標記」**，它會給一段
   `<meta name="google-site-verification" content="AbCd1234..." />`。
   **把 content 引號裡那一串**複製下來。
5. 打開 `src/content/site.ts`，填進 `siteVerification.google`，推 `main`，等 Actions 跑完（約 1 分鐘）。
6. 回 Search Console 按「驗證」。
7. 通過後，左側「Sitemap」→ 輸入 `sitemap-index.xml` → 提交。

### Bing Webmaster Tools
開 <https://www.bing.com/webmasters>，登入後可直接選 **「從 Google Search Console 匯入」**，
最省事。要手動的話流程同上，驗證碼填進 `siteVerification.bing`，sitemap 網址是
`https://brianann2339.github.io/hou-law/sitemap-index.xml`。

> 收錄不是即時的，通常幾天到兩週。Search Console 的「網址審查」可以看單一頁面有沒有被收錄。

## 商家檔案（Google／Apple／Bing 地圖）

事務所周邊至少 10 家同業在 Apple 地圖有商家標記，本所目前三個平台都查無。建議各建一筆
（**兩所各自建，不要合併成一筆**）：

- Google 商家：<https://business.google.com/> — 類別選「律師事務所」，名稱、地址、電話、營業時間、網址與本站一致。
- Apple Business Connect：<https://businessconnect.apple.com/>
- Bing Places：<https://www.bingplaces.com/>

⚠️ 一旦 Google 上有了商家檔案，第三方目錄站（如台律網）會自動抓走並生成頁面，內容不受本所控制。
評價只能邀請，**不得給予任何對價**（推展業務規範 §5 III 的邏輯）。

## 與 tsai-law 的關係

兩個 repo 是**同一套模板、兩份內容**。除了 `src/content/site.ts`、`astro.config.mjs`、
`public/robots.txt`、`README.md` 之外的檔案兩邊應保持一致；改到共用元件時記得兩邊都改。

## 技術

Astro 7 靜態輸出，無前端框架。字體 Noto Serif TC／Noto Sans TC（Google Fonts）。
每頁含 schema.org 結構化資料（Attorney／Person／FAQPage）與 sitemap。
