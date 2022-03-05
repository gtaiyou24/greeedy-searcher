from pytest import fail, mark, raises

from domain.model.url import URL


class TestURL:
    class Test_生成について:
        def test_文字列のリンク指定でURLを生成できる(self):
            try:
                URL("https://store.aclent.jp/")
            except Exception:
                fail("This code should be executed.")

        def test_URLではない文字列で生成するとAssertionErrorを送出する(self):
            with raises(AssertionError):
                URL("abcdefg")

        @mark.parametrize("link", [None, "", ' '])
        def test_URLなしで生成するとAssertionErrorを送出する(self, link):
            with raises(AssertionError):
                URL(link)
