name: 🎬 Toffee Auto Playlist Builder

on:
  schedule:
    - cron: "0 */6 * * *"    # প্রতি ৬ ঘণ্টায় অটো রান (বাংলাদেশ সময় অনুযায়ী)
  workflow_dispatch: {}       # চাইলে ম্যানুয়ালি রান করা যাবে

permissions:
  contents: write

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: 📦 Checkout repository
        uses: actions/checkout@v4

      - name: 🐍 Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.10"

      - name: 📦 Install dependencies
        run: pip install requests

      - name: ▶️ Run Toffee Script
        env:
          TOFFEE_JWT: ${{ secrets.TOFFEE_JWT }}
        run: python toffee_play.py

      - name: 💾 Commit and Push Playlist
        run: |
          git config --global user.name "GitHub Actions"
          git config --global user.email "actions@github.com"
          git add toffee_channels.m3u
          git commit -m "🔄 Auto updated Toffee playlist"
          git push
