# Septuagint Classifier

### What is Septuagint and why to classify it?

[Septuagint](https://en.wikipedia.org/wiki/Septuagint) is a translation of the Hebrew Bible to Ancient Greek made in 3rd–1st centuries BCE. "Septuaginta" means 70 in Latin, the translation's got this name because it is traditionally attributed to the Seventy Translators. That's also the reason for using Roman number LXX referring to the Septuagint.

LXX includes the Greek text of the Hebrew Bible's canonical books as well as some other texts (for some of them we don't even have any Hebrew text, only the Greek version). In general we have 57 different texts there.

The ideas of the project are:
1. to explore possibility of classification LXX texts by 57 groups;
2. to use this classification for exploring textual connections between the Greek New Testament and LXX.

### How it is done

Model used: Ancient-Greek-BERT

Dataset used: [my dataset](https://huggingface.co/datasets/epaolinos/septuagint) based on [Septuagint dataset](https://www.kaggle.com/datasets/abbrivia/septuagint) from Kaggle. I split all the chapters by verses, extracted book name, verse and chapter numbers. Also I added genre labels that could be useful in the future.

The model was fine-tuned for classification by book names and resulted
```f1 = 0.87``` after 3 epochs of training.

After training you can get prediction for any Ancient Greek text, and try it on the New Testament books.

### What's next

1. Now we have a lot of Joshua noise trying to classify the Gospel texts. Joshua and Jesus are the same name in Hebrew and Greek, so naturally every mention of Jesus is considered to be related to the Book of Joshua, no matter if there are any other textual connections. In the next version I'm going to fix that.
2. I want to continue this project and try genre and other classifications that could lead us to any anomalies and irregularities in the LXX and New Testament texts.