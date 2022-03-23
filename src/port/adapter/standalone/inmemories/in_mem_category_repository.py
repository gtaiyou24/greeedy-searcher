import json
from typing import List

from domain.model.category import CategoryRepository, Category, CategoryId, CategoryName, CategoryTree
from domain.model.gender import Gender
from domain.model.url import URL


class InMemCategoryRepository(CategoryRepository):
    __women_category_tree: List[CategoryTree] = [
        # トップス
        CategoryTree(
            Category(CategoryId("women-tops"), Gender.WOMEN, CategoryName("トップス"),
                     URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"),
                     [CategoryId("women-tops-1"), CategoryId("women-tops-2"), CategoryId("women-tops-3"),
                      CategoryId("women-tops-4"), CategoryId("women-tops-5"), CategoryId("women-tops-6"),
                      CategoryId("women-tops-7"), CategoryId("women-tops-8"), CategoryId("women-tops-9")]),
            [
                CategoryTree(
                    Category(CategoryId("women-tops-1"), Gender.WOMEN, CategoryName("Tシャツ/カットソー"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-2"), Gender.WOMEN, CategoryName("シャツ/ブラウス"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-3"), Gender.WOMEN, CategoryName("ポロシャツ"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-4"), Gender.WOMEN, CategoryName("ベスト"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-5"), Gender.WOMEN, CategoryName("パーカー"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-6"), Gender.WOMEN, CategoryName("スウェット"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-7"), Gender.WOMEN, CategoryName("カーディガン"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-8"), Gender.WOMEN, CategoryName("タンクトップ"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-tops-9"), Gender.WOMEN, CategoryName("キャミソール"),
                             URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), []),
                    [])
             ]
        ),
        # ジャケット/アウター
        CategoryTree(
            Category(CategoryId("women-outerwear"), Gender.WOMEN, CategoryName("ジャケット/アウター"),
                     URL("https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif"),
                     [CategoryId("women-outerwear-1"), CategoryId("women-outerwear-2"), CategoryId("women-outerwear-3"),
                      CategoryId("women-outerwear-4"), CategoryId("women-outerwear-5"), CategoryId("women-outerwear-6"),
                      CategoryId("women-outerwear-7"), CategoryId("women-outerwear-8"), CategoryId("women-outerwear-9"),
                      CategoryId("women-outerwear-10"), CategoryId("women-outerwear-11"), CategoryId("women-outerwear-12"),
                      CategoryId("women-outerwear-13"), CategoryId("women-outerwear-14"), CategoryId("women-outerwear-15"),
                      CategoryId("women-outerwear-16"), CategoryId("women-outerwear-17"), CategoryId("women-outerwear-18"),
                      CategoryId("women-outerwear-19"), CategoryId("women-outerwear-20")]),
            [
                CategoryTree(
                    Category(CategoryId("women-outerwear-1"), Gender.WOMEN, CategoryName("テーラードジャケット"),
                             URL("https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif"), []),
                    []),
                CategoryTree(
                    Category(CategoryId("women-outerwear-2"), Gender.WOMEN, CategoryName("ノーカラージャケット"),
                             URL("https://www.dzimg.com/Dahong/202109/1200225_19202545_k3.gif"), []),
                    []),
            ]
        ),
        # Category(CategoryId("women-outerwear-3"), Gender.WOMEN, CategoryName("ノーカラーコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-4"), Gender.WOMEN, CategoryName("デニムジャケット"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-5"), Gender.WOMEN, CategoryName("ライダースジャケット"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-6"), Gender.WOMEN, CategoryName("ブルゾン"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-7"), Gender.WOMEN, CategoryName("ミリタリージャケット"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-8"), Gender.WOMEN, CategoryName("MA-1"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-9"), Gender.WOMEN, CategoryName("ダウンジャケット/コート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-10"), Gender.WOMEN, CategoryName("ダウンベスト"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-11"), Gender.WOMEN, CategoryName("ダッフルコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-12"), Gender.WOMEN, CategoryName("モッズコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-13"), Gender.WOMEN, CategoryName("ピーコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-14"), Gender.WOMEN, CategoryName("ステンカラーコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-15"), Gender.WOMEN, CategoryName("トレンチコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-16"), Gender.WOMEN, CategoryName("チェスターコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-17"), Gender.WOMEN, CategoryName("ムートンコート"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-18"), Gender.WOMEN, CategoryName("マウンテンパーカー"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-19"), Gender.WOMEN, CategoryName("スタジャン"),
        #          URL(""), []),
        # Category(CategoryId("women-outerwear-20"), Gender.WOMEN, CategoryName("ポンチョ"),
        #          URL(""), []),
        #
        # # パンツ
        # Category(CategoryId("women-pants"), Gender.WOMEN, CategoryName("パンツ"),
        #          URL(""), []),
        # Category(CategoryId("women-pants-1"), Gender.WOMEN, CategoryName("デニムパンツ"),
        #          URL(""), []),
        # Category(CategoryId("women-pants-2"), Gender.WOMEN, CategoryName("カーゴパンツ"),
        #          URL(""), []),
        # Category(CategoryId("women-pants-3"), Gender.WOMEN, CategoryName("チノパンツ"),
        #          URL(""), []),
        # Category(CategoryId("women-pants-4"), Gender.WOMEN, CategoryName("スウェットパンツ"),
        #          URL(""), []),
        # Category(CategoryId("women-pants-5"), Gender.WOMEN, CategoryName("スラックス"),
        #          URL(""), []),
        #
        # # スカート
        # Category(CategoryId("women-skirt"), Gender.WOMEN, CategoryName("スカート"),
        #          URL(""), []),
        #
        # # オールインワン
        # Category(CategoryId("women-allinone"), Gender.WOMEN, CategoryName("オールインワン"),
        #          URL(""), []),
        #
        # # ワンピース
        # Category(CategoryId("women-onepiece"), Gender.WOMEN, CategoryName("ワンピース"),
        #          URL(""), []),
        #
        # # バッグ
        # Category(CategoryId("women-bag"), Gender.WOMEN, CategoryName("バッグ"),
        #          URL(""), []),
        #
        # # シューズ
        # Category(CategoryId("women-shoes"), Gender.WOMEN, CategoryName("シューズ"),
        #          URL(""), []),
        #
        # # キャップ
        # Category(CategoryId("women-cap"), Gender.WOMEN, CategoryName("キャップ"),
        #          URL(""), []),
    ]

    __men_category_tree: List[CategoryTree] = [
        CategoryTree(
            Category(CategoryId("men-all"), Gender.MEN, CategoryName("すべてのアイテム"),
                     URL("https://daikore.com/wp-content/uploads/2021/03/d4.jpg"), []),
            [])
    ]

    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        if gender == Gender.WOMEN:
            return self.__women_category_tree
        elif gender == Gender.MEN:
            return self.__men_category_tree
        else:
            return []
