
# 到達目標

## データサイエンスとは
---
実証主義人文・社会科学の方法論に関する研究分野。  
因果関係の理解だけではなく、予測や社会実装も主な関心に含まれる。

## データサイエンティストの細分類
---
- データエンジニア
- アナリスト
- データサイエンティスト
- 機械学習エンジニア
- リサーチャー

参考 : [なぜデータサイエンスのゼネラリストになるべきではないのか](http://ainow.ai/2018/12/18/156854/)

## データサイエンティストとしてのレベル
---
1. 初級 - データ分析手法を実行できる
1. 中級 - 分析結果の妥当性を保証できる・分析の専門分野を持つ
1. 上級 - 分散処理が必要なレベルの大規模データを扱える・前例のないような未知の状況にも対応できる・最先端の手法を開発・実装できる

参考 : [データサイエンティスト スキルチェックリスト 2017年版](https://www.slideshare.net/DataScientist_JP/2017-81179087)

1. 見習いレベル (Assisstant Data Scientist)
1. 独り立ちレベル (Associate Data Scientist)
1. 棟梁レベル (Full Data Scientist)
1. 業界を代表するレベル (Senior Data Scientist)

## データ分析プロジェクトのプロセス
---
1. ビジネス理解 (Business Understanding)
1. データ理解 (Data Understanding)
1. データ準備 (Data Preparation)
1. モデリング (Modeling)
1. 評価 (Evaluation)
1. 実行 (Deployment)

<img style="width: 50%;" alt="CRISP-DM" src="./img/CRISP-DM_Process_Diagram.png" />
By <a href="//commons.wikimedia.org/w/index.php?title=User:Kennethajensen&amp;action=edit&amp;redlink=1" class="new" title="User:Kennethajensen (page does not exist)">Kenneth Jensen</a> - Own work based on: <a rel="nofollow" class="external free" href="ftp://public.dhe.ibm.com/software/analytics/spss/documentation/modeler/18.0/en/ModelerCRISPDM.pdf">here</a> (Figure 1), <a href="https://creativecommons.org/licenses/by-sa/3.0" title="Creative Commons Attribution-Share Alike 3.0">CC BY-SA 3.0</a>, <a href="https://commons.wikimedia.org/w/index.php?curid=24930610">Link</a>

## カバー範囲
---
複数職域にまたがる領域をカバーするので、全てを完璧に理解できなくても可。それぞれの目標に応じて適当に。

下図表で濃い色は本講座でカバーする範囲、薄い色は少し触れる範囲。

### 細分類×レベル
---
<table class="border text-center">
    <tr class="border-bottom-bold background-dark">
        <td class="border-right-bold"></td>
        <th>初級</th>
        <th>中級</th>
        <th>上級</th>
    </tr>
    <tr class="background-bright">
        <th class="border-bottom border-right-bold background-dark">データエンジニア</th>
        <td></td>
        <td></td>
        <td></td>
    </tr>
    <tr class="background-bright">
        <th class="border-bottom border-right-bold background-dark">アナリスト</th>
        <td class="background-lightblue"></td>
        <td></td>
        <td></td>
    </tr>
    <tr class="background-bright">
        <th class="border-bottom border-right-bold background-dark">データサイエンティスト</th>
        <td class="background-blue"></td>
        <td class="background-blue"></td>
        <td></td>
    </tr>
    <tr class="background-bright">
        <th class="border-bottom border-right-bold background-dark">機械学習エンジニア</th>
        <td class="background-blue"></td>
        <td class="background-blue"></td>
        <td></td>
    </tr>
    <tr class="background-bright">
        <th class="border-bottom border-right-bold background-dark">リサーチャー</th>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

### 細分類×プロセス
---
それぞれのロールの守備範囲を狭めにしているので、実際にはもっと広いプロセスに関わらないといけない。

<table class="background-bright text-center">
    <tr class="border-bottom-bold background-dark">
        <td class="border-right-bold"></td>
        <th style="width: 7.5em;">ビジネス理解</th>
        <td colspan="2">→</td>
        <th style="width: 7.5em;">データ理解</th>
        <td>→</td>
        <th style="width: 7.5em;">データ準備</th>
        <td>→</td>
        <th style="width: 7.5em;">モデリング</th>
        <td colspan="2">→</td>
        <th style="width: 7.5em;">評価</th>
        <td>→</td>
        <th style="width: 7.5em;">実行</th>
    </tr>
    <tr class="border">
        <th class="border-right-bold border-left-none border-top-none border-bottom-none background-dark">データエンジニア</th>
        <td class="border-none" colspan="3"></td>
        <td colspan="10"></td>
    </tr>
    <tr>
        <td class="border-right-bold background-dark"></td>
    </tr>
    <tr class="border">
        <th class="border-right-bold border-left-none border-top-none border-bottom-none background-dark">アナリスト</th>
        <td class="border-right-none background-lightblue" colspan="2"></td>
        <td class="border-left-none background-blue" colspan="2"></td>
        <td class="border-none" colspan="6"></td>
        <td colspan="3"></td>
    </tr>
    <tr>
        <td class="border-right-bold background-dark"></td>
    </tr>
    <tr class="border">
        <th class="border-right-bold border-left-none border-top-none border-bottom-none background-dark">データサイエンティスト</th>
        <td class="border-none"></td>
        <td class="border-none" colspan="2"></td>
        <td class="background-blue" colspan="5"></td>
        <td class="border-none" colspan="5"></td>
    </tr>
    <tr>
        <td class="border-right-bold background-dark"></td>
    </tr>
    <tr class="border">
        <th class="border-right-bold border-left-none border-top-none border-bottom-none background-dark">機械学習エンジニア</th>
        <td class="border-none" colspan="5"></td>
        <td class="border-right-none background-blue" colspan="4"></td>
        <td class="border-left-none" colspan="4"></td>
    </tr>
    <tr>
        <td class="border-right-bold background-dark"></td>
    </tr>
    <tr class="border">
        <th class="border-right-bold border-left-none border-top-none border-bottom-none background-dark">リサーチャー</th>
        <td class="border-none" colspan="7"></td>
        <td></td>
        <td class="border-none" colspan="5"></td>
    </tr>
</table>
