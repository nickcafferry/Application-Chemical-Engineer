GC-MS-Analysis
===============

1. 调用数据;
2. Mass Spectrometry and 谱图检索报告 (选择屏幕);
3. Alt+S+S用于背景删除
4. 生成百分比报告.
5. 修改runlib(用记事本打开)相关的检索名与峰面积;
6. 再次生成百分比报告, 并返回记事本, 填写保留时间后面的百分比.

.. raw:: html
   :file: GC-MS-Analysis-1.html
   
.. raw:: html
   :file: GC-MS-Analysis-2.html

.. raw:: html
   :file: GC-MS-Analysis-3.html


.. raw:: html
   :file: GC-MS-Analysis-5.html

进样选择方法: 25-1适用于浓度低的样品进样; 100-1适用于浓度高的进样; 还有6-1.

同分异构体虽然质谱图一样，但是保留时间必然有区别。

销售分析调香OEB销售闭合回路
-------------------------

销售=>分析=>调香=>OEB=>销售 闭合回路

GCMS 原料分析
---------------

要单独用表格记录原料分析， 将待测原料用酒精进行稀释5%，然后使用602280方法(浓度较高)，取0.5ml进行进样，注意用PC编号和中文名字进行命名进样。

`FA13008 The First Experiment <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TheFirstSDE.html>`_
------------------------------

The first experiment of SDE was done and analysed by Tongjia. You can download the source code by clicking this link  :download:`The First Experiment <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TheFirstSDE.html>`

`FA13008 TIC <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TIC.html>`_
----------------

You can download the source code by clicking this link  :download:`FA13008 TIC <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TIC.html>`


`FA13008 Pentane vs t-butyl methyl mester <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008PentanevsT-butyl-methyl-mester.html>`_
--------------------------

You can download the source code by clicking this link  :download:`FA13008 Pentane vs t-butyl methyl mester<https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008PentanevsT-butyl-methyl-mester.html>`

`FA13008 t-butyl methyl mester <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008T-butyl-methyl-mesterAirvsRotatingVapor.html>`_
-------------------------

You can download the source code by clicking this link  :download:`FA13008 t-butyl methyl mester<https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008T-butyl-methyl-mesterAirvsRotatingVapor.html>`

`FA13008 Pure vs SDE <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008PurevsSDE.html>`_
-------------------------------

You can download the source code by clicking this link  :download:`FA13008 Pure vs SDE <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008PurevsSDE.html>`

`The impact of vapor pressure and mole fraction on the recovery of different components using SDE <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/The_impact_of_vapor_pressure_and_mole_fraction_on_SDE_efficiency.html>`_
--------------------------------------------------

You can download the source code by clicking this link  :download:`The impact of vapor pressure and mole fraction <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/The_impact_of_vapor_pressure_and_mole_fraction_on_SDE_efficiency.html>`

`TheimpactofvaporpressureandmolefractionandlogP <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/The_impact_of_vapor_pressure_and_mole_fraction_and_logP_on_SDE_efficiency.html>`_
----------------------------------------------

由正戊烷萃取出来的FA13008样品，头香保留比较好；而由二氯甲烷萃取出来的FA13008整体性保留比较好，尤其是中段及后段的香味。

`The Four important factors on SDE Efficiency <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/The_Four_Important_Factors.html>`_
------------------------------------

You can download the source code from here :download:`source code <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/The_Four_Important_Factors.html>`.

`FA13008 CH2Cl2 <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TIC_SPME_Dichlromethane.html>`_
-----------------------------

You can download the source code from here :download:`source code <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TIC_SPME_Dichlromethane.html>`.

GC-LC Concordance Software
--------------------------

GC-LC concordance software dramatically enhances the possibilities of chromatography on complex products and chromatographic fingerpringts by solving retention time shifting in complex chromatograms comparison.

Optimization of Working Parameters
------------------------------------

The best compromise between the above-mentioned parameters(:strong:`Solvent`, :strong:`Salting-out`, :strong:`Distillation-Extraction Time`, :strong:`Oxygen Effect`) can be determined empirically. 

:strong:`Method 1`:  `Optimization acheived by varying four variables: 1. temperature of the sample; 2. temperature of the solvent baths; 3. the coolant temperature; 4. the isolation time <https://www.sci-hub.ren/10.1016/0021-9673(93)80009-w>`_ 

:strong:`Method 2`: `A face centred cube experimental design <https://www.sci-hub.ren/10.1016/s0003-2670(98)00861-7>`_

:strong:`Conclusions`:

- Recoveries differ, depending on the volatilities and solubilities of the analytes in the solvent.

- Too high a solvent temperature leads to decreasing extraction efficiencies.

- The isolation time decreases as the sample temperature increases.

:strong:`Method 3`: Another alternative to optimize SDE working conditions lies in the use of a mathematical model.

SDE工作条件影响汇总
--------------------

- 溶剂的影响::
   
   许多比水的密度高或者低的溶剂用于SDE实验, 并做了相应的比较: 二氯甲烷, 正戊烷, 异戊烷, 正己烷, 氯仿, 
   乙酸乙酯, 乙醚, 叔丁基甲醚, 三氯氟甲烷, 1,1,2-三氯三氟乙烷以及溶剂混合物比如正戊烷/乙醚. 
   通常得出来的结论是, 二氯甲烷一般来说是萃取的最好溶剂. 对于特定的化合物来说, 其他的溶剂可能表现出更高的效率, 
   但是实用性最广的仍然是二氯甲烷, 如图5展示出来的半挥发性化合物. 
   

`Comparison of solvent efficiency. Average recoveries are 47%, 59%, 53%, 58% and 36% <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/solvent_choice.html>`_


- 盐析效应::
   
   为降低挥发组分在水中的溶解度, 向样品烧瓶中加入盐溶液被提出来了. 这看起来只是特别适合提取极性物质的回收率, 
   例如香豆素或者2-苯乙醇; 但是, 香兰素和乙基香兰素提取量仍然可以忽略.
   
- 蒸馏-萃取时间::
 
   最优化的蒸馏-萃取时间从实验上已经被求证过: 达到48h的蒸馏萃取时间已经被验证可以从肥皂中提取挥发度比较
   低的化合物(比如: 肉桂醇, 2-苯乙醇). 值得注意的是, 含有油脂类的基质会急剧增加获取可接受的回收率的时间 
   
`Lipid Matrix <https://www.sci-hub.ren/10.1271/bbb1961.47.2933>`_ 
   
   
   
