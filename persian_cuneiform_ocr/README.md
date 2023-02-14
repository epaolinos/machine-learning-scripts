# Persian cuneiform OCR: Antiquity meets ML

### What is Persian cuneiform?

[Cuneiform](https://en.wikipedia.org/wiki/Cuneiform) is a logo-syllabic script known for the characteristic wedge-shaped impressions which form its signs. [Persian cuneiform](https://en.wikipedia.org/wiki/Old_Persian_cuneiform) was the primary script for the Old Persian language. It includes about 50 characters.

Example: 𐎧𐏁𐎠𐎹𐎰𐎡𐎹 pronounced _xšāyaθiya_, meaning "king".

### What is done

I'm in the early step of studying Machine Learning, so I've just tried some basic techniques to train OCR for the Persian script. Also, I'm not aware of models for any cuneiform script recognition.

Model used: [trocr-base-stage1](https://huggingface.co/microsoft/trocr-base-stage1)

Dataset used: 100 screenshots of cuneiform words or phrases, including technical signs like brackets that were not used in original texts but do occur in scientific publications.

The dataset is surely too small for the task and needs to be extended. The validation loss gets lower during the training but is still too high after 3 epochs. I'm going to continue working on this.
