# All-Language-OCRs
Model checkpoints are uploaded here

1. Kannada OCR
   Kannada Model is based on PARSeq whcih performs well on both scene text and printed text data
   Trained on ~9 million synthetic images (SynthTiger + TRDG)
   Validated on ~0.8 million synthetic images (SynthTiger + TRDG)
   Tested on some real world datasets:
     1. Kannada printed text page images: https://github.com/MILE-IISc/Kannada-OCR-test-images-with-ground-truth
     2. Konkani in Kannada script printed text images: https://github.com/MILE-IISc/KonkaniDocumentsInKannadaScript
     3. Images collected from MLe2e and CVSI15:
          (CVSI15) http://www.ict.griffith.edu.au/cvsi2015/Dataset.php
          (MLe2e) https://paperswithcode.com/dataset/mle2e
   Results:
   Test on Kannada Realworld Dataset:
     | Dataset           | # samples | Accuracy | 1 - NED | Confidence | Label Length |
     |:-----------------:|----------:|---------:|--------:|-----------:|-------------:|
     | kannada_printed   |     13498 |    96.15 |   98.80 |      97.82 |         7.39 |
     | kannada_realworld |       978 |    93.56 |   98.30 |      97.50 |         6.93 |
     | kannada_konkani   |      1563 |    93.35 |   97.75 |      96.71 |         5.85 |
     |-------------------|-----------|----------|---------|------------|--------------|
     | Combined          |     16039 |    95.72 |   98.66 |      97.69 |         7.21 |

2. Assamese OCR:
   Coming up next!
