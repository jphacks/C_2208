# 情報リテラシー向上Bot「まもるくん」

![image](https://user-images.githubusercontent.com/106864912/197318590-d281e066-0932-4440-bc87-1933d76fef1b.png)

![image](https://user-images.githubusercontent.com/106864912/197363153-9f9494e8-1f2a-4f37-85bb-8151422ed797.png)


## 製品概要
### 背景(製品開発のきっかけ、課題等）
私たちは、日本の情報・デジタルリテラシーの向上を図るために小・中学生を対象にしたリテラシー向上のための学習ツールBotを開発した。
昨今、VRやARを利用した災害シミュレーションアプリなどデジタル技術を活用した防災イベントやプロダクトが盛んである。
一方で、2025年以降大学共通テストに新たに情報の科目が加わるなど、これからの社会において情報リテラシーは必須のスキルとなりつつある。そのため、小・中学生から情報リテラシーを楽しく学べるツールがあれば今後の社会を生き抜く上で良い教育だと考え、このプロダクトを開発することにした。
### 製品説明（具体的な製品の説明）
### 特長
#### 1. 特長1　情報リテラシーを○×クイズを通して学べる
#### 2. 特長2　スマホとLINEさえあれば、いつでもどこでも学習可能

### 解決出来ること
- 中高生の情報リテラシーの向上
### 今後の展望
- 小中学生に向けた、形態素解析APIを用いた柔らかい文章に変換。
- 実際に情報リテラシーが問われる状況を疑似体験できる機能の実装。
- 解説サイトの構築
- LINEリッチメニューの実装
- 完成イメージ↓

![image](https://user-images.githubusercontent.com/106864912/197363180-3a6dd5de-35bd-4db2-9e9f-59be26f9f5fb.png)

### 注力したこと（こだわり等）
* **いつでもどこでも誰でも**使えるように最も普及しているSNSのLINEをプラットフォームに選んだ。
* LINEBOTから出題される問題に回答しやすいようにQuickReplyというボタンのタップ動作でメッセージ送信できるようにした。

## 開発技術
### 活用した技術
#### サーバ・ホスティングサービス
* AWS（API Gateway，Lambda）

#### API・データ
* LINE Messaging API
* ネットリテラシー検定機構（https://ssl.net-literacy.org/）

#### フレームワーク・ライブラリ・モジュール
* line-bot-sdk-python
* Flask

## コーディング規約
- コミットメッセージのフォーマットは以下を参考にされたい。
```
[update] 更新した内容・理由
[add] 追加した内容・理由
[remove] 削除した内容・理由
[fix] 修正した内容・理由
```
- メインブランチは**masterブランチ**とする。
- メインブランチが更新され次第、各々のブランチを更新。
- masterブランチにダイレクトマージは禁止。（プルリクエスト推奨）
- バージョン変更は```git revert```推奨
- ブランチは機能毎で切る（個人ごとではない）
