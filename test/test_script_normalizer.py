from collections import namedtuple
import unittest
from lstm_word_segmentation.helpers import normalize_string


class TestScriptNormalizer(unittest.TestCase):
    def test_normalize_string(self):
        TestCase = namedtuple("TestCase", ["in_str", "scripts", "out_str"])
        cases = [
            TestCase("abc", ["Latn"], "abc"),
            TestCase("abc", [], "LLL"),
            TestCase("a𑄌", ["Latn", "Cakm"], "a𑄌"),
            TestCase("a𑄌", ["Latn"], "a𑄃"),
            TestCase("a𑄌", ["Cakm"], "L𑄌"),
            TestCase("a𑄌", [], "L𑄃"),
            # NOTE: ASCII digits have script Common, not Latin
            TestCase("123", ["Latn"], "000"),
            TestCase("၁၁၁", ["Mymr"], "၁၁၁"),
            TestCase("၁၁၁", [], "၀၀၀"),
            # NOTE: Currency symbols have script Common
            TestCase("฿100", ["Thai"], "$000"),
            TestCase("฿100", [], "$000"),
            TestCase("พันโทหญิง สมเด็จพระนางเจ้าอินทรศักดิศจี พระวรราชชายา (พระนามเดิม: ประไพ; 10 มิถุนายน พ.ศ. 2445 — 30 พฤศจิกายน พ.ศ. 2518) พระวรราชชายาในพระบาทสมเด็จพระมงกุฎเกล้าเจ้าอยู่หัว", ["Thai"], "พันโทหญิง สมเด็จพระนางเจ้าอินทรศักดิศจี พระวรราชชายา (พระนามเดิม: ประไพ; 00 มิถุนายน พ.ศ. 0000 — 00 พฤศจิกายน พ.ศ. 0000) พระวรราชชายาในพระบาทสมเด็จพระมงกุฎเกล้าเจ้าอยู่หัว"),
            TestCase("พันโทหญิง สมเด็จพระนางเจ้าอินทรศักดิศจี พระวรราชชายา (พระนามเดิม: ประไพ; 10 มิถุนายน พ.ศ. 2445 — 30 พฤศจิกายน พ.ศ. 2518) พระวรราชชายาในพระบาทสมเด็จพระมงกุฎเกล้าเจ้าอยู่หัว", [], "ทัทททททิท ทททท็ททททททททท้ททิททททัททิทที ทททททททททททท (ททททททททิท: ททททท; 00 ทิทุทททท ท.ท. 0000 — 00 ททททิทททท ท.ท. 0000) ทททททททททททททททททททททททท็ทททททททุทททท้ททท้ทททู่ทัท"),
        ]
        for cas in cases:
            actual = normalize_string(cas.in_str, cas.scripts)
            self.assertEqual(cas.out_str, actual, cas)


if __name__ == "__main__":
    unittest.main()
