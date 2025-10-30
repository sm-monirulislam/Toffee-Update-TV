name: 🎬 Toffee Auto Playlist Builder

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install requests

      - name: Run Toffee Script
        env:
          TOFFEE_JWT: ${{ secrets.TOFFEE_JWT }}
        run: python toffee_play.py
