Python 機械学習 - コード例


## 第2章：分類のためのシンプルな機械学習アルゴリズムのトレーニング

### 章立ての概要

- 人工ニューロン - 機械学習の初期の歴史を垣間見る
  - 人工神経細胞の正式な定義
  - パーセプトロンの学習ルール
- Pythonでパーセプトロン学習アルゴリズムを実装する
  - オブジェクト指向のパーセプトロンAPI
  - Irisデータセットでのパーセプトロンモデルの学習
- 適応的な線形ニューロンと学習の収束
  - 勾配降下によるコスト関数の最小化
  - Pythonで適応型リニアニューロンを実装する
  - 特徴量スケーリングによる勾配降下法の改善
  - 大規模機械学習と確率的勾配降下法
- 概要

### コード例を使用する際の注意点

本書のコード例に触れるには、Jupyter Notebook (`.ipynb` ファイル) を使用することをお勧めします。Jupyter Notebookを使用すると、コードをステップごとに実行し、結果の出力（プロットや画像を含む）をすべて1つの便利なドキュメントにまとめることができるようになります。

![](images/jupyter-example-1.png)



Anaconda Pythonディストリビューションを使用している場合、jupyter notebookをインストールするために必要なのは、ターミナルで以下のコマンドを実行することです。

    conda install jupyter notebook

そして、jupyter notebookを起動するには、次のように実行します。

    ジュピターノート

ブラウザでウィンドウを開き、開きたい `.ipynb` ファイルがある目的のディレクトリに移動します。

**詳しいインストール方法や設定方法は、[第1章のREADME.mdファイル](../ch01/README.md)**に記載されています。

**Jupyter Notebookをインストールしない場合でも、GitHubにあるノートブックファイルをクリックするだけで閲覧することができます。[ch02.ipynb`](ch02.ipynb))**.

コード例に加えて、各Jupyterノートブックに目次を追加し、本の内容と一致するセクションヘッダーを追加しました。また、オリジナルの画像や図を掲載することで、本を読みながらインタラクティブにコードを操作しやすくなることを期待しています。

![](images/jupyter-example-2.png)


これらのノートブックを作成したとき、私はあなたの読書（とコーディング）体験をできるだけ便利にすることを望んでいました。しかし、もしあなたがJupyter Notebooksを使いたくないのであれば、私はこれらのノートブックを通常のPythonスクリプトファイル（`.py`ファイル）に変換し、平文エディタで表示および編集できるようにしました。