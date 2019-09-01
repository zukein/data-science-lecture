# 【重要】事前環境設定のお願い

初回講義の際に必要となる環境です。
以下の手順を参考にご用意ください。

## Rコマンダーのインストール(任意)

### R言語をインストール

- Mac
   1. [R言語](https://cran.r-project.org/bin/macosx/)
   2. [XQuartz](https://www.xquartz.org/)

- Win
   1. [R言語](https://cran.r-project.org/bin/windows/)

### RStudio(Rの統合開発環境)をインストール(任意)

1. [RStudio](https://www.rstudio.com/products/rstudio/download/#download)

### Rコマンダーをインストール

1. RまたはRStudioのコンソールから以下を入力してパッケージをインストール
   > install.packages(‘Rcmdr’, dependencies=TRUE)

## 実行環境の構築

以下から環境を選択

- Docker
  - 講師と同じ環境
  - WindowsはWindows10pro以外だと設定が難しい(Docker Toolboxを試してみて問題があれば以下のAnaconda/Minicondaを使用してください)
- Anaconda/Miniconda
  - 比較的設定は容易
  - Pythonライブラリ以外の必要なものは自分でインストールする必要あり
- Google ColabやAzure Notebooks(サポート対象外)
  - タブレットからでも実行できる
  - 3Dやインタラクティブなコンテンツなど一部動かないものがある
  - デフォルトの環境にプリインストールされているもの以外は自分で導入する必要あり

### Dockerで構築

1. Dockerをインストール

   - [Mac](https://store.docker.com/editions/community/docker-ce-desktop-mac)
   - [Windows10pro](https://store.docker.com/editions/community/docker-ce-desktop-windows)
   - [Windows10pro以外](https://docs.docker.com/toolbox/overview/)

(以降、dockerが起動している状態で進める)

2. このリポジトリをクローンまたはファイルをコピーする(親ディレクトリ含め間に日本語やスペースが入らないように)

3. localhost(127.0.0.1)の8888ポートや6006ポートを使用している(他のJupyterを起動しているなど)の場合は.envのJUPYTER_PORTやTENSOR_BOARD_PORTの値を変更する

4. ターミナルからダウンロードしたフォルダに移動する(`cd`コマンドを使用)

5. workspace/up.shの権限を実行可能なように変更しておく
   Mac
   > chmod 777 workspace/up.sh
   Windows
   > icacls workspace\up.sh /grant Everyone:F

6. 以下のコマンドを実行する

   > docker-compose build

### Anaconda/Minicondaで構築

1. Graphvizをインストール

   - [Graphviz](http://www.graphviz.org/download/)

2. Anaconda/Minicondaをインストール(まだインストールされていない場合)

   - [Miniconda(Python3系)](https://conda.io/miniconda.html)

3. 仮想環境を構築する

   - 以下のファイルの中身を1行ずつターミナル/コマンドプロンプトに貼り付けて実行
     - miniconda

4. 仮想環境に入る

   > conda activate dslec

5. Jupyter notebookのコンフィグファイルを作成

   > jupyter notebook --generate-config

6. カスタムCSSを配置

   - 作成されたコンフィグファイルの場所(.jupyter)の下にcustomというフォルダを作成し、その中にmy-light.cssをcustom.cssという名前でコピーする

7. Jupyter extensionsをインストールする

   - 以下のファイルの中身を1行ずつターミナル/コマンドプロンプトに貼り付けて実行
     - nbextension

8. matplotlibの日本語化

   - ネットで"matplotlib 日本語"などで検索して日本語表示できるようにしておく

## Jupyter notebookの使用方法

### Dockerから使用

1. Jupyterを起動する

   > docker-compose up -d

2. Jupyterにアクセスする

   - Docker Toolboxを使っている場合は、以下のコマンドでIPアドレスを調べておき次の127.0.0.1と置き換える
     > docker-machine inspect --format='{{.Driver.IPAddress}}' dev

   - ブラウザから127.0.0.1:8888にアクセスし、passwordにjupyterと入力する

3. Jupyterを終了する

   > docker-compose stop

### Anaconda/Minicondaから使用

1. 仮想環境に入る

   > conda activate dslec

2. Jupyterを起動する(passwordはjupyter)

   > jupyter notebook

3. Jupyterを終了する

   > Ctrl+C  
   > conda deactivate

## コンテンツについて

- `index.ipynb`が目次になっているので、そこから各ページに飛ぶ
- データの読み込み等に必要なので、各ページでは上から順に`Shift+Enter`で実行しながら下に進む
