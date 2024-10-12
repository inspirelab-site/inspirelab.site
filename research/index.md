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
fMRI BOLD brain dynamics are sensitive indicators for brain disorders, but understanding altered brain causal interactions requires incorporating causal information. To address this, we develop methods to model dynamic causal interactions, enhancing traditional correlation analysis by identifying the directionality of information flow and assessing whole-brain connectivity. These metrics reveal new insights into the spatiotemporal nature of cognitive functions, including memory consolidation. 
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
{% include feature.html image="research/images/information-flow-diagram.png" link="https://doi.org/10.3389/fnins.2017.00271" flip=false  style="bare"  text=text%}


### Investigating Spatiotemporal Brain Dynamics across Species 
{% capture text %}
We develop novel analytical methods to investigate spontaneous fluctuations in blood oxygen level-dependent (BOLD) signals measured by fMRI. Using rodent models, we study the neuronal processes behind these fluctuations and translate our findings to human studies, focusing on similarities and differences in brain function and anatomy. Additionally, we explore how these dynamic processes respond to various cognitive tasks in humans. 
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
{% capture text %} In collaboration with our clinical partners, we develop innovative analyses to assess functional brain dynamics in various neurological disorders measured by functional neuroimaging data. Specifically, we quantify the spatiotemporal dynamic processes in functional brain systems to decipher the neuropathophysiology of brain diseases such as post-concussive syndrome, obesity, and prenatal opioid exposure. {%
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
Cryo-electron microscopy (cryo-EM) provides essential 2D projection images of nano-scale bio-particles like viruses for understanding their biological function. Unlike traditional methods that assume strict geometric symmetry, we adopted a more realistic approach, allowing for individual particle asymmetry while maintaining overall mean and covariance symmetry. This novel method eliminated long-standing distortions in 3D reconstructions. Collaborating with virologists from the Scripps Institute, we uncovered allosteric effects along the symmetry axes of bacteriophage HK97. This algorithm can be applicable to most spherical virus particles with icosahedral and octahedral symmetries. {%
  include button.html
  link="papers/?search=%22tag:%20image-reconstruction%22"
  text="Browse our 'image-reconstruction' papers"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}
{% include feature.html image="research/images/virus-recon.png" link="https://doi.org/10.1016/j.jsb.2017.12.013" flip=true style="bare" text=text %}
