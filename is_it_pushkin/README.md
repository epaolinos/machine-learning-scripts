# Is it Pushkin?

### Pushkin and horses

*The Little Humpbacked Horse* is famous Russian fairy-tale poem written by [Pyotr Yershov](https://en.wikipedia.org/wiki/Pyotr_Pavlovich_Yershov) in 1834. After publishing of the tale many people suggested it was not only influenced but even authored by [Alexander Pushkin](https://en.wikipedia.org/wiki/Alexander_Pushkin), the greatest Russian poet. Supposedly, Pushkin wanted to evade possible censorship for the political motives in the tale, so he published it under Yershov's name. Yershov himself was only 19 years old and would never write anything as brilliant.

Today's mainstream researchers don't take seriously the idea of Pushkin's authorship. Apart from other reasons, Pushkin had other "political" publications in that period, and also some lines in the tale seem too immature to belong to him.

However, we will try to make some ML classification and see results.

### How it is done

Model used: ruRoberta-large

Firstly I tried to make classification "Pushkin vs. Yershov", but it became clear soon that this approach is too unbalanced. We have too many Pushkin poems compared to Yershov's, that's why any unknown text tends to get attrebuted to Pushkin, even if we try to balance it using hyperparameters.

So the next approach was to make "Pushkin vs. not-Pushkin" classification. I made a dataset of Pushkin and five other Russian poets of 19th century: Yershov, Lermontov, Nekrasov, Tutchev, and Fet. Their poems are split by sentences.

The classification resulted ```f1 = 0.80``` (compare to ```f1 = 0.50``` if we suppose it's always Pushkin and ```f1 = 0.40``` for random results).

If we try to classify *The Horse*'s sentences, the model predicts "Not Pushkin" for 1841 of them and "Pushkin" for the other 584.

### What's next

It would be interesting to extend the training dataset, to use some other metrics, and to check the model on some other data (maybe, prosaic texts, for example).