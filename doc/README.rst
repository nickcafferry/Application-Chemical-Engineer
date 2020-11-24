`Fechii-Gas Chromatography Mass Spectrometry <https://github.com/nickcafferry/Fechii-Application-Chemical-Engineer/tree/master>`_
===============

|Documentation Status| |Licence|

.. |Licence| image:: https://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/nickcafferry/Fechii-Application-Chemical-Engineer/blob/master/LICENSE
   
.. |Documentation Status| image:: https://readthedocs.org/projects/fechii-application-chemical-engineer/badge/?version=latest
   :target: https://fechii-application-chemical-engineer.readthedocs.io/en/latest/?badge=latest


Copyright |copy| Wei MEI, |MLMS (TM)| |---| all rights reserved. |bamboo|
"""""""""""""""""""""""""

.. |copy| unicode:: 0xA9 .. copyright sign
.. |MLMS (TM)| unicode:: MLMS U+2122
   .. with trademark sign
.. |---| unicode:: U+02014 .. em dash
   :trim:

.. |bamboo| unicode:: 0x1F024 .. bamboo


Agilent 7890/5975C-GC/MSD
-------------------------

气相色谱仪类型: 7890A

质谱仪类型: 5973C 通常情况下,不需要设计参数.

开机以及关机

a. 仪器参数的设定;
b. 分析方法的编辑;
c. 谱库的检索;
d. 报告的打印.

故障排查: 首先, 有两个泵, 一个在地上, 一个在仪器里面, 在仪器里面要看一下比较烫.
比较严重的故障:1. 真空泵反油, 主机器扳烧毁.

.. attention:: 
   
   1. 老化柱子: 分段老化。程序升温老化(最好的老化方法)。如HP-5柱，不到20min将其升温完，并反复进行数次。再升至280度，反复数次。接到质谱仪上看基线情况。270度，必须观测到基线提高。再老化到300度半小时。无论何种方式，载气必须充足。
   
   2. 进样口用灰色隔垫，减少隔垫流失。
   
   3. GC/MS接口处必须用vesper垫圈(5062-3508). 注意安装方向(大的一端朝向质谱)。
   
   4. 新柱子安装时无方向性，但一旦使用过，再不要改变方向。
   
   保存柱子时注意将两端密封好，避免水和空气破环柱子内涂层。
      


.. code:: python 
   
   >>> m/z 15, 29, 43, 57, 71, 85, 99 -------->  (Aliphatic hydrocarbons: 脂肪烃或链状烃) 代表物： `正庚烷 Heptane <https://pubchem.ncbi.nlm.nih.gov/compound/8900>`
   
   >>> m/z 19, 31, 50, 69 -------->  (Perfluoro compounds: 全氟化合物) 代表物：`四氟化碳 Carbon tetrafluoride  <https://pubchem.ncbi.nlm.nih.gov/compound/6393>`
   
   >>> m/z 30, 44, 58 ----------> (Amines: 胺类) 代表物：`尸胺 Cadaverine <https://pubchem.ncbi.nlm.nih.gov/compound/273>`
   
   >>> m/z 31,45, 59 -----------> (Alcohols or ethers) 代表物：`alpha 松油醇 alpha-TERPINEOL <https://pubchem.ncbi.nlm.nih.gov/compound/17100>`; 代表物：`甲基叔戊基醚 Tert-Amyl methyl ether <https://pubchem.ncbi.nlm.nih.gov/compound/61247>`
   
   >>> m/z 39, 50, 51, 52, 63, 65, 76, 77, 91 --------------> (Aromatic hydrocarbons) 代表物：`六甲基苯 Hexamethylbenzene <https://pubchem.ncbi.nlm.nih.gov/compound/6908>`
   
   >>> m/z 41, 54, 68 ----------------> Aliphatic nitriles
   
   >>> m/z 41, 55, 69 ----------------> Unsaturated hydrocarbons 
   
   >>> m/z 41, 69 ---------------> Methacrylates
   
   >>> m/z 43, 58 ---------------> Methyl ketones
   
   >>> m/z 43, 87 ---------------> Glycol diacetates
   
   >>> m/z 44, 42 ---------------> (CH3)2N-
   
   >>> m/z 53, 80 ---------------> Pyrrole derivatives
   
   >>> m/z 55, 99 ---------------> Glycol diacrylates
   
   >>> m/z 59, 72 ---------------> Amides
   
   >>> m/z 60, 73 ---------------> Underivatized acids
   
   >>> m/z 61, 89 ----------------> Sulfur compounds
   
   >>> m/z 67, 81, 95 ------------> 1-Acetylenes
   
   >>> m/z 69, 41, 86 ------------> "Segemented" fluoromethacrylates
   
   >>> m/z 69, 77, 65 ------------> "Segemented" fluoroiodies
   
   >>> m/z 74, 87 ------------> Methyl esters
   
   >>> m/z 76, 42, 61 --------> (CH3)2NS-
   
   >>> m/z 82, 67 -------> Cyclohexyl compounds
   
   >>> m/z 83, 82, 54 -------> A cyclohexyl ring
   
   >>> m/z 87, 43 -------> Glycol diacetates
   
   >>> m/z 89, 61 --------> Sulfur-containing compounds
   
   >>> m/z 86, 100, 114 ------> Diamines
   
   >>> m/z 99, 55 -----> Glycol acrylates
   
   >>> m/z 104, 91 -------> Alkylbenzenes
   
   >>> m/z 104, 117 -------> Alkylbenzenes
