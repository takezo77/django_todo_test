# PartsOuq Scraper (Semi-Auto)

## 概要
自動車部品サイト [PartsOuq.com](https://partsouq.com/) から、純正部品データ（メーカー、車種、型番、部品名など）を収集するスクレイピングツールです。

このサイトは強力な Cloudflare Bot Protection を導入しているため、**「Playwright を使用してブラウザを起動し、Cloudflare のチャレンジ（CAPTCHA等）が表示された場合は人間が手動で解決する」** という **半自動（Human-in-the-loop）アプローチ** を採用しています。

## 📁 主要ファイル
- **`partsouq_final.py`**: **【現在のメインコード】**。ToyotaおよびNissanの取得ロジック実装済み。全カテゴリ巡回、Excel自動保存機能付き。
- `partsouq_optimized.py`: サイト構造解析・デバッグに使用した開発版。
- `partsouq_chrome_profile.py`: ユーザーのChromeプロファイルを流用しようとした試作版（現在は不使用）。
- `partsouq_cookie_scraper.py`: Cookie注入を試みた版（Cloudflare突破できず不使用）。

## 🚀 実行方法

### 1. 環境セットアップ
```bash
# 仮想環境の有効化
source scraper_env/bin/activate

# 依存ライブラリのインストール
pip install playwright openpyxl
playwright install chromium
```

### 2. スクリプト実行
```bash
python partsouq_final.py
```

### 3. 【重要】実行中の操作
1. ブラウザ（Chromium）が起動します。
2. **"Checking if the site connection is secure" (Cloudflare)** 画面が表示された場合：
   - **手動で「I am human（人間です）」等のチェックボックスをクリックしてください。**
3. Cloudflareを突破すると、スクリプトが自動的に検知してスクレイピングを開始します。
4. 処理中はターミナルに進捗ログが表示され、ブラウザが自動操作されます。※ブラウザは閉じないでください。

## ✅ 実装済みの機能とロジック

### 1. Cloudflare回避ロジック
- `wait_for_cloudflare(page)` 関数にて実装。
- ページタイトルを監視し、Cloudflareの待機画面であればループしてユーザー入力を待つ。

### 2. 対応済みのサイト構造パターン
PartsOuqはメーカーによって遷移フローが異なりますが、以下の主要2パターンを実装・検証済みです。

#### パターンA：リンク遷移型（Toyota等）
- フロー: `Locate` (一覧) -> `Pick` (車種選択) -> `Vehicle` (仕様選択) -> `Unit` (部品カテゴリ) -> `Data`
- 車種や仕様が全てリンクとして表示されているタイプ。
- **実装状況**: `scrape_toyota()` にて実装済み。全カテゴリのループ取得も動作確認完了。

#### パターンB：プルダウン検索型（Nissan等）
- フロー: `Locate` -> `Pick` (地域選択) -> **Select2プルダウン操作** -> `Vehicle` -> ...
- 車種を選択するために検索ボックス（Select2）への入力が必要。
- **攻略ポイント**: `Page.fill` では要素特定が不安定なため、**「プルダウンを開く -> `keyboard.type` で入力 -> Enter」** というキーボードエミュレーションで安定化させた。
- **実装状況**: `scrape_nissan()` にて実装済み。

### 3. データ取得・保存
- **取得項目**: メーカー, 車種(Model), 仕様(Spec), グループ(Group), 部品番号(PartNumber), 部品名(PartName)
- **保存**: `partsouq_data/partsouq_result.xlsx` に保存。
- **安全性**: データ消失を防ぐため、1カテゴリ処理ごとにExcelを上書き保存しています。

## 📝 開発状況と次のステップ (2026-01-20 時点)

### 現在のステータス
- **Toyota**: 車種 `1000` -> `STANDARD TOOL` 等のデータ取得に成功。ループ処理も確認済み。
- **Nissan**: 地域 `Australia` -> 車種 `200SX` (プルダウン操作) -> データ取得に成功。
- **GitHub**: `https://github.com/takezo77/get_parts.git` にプッシュ済み。

### AIエージェントへの引き継ぎ事項
1. **他メーカーへの展開**:
   - 残りのメーカー（Lexus, Mitsubishi, Subaru, Suzuki, Mazda, Honda, Infiniti）も、Toyota型かNissan型のどちらかのロジックで対応可能です。
   - `partsouq_final.py` 内に `scrape_honda()` 等を追加し、`main()` で呼び出してください。
2. **全件取得時の懸念**:
   - 全モデル・全仕様を網羅するとデータ量が膨大（数百万件）になり、時間がかかります。
   - 「代表的な仕様に絞る」などの要件定義に基づいてループ範囲を調整してください。
3. **セレクタの脆弱性**:
   - 部品番号抽出は現在「数字を含むテキスト」を簡易的に判定しています。精度を上げるなら `regex` の調整が必要です。

---
**Created by Antigravity Agent**
