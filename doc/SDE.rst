SDE Apparatus
=================

.. attention::
  
  1. Do not use the temperature measurement of the right heater for adjusting temperature;
  
  2. Do use the "cycle" and "snow" buttons on the panel of the cooling system;
  
  3. Do not open the vaccum pump when the extraction flask is not boiling;
  
  4. Do open the heater to heat the flask with extraction agent;
  
  5. Do not close the vaccum pump while the while system does not cool down;

1. 注意加入沐浴露到烧杯之后，千万一定要搅拌均匀，因为有机和水不混溶;

2. Please pay attention to the vaccum device when using rotating vaporisation machine. Because when the vaccumn device is off, there will be bubbles coming up from the bottom of the tank:

.. raw:: html

    <video poster="https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/logo.jpg" width="800" height="466" controls="controls">
        <source src="https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/videos/foaming.mov">
    </video>

3. When the vaccumn device is on, see what happened:

.. raw:: html

    <video poster="https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/logo.jpg" width="800" height="466" controls="controls">
        <source src="https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/videos/vacumn-not-foaming.mov">
    </video>

Properties
===============

1. The latent heat of condensation of pentane is 335 kJ/kg;

2. Pentane(n-): Its thermal conductivity value is 0.135 W/m*K. And it is recoommended over the tempeerature limit-303 K;

3. Water: Its thermal conductivity value is 0.57 W/m*K. And it is recoomended over the temperature limit-273K;

4. For water at 373 K, the latent heat of vaporisation is 2257 kJ/kg;

5. For pentane at 313 K, the latent heat of vaporisation is 180 kJ/kg;

6. Use the following chart for searching latent-of-heat;

.. raw:: html
  :file: latent-of-heat.html

If the volume of extractant is smaller than 1 ml or 0.5 ml, you can use the pentane or dichlormethane to increase the volume of the extractant and then concentrate it either by air dry or by rotating vapourisation techiques. 


SDE vs SPME
------------

1. SPME was more efficient in extracting low molecular weight and high volatility compounds;
2. SDE was able to extract compounds with low volatilities that were not extracted using SPME;
3. the ratio between some compounds from lipid oxidation and those from degradation of amino acids was much lower in SDE extracts than with SPME, which could be a consequence of the development of Strecker degradation of amino acids during distillation in SDE owing to the high temperatures used;
4. Similarly, diunsaturated aldehydes detected in SDE extracts were absent using SPME, probably owing to oxidation of polyunsaturated fatty acids in SDE as a consequence of the temperature during extraction;
5. SDE和SPME均无法提取低挥发性的化学组份, 例如FA13008的乙基麦芽酚，香兰素和乙基香兰素均无法用SDE和SPME提取出来，可参见 `FA13008 SDE vs SPME <https://fechii-application-chemical-engineer.readthedocs.io/en/latest/_static/FA13008/FA13008TIC.html>`_;
6. "SDE method is preferred to the analysis of compounds with low volatility including fatty acids and esters. HS-SPME was a useful technique for the analysis of readily voltatile components for the characteristics of R. serra aroma." ---- :strong:`GC/MS analysis of volatiles obtained by headspace solid-phase microextraction and simultaneous–distillation extraction from Rabdosia serra (MAXIM.) HARA leaf and stem`.


SDE
-----------------------

This theoretical model allowed the investigation of the influence of the different SDE parameters on recovery. Simulation curves are shown in Figure 12. In agreement with the experiemental optimization of Careri et al., :strong:`the sample and solvent temperatures (i.e., flows of their respective vapours)`, :strong:`the solubility of analytes in the solvent` and :strong:`their volatilities` were important factors. This provides a theoretical justification for some observations made at the beginning of this article:

- The solvent polarity should be a compromise, taking into account the polarity range of solutes: a polar compound will not be satisfactorily extracted, e.g., by pentane.

- Extremely water-soluble compounds (e.g., vanillin, 4-hydroxy-2,5-dimethyl-3(2H)-furanone) have low volatilities and are poorly SDE-isolated.

- As air-to-water partition coefficients are lower under vacuum than at atmospheric pressure, V-SDE may require a longer isolation duration than A-SDE.

The belief that 'mixing of the vapours before condensation should give a more intimate contact of the substances' and could be the key of an efficent extraction is not confirmed by Equation(5). Experimental verification using coumarin rather suggests taht extraction occurs between liquid phases, as its efficency markedly increased by stirring.

                                                                                             ---- :strong:`Simultaneous distillation-extraction: from birth to maturity--review`

.. toctree::
    :maxdepth: 5
    :caption: SDE CH2Cl2 FA13008
    
    SDE_CH2Cl2_FA13008

Salting-out
-----------

To decrease the water solubility of volatiles, the addition of salt to the sample flask has been proposed. This seems especially to increase the recovery of polar compounds, such as coumarin or 2-phenylethyl alcohol; however, yields of vanillin and ethyl vanillin remain negligible.

                                                     ----- :strong:`Simultaneous distillation-extraction: from birth to maturity--review`
                                                     

