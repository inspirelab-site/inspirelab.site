---
title: Research
nav:
  order: 2
  tooltip: Research themes and works
---

# {% include icon.html icon="fa-solid fa-microscope" %}Research
We work in the interphase of data science and brain science. We develop advanced models and innovative data science methodologies to elucidate brain function, neurological disorders, and other biological processes. By leveraging multimodal functional neuroimaging data—including fMRI-BOLD, LFP, optical imaging, and MEG—from animal models, healthy individuals, and patients, we decode complex brain activities and diseases. This integrative approach aims to provide groundbreaking insights that advance both fundamental understanding and translational applications in brain science, informatics, and beyond. Below are research themes we have been working on.
* [Modeling and Inferences in Causal Interactions among Brain Networks](#section-1) 
* [Investigating Spatiotemporal Brain Dynamics across Species ](#section-2)
* [Assessing Functional Brain Dynamics in Neurological Disorders](#section-3)
* [3D Reconstruction from Cryo-EM: Statistical Characterization of Virus Particles](#section-4)
<a name="section-1"></a>

{% include section.html %}
### Modeling and Inferences in Causal Interactions among Brain Networks
{% capture text %}
Functional brain dynamics, captured through neuroimaging techniques such as fMRI, LFP/EEG, and optical imaging, are sensitive indicators of brain disorders, each providing insights at different spatial and temporal scales. However, understanding altered brain interactions requires integrating causal information. To address this, we develop advanced computational methods—including but not limited to, information theory, statistical/machine/deep learning, optimization, and network science—to model dynamic causal interactions. These approaches offer novel insights into the spatiotemporal dynamics of both neurophysiological and cognitive functions.
{%
  include button.html
  link="papers/?search=%22tag:%20causal-interactions%22"
  text="Browse our 'causal-interaction' papers"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
<a name="section-2"></a>
{% include feature.html image="research/images/information-flow-diagram3.png" link="https://doi.org/10.64898/2026.02.15.706049" flip=false  style="bare"  text=text%}


### Investigating Spatiotemporal Brain Dynamics across Species 
{% capture text %}
We develop novel analytical methods leveraging statistical and machine learning techniques to explore the spatiotemporal dynamics of the brain using multimodal neuroimaging data from both rodents and humans. Using rodent models, we study the neuronal processes behind these fluctuations and translate our findings to human studies, focusing on similarities and differences in brain function and anatomy. Additionally, we explore how these dynamic processes respond to various cognitive tasks in humans. 
{%
  include button.html
  link="papers/?search=%22tag:%20brain-dynamics%22"
  text="See our 'brain-dynamics' papers"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
<a name="section-3"></a>
{% include feature.html image="research/images/cross-species.png"  link="https://doi.org/10.3389/fnins.2022.816331" flip=true  style="square"  text=text%}

### Assessing Functional Brain Dynamics in Neurological Disorders
{% capture text %} 
In collaboration with our clinical partners, we develop innovative biomarkers for neurological disorders using functional neuroimaging data. We employ statistical learning to quantify the spatiotemporal dynamics of functional brain systems, aiming to decipher the neuropathophysiology of conditions like post-concussive syndrome, obesity, and prenatal opioid exposure. Additionally, we leverage artificial intelligence models to predict therapy responses and enhance our understanding of these conditions.
{%
  include button.html
  link="papers/?search=%22tag:%20neuro-disorders%22"
  text="See our 'neuro-disorders' papers"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
{% include feature.html image="research/images/information-flow-brain.png"  flip=false  style="bare"  text=text%}

<a name="section-4"></a>

### 3D Reconstruction from Cryo-EM: Statistical Characterization of Virus Particles
{% capture text %}
Cryo-electron microscopy (cryo-EM) provides essential 2D projection images of nano-scale bio-particles like viruses for understanding their biological function. Unlike traditional methods that assume strict geometric symmetry, we adopted a more realistic approach, allowing for individual particle asymmetry while maintaining overall mean and covariance symmetry. Specifically, we introduced a novel theorem in group representation theory and developed new statistical inference models and algorithms.
 This novel method eliminated long-standing distortions in 3D reconstructions. Collaborating with virologists from the Scripps Institute, we uncovered allosteric effects along the symmetry axes of bacteriophage HK97. This algorithm can be applicable to most spherical virus particles with icosahedral and octahedral symmetries. {%
  include button.html
  link="papers/?search=%22tag:%20image-reconstruction%22"
  text="Browse our 'image-reconstruction' papers"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
{% include feature.html image="research/images/virus-recon.png" link="https://doi.org/10.1016/j.jsb.2017.12.013" flip=true style="bare" text=text %}
