# Machine learning isotropic **_g_** values of radical polymers 

Davis Thomas Daniel<sup>1,2</sup>, Souvik Mitra<sup>3</sup>, Diddo Diddens<sup>3,4</sup>, Rüdiger A. Eichel<sup>1,4</sup> and Josef Granwehr<sup>1,2</sup>


1. Institute of Energy and Climate Research (IEK-9), Forschungszentrum Jülich GmbH, Jülich, 52425, Germany
2. Institute of Technical and Macromolecular Chemistry, RWTH Aachen University, Aachen, 52056, Germany
3. Institute of Physical Chemistry, University of Münster, 48149, Münster, Germany
4. Institute of Physical Chemistry, RWTH Aachen University, Aachen 52056, Germany
5. Helmholtz-Institute Münster (IEK-12), Forschungszentrum Jülich GmbH, Jülich, Münster, 48149, Germany, 52425, Germany

![toc.png](Scripts/TOC.png)

This repository contains the relevant files and scripts to reproduce the results described in the aforementioned manuscript. 
The model can be used for predictions of PTMA _g_ values as shown [here](https://jugit.fz-juelich.de/d.daniel/ptma-ml/-/blob/main/PTMA-ML.ipynb).

Files and folders :

**[PTMA-ML.ipynb](https://jugit.fz-juelich.de/d.daniel/ptma-ml/-/blob/main/PTMA-ML.ipynb)** : 

> Contains a jupyter notebook with details of the ML workflow used in the work (can be viewed directly in the repository):  defining molecular descriptor parameters, training, hyperparameter optimisation, cross-validation, loading the trained model and predictions. More details on running jupyter notebooks can be found [here](https://jupyter.org/install).


* **Datasets** : 

> Contains PTMA polymer structures from TR,TE-1 and TE-2 data sets transformed using a molecular descriptor (SOAP,MBTR or DAD).
> Structure data sets have 'structure_data' in the title, DFT calculated g values have 'giso_DFT_data' in the title, predicted g values have 'predicted' in the title.


* **XYZ_files**:

> Contains raw xyz files of whole structure dataset (WSD) and TE-2 data set extracted from different times frame of Molecular dynamics trajectories.

* **Models** :

> Contains trained models , trained using MBTR, SOAP and DAD feature vectors and Extremely randomised trees (ERT) method.

* **Final_Model** :

> Contains the final ERT-MBTR model (see manuscript for details).

* **Scripts** :

> Contains the scripts to directly predict g<sub>iso</sub> from xyz files using a trained model.

## License
MIT (Temporary)
