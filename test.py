from __init__ import *
import unittest
from StringIO import StringIO


class TestAll(unittest.TestCase):
  def test_density_merged_graph_construction(self):
    fp = StringIO(SAMPLE_GRAPH)
    g = DensityMergedGraph(fp)
    self.assertTrue(g)
    self.assertEqual(type(g.__str__()), str)
    self.assertEqual(g.bicliques[0]['rows'], [28])
    self.assertEqual(g.bicliques[4]['cols'], [12569])
    self.assertEqual(len(g.bicliques), 7)


SAMPLE_GRAPH = """29 ; 637 956 2853 2941 2991 3053 3130 3148 3663 4024 4104 4739 6069 6951 7497 7578 8185 8737 8847 9272 9790 11691 12778 13147 13470 14237 14301 14670 14734 15260 15526 15539 15896 16340 16509 16796 16853 16902 17285 17350 17760 18353 18509 18731 19650 19662 19696 19798 19876 19891 19904 20407 20437 20624 20849 21542 ; density: 0.982143
45 ; 956 1007 1722 2513 2929 2941 3411 3715 4544 4855 4920 5947 5963 6622 6744 6786 6796 7149 7233 7273 7523 8081 8359 9305 9435 9899 10345 10691 10703 10898 11043 12117 12386 12710 13849 13988 14192 14832 15364 15702 15944 15988 16221 16687 17265 17298 17760 18186 18365 19771 19979 20310 20359 20867 21159 21425 ; density: 0.982143
121 ; 150 2634 3828 4152 4483 4607 5766 6453 7028 8820 9706 11731 11957 12133 12204 12890 12996 13166 14316 14619 15554 15773 17622 17689 18880 18986 20067 20803 21396 21443 21906 ; density: 0.967742
35 ; 969 1756 3035 3409 5819 8770 9790 11799 12494 12746 13162 14264 14986 15729 15910 16340 16808 16812 ; density: 0.944444
3 9 15 61 126 ; 12569 ; density: 1
29 65 80 95 96 ; 17285 ; density: 0.8
77 86 ; 45 120 123 147 156 164 178 180 216 250 272 291 302 338 374 412 424 451 492 509 533 542 545 607 681 762 792 806 807 813 830 845 850 855 909 938 957 967 1022 1031 1071 1072 1097 1131 1173 1175 1213 1231 1256 1327 1337 1341 1372 1387 1416 1454 1479 1483 1504 1537 1605 1680 1706 1742 1822 1829 1839 1887 1972 1980 1984 1990 2042 2046 2129 2178 2191 2227 2229 2233 2250 2271 2295 2323 2343 2356 2393 2416 2431 2460 2464 2473 2487 2550 2553 2570 2586 2596 2605 2644 2655 2752 2766 2802 2815 2830 2901 2906 2908 2974 2990 3004 3032 3056 3059 3068 3071 3086 3109 3125 3126 3155 3165 3191 3217 3240 3241 3268 3270 3275 3353 3354 3366 3406 3437 3447 3475 3516 3560 3567 3582 3620 3708 3723 3726 3772 3781 3788 3901 3917 3919 3926 3933 3961 3964 4002 4050 4068 4112 4215 4250 4260 4269 4290 4320 4331 4342 4380 4391 4400 4425 4447 4497 4558 4601 4696 4698 4725 4729 4742 4764 4771 4804 4840 4846 4886 4898 4900 4905 4919 4946 5018 5034 5051 5057 5082 5119 5131 5138 5179 5209 5366 5395 5497 5542 5558 5567 5587 5647 5712 5787 5805 5818 5832 5839 5859 5882 5885 5890 5923 5948 5955 5993 6003 6004 6065 6107 6141 6142 6176 6187 6251 6297 6301 6342 6383 6398 6414 6454 6460 6487 6496 6529 6548 6549 6597 6608 6616 6624 6638 6641 6646 6649 6747 6753 6788 6817 6837 6842 6896 6927 6940 6974 6990 7030 7108 7109 7119 7131 7137 7145 7186 7210 7213 7215 7217 7228 7315 7415 7419 7477 7479 7496 7502 7565 7586 7589 7595 7601 7657 7673 7683 7713 7744 7747 7883 7893 7896 7914 7955 7966 7974 7991 8054 8087 8092 8138 8161 8183 8199 8211 8234 8243 8255 8265 8295 8314 8363 8395 8415 8464 8482 8483 8501 8523 8563 8570 8622 8656 8662 8675 8690 8808 8824 8853 8911 8917 8925 8936 8945 8962 9004 9031 9041 9054 9059 9065 9079 9088 9114 9159 9208 9221 9226 9228 9259 9260 9262 9268 9292 9294 9330 9375 9398 9422 9437 9461 9465 9481 9488 9523 9567 9579 9597 9612 9616 9637 9692 9700 9707 9708 9736 9807 9814 9889 9893 9962 10007 10025 10036 10088 10092 10182 10191 10240 10252 10262 10276 10336 10340 10353 10377 10405 10429 10443 10452 10539 10541 10545 10567 10583 10623 10729 10731 10754 10762 10782 10800 10817 10832 10880 10902 10904 10929 10930 10972 10988 11093 11120 11121 11124 11157 11223 11229 11255 11356 11379 11404 11406 11548 11581 11626 11664 11719 11736 11743 11796 11834 11857 11970 11979 12015 12018 12043 12055 12064 12087 12098 12119 12134 12232 12260 12286 12301 12313 12338 12362 12368 12373 12475 12520 12598 12603 12607 12628 12643 12646 12661 12673 12701 12756 12761 12771 12803 12807 12830 12832 12854 12896 12906 12916 12928 12961 12991 12999 13016 13029 13080 13091 13134 13135 13159 13223 13226 13286 13322 13332 13360 13433 13483 13486 13491 13540 13547 13549 13569 13586 13609 13619 13623 13665 13678 13686 13687 13723 13737 13757 13807 13820 13834 13867 13891 13897 13938 13966 14013 14033 14070 14106 14142 14203 14222 14250 14271 14282 14291 14322 14337 14380 14439 14477 14541 14564 14566 14568 14569 14607 14618 14639 14704 14708 14738 14744 14745 14792 14813 14840 14875 14882 14921 14922 14925 14943 14946 14950 14973 14985 14988 15073 15093 15145 15172 15193 15201 15266 15276 15308 15346 15365 15387 15410 15423 15432 15509 15552 15612 15615 15644 15652 15673 15699 15710 15741 15753 15783 15858 15862 15863 15873 15905 15919 15949 15985 15991 16020 16051 16084 16142 16175 16200 16217 16223 16227 16254 16333 16349 16386 16391 16421 16431 16443 16446 16465 16472 16518 16581 16616 16625 16650 16670 16683 16700 16708 16716 16743 16781 16797 16822 16860 16872 16923 16932 16947 16951 17073 17082 17167 17206 17270 17404 17435 17506 17509 17528 17537 17546 17547 17563 17565 17608 17611 17705 17711 17725 17820 17879 17904 17974 18034 18040 18082 18105 18125 18168 18289 18326 18337 18349 18371 18453 18455 18459 18481 18557 18558 18593 18615 18617 18690 18693 18699 18714 18724 18776 18783 18784 18798 18835 18860 18927 18929 18962 18988 18999 19016 19036 19071 19104 19107 19119 19216 19217 19220 19237 19240 19297 19305 19337 19339 19352 19405 19417 19425 19461 19492 19525 19565 19568 19570 19675 19678 19710 19743 19754 19768 19794 19825 19830 19859 19874 19875 19888 19890 19947 19994 20017 20052 20055 20100 20101 20180 20203 20210 20219 20229 20268 20281 20327 20336 20418 20423 20448 20455 20502 20504 20516 20519 20571 20594 20676 20714 20726 20734 20760 20814 20817 20821 20838 20846 20856 20897 20898 20945 20990 20995 21007 21020 21039 21048 21052 21077 21111 21115 21132 21161 21204 21253 21265 21285 21317 21357 21390 21429 21431 21448 21487 21494 21508 21515 21529 21569 21651 21700 21717 21733 21742 21756 21774 21792 21809 21816 21829 21835 21847 21855 21866 21879 21929 21961 21999 22021 22031 22035 22058 22091 22104 22105 22118 22133 22153 ; density: 0.884118
"""

if __name__ == "__main__":
  unittest.main()

