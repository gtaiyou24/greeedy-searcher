# greeedy-searcher

## 開発

<details><summary>起動方法</summary>

```bash
$ cd ~/path/to/greeedy-searcher

# .envファイルをコピーして、適切な値に書き換える
$ cp ./elasticsearch/.env.sample ./elasticsearch/.env

# コンテナを起動
$ docker-compose up --build

# App(FastAPI)を起動
$ docker-compose run --rm \
  -v `pwd`/src:/app/ \
  -p 8000:8000 \
  app uvicorn start_api:api --host 0.0.0.0 --reload
```

 - [Swagger UI](http://0.0.0.0:8000/docs)
 - [Elasticsearch](http://0.0.0.0:9200)

</details>

<details><summary>UT実行方法</summary>

```bash
$ cd ~/path/to/greeedy-searcher

$ pytest -v .
```
</details>

ユーザ辞書

 - [ファッション・アパレル用語索引｜モダリーナのアパレル・ファッション図鑑](https://www.modalina.jp/modapedia/)
 - [ファッション用語集 - ファッションプレス](https://www.fashion-press.net/words/)

## デプロイ

<details><summary>デプロイ手順</summary>

```bash
$ cd ~/path/to/greeedy-searcher

# Dockerイメージをビルド
$ docker build -t greeedy-searcher:{タグ名} src/.

# Docker Hubにプッシュ
$ docker tag greeedy-searcher:{タグ名} {DockerHubのアカウント名}/greeedy-searcher:{タグ名}
$ docker login
$ docker push {DockerHubのアカウント名}/greeedy-searcher:{タグ名}
```

[Lightsail](https://lightsail.aws.amazon.com/ls/webapp/home) のコンテナを再デプロイする。

 - [Lightsail](https://lightsail.aws.amazon.com/ls/webapp/home)
 - [Amazon OpenSearch Service](https://ap-northeast-1.console.aws.amazon.com/esv3/home?region=ap-northeast-1#opensearch/dashboard)
 - [Docker Hub](https://hub.docker.com/)

</details>


## 参考資料

### Elasticsearch
<table>
<tr>
    <td>導入事例</td>
    <td> <a href="https://techblog.zozo.com/entry/migrating-zozotown-search-platform">ZOZOTOWNの検索基盤におけるElasticsearch移行で得た知見 - ZOZO TECH BLOG</a> </td>
</tr>
<tr>
    <td>CRUD操作について</td>
    <td><a href="https://dev.classmethod.jp/articles/elasticsearch-starter-1/">Elasticsearch 入門。その1 | DevelopersIO</a></td>
</tr>
<tr>
    <td>Bulk API/検索について</td>
    <td><a href="https://dev.classmethod.jp/articles/elasticsearch-starter2/">Elasticsearch 入門。その2 | DevelopersIO</a></td>
</tr>
<tr>
    <td>転置インデックス/アナライザ/マッピングについて</td>
    <td><a href="https://dev.classmethod.jp/articles/elasticsearch-starter3/">Elasticsearch 入門。その3 | DevelopersIO</a></td>
</tr>
<tr>
    <td>Cluster/Node/Shardについて</td>
    <td><a href="https://dev.classmethod.jp/articles/elasticsearch-starter4/">Elasticsearch 入門。その4 | DevelopersIO</a></td>
</tr>
</table>

日本語検索のためのインデックス方法

 - [Elasticsearchで日本語検索を扱うためのマッピング定義 - ZOZO TECH BLOG](https://techblog.zozo.com/entry/elasticsearch-mapping-config-for-japanese-search)
 - [Elasticsearchで日本語の全文検索の機能を実装する | Elastic Blog](https://www.elastic.co/jp/blog/how-to-implement-japanese-full-text-search-in-elasticsearch)

ユーザ辞書に関するトピック

 - [Kuromojiユーザ辞書に定義済みの単語で構成された複合語の形態素解析について - Elastic In Your Native Tongue / 日本語による質問・議論はこちら - Discuss the Elastic Stack](https://discuss.elastic.co/t/kuromoji/285149)
 - [辞書シノニム管理の運用 - dely tech blog](https://tech.dely.jp/entry/2018/10/19/100000)
 - [「ホットペッパービューティー」美容クリニックでのElasticsearchのユーザー辞書登録による検索改善 - Tech Blog - Recruit Engineer](https://engineer.recruit-lifestyle.co.jp/techblog/2021-04-22-hpbc-search-dictionary/)
 
運用に関するトピック

 - [[新機能]Amazon Elasticsearch Service でファイルベースのシノニム、ユーザー辞書などに対応するカスタムパッケージを利用可能になりました | DevelopersIO](https://dev.classmethod.jp/articles/amazon-elasticsearch-service-filebase-synonym-userdictionary/)
 - [Amazon OpenSearch Service のカスタムパッケージ - Amazon OpenSearch Service (Amazon Elasticsearch Service の後継サービス)](https://docs.aws.amazon.com/ja_jp/opensearch-service/latest/developerguide/custom-packages.html)

### AWS

 - [Lightsail コンテナ: クラウドでコンテナを実行する簡単な方法 | Amazon Web Services ブログ](https://aws.amazon.com/jp/blogs/news/lightsail-containers-an-easy-way-to-run-your-containers-in-the-cloud/)