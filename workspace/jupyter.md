
## [Jupyter Notebook](https://jupyter.org/) とは
---
プログラムのコード・数式・グラフ・テキストなどを 1 つのファイルにまとめて保存できるアプリケーション。データの可視化・統計モデリング・機械学習などでよく利用される。  
IDE (統合開発環境) のような [JupyterLab](https://jupyterlab.readthedocs.io/en/stable/) の開発も進んでいるが、セキュリティ上の理由から Javascript の実行に制約があり、インタラクティブなグラフ表示などに支障があるため今回は使用しない。

Python 以外にも様々な言語が利用可能。  
[beakerx](https://nbviewer.jupyter.org/github/twosigma/beakerx/blob/master/doc/groovy/GeneralAutotranslation.ipynb) を利用すると、変数の中身を別言語にコピー可能。

[Binder](https://mybinder.readthedocs.io/en/latest/) を利用するとクラウドで実行環境も提供可能。

## Jupyter Notebook の使い方

### セルの選択
---
↑・↓でセルを選択。

### 編集モードとコマンドモード
---
セルを選択してから`Enter`で編集モードに移行、`Esc`でコマンドモードに復帰。  
編集モードではセルの内容を編集でき、コマンドモードではセルを選択・実行できる。

### セルの種類
---
<table>
    <tr>
        <th>Markdown セル</th>
        <td class="text-left">Markdown 形式で編集し、実行すると HTML で表示される</td>
    </tr>
    <tr>
        <th>Code セル</th>
        <td class="text-left">Python のコードを記述し、実行するとコードの実行結果が表示される</td>
    </tr>
</table>

### セルの実行
---
セルの実行は`Shift+Enter` (実行後、次のセルに移動) または`Ctrl+Enter` (その場で実行) 。

### セルの種類変更
---
コマンドモード中に`M`で Markdown セルに、`Y`で Code セルに変更。

### セルの挿入
---
コマンドモード中に`A` (上に挿入) または`B` (下に挿入) 。

### 関数等の詳細確認
---
コード入力中に`Shift+Tab`で docstring を表示。 (`Shift`を押したまま`Tab`を何度か押すと表示領域が広がる)

### その他のキーボードショートカット
---
メニューバーの`Help`->`Keyboard Shortcuts`で確認。
