---
title: Home
nav:
  order: 1
  tooltip: Homepage
---
# Welcome to INSPIRE Lab!
**I**maging- and **N**euro-computation**s** for **P**recision **I**nformatics **Re**search (**INSPIRE**) Lab, led by [Dr. Nan Xu](members/nan-xu.html), is anchored at the intersection of data science and brain science. We are dedicated to developing advanced computational models and data science approaches to uncover brain function, neurological disorders, and other biological processes. By leveraging multimodal functional neuroimaging data—including fMRI-BOLD, LFP, optical imaging, and MEG—from animal models, healthy individuals, and patients, we decode complex brain activities and diseases. This integrative approach aims to provide groundbreaking insights that advance both fundamental understanding and translational applications in brain science, informatics, and beyond.
## Highlights
{% include list.html data="posts" component="post-excerpt" filters="tags: latest" style="fill"%}

{% capture text %}
We develop advanced data science approaches to interpret data from cutting-edge imaging techniques, providing novel insights for brain science, informatics, and beyond.
{%
  include button.html
  link="research"
  text="See our research themes"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{%
  include button.html
  link="papers"
  text="Publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="research/images/research.jpg"
  link="research"
  title="Our Research"
  text=text
%}

{% capture text %} 
We are an interdisciplinary team of researchers passionate about innovative, rigorous, and transparent science. We warmly welcome students and trainees from diverse backgrounds, fostering mutual respect and collaboration. We are committed to fairness and inclusion, ensuring that everyone feels supported and valued.
{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{%
  include button.html
  link="contact"
  text="Join us!"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="team/images/team0.png"
  link="team"
  title="Our Team"
  text=text
%}

{% capture text %}
Explore our new repositories of data science software tools. Our code is completely open source, and we welcome contributions from the community. Join us to advance open science!
{%
  include button.html
  link="software"
  text="Browse our open software"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}
{% endcapture %}

{%
  include feature.html
  image="software/images/software.jpg"
  title="Open Software"
  flip=true
  style="bare"
  text=text
%}
