# PartsOuq Car Parts Scraper

自動車部品サイト [PartsOuq.com](https://partsouq.com/) から、純正部品データ（メーカー、型番、部品名など）を自動収集するためのPythonスクレイピングツールです。

## 📂 プロジェクトの経緯と構成
元々別のプロジェクト（Django Todoアプリ）ディレクトリ内で検証を行っていましたが、本スクレイピング機能を独立させるため、必要なファイル群をこの `get_parts` リポジトリに抽出・統合しました。

現在は **このフォルダ単体で動作する** ように整理されています。

## 🛠 機能概要
PartsOuqは強力なBot対策（Cloudflare）を導入しているため、以下の**半自動（Semi-Auto）アプローチ**を採用しています。

1. **ブラウザ起動**: Playwrightを使用してChromiumブラウザを立ち上げます。
2. **手動認証**: "Checking if the site connection is secure" (Cloudflare) 画面が出たら、ユーザーが手動でチェックボックスをクリックします。
3. **自動収集**: 認証を突破すると、スクリプトが自動的にページを巡回し、データをExcelに保存します。

## � ファイル構成
- **`partsouq_final.py`**: **【メイン実行ファイル】**。完成されたスクレイピングロジック（Toyota/Nissan対応、ループ処理、Excel保存）が含まれています。
- `partsouq_optimized.py`: 開発過程で使用した、サイト構造解析用のプロトタイプ。
- `partsouq_screen_*.py`: スクリーンショット撮影や検証に使用した補助スクリプト群。
- `partsouq_data/`: 取得したExcelデータや、デバッグ用スクリーンショットの保存先。
- `requirements.txt`: 必要なPythonライブラリ一覧（もしなければ `pip install playwright openpyxl` でOK）。

## 🚀 使い方

### 1. 準備
Python環境が必要です。依存ライブラリをインストールします。

```bash
pip install playwright openpyxl
playwright install chromium
```

### 2. 実行
メインスクリプトを実行します。

```bash
python partsouq_final.py
```

### 3. 操作手順
1. スクリプトを実行すると、ブラウザウィンドウが開きます。
2. **Cloudflareの認証画面（「I am human」など）が表示されたら、手動でクリックして突破してください。**
3. 突破後、自動的にメーカー（ToyotaやNissanなど）のカタログページへ移動し、データの収集が始まります。
4. 収集状況はターミナルに表示され、データは `partsouq_data/partsouq_result.xlsx` にリアルタイムで保存されます。

## ✅ 対応済みメーカーとロジック
現在、以下の2パターンのサイト構造に対応しています。

1. **Toyotaパターン（リンク遷移型）**
   - リンクをクリックしていくだけで部品リストに到達できるタイプ。
   - `scrape_toyota()` 関数で実装済み。
   - 対応メーカー推測: Toyota, Lexus, Mitsubishi, Subaru, Suzuki, Mazda, Honda

2. **Nissanパターン（プルダウン検索型）**
   - 車種選択時にプルダウンメニューへの入力が必要なタイプ。
   - キーボードエミュレーションで入力を行う高度なロジックを実装済み。
   - `scrape_nissan()` 関数で実装済み。
   - 対応メーカー推測: Nissan, Infiniti

## 📝 今後の作業
- 他のメーカー（Honda, Mazdaなど）を追加する場合は、`partsouq_final.py` 内の `main()` 関数で適切なスクレイピング関数（`scrape_toyota` または `scrape_nissan` のロジックを流用）を呼び出してください。
- 取得件数が多い場合、スクリプト内のループ制限（現在はテスト用に制限している箇所があれば）を解除して全件取得を行ってください。

---
**Repository**: https://github.com/takezo77/get_parts.git
