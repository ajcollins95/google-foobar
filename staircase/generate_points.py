import sys
import timeit
from solution import *

def genPoints():
    for i in range(3,200):
        start_time = timeit.default_timer()
        ans = solution(i)
        elapsed = timeit.default_timer() - start_time
        print('({_input}, {_output}), #Time elapsed: {_elapsed}'.format(
            _input = i,
            _output = ans,
            _elapsed = elapsed
        ))



genPoints()

"""
(3, 1), #Time elapsed: 1.19209289551e-05
(4, 1), #Time elapsed: 5.00679016113e-06
(5, 2), #Time elapsed: 5.96046447754e-06
(6, 3), #Time elapsed: 1.19209289551e-05
(7, 4), #Time elapsed: 1.00135803223e-05
(8, 5), #Time elapsed: 1.28746032715e-05
(9, 7), #Time elapsed: 1.69277191162e-05
(10, 9), #Time elapsed: 2.90870666504e-05
(11, 11), #Time elapsed: 3.00407409668e-05
(12, 14), #Time elapsed: 4.6968460083e-05
(13, 17), #Time elapsed: 6.19888305664e-05
(14, 21), #Time elapsed: 8.58306884766e-05
(15, 26), #Time elapsed: 0.000107049942017
(16, 31), #Time elapsed: 0.000128030776978
(17, 37), #Time elapsed: 0.000174045562744
(18, 45), #Time elapsed: 0.000248908996582
(19, 53), #Time elapsed: 0.000290155410767
(20, 63), #Time elapsed: 0.000439882278442
(21, 75), #Time elapsed: 0.000482797622681
(22, 88), #Time elapsed: 0.000728845596313
(23, 103), #Time elapsed: 0.000727891921997
(24, 121), #Time elapsed: 0.00114297866821
(25, 141), #Time elapsed: 0.00246715545654
(26, 164), #Time elapsed: 0.00237107276917
(27, 191), #Time elapsed: 0.00266003608704
(28, 221), #Time elapsed: 0.00229907035828
(29, 255), #Time elapsed: 0.0059130191803
(30, 295), #Time elapsed: 0.00370717048645
(31, 339), #Time elapsed: 0.00445604324341
(32, 389), #Time elapsed: 0.00675010681152
(33, 447), #Time elapsed: 0.0111742019653
(34, 511), #Time elapsed: 0.00901103019714
(35, 584), #Time elapsed: 0.0120549201965
(36, 667), #Time elapsed: 0.0119321346283
(37, 759), #Time elapsed: 0.020289182663
(38, 863), #Time elapsed: 0.0191628932953
(39, 981), #Time elapsed: 0.0235729217529
(40, 1112), #Time elapsed: 0.0266311168671
(41, 1259), #Time elapsed: 0.0329270362854
(42, 1425), #Time elapsed: 0.0412170886993
(43, 1609), #Time elapsed: 0.0482039451599
(44, 1815), #Time elapsed: 0.0588698387146
(45, 2047), #Time elapsed: 0.0690090656281
(46, 2303), #Time elapsed: 0.0800540447235
(47, 2589), #Time elapsed: 0.0953280925751
(48, 2909), #Time elapsed: 0.111762046814
(49, 3263), #Time elapsed: 0.13715004921
(50, 3657), #Time elapsed: 0.155779838562
(51, 4096), #Time elapsed: 0.190223932266
(52, 4581), #Time elapsed: 0.220133066177
(53, 5119), #Time elapsed: 0.253752946854
(54, 5717), #Time elapsed: 0.30523109436
(55, 6377), #Time elapsed: 0.359723091125
(56, 7107), #Time elapsed: 0.432333230972
(57, 7916), #Time elapsed: 0.493944883347
(58, 8807), #Time elapsed: 0.595079898834
(59, 9791), #Time elapsed: 0.733650922775
(60, 10879), #Time elapsed: 0.861831903458
(61, 12075), #Time elapsed: 0.986745119095
(62, 13393), #Time elapsed: 1.18908500671
(63, 14847), #Time elapsed: 1.41965985298
(64, 16443), #Time elapsed: 1.53696513176
(65, 18199), #Time elapsed: 1.84474897385
(66, 20131), #Time elapsed: 2.16827201843
(67, 22249), #Time elapsed: 2.58857607841
(68, 24575), #Time elapsed: 3.07976508141
(69, 27129), #Time elapsed: 3.51418709755
(70, 29926), #Time elapsed: 4.12738394737
(71, 32991), #Time elapsed: 4.85473203659
(72, 36351), #Time elapsed: 5.76592803001
(73, 40025), #Time elapsed: 6.49856495857
(74, 44045), #Time elapsed: 7.75691699982
"""