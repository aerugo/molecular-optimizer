# Dataset

## QSAR aquatic toxicity
https://archive.ics.uci.edu/dataset/505/qsar+aquatic+toxicity

This dataset was used to develop quantitative regression QSAR models to predict acute aquatic toxicity towards the fish Pimephales promelas (fathead minnow) on a set of 908 chemicals. to predict acute aquatic toxicity towards Daphnia Magna. LC50 data, which is the concentration that causes death in 50% of test D. magna over a test duration of 48 hours, was used as model response. The model comprised 8 molecular descriptors: TPSA(Tot) (Molecular properties), SAacc (Molecular properties), H-050 (Atom-centred fragments), MLOGP (Molecular properties), RDCHI (Connectivity indices), GATS1p (2D autocorrelations), nN (Constitutional indices), C-040 (Atom-centred fragments). Details can be found in the quoted reference: M. Cassotti, D. Ballabio, V. Consonni, A. Mauri, I. V. Tetko, R. Todeschini (2014). Prediction of acute aquatic toxicity towards daphnia magna using GA-kNN method, Alternatives to Laboratory Animals (ATLA), 42,31:41; doi: 10.1177/026119291404200106

## Citation
Ballabio,Davide, Cassotti,Matteo, Consonni,Viviana, and Todeschini,Roberto. (2019). QSAR aquatic toxicity. UCI Machine Learning Repository. https://doi.org/10.24432/C5SG7H.

# Motivation

## Purpose
The dataset was created to develop a QSAR (Quantitative Structure-Activity Relationship) model to predict acute aquatic toxicity toward Daphnia magna, a species of water flea used as an indicator organism in aquatic toxicity testing. The model aimed to offer an alternative to experimental testing methods, which are more costly and time-consuming. The model used a modified k-Nearest Neighbour (kNN) strategy to predict the toxicity based on the molecular structure of organic compounds​​.

## Creators and Funding
The research team from the University of Milano-Bicocca, Department of Earth and Environmental Sciences, conducted the study. The team included contributors from various institutions and countries, reflecting a collaborative international effort. The European Union Seventh Framework Programme partly financed the research under the Marie Curie Initial Training Network Environmental ChemOinformatics (ECO)​​.

# Composition

## Instances Representation
The dataset comprises 546 organic molecules, each described by various molecular descriptors​​.

## Instance Count and Missing Data
It includes 546 instances, each representing an organic molecule. During data curation, certain records were excluded due to inconsistencies or missing information, ensuring a consistent final dataset​​.

## Confidentiality
The dataset is public and consists of non-confidential, synthesized molecular information. It's not covered by legal privilege or confidentiality agreements.

# Collection Process

## Data Acquisition
The data were retrieved from three databases (ECOTOX, EAT5, and OASIS) and available scientific publications. The OASIS database was accessed through the OECD QSAR Toolbox. The LC50 data (concentration causing 50% mortality in Daphnia magna) were extracted using ad hoc-designed workflows​​.

## Sampling Strategy
Not explicitly stated, but given the nature of the study, it likely involved a comprehensive collection of available data on organic compounds and their aquatic toxicity levels.

## Timeframe
Not specified.

# Preprocessing/cleaning/labelling

## Preprocessing Steps
The data underwent significant curation to ensure consistency. This included verifying molecular structures, removing ambiguous structures, filtering out disconnected structures like salts and mixtures, and dealing with stereochemistry. The lethal concentrations were standardized and transformed to a logarithmic scale. Median values were used to handle multiple toxicity values for the same chemical​​.

## Raw and Processed Data
The study does not specify if the raw data is saved alongside the processed data, but given the detailed description of the curation process, it is likely that some form of original data preservation was involved to enable verification and further analysis.

# Uses

## Potential Applications
Apart from predicting aquatic toxicity, the dataset can potentially be used in broader toxicological studies, environmental risk assessment, and the development of other predictive models for chemical safety.

## Impact Considerations
While the dataset and model provide valuable tools for toxicity prediction, reliance on it should be balanced with understanding its limitations, such as the representativeness of the molecules and the accuracy of predictions outside the tested chemical space. Users should be aware of these aspects to avoid misuse or over-reliance on the model for regulatory or safety-critical decisions​​.

## Inappropriate Uses
The dataset and the model should not be used as the sole decision-making tool for regulatory approval or rejection of chemicals. It is a supplementary tool designed to reduce but not replace experimental toxicity testing.

# Distribution

## Distribution and Access
The dataset is freely available for academic and research purposes.

# Maintenance

## Dataset Maintenance
The maintenance details are not explicitly mentioned. Given the academic nature of the study, the research group at the University of Milano-Bicocca or collaborators might provide informal support or updates.