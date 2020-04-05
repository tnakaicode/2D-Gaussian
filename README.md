# 2D-Gaussian

<https://en.wikipedia.org/wiki/Multivariate_normal_distribution>  
<https://stackoverflow.com/questions/47936890/how-to-calculate-the-angle-of-ellipse-gaussian-distribution>  
<https://stackoverflow.com/questions/20105364/how-can-i-make-a-scatter-plot-colored-by-density-in-matplotlib>  
<https://towardsdatascience.com/simple-example-of-2d-density-plots-in-python-83b83b934f67>  

<https://pypi.org/project/mpl-scatter-density/>

MNE : Magnetoencephalography (MEG) and Electroencephalography (EEG) in Python <http://mne.tools>  
MNE：Pythonの脳磁図（MEG）および脳波(EEG)

Compute envelope correlations of orthogonalized activity 1 2 in source space using resting state CTF data in a volume source space.
ボリュームソース空間の静止状態CTFデータを使用して、ソース空間の直交化されたアクティビティ1 2のエンベロープ相関を計算します。

形体の「最大実体状態（MMC： Maximum Material Condition）」を決めるサイズのことです。最大実体状態とは、形体のどこでもが、その形体の実体（体積）が最大になる許容限界サイズのことで、たとえば、最小の穴径、最大の軸径を持つ形体の状態のことです。つまり、最大実体サイズとは、形体の最大実体状態を決めるサイズのことです。
図面で指示されたサイズ公差の最大実体状態でできた型崩れのない領域のことで、対象物は最大実体サイズの領域内に存在しなければなりません。
寸法に包絡の条件を適用する場合は、サイズ公差に続けてを記入します。「E」はEnvelope（封筒）の意味で、最大実体サイズを持つ完全形状の包絡面という「封筒」の中に、サイズ公差を守った部品が入れば合格で、入らなければ不合格と決めることを指示する記号です。

This is the size that determines the "maximum material condition (MMC)" of the feature. The maximum body state is the allowable limit size at which the body (volume) of the body becomes the maximum, for example, the state of the body with the smallest hole diameter and the largest shaft diameter. In other words, the maximum entity size is the size that determines the maximum entity state of the feature.
A shape-free area created by the maximum physical state of the size tolerance specified in the drawing, and the object must be within the area of ​​the maximum physical size.
To apply envelope conditions to dimensions, enter the size tolerance followed by. "E" stands for Envelope, which means that if a part that adheres to the size tolerance is included in the "envelope", which is a fully-shaped envelope with the maximum physical size, it will be accepted, otherwise it will be rejected. Is a symbol that indicates

Bivariate case
In the 2-dimensional nonsingular case (${\displaystyle k=rank(\sum )=2}$), the probability density function of a vector ${\displaystyle {\text{[XY]′}}}$ is:

$$ {\displaystyle f(x,y)={\frac {1}{2\pi \sigma _{X}\sigma _{Y}{\sqrt {1-\rho ^{2}}}}}\exp \left(-{\frac {1}{2(1-\rho ^{2})}}\left[{\frac {(x-\mu _{X})^{2}}{\sigma _{X}^{2}}}+{\frac {(y-\mu _{Y})^{2}}{\sigma _{Y}^{2}}}-{\frac {2\rho (x-\mu _{X})(y-\mu _{Y})}{\sigma _{X}\sigma _{Y}}}\right]\right)} $$

where $\rho$ is the correlation between X and Y and where $\sigma _{X}>0$  and $\sigma _{Y}>0$. In this case,

$$ {\displaystyle {\boldsymbol {\mu }}={\begin{pmatrix}\mu _{X}\\\mu _{Y}\end{pmatrix}},\quad {\boldsymbol {\Sigma }}={\begin{pmatrix}\sigma _{X}^{2}&\rho \sigma _{X}\sigma _{Y}\\\rho \sigma _{X}\sigma _{Y}&\sigma _{Y}^{2}\end{pmatrix}}.} $$

The bivariate iso-density loci plotted in the {\displaystyle x,y}x,y-plane are ellipses. As the absolute value of the correlation parameter {\displaystyle \rho }\rho  increases, these loci are squeezed toward the following line :

${\displaystyle y(x)=\operatorname {sgn}(\rho ){\frac {\sigma _{Y}}{\sigma _{X}}}(x-\mu _{X})+\mu _{Y}.}$

This is because this expression, with {\displaystyle sgn(\rho )}{\displaystyle sgn(\rho )} (where sgn is the Sign function) replaced by {\displaystyle \rho }\rho , is the best linear unbiased prediction of {\displaystyle Y}Y given a value of {\displaystyle X}X.[7]

$$ {\displaystyle f(\mathbf {x} )=\left(\det \nolimits ^{*}(2\pi {\boldsymbol {\Sigma }})\right)^{-{\frac {1}{2}}}\,e^{-{\frac {1}{2}}(\mathbf {x} -{\boldsymbol {\mu }})^{\!{\mathsf {T}}}{\boldsymbol {\Sigma }}^{+}(\mathbf {x} -{\boldsymbol {\mu }})}} $$

$$ f(x) = \frac{1}{\sqrt{(2 \pi)^k \det \Sigma}} \exp\left( -\frac{1}{2} (x - \mu)^T \Sigma^{-1} (x - \mu) \right) $$
