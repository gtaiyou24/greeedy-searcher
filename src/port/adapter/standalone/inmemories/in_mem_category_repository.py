from typing import List, Optional

from domain.model.category import CategoryRepository, Category, CategoryId, CategoryName, CategoryTree
from domain.model.gender import Gender
from domain.model.query import QuerySet, Operator, Query
from domain.model.url import URL


WOMEN_トップス = Category(CategoryId("women-tops"), Gender.WOMEN, CategoryName("トップス"),
                      URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"),
                      [CategoryId("women-tops-1"), CategoryId("women-tops-2"), CategoryId("women-tops-3"),
                       CategoryId("women-tops-4"), CategoryId("women-tops-5"), CategoryId("women-tops-6"),
                       CategoryId("women-tops-7"), CategoryId("women-tops-8"), CategoryId("women-tops-9")],
                      QuerySet({Operator.OR: [Query("トップス")]}))
WOMEN_Tシャツ = Category(CategoryId("women-tops-1"), Gender.WOMEN, CategoryName("Tシャツ/カットソー"),
                      URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                      QuerySet({Operator.OR: [Query("Tシャツ"), Query("カットソー")]}))
WOMEN_シャツブラウス = Category(CategoryId("women-tops-2"), Gender.WOMEN, CategoryName("シャツ/ブラウス"),
                         URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                         QuerySet({Operator.OR: [Query("シャツ"), Query("ブラウス")]}))
WOMEN_ポロシャツ = Category(CategoryId("women-tops-3"), Gender.WOMEN, CategoryName("ポロシャツ"),
                       URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                       QuerySet({Operator.OR: [Query("ポロシャツ")]}))
WOMEN_ベスト = Category(CategoryId("women-tops-4"), Gender.WOMEN, CategoryName("ベスト"),
                     URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                     QuerySet({Operator.OR: [Query("ベスト")]}))
WOMEN_パーカー = Category(CategoryId("women-tops-5"), Gender.WOMEN, CategoryName("パーカー"),
                      URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                      QuerySet({Operator.OR: [Query("パーカー")]}))
WOMEN_スウェット = Category(CategoryId("women-tops-6"), Gender.WOMEN, CategoryName("スウェット"),
                       URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                       QuerySet({Operator.OR: [Query("スウェット")]}))
WOMEN_スウェット = Category(CategoryId("women-tops-7"), Gender.WOMEN, CategoryName("スウェット"),
                       URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                       QuerySet({Operator.OR: [Query("スウェット")]}))
WOMEN_カーディガン = Category(CategoryId("women-tops-8"), Gender.WOMEN, CategoryName("カーディガン"),
                        URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("カーディガン")]}))
WOMEN_タンクトップ = Category(CategoryId("women-tops-9"), Gender.WOMEN, CategoryName("タンクトップ"),
                        URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("タンクトップ")]}))
WOMEN_キャミソール = Category(CategoryId("women-tops-9"), Gender.WOMEN, CategoryName("キャミソール"),
                        URL("https://cdn.grail.bz/images/goods/d/mb1182/mb1182_v1.jpg"), [],
                        QuerySet({Operator.OR: [Query("キャミソール")]}))


class InMemCategoryRepository(CategoryRepository):
    __women_category_tree: List[CategoryTree] = [
        CategoryTree(WOMEN_トップス, [
            CategoryTree(WOMEN_Tシャツ, []),
            CategoryTree(WOMEN_シャツブラウス, []),
            CategoryTree(WOMEN_ポロシャツ, []),
            CategoryTree(WOMEN_ベスト, []),
            CategoryTree(WOMEN_パーカー, []),
            CategoryTree(WOMEN_スウェット, []),
            CategoryTree(WOMEN_カーディガン, []),
            CategoryTree(WOMEN_タンクトップ, []),
            CategoryTree(WOMEN_キャミソール, [])
        ])
    ]

    __men_category_tree: List[CategoryTree] = [
        CategoryTree(
            Category(CategoryId("men-all"), Gender.MEN, CategoryName("すべてのアイテム"),
                     URL("https://daikore.com/wp-content/uploads/2021/03/d4.jpg"), [],
                     QuerySet({Operator.OR: []})),
            [])
    ]

    def category_tree(self, gender: Gender) -> List[CategoryTree]:
        if gender == Gender.WOMEN:
            return self.__women_category_tree
        elif gender == Gender.MEN:
            return self.__men_category_tree
        else:
            return []

    def category_of(self, category_id: CategoryId) -> Optional[Category]:
        all_category_tree = self.__women_category_tree + self.__men_category_tree
        for a_category_tree in all_category_tree:
            if a_category_tree.is_in(category_id):
                return a_category_tree.category_of(category_id)
        return None
