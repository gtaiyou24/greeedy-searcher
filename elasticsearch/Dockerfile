FROM docker.elastic.co/elasticsearch/elasticsearch:7.14.1

# プラグインをインストールする
RUN elasticsearch-plugin install analysis-kuromoji && \
    elasticsearch-plugin install analysis-icu

# 類義語/ユーザー辞書
COPY synonyms.txt /usr/share/elasticsearch/config/extra/synonyms.txt
COPY user_dictionary.txt /usr/share/elasticsearch/config/extra/user_dictionary.txt
