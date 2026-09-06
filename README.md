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

### 放照片
1. 照片放 `public/images/`，例如 `hou.jpg`。
2. `site.ts` 把 `lawyer.photo: ''` 改成 `'hou.jpg'`。
3. 建議直式 4:5、短邊 800px 以上。留空會顯示「照片預留位置」，不破版。

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

## 與 tsai-law 的關係

兩個 repo 是**同一套模板、兩份內容**。除了 `src/content/site.ts`、`astro.config.mjs`、
`public/robots.txt`、`README.md` 之外的檔案兩邊應保持一致；改到共用元件時記得兩邊都改。

## 技術

Astro 7 靜態輸出，無前端框架。字體 Noto Serif TC／Noto Sans TC（Google Fonts）。
每頁含 schema.org 結構化資料（Attorney／Person／FAQPage）與 sitemap。
